// In case of error check the followings:
// 1. is the contract address correct?
// 2. is your server running on http://127.0.0.1:8545
// 3. Are you entering the correct candidate id
// 4. Are you trying to vote twice with the same account address?

// Check if Ganache is running on port 8545
// Change it otherwise
const web3 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:7545"));

//Copy contract Address Here
const contractAddress = "0xeA37329612EE56140A12761Cf3847B412dFc3C8d";

//defining contract abi and connecting to it
//Copy ABI here
abi = [
	{
		"constant": false,
		"inputs": [],
		"name": "closeVoting",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "candidateId",
				"type": "uint8"
			}
		],
		"name": "vote",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "candidateIds",
				"type": "uint8[]"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "_voter",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "_candidateId",
				"type": "uint8"
			},
			{
				"indexed": false,
				"name": "_newVotesCount",
				"type": "uint8"
			}
		],
		"name": "Vote",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_winner",
				"type": "uint8"
			}
		],
		"name": "Closed",
		"type": "event"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getCandidates",
		"outputs": [
			{
				"name": "",
				"type": "uint8[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "candidateId",
				"type": "uint8"
			}
		],
		"name": "getVotesNum",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getWinner",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
] ;
VotingContract = web3.eth.contract(abi);
contractInstance = VotingContract.at(contractAddress);

//defining vote event
voteEvent = contractInstance.Vote(
  {},
  {
    fromBlock: 0,
    toBlock: "latest"
  }
);

//defining close event
closedEvent = contractInstance.Closed(
  {},
  {
    fromBlock: 0,
    toBlock: "latest"
  }
);

// Getting the candidates from the blockchain
function InitCandidates(candidateIds) {
  console.log(candidateIds);
  let table = `<table class="table table-bordered">
					<thead>
					<tr>
						<th>Candidate</th>
						<th>Votes</th>
					</tr>
					</thead>
					<tbody>`;
  candidateIds.forEach(
    candidateId =>
      (table += `<tr> <td>${candidateId}</td> <td id="candidate-${candidateId}">0</td>`)
  );

  table += "<tbody></table>";
  $("#candidates-wrapper").html(table);
  candidateIds.forEach(candidateId => updateVotesForCandidate(candidateId));
}

// Getting the available addresses using web3
function initAddresses() {
  const addresses = web3.eth.accounts;
  const $addressSelect = $("#address");
  addresses.forEach(address =>
    $addressSelect.append(
      $("<option/>", {
        value: address,
        text: address
      })
    )
  );
}

// Updating the votes for a candidate
function updateVotesForCandidate(candidateId) {
  contractInstance.getVotesNum.call(candidateId, function(err, res) {
    console.log(res.toString());
    $("#candidate-" + candidateId).html(res.toString());
  });
}

// Voting for a candidate
function voteForCandidate() {
  candidateId = parseInt($("#candidate").val());
  address = $("#address").val();
  errorWrapper = $("#error-wrapper");
  errorWrapper.addClass("d-none");
  contractInstance.vote(candidateId, { from: $("#address").val() }, function(
    err,
    res
  ) {
    if (err) {
      console.log(err);
      errorWrapper.removeClass("d-none");
      errorWrapper.html(`<p> An Error Occured. Check the Followings:</p>
	  <p> 1. Is the contract address correct?</p>
	  <p> 2. Is ganache running on http://127.0.0.1:8545</p>
	  <p> 3. Are you entering the correct candidate id</p>
	  <p> 4. Are you trying to vote twice with the same account address?</p>`);
    } else {
      errorWrapper.addClass("d-none");
    }
  });
}

function closeVoting() {
  contractInstance.closeVoting({}, { from: $("#address").val() }, function(
    err,
    res
  ) {
    if (err) {
      console.log(err);
      errorWrapper = $("#error-wrapper");
      errorWrapper.removeClass("d-none");
      errorWrapper.html(`<p> An Error Occured. Check the Followings:</p>
      <p> 1. Is the contract address correct?</p>
      <p> 2. Is ganache running on http://127.0.0.1:8545</p>
      <p> 3. Are you using the correct account address? (only admin can close the voting)</p>
      <p> 4. Is voting open?</p>`);
    } else {
      errorWrapper.addClass("d-none");
      // updateVotesForCandidate(candidateId);
    }
  });
}

//watching for vote event
voteEvent.watch(function(err, result) {
  if (err) {
    console.log(err);
    return;
  }
  var hash = result.transactionHash;
  var voter = result.args._voter.toString();
  var candidateId = result.args._candidateId.toString();
  var votesCounte = result.args._newVotesCount.toString();
  updateVotesForCandidate(candidateId);
});

//watching for close event
closedEvent.watch(function(err, result) {
  if (err) {
    console.log(err);
    return;
  }
  var hash = result.transactionHash;
  var winner = result.args._winner.toString();
  winnerWrapprt = $("#winner-wrapper");
  winnerWrapprt.removeClass("d-none");
  winnerWrapprt.html(`<p> Voting is Closed </p>
  <p>Winner: ${winner}</p>`);
  $("#close-button").prop("disabled", true);
  $("#vote-button").prop("disabled", true);
});

// Initializing the user interface
$(document).ready(function() {
  initAddresses();
  contractInstance.getCandidates.call(function(err, res) {
    candidateIds = res.map(candidate => candidate.toString());
    InitCandidates(candidateIds);
  });
});
