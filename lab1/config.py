from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')
#Kye37LGjYaDHEW5hreTtq3Mah2537tZdPFMUdcGHwvABJK2e2F5X

# TODO: Fill this in with your private key.
my_private_key = CBitcoinSecret(
    'cQhezNyeQknhnXrerkvV8yxiUnFWHQyaeQUinqnt7Qrmh7GsTnDv')
my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')
