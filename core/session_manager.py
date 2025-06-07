# core/session_manager.py
import pickle
import os
from config import OUTPUT_DIR

class SessionManager:
    def __init__(self, session_name):
        self.session_name = session_name
        self.session_file = os.path.join(OUTPUT_DIR, f"{session_name}.session")
        self.session_data = {}

    def save_session(self):
        try:
            with open(self.session_file, 'wb') as f:
                pickle.dump(self.session_data, f)
            return True
        except Exception as e:
            print(f"[!] Error saving session: {str(e)}")
            return False

    def load_session(self):
        if not os.path.exists(self.session_file):
            return False
            
        try:
            with open(self.session_file, 'rb') as f:
                self.session_data = pickle.load(f)
            return True
        except Exception as e:
            print(f"[!] Error loading session: {str(e)}")
            return False

    def get(self, key, default=None):
        return self.session_data.get(key, default)

    def set(self, key, value):
        self.session_data[key] = value
