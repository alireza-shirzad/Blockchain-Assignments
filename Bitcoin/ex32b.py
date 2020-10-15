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

def MULTI_P2PKH_scriptPubKey(Ata_public_key,Faraz_public_key,ShareHolder1_public_key,ShareHolder2_public_key,ShareHolder3_public_key):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [
        3, ShareHolder1_public_key, ShareHolder2_public_key, ShareHolder3_public_key, 3, OP_CHECKMULTISIGVERIFY,
        1, Ata_public_key, Faraz_public_key, 2, OP_CHECKMULTISIG,
    ]
    ######################################################################


def MULTI_P2PKH_scriptSig(txin, txout, txin_scriptPubKey, Faraz_private_key,Ata_private_key,ShareHolder1_private_key,ShareHolder2_private_key,ShareHolder3_private_key):
    Faraz_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             Faraz_private_key,)
    Ata_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             Ata_private_key,)
    ShareHolder1_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             ShareHolder1_private_key,)
    ShareHolder2_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             ShareHolder2_private_key,)
    ShareHolder3_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             ShareHolder3_private_key,)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return [
        OP_0, Faraz_signature, OP_0,ShareHolder1_signature, ShareHolder2_signature, ShareHolder3_signature
    ]
    ######################################################################

def send_MULTI_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                Faraz_private_key,
                                Ata_private_key,
                                ShareHolder1_private_key,
                                ShareHolder2_private_key,
                                ShareHolder3_private_key,
                                network):

    Faraz_public_key = Faraz_private_key.pub
    Faraz_address = P2PKHBitcoinAddress.from_pubkey(Faraz_public_key)
    Ata_public_key = Ata_private_key.pub
    Ata_address = P2PKHBitcoinAddress.from_pubkey(Ata_public_key)
    ShareHolder1_public_key = ShareHolder1_private_key.pub
    ShareHolder1_address = P2PKHBitcoinAddress.from_pubkey(ShareHolder1_public_key)
    ShareHolder2_public_key = ShareHolder2_private_key.pub
    ShareHolder2_address = P2PKHBitcoinAddress.from_pubkey(ShareHolder2_public_key)
    ShareHolder3_public_key = ShareHolder3_private_key.pub
    ShareHolder3_address = P2PKHBitcoinAddress.from_pubkey(ShareHolder3_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = MULTI_P2PKH_scriptPubKey(Ata_public_key,Faraz_public_key,ShareHolder1_public_key,ShareHolder2_public_key,ShareHolder3_public_key)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = MULTI_P2PKH_scriptSig(txin, txout, txin_scriptPubKey, Faraz_private_key,Ata_private_key,ShareHolder1_private_key,ShareHolder2_private_key,ShareHolder3_private_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000066 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '82d80d60a69c18faa6c1a001f32bed15663714f020e461165b1e8003a5d7757b')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_MULTI_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        Faraz_private_key,
        Ata_private_key,
        ShareHolder1_private_key,
        ShareHolder2_private_key,
        ShareHolder3_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)
