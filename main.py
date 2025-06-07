# main.py
import sys
from core.engine import KasauSecEngine

def main():
    print("""
    ██╗  ██╗ █████╗ ███████╗ █████╗ ██╗   ██╗███████╗███████╗ ██████╗
    ██║ ██╔╝██╔══██╗██╔════╝██╔══██╗██║   ██║██╔════╝██╔════╝██╔═══██╗
    █████╔╝ ███████║███████╗███████║██║   ██║█████╗  █████╗  ██║   ██║
    ██╔═██╗ ██╔══██║╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══╝  ██║   ██║
    ██║  ██╗██║  ██║███████║██║  ██║ ╚████╔╝ ███████╗███████╗╚██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝ ╚═════╝
    """)
    print("🔥 KasauSec Terminal Interface v2.0 🔥")
    print("🔐 Advanced Security Scanner Framework 🔐\n")
    
    try:
        KasauSecEngine().start()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Critical error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
