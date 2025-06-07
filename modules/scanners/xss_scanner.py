# modules/scanners/xss_scanner.py
from core.scanner_base import ScannerBase
from core.report_manager import ReportManager

class XSSScanner(ScannerBase):
    def __init__(self, target):
        super().__init__(target)
        self.report = ReportManager("xss_scan")

    def scan(self):
        print("""
        ╔════════════════════════════╗
        ║     🧪 XSS SCANNER 🧪      ║
        ╚════════════════════════════╝
        """)
        
        print(f"[*] Scanning {self.target} for XSS vulnerabilities...")
        
        payloads = [
            '<script>alert(1)</script>',
            '" onerror="alert(1)"',
            "'><img src=x onerror=alert(1)>",
            'javascript:alert(1)'
        ]
        
        vulnerable = False
        
        for payload in payloads:
            test_url = f"{self.target}/search?q={payload}"
            print(f"[*] Testing payload: {payload[:20]}...")
            
            resp = self._send_request(test_url)
            if resp and payload in resp.text:
                print(f"[!] Potential XSS found with payload: {payload[:20]}...")
                self.report.add_result(f"XSS Vulnerability: {test_url}")
                vulnerable = True
                
        if not vulnerable:
            print("[+] No XSS vulnerabilities detected")
            self.report.add_result("No XSS vulnerabilities found")
            
        self.report.save()
