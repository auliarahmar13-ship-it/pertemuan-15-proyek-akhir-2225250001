# Proposal Proyek Akhir Algoritma dan Pemrograman

## 1. Judul Proyek

**Program Rekap dan Analisis Nilai Matematika Kelas**

## 2. Latar Belakang

Pengolahan nilai matematika memerlukan proses pencatatan, pemeriksaan, dan perhitungan agar hasilnya dapat diketahui dengan lebih mudah. Oleh karena itu, dirancang sebuah program sederhana untuk membaca data nilai, memvalidasi data, menghitung statistik nilai, menentukan ketuntasan, dan menyimpan laporan hasil analisis.

## 3. Pengguna dan Tujuan

**Pengguna:** Guru atau pihak yang mengolah nilai matematika kelas.

**Tujuan:**
1. Mempermudah pembacaan data nilai dari file.
2. Memeriksa validitas nilai.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Menentukan status ketuntasan berdasarkan KKM.
5. Menghasilkan laporan analisis nilai.

## 4. Ruang Lingkup Proyek

Program dirancang untuk:
- Membaca data nilai dari file.
- Memvalidasi nilai dalam rentang 0–100.
- Menghitung statistik nilai yang valid.
- Menentukan status tuntas dan tidak tuntas berdasarkan KKM 75.
- Menyimpan laporan ke file teks.
- Menangani file yang tidak ditemukan dan data yang tidak valid.

## 5. Kebutuhan Program

### Kebutuhan perangkat lunak
- Python
- Visual Studio Code
- Git
- GitHub

### Kebutuhan fungsional
1. Program dapat membaca data nilai dari file.
2. Program dapat memvalidasi data dan rentang nilai.
3. Program dapat menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Program dapat menentukan status ketuntasan.
5. Program dapat menyimpan hasil analisis ke file laporan.
6. Program dapat menangani kesalahan pembacaan file dan data tidak valid.

## 6. Rancangan Input, Proses, dan Output (IPO)

| Bagian | Keterangan |
|---|---|
| Input | Data nama dan nilai dari file |
| Proses | Membaca file, memvalidasi data, menghitung statistik, menentukan status ketuntasan |
| Output | Ringkasan statistik dan laporan hasil analisis dalam file teks |

## 7. Algoritma dan Pseudocode

```text
MULAI
    baca data dari file

    jika file tidak ditemukan:
        tampilkan pesan error
        SELESAI

    untuk setiap baris data:
        validasi format dan nilai
        simpan data valid

    jika tidak ada data valid:
        tampilkan pesan
        SELESAI

    hitung rata-rata, nilai minimum, dan nilai maksimum
    tentukan status ketuntasan berdasarkan KKM 75
    tampilkan ringkasan
    simpan laporan ke file teks
SELESAI
```

## 8. Rancangan Struktur Program

Program direncanakan terdiri atas beberapa fungsi berikut:

| Fungsi | Tugas |
|---|---|
| `baca_data()` | Membaca data dari file |
| `validasi_nilai()` | Memeriksa format dan rentang nilai |
| `hitung_statistik()` | Menghitung statistik nilai |
| `tentukan_status()` | Menentukan status ketuntasan |
| `simpan_laporan()` | Menyimpan laporan ke file |
| `main()` | Mengatur jalannya program |

## 9. Rancangan Struktur Data

1. **List:** Menyimpan kumpulan nilai yang valid.
2. **Dictionary atau list berisi dictionary:** Menyimpan data nama dan nilai setiap mahasiswa.
3. **String dan file teks:** Menyimpan serta menuliskan laporan hasil analisis.

## 10. Rencana Pengujian

| Kode | Data atau Kondisi | Hasil yang Diharapkan |
|---|---|---|
| TC01 | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Nilai 105 | Ditolak dengan pesan validasi |
| TC05 | File tidak ditemukan | Program menampilkan pesan kesalahan |
| TC06 | Semua nilai minimal 75 | Semua data dinyatakan tuntas |

## 11. Pembagian Tugas

Proyek dikerjakan secara individu.

| Tugas | Penanggung Jawab |
|---|---|
| Perancangan proposal | Mahasiswa |
| Perancangan algoritma dan struktur program | Mahasiswa |
| Implementasi program | Mahasiswa |
| Pengujian dan debugging | Mahasiswa |
| Dokumentasi dan presentasi | Mahasiswa |

## 12. Jadwal Pengerjaan

| Pertemuan | Rencana Kegiatan |
|---|---|
| Pertemuan 14 | Perancangan proyek, proposal, algoritma, struktur program, dan test case |
| Pertemuan 15 | Implementasi, pengujian, debugging, dan dokumentasi |
| Pertemuan 16 | Presentasi atau demonstrasi proyek |

## 13. Repository GitHub

Tautan repository akan ditambahkan setelah repository GitHub dibuat.

