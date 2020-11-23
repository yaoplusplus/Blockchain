######################################################################
# 区块链第三次作业 2020.11.20
# by 吕建瑶 1811400
# address: n1TfLmj1oZB9MD2f54XYmSxpoG1zQFMwzs
#######################################################################
from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
ex3a_txout_scriptPubKey =[
OP_2DUP,
OP_ADD,
1812,
OP_EQUALVERIFY,
OP_SUB,
400,
OP_EQUAL]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0015
    txid_to_spend = (
        '78f73f3370fc4ec9a5d015d3ad40b69c9d918f88e310c08644c9a472857800f9')
    utxo_index = 1
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex3a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
# txid:8312075bf320f93910a43c394fdfbb9207adb30863d7d610d5e10877c7513614