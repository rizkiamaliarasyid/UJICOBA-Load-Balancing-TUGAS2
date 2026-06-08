import concurrent.futures
import urllib.request
import re

url = "http://localhost:8085"

def ambil_nama_server(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            html = response.read().decode('utf-8')
            # Mencari teks di dalam tag <h1> atau teks WEB SERVER
            match = re.search(r'WEB SERVER [A-Z ]*\(?([a-zA-Z0-9_-]+)\)?', html)
            if match:
                return match.group(1)
            return "Server Terpanggil (Nama tidak ketemu)"
    except Exception as e:
        return f"Error: {e}"

print("--- MEMULAI PENGUJIAN BERSAMAAN ---")
# Menembak 5 request secara SEKALIGUS (Simultan)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    urls = [url] * 5
    hasil = list(executor.map(ambil_nama_server, urls))

# Cetak hasilnya
for i, nama in enumerate(hasil, 1):
    print(f"Request {i}: Terarah ke -> {nama}")
    