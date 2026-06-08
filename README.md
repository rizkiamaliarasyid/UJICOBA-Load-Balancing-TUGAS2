# LAPORAN HASIL PENGUJIAN LOAD BALANCING
## ANALISIS PERBANDINGAN ALGORITMA ROUND ROBIN DAN LEAST CONNECTIONS

## 👤 Identitas Mahasiswa & Akademik

* **Nama Lengkap :** Rizki Amalia Rasyid Ridha
* **NIM :** 105841121223
* **Kelas :** RPL 6 A
* **Dosen Pengampu :** Runal Rezkiawan, S.Kom., M.T.

**PROGRAM STUDI INFORMATIKA** **FAKULTAS TEKNIK** **UNIVERSITAS MUHAMMADIYAH MAKASSAR** **2026**

---

## 🚀 Arsitektur Kluster Server
Sistem ini mengorkestrasi 4 kontainer Docker yang berjalan bersamaan di dalam satu jaringan lokal virtual (*bridge network*):
* **Nginx Load Balancer** (Berjalan pada Port utama host: `8085`)
* **Web Server 1** (`web-1` - Aplikasi Flask Port `5000`)
* **Web Server 2** (`web-2` - Aplikasi Flask Port `5000`)
* **Web Server 3** (`web-3` - Aplikasi Flask Port `5000`)

## 🛠️ Struktur Komponen Kode Program
* `docker-compose.yml` - Konfigurasi manajemen dan orkestrasi multi-kontainer Docker.
* `nginx.conf` - Berkas inti pengaturan konfigurasi arsitektur algoritma *Load Balancing*.
* `app.py` - Aplikasi web utama berbasis Flask dengan simulasi waktu proses konstan sebesar 0.1 detik.
* `tes.py` - Skrip otomatisasi pengujian beban simultan menggunakan pendekatan *multi-threading*.

## 🧪 Metode & Algoritma yang Dianalisis
1. **Round Robin (RR):** Distribusi lalu lintas data secara bergilir dan berurutan kaku ke setiap kontainer *backend* tanpa memedulikan status beban aktual pada server.
2. **Least Connections (LC):** Distribusi lalu lintas data secara dinamis berdasarkan hasil evaluasi metrik jumlah koneksi aktif paling sedikit secara *real-time*.
