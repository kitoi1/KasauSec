
# utils/http_helpers.py
import requests
from time import time
from ..config import TIMEOUT, USER_AGENT

def _print_http_logo():
    print("""
    ╔════════════════════════════╗
    ║     🌐 HTTP HELPER 🌐      ║
    ╚════════════════════════════╝
    """)

def get(url, headers=None, timeout=TIMEOUT):
    _print_http_logo()
    headers = headers or {}
    headers.setdefault('User-Agent', USER_AGENT)
    
    try:
        start = time()
        response = requests.get(
            url, 
            headers=headers, 
            timeout=timeout,
            allow_redirects=False,
            verify=False
        )
        elapsed = (time() - start) * 1000
        print(f"[→] GET {url} - {response.status_code} ({elapsed:.2f}ms)")
        return response
    except requests.exceptions.RequestException as e:
        print(f"[✗] GET {url} - Error: {type(e).__name__}")
        return None
    except Exception as e:
        print(f"[!] Unexpected GET error: {str(e)}")
        return None

def post(url, data=None, json=None, headers=None, timeout=TIMEOUT):
    _print_http_logo()
    headers = headers or {}
    headers.setdefault('User-Agent', USER_AGENT)
    headers.setdefault('Content-Type', 'application/x-www-form-urlencoded')
    
    try:
        start = time()
        response = requests.post(
            url,
            data=data,
            json=json,
            headers=headers,
            timeout=timeout,
            allow_redirects=False,
            verify=False
        )
        elapsed = (time() - start) * 1000
        print(f"[→] POST {url} - {response.status_code} ({elapsed:.2f}ms)")
        return response
    except requests.exceptions.RequestException as e:
        print(f"[✗] POST {url} - Error: {type(e).__name__}")
        return None
    except Exception as e:
        print(f"[!] Unexpected POST error: {str(e)}")
        return None
