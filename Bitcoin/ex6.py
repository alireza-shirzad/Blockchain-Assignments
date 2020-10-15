from bitcoin.core.script import *

######################################################################
# These functions will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
#
# TODO: Fill these in to create scripts that are redeemable by both
#       of the above conditions.
# See this page for opcode documentation: https://en.bitcoin.it/wiki/Script

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [
        OP_DEPTH, 3, OP_EQUAL,
        OP_IF, OP_HASH160, hash_of_secret, OP_EQUALVERIFY, OP_CHECKSIG,
        OP_ELSE, 2, public_key_sender, public_key_recipient, 2, OP_CHECKMULTISIG,
        OP_ENDIF
    ]

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient,pub_recipant, secret):
    return [
        sig_recipient, pub_recipant, secret
    ]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [
        OP_0, OP_0, sig_sender, sig_recipient
    ]
######################################################################

######################################################################
#
# Configured for your addresses
#
# TODO: Fill in all of these fields
#

alice_txid_to_spend     = "9d513dd2003adb4a517da43a0527deb5b6caba19d63646f5c1cbc7fb6b84e528"
alice_utxo_index        = 11
alice_amount_to_send    = 0.00016666

bob_txid_to_spend       = "666fd38e48d77f8a6ebef18e8aaf837f5dbc88ec3d4b77b370351fc1d5348195"
bob_utxo_index          = 1
bob_amount_to_send      = 0.00003

# Get current block height (for locktime) in 'height' parameter for each blockchain (and put it into swap.py):
#  curl https://api.blockcypher.com/v1/btc/test3
btc_test3_chain_height  = 1635174

#  curl https://api.blockcypher.com/v1/bcy/test
bcy_test_chain_height   = 2672882

# Parameter for how long Alice/Bob should have to wait before they can take back their coins
## alice_locktime MUST be > bob_locktime
alice_locktime = 5
bob_locktime = 3

tx_fee = 0.0001

# While testing your code, you can edit these variables to see if your
# transaction can be broadcasted succesfully.
broadcast_transactions = False
alice_redeems = False

######################################################################
