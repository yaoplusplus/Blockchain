######################################################################
# 区块链第三次作业 2020.11.20
# by 吕建瑶 1811400
# address: n1TfLmj1oZB9MD2f54XYmSxpoG1zQFMwzs
#######################################################################
from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import P2PKH_scriptPubKey
from ex3a import ex3a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.001
txid_to_spend = '8312075bf320f93910a43c394fdfbb9207adb30863d7d610d5e10877c7513614'
utxo_index = 0
######################################################################

txin_scriptPubKey = ex3a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 3a.
txin_scriptSig = [1106,706]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey)
print(response.status_code, response.reason)
print(response.text)
# txid:82b2b70c41c3360acd88d74fb940274e0a9c3e4a9ce8ec759c6e53758727ee2f