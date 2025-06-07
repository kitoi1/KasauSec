# utils/logger.py
from datetime import datetime
import sys

class Logger:
    def __init__(self, name="KASAUSEC"):
        self.name = name
        self._print_logo()

    def _print_logo(self):
        print(f"""
        ╔════════════════════════════╗
        ║     📜 {self.name} LOGGER 📜    ║
        ╚════════════════════════════╝
        """)

    def _timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def info(self, message):
        print(f"[{self._timestamp()}] ℹ️  INFO: {message}")

    def warning(self, message):
        print(f"[{self._timestamp()}] ⚠️  WARN: {message}", file=sys.stderr)

    def error(self, message):
        print(f"[{self._timestamp()}] ✖ ERROR: {message}", file=sys.stderr)

    def success(self, message):
        print(f"[{self._timestamp()}] ✔ SUCCESS: {message}")

    def debug(self, message):
        print(f"[{self._timestamp()}] 🐛 DEBUG: {message}")

    def critical(self, message):
        print(f"[{self._timestamp()}] ‼️ CRITICAL: {message}", file=sys.stderr)
        sys.exit(1)
