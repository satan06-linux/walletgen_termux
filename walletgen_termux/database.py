"""
Offline Database of Known Rich Addresses
Download full DB: https://github.com/tony-btc0/seed-phrase-generator/releases
"""

import json
import os

DB_FILE = "rich_addresses.json"

# Sample DB (expand with real data)
RICH_DB = {
    "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa": 50.0,
    "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh": 10.0,
    "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2": 100.0
}

def load_db():
    """Load rich address database"""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return RICH_DB

def check_offline(addr):
    """Fast offline check"""
    db = load_db()
    return db.get(addr, 0)

def is_rich_hit(addr, balance):
    """$50+ rich hit detector"""
    offline_bal = check_offline(addr)
    return offline_bal > 0 or balance > 50