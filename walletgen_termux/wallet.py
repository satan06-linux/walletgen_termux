"""
Multi-coin Address Generator from Private Key
BTC/ETH/SOL/LTC/DOGE/BCH
"""

import hashlib
import base58
from ecdsa import SigningKey, SECP256k1
import eth_account
from bech32 import bech32_encode, convertbits

def priv_to_btc(priv_hex, compressed=True):
    """BTC Legacy/P2WPKH"""
    sk = SigningKey.from_string(bytes.fromhex(priv_hex), curve=SECP256k1)
    vk = sk.verifying_key
    
    if compressed:
        pubkey = vk.to_string("compressed")
    else:
        pubkey = b'\x04' + vk.to_string()
    
    sha = hashlib.sha256(pubkey).digest()
    rip = hashlib.new('ripemd160', sha).digest()
    
    # Legacy
    legacy = base58.b58encode_check(b'\x00' + rip).decode()
    
    # Bech32
    words = convertbits(rip, 8, 5)
    bech32_addr = bech32_encode('bc', [0] + words)
    
    return legacy, bech32_addr

def priv_to_eth(priv_hex):
    """ETH address"""
    acct = eth_account.Account.from_key(priv_hex)
    return acct.address

def priv_to_sol(priv_hex):
    """SOL simplified"""
    seed = hashlib.sha256(bytes.fromhex(priv_hex)).digest()
    words = convertbits(seed[:32], 8, 5)
    return bech32_encode('sol', words)

def priv_to_multi(priv_hex):
    """All addresses"""
    btc_legacy, btc_bech32 = priv_to_btc(priv_hex)
    eth = priv_to_eth(priv_hex)
    sol = priv_to_sol(priv_hex)
    return {
        'BTC_LEGACY': btc_legacy,
        'BTC_BECH32': btc_bech32,
        'ETH': eth,
        'SOL': sol
    }