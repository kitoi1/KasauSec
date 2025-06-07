# core/engine.py
import time
from core.dispatcher import Dispatcher

class KasauSecEngine:
    def start(self):
        print("""
        ╔════════════════════════════╗
        ║    ⚡ KASAUSEC ENGINE ⚡    ║
        ╚════════════════════════════╝
        """)
        print("[*] Initializing Scan Engine...")
        time.sleep(1)
        
        try:
            print("[*] Launching Dispatcher...")
            Dispatcher().run_all()
        except Exception as e:
            print(f"[!] Engine Error: {str(e)}")
            raise
