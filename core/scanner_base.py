# core/scanner_base.py
import requests
from config import USER_AGENT, TIMEOUT

class ScannerBase:
    def __init__(self, target):
        if not target.startswith(('http://', 'https://')):
            target = f"http://{target}"
        self.target = target.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': USER_AGENT})
        self.timeout = TIMEOUT

    def _send_request(self, url, method='GET', **kwargs):
        try:
            resp = self.session.request(
                method,
                url,
                timeout=self.timeout,
                **kwargs
            )
            return resp
        except requests.RequestException as e:
            print(f"[!] Request failed: {str(e)}")
            return None

    def scan(self):
        raise NotImplementedError("Scan method must be implemented by subclass")
