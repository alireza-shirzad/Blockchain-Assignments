from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (alice_secret_key_BTC, alice_public_key_BTC, alice_address_BTC,
                    alice_address_BTC, network_type)
from ex1 import P2PKH_scriptPubKey
from ex4a import Q4a_txout_scriptPubKey

Q4b_txout_scriptPubKey = [
    OP_DUP,OP_HASH160,alice_address_BTC,OP_EQUALVERIFY,OP_CHECKSIG
    ]

######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.0002 # amount of BTC in the output you're splitting minus fee
txid_to_spend = (
        'c966cbd1c93ad65cac6db6f7edc131390a90d548da1e25a061ba89a0c2603572')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q4a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 2a.
txout = create_txout(amount_to_send, Q4b_txout_scriptPubKey)
txin = create_txin(txid_to_spend, utxo_index)
signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                         alice_secret_key_BTC)

txin_scriptSig = [
    signature,alice_public_key_BTC
]
######################################################################
#txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, Q4b_txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)

