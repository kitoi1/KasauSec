# config.py
import os

# Configuration Settings
OUTPUT_DIR = "reports/"
THREADS = 10
TIMEOUT = 5
USER_AGENT = "KasauSecScanner/2.0"

# Ensure output directory exists
try:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
except OSError as e:
    print(f"[!] Error creating output directory: {e}")
