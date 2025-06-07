# core/dispatcher.py
from modules.recon.subdomain_enum import SubdomainEnumerator
from modules.scanners.xss_scanner import XSSScanner
from modules.scanners.sqli_scanner import SQLIScanner
from modules.scanners.rce_scanner import RCEScanner
import validators

class Dispatcher:
    def run_all(self):
        print("""
        ╔════════════════════════════╗
        ║    🚀 SCAN DISPATCHER 🚀   ║
        ╚════════════════════════════╝
        """)
        
        while True:
            target = input("[?] Enter target domain or URL: ").strip()
            if not target:
                print("[!] Please enter a valid target")
                continue
                
            if not validators.url(target) and not validators.domain(target):
                print("[!] Invalid target format. Please enter a valid URL or domain")
                continue
                
            break

        scanners = [
            SubdomainEnumerator(target),
            XSSScanner(target),
            SQLIScanner(target),
            RCEScanner(target)
        ]

        for scanner in scanners:
            try:
                if hasattr(scanner, 'run'):
                    scanner.run()
                elif hasattr(scanner, 'scan'):
                    scanner.scan()
            except Exception as e:
                print(f"[!] Error running {scanner.__class__.__name__}: {str(e)}")
                continue
