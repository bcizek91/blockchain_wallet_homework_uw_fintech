from constants import *
import os
from dotenv import load_dotenv
import subprocess
import json
from bit import PrivateKeyTestnet
from web3 import Account, Web3
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
from bit.network import NetworkAPI
from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

load_dotenv()

def derive_wallets(coin): 
    mnemonic = os.getenv("MNMEMONIC_KEY_HW")
    coin = coin
    depth = 3
    command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --cols=all --coin={coin} --numderive={depth} --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return json.loads(output)

coins = {'ETH': derive_wallets(ETH),
        BTCTEST: derive_wallets(BTCTEST)}

def priv_key_to_account(coin, priv_key):
    if coin==ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin==BTCTEST:
        return PrivateKeyTestnet(priv_key)
    
def create_tx(coin, account, to, amount):
    if coin is ETH:
        gasEstimate = self.w3.eth.estimateGas(
            {"from": account.address, "to": to, "value": amount}
        )
        return {
            "from": account.address,
            "to": to,
            "value": w3.toWei(amount, 'ether'),
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": self.w3.eth.getTransactionCount(account.address),
        }
    elif coin is BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    elif coin is BTC:
        return PrivateKey.prepare_transaction(account.address, [(to, amount, BTC)])
    else:
        return None
        
def send_tx(coin, account, to, amount):
    raw_tx = create_tx(coin, account, to, amount)
    signed_tx = account.sign_transaction(raw_tx)
    if coin is ETH:
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    elif coin is BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(signed_tx)
    elif coin is BTC:
        return NetworkAPI.broadcast_tx(signed_tx)
    else:
        return None