import urllib.request
import re
import time

url = "http://localhost:8085"

print("--- MEMULAI PENGUJIAN ROUND ROBIN (ANTREAN SATU PER SATU) ---")

for i in range(1, 6):
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            html = response.read().decode('utf-8')
            match = re.search(r'WEB SERVER [A-Z ]*\(?([a-zA-Z0-9_-]+)\)?', html)
            nama_server = match.group(1) if match else "Tidak ketemu"
            print(f"Request {i}: Terarah ke -> {nama_server}")
        # Beri jeda sedikit agar server tidak kaget
        time.sleep(0.1)
    except Exception as e:
        print(f"Request {i}: Error -> {e}")