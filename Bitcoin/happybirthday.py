from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from config import (my_private_key, my_public_key, my_address,
                    Ata_private_key, Ata_public_key, Ata_address,
                    Faraz_private_key, Faraz_public_key, Faraz_address,
                    ShareHolder1_private_key, ShareHolder1_public_key, ShareHolder1_address,
                    ShareHolder2_private_key, ShareHolder2_public_key, ShareHolder2_address,
                    ShareHolder3_private_key, ShareHolder3_public_key, ShareHolder3_address,
                    faucet_address, network_type)
from ex1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [
        OP_DUP,OP_HASH160,address,OP_EQUALVERIFY,OP_CHECKSIG
    ]

def Message_P2PKH_scriptPubKey(Ata_public_key,Faraz_public_key,ShareHolder1_public_key,ShareHolder2_public_key,ShareHolder3_public_key):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [
        OP_RETURN, b"Happy Birthday Hamed"
    ]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return [
        signature,public_key
    ]
    ######################################################################

def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey,
        sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00016666 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '6fe6f670532225e620af9558bfaf538707b0458f99d4d4b4e960efc64bbf51f5')
    utxo_index = 24 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = Message_P2PKH_scriptPubKey(Ata_public_key,Faraz_public_key, ShareHolder1_public_key,ShareHolder2_public_key,ShareHolder3_public_key)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        my_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)
