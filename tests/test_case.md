# Dokumentasi Pengujian Program

Pengujian dilakukan untuk memeriksa validasi nilai, perhitungan statistik, ketuntasan, dan penanganan kesalahan.

| Kode | Skenario Pengujian | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| TC01 | Nilai 80, 70, 90 | Rata-rata 80, minimum 70, maksimum 90 | Sesuai harapan | Lulus |
| TC02 | Nilai 0 | Nilai diterima | True | Lulus |
| TC03 | Nilai 100 | Nilai diterima | True | Lulus |
| TC04 | Nilai 105 | Nilai ditolak | False | Lulus |
| TC05 | File tidak ditemukan | Pesan kesalahan dan daftar kosong | Pesan kesalahan dan daftar kosong | Lulus |
| TC06 | Semua nilai minimal 75 | Semua data tuntas | 3 tuntas, 0 tidak tuntas | Lulus |

## Kesimpulan

Berdasarkan enam skenario pengujian, hasil program sesuai dengan hasil yang diharapkan. Pengujian mencakup nilai batas, nilai di luar rentang, perhitungan statistik, penanganan file yang tidak ditemukan, dan penentuan ketuntasan berdasarkan KKM 75.