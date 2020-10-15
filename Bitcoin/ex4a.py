from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (alice_secret_key_BTC, alice_public_key_BTC, alice_address_BTC,
                    alice_address_BTC, network_type)
from ex1 import send_from_P2PKH_transaction
BlockNum = 1634451 + 5

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q4a_txout_scriptPubKey = [
    BlockNum,OP_CHECKLOCKTIMEVERIFY,OP_DROP,OP_DUP,OP_HASH160,alice_address_BTC,OP_EQUALVERIFY,OP_CHECKSIG
    ]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0012 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '9d513dd2003adb4a517da43a0527deb5b6caba19d63646f5c1cbc7fb6b84e528')
    utxo_index = 6 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q4a_txout_scriptPubKey, alice_secret_key_BTC, network_type)
    print(response.status_code, response.reason)
    print(response.text)
