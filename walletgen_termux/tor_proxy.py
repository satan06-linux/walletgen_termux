"""
TOR Proxy Configuration for Termux
"""

import socks
import socket

def setup_tor(host='127.0.0.1', port=9050):
    """Setup TOR socks5 proxy"""
    socks.set_default_proxy(socks.SOCKS5, host, port)
    socket.socket = socks.socksocket
    print(f"✅ TOR Proxy: socks5://{host}:{port}")

def test_tor():
    """Test TOR connection"""
    try:
        import requests
        resp = requests.get('http://httpbin.org/ip', timeout=10)
        print(f"🌐 TOR IP: {resp.json()['origin']}")
        return True
    except:
        print("❌ TOR test failed")
        return False