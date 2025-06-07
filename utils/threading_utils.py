# utils/threading_utils.py
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..config import THREADS

def _print_threading_logo():
    print("""
    ╔════════════════════════════╗
    ║     🔄 THREAD MANAGER 🔄    ║
    ╚════════════════════════════╝
    """)

class ThreadManager:
    def __init__(self, max_workers=THREADS):
        _print_threading_logo()
        self.max_workers = max_workers

    def run_concurrently(self, tasks, func, callback=None):
        """Run tasks concurrently with ThreadPoolExecutor"""
        results = []
        try:
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                future_to_task = {
                    executor.submit(func, task): task 
                    for task in tasks
                }
                
                for future in as_completed(future_to_task):
                    task = future_to_task[future]
                    try:
                        result = future.result()
                        if callback:
                            callback(task, result)
                        results.append(result)
                    except Exception as e:
                        print(f"[!] Task failed: {task} - {str(e)}")
                        
            return results
        except Exception as e:
            print(f"[!] Thread pool error: {str(e)}")
            return []

    def map_concurrently(self, iterable, func):
        """Simple parallel mapping"""
        try:
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                return list(executor.map(func, iterable))
        except Exception as e:
            print(f"[!] Mapping error: {str(e)}")
            return []
