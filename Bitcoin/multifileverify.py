import hashlib
from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core.script import *
from utils import *
from config import (alice_public_key_BTC, alice_secret_key_BTC, alice_address_BTC,
                    network_type)
FileNumbers = int(input("Please Enter the Number of files: "))
SelectParams('testnet')
article = ''
for i in range(FileNumbers):
    FileName = input("Please ENTER a file name:")
    article+open(FileName).read()
article_hash_Object = hashlib.sha256()
article_hash_Object.update(article.encode())
article_hash = article_hash_Object.hexdigest()
SalarSKey = CBitcoinSecret.from_secret_bytes(article_hash.encode())
SalarPKey = SalarSKey.pub
SalarAddress = P2PKHBitcoinAddress.from_pubkey(SalarPKey)
print("Private key: %s" % article_hash)
print("Address: %s" % SalarAddress)





def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [
        OP_DUP,OP_HASH160,address,OP_EQUALVERIFY,OP_CHECKSIG
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
    amount_to_send = 0.00000001 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '7dd96e5b9849f080f528e7434395413fddf3275a533e928c6bbee5b76ae06ce8')
    utxo_index = 9 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(SalarAddress)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        alice_secret_key_BTC,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)
