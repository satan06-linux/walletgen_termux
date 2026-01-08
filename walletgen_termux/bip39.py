"""
BIP39 Mnemonic Generator + Validation
"""

from mnemonic import Mnemonic
import hashlib

mnemo = Mnemonic("english")

def generate_seed(strength=128, words=12):
    """Generate valid BIP39 seed"""
    return mnemo.generate(strength=strength)

def validate_seed(seed_phrase):
    """Validate BIP39 checksum"""
    return mnemo.check(seed_phrase)

def seed_to_master(seed_phrase, passphrase=""):
    """BIP39 → Master seed"""
    return mnemo.to_seed(seed_phrase, passphrase)

def entropy_to_mnemonic(entropy_bytes):
    """Entropy → Mnemonic"""
    return mnemo.to_mnemonic(entropy_bytes)

def common_patterns():
    """Rockyou-style patterns"""
    words = ["password", "123456", "bitcoin", "wallet", "money", "crypto"]
    return " ".join(random.choices(words, k=12))