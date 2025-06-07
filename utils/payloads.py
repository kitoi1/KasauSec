# utils/payloads.py
import os
import json
from pathlib import Path

def _print_payloads_logo():
    print("""
    ╔════════════════════════════╗
    ║     🎯 PAYLOAD MANAGER 🎯   ║
    ╚════════════════════════════╝
    """)

class PayloadManager:
    def __init__(self, base_path="assets/payloads"):
        _print_payloads_logo()
        self.base_path = base_path
        Path(base_path).mkdir(parents=True, exist_ok=True)

    def load(self, payload_type):
        """Load payloads from file"""
        path = os.path.join(self.base_path, f"{payload_type}.txt")
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Payload file not found: {path}")
                
            with open(path, 'r') as f:
                return [line.strip() for line in f if line.strip()]
                
        except Exception as e:
            print(f"[!] Failed to load payloads: {str(e)}")
            return []

    def save(self, payload_type, payloads):
        """Save payloads to file"""
        path = os.path.join(self.base_path, f"{payload_type}.txt")
        try:
            with open(path, 'w') as f:
                f.writelines(f"{p}\n" for p in payloads)
            return True
        except Exception as e:
            print(f"[!] Failed to save payloads: {str(e)}")
            return False

    def load_json(self, payload_type):
        """Load JSON formatted payloads"""
        path = os.path.join(self.base_path, f"{payload_type}.json")
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"[!] Failed to load JSON payloads: {str(e)}")
            return {}
