# core/report_manager.py
import os
from datetime import datetime
from config import OUTPUT_DIR

class ReportManager:
    def __init__(self, scan_name):
        self.scan_name = scan_name
        self.results = []
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.report_file = os.path.join(OUTPUT_DIR, f"{scan_name}_{self.timestamp}.txt")

    def add_result(self, result):
        self.results.append(result)

    def save(self):
        if not self.results:
            print("[!] No results to save")
            return False

        try:
            with open(self.report_file, 'w') as f:
                f.write(f"KasauSec Scan Report - {self.scan_name}\n")
                f.write(f"Generated at: {self.timestamp}\n\n")
                f.write("="*50 + "\n")
                for r in self.results:
                    f.write(f"{r}\n")
            print(f"[+] Report saved to {self.report_file}")
            return True
        except IOError as e:
            print(f"[!] Error saving report: {str(e)}")
            return False
