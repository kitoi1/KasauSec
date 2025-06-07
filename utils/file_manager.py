# utils/file_manager.py
import os
import hashlib
from pathlib import Path

def _print_file_logo():
    print("""
    ╔════════════════════════════╗
    ║     📁 FILE MANAGER 📁     ║
    ╚════════════════════════════╝
    """)

class FileManager:
    def __init__(self):
        _print_file_logo()

    def read_lines(self, file_path):
        """Read file and return lines as list"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f.readlines() if line.strip()]
        except Exception as e:
            print(f"[!] Failed to read {file_path}: {str(e)}")
            return []

    def write_lines(self, file_path, lines, mode='w'):
        """Write lines to file"""
        try:
            with open(file_path, mode, encoding='utf-8') as f:
                f.writelines(f"{line}\n" for line in lines)
            return True
        except Exception as e:
            print(f"[!] Failed to write {file_path}: {str(e)}")
            return False

    def get_file_hash(self, file_path, algorithm='sha256'):
        """Calculate file hash"""
        try:
            hasher = hashlib.new(algorithm)
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            print(f"[!] Failed to hash {file_path}: {str(e)}")
            return None

    def ensure_directory(self, dir_path):
        """Create directory if it doesn't exist"""
        try:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            print(f"[!] Failed to create directory {dir_path}: {str(e)}")
            return False
          
