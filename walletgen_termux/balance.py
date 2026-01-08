"""
Multi-coin Balance APIs + Offline Cache
"""

import requests
import time
from tor_proxy import setup_tor

APIs = {
    'BTC': 'https://blockstream.info/api/address/{}/balance',
    'BTC_Bech32': 'https://blockstream.info/api/address/{}/balance',
    'ETH': 'https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest',
    'SOL': 'https://api.mainnet-beta.solana.com',
    'LTC': 'https://api.blockcypher.com/v1/ltc/main/addrs/{}/balance',
    'DOGE': 'https://sochain.com/api/v2/get_address_balance/DOGE/{}',
    'BCH': 'https://rest.bitcoin.com/v2/address/details/{}'
}

def check_balance(addr, coin):
    """Check single coin"""
    try:
        if coin == 'SOL':
            rpc = {"jsonrpc":"2.0","id":1,"method":"getBalance","params":[addr]}
            resp = requests.post(APIs[coin], json=rpc, timeout=10).json()
            return resp['result']['value'] / 1e9 if 'result' in resp else 0
        elif coin == 'ETH':
            resp = requests.get(APIs[coin].format(addr), timeout=10).json()
            return int(resp['result']) / 1e18 if resp.get('status') == '1' else 0
        else:
            url = APIs[coin].format(addr)
            resp = requests.get(url, timeout=10).json()
            return resp / 1e8 if isinstance(resp, (int, float)) else 0
    except:
        return 0

def check_multi_wallet(wallets):
    """Check all coins"""
    balances = {}
    for coin, addr in wallets.items():
        bal = check_balance(addr, coin)
        balances[coin] = bal
        if bal > 50:  # $50+ HIT
            return True, balances
        time.sleep(0.1)  # Rate limit
    return False, balances