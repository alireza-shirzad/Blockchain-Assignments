from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')

# For questions 1-3, we are using 'btc-test3' network. For question 4, you will
# set this to be either 'btc-test3' or 'bcy-test'
network_type = 'bcy-test'


######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

my_private_key = CBitcoinSecret(
    'cPmc9fw2cwTfmF3hGcjzFarLXR8gcLEEXetsqGCqwGtjAxpex8uZ')
#mtDNzmnQdbZeymhHtWjBgUXM4RyUTDoeDr
my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
######################################################################
Faraz_private_key = CBitcoinSecret(
    'cQEHmt4ErW7rsvZh8zjDMKrFAhzd2w2pA3NKBwQaeC3vwDQsv3nq')
#myaZRyNwSJwDzUk9PgwNTX7bEz3DwtjjrL
Faraz_public_key = Faraz_private_key.pub
Faraz_address = P2PKHBitcoinAddress.from_pubkey(Faraz_public_key)
######################################################################
Ata_private_key = CBitcoinSecret(
    'cQn3fLmNCMAwFqGUfjJ2YSLqBfUvtpfMdvncNPRALhnpHZJ3yaBn')
#n2LHdMH4MshPj2a5iTytPt8MFgbmuA7soQ
Ata_public_key = Ata_private_key.pub
Ata_address = P2PKHBitcoinAddress.from_pubkey(Ata_public_key)

######################################################################
ShareHolder1_private_key = CBitcoinSecret(
    'cQjG59dJtUrGanTC4fhVcpe5bxnFy7toNWMcpUtG4BXAPSwJWFju')
#mqUogj1oifmyQixGDtZBEnZts5oCqMrukA
ShareHolder1_public_key = ShareHolder1_private_key.pub
ShareHolder1_address = P2PKHBitcoinAddress.from_pubkey(ShareHolder1_public_key)
######################################################################
ShareHolder2_private_key = CBitcoinSecret(
    'cUE9DHc28vAhrooq8i7PjXRHnsWcT231JyuutLYQBX8NtQbEh65u')
#mh8RQKMRLMQRsQReF17bTiN1CBZ19F8du2
ShareHolder2_public_key = ShareHolder2_private_key.pub
ShareHolder2_address = P2PKHBitcoinAddress.from_pubkey(ShareHolder2_public_key)
######################################################################
ShareHolder3_private_key = CBitcoinSecret(
    'cRimZ72WUCRa48HwV6UnBGtGhh783i8tk5JQx45GRV2e6SzuxDCs')
#myzDKwsmVGsbVduRqYFSBhNBaWuJQvCnS3
ShareHolder3_public_key = ShareHolder3_private_key.pub
ShareHolder3_address = P2PKHBitcoinAddress.from_pubkey(ShareHolder3_public_key)


######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cMd7kjLkBkdUeTHVaddXexSnh8Uz9hUnKEJFNriXS9ftkBMxtLm7')
#mwKURPwBSTrUy8kBfkPTBhfpwihv1tEwmf
# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cVMsFRAByhVxcvWMnQGhYX2wML1kMTeHrkMcmHyhzwaMCtJjbcLc')
#mgCZdTgaeZ36Mjfhtg3qsaKeSqUbDprb4h
# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
######################################################################


######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=$YOURTOKEN
# This request will return a private key, public key and address. Make sure to save these.
#
# Send coins with
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=<YOURTOKEN>
# This request will return a transaction reference. Make sure to save this.

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('f516fd5c442c2ed67ce061fd1f7fc1325a2bf9b0cd34c356123558f7196b6d50'))
#CFz2J73x17z81Rnkrxug4m7WKYQjBujrMC
# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('e4af27277ba876a801a04c8f5f7665844630fa34d6d567c16bcfb9e0ba600331'))
#C2x7ZHpkdU7b6bmS3MVTeH6K4V8D5oR98s
# Can be imported by alice.py or bob.py
alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)

######################################################################
