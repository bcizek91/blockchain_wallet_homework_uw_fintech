# Building a Multi-Blockchain Wallet in Python
<br><br>
## doge_wallet
___
Doge wallet is a python program which leverages the hd-wallet framework to dervive account details for a variety of cryptocurrencies. The functions leverages a mnemonic phrase to convert a pirvate key to account objects, enabling the wallet(s) to send/receive transactions

This program is built using hd-wallet-dervice, Web3.py, bit and eth-account packages.

### Functions 
---
```
derive_wallets(coin)
    Using a mnemonic phrase, generates wallets for cryptocurrencies

priv_key_to_account(coin, priv_key)
    Return private key to account.

create_tx(coin, account, to, amount):
    Creates raw transactions to enable sending transactions

send_tx(coin, account, to, amount)
    Send transaction.
```

### Program Setup
___
Functions listed above were created using hd-wallet and php, requiring the following installation in the wallet folder:
```
pip install -r requirements.txt
```
hd-wallet-derive sourced from GitHub:
```
git clone https://github.com/dan-da/hd-wallet-derive.git
cd hd-wallet-derive
php -r "readfile('https://getcomposer.org/installer');" | php
php composer.phar install

export MSYS=winsymlinks:nativestrict
ln -s hd-wallet-derive/hd-wallet-derive.php derive
```
Verification of hd-wallet-derive:
```
./hd-wallet-derive.php -g --key=xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c
```

### BTC Testnet Transaction
Leveraging a mnemonic phrase in the local .env file executed the following succesfully:
```python
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

from wallet import *

account_from = priv_key_to_account(BTCTEST, coins[BTCTEST][0]['privkey'])
account_to = coins[BTCTEST][1]['address']
send_tx(BTCTEST, account_from, account_to, '0.00055')
```
![](Images/BTCTEST_TX.png)
![](Images/BTCTEST_TX_CONFIRMATION.png)

### ETH Transaction
Was not able to succesfully perform ETH test transaction as I have been leveraging my company's corporate laptop for this class and our Crowdstrike security software has been warning me about malicious activity and finally blocked and wiped everything related to my local ETH blockchain. Had to recreate an environment for web3 and bit packages, but still blocked to no avail. 
![](Images/ETH_DENIAL.png)
![](Images/web3_denial.png)