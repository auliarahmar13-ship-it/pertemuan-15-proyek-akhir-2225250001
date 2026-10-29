# Proyek Akhir Algoritma dan Pemrograman

## Identitas Mahasiswa

| Keterangan | Isi |
|---|---|
| Nama | Aulia Rahma Ramadhani |
| NIM | 2225250001 |
| Kelas | 3A |
| Mata Kuliah | Algoritma dan Pemrograman |

## Deskripsi Proyek

Proyek ini dirancang untuk membuat **Program Rekap dan Analisis Nilai Matematika Kelas**. Program digunakan untuk membaca data nilai mahasiswa dari file, memvalidasi nilai, menghitung statistik nilai, menentukan status ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM), dan menyimpan hasil analisis ke dalam file laporan.

Pada tahap Pertemuan 14, proyek berfokus pada perancangan program sebelum dilanjutkan ke tahap implementasi dan pengujian.

## Tujuan Proyek

1. Membaca data nilai dari file.
2. Memvalidasi nilai agar berada pada rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Menentukan status ketuntasan berdasarkan KKM 75.
5. Menyimpan hasil analisis ke dalam file laporan teks.

## Fitur Program

- Membaca data nilai dari file.
- Memvalidasi format data dan rentang nilai.
- Menghitung statistik nilai.
- Menentukan jumlah mahasiswa tuntas dan tidak tuntas.
- Menyimpan hasil analisis ke dalam file laporan.
- Menangani kondisi file tidak ditemukan dan data tidak valid.

## Struktur Folder

```text
pertemuan-14-proyek-akhir-2225250001/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

## Kebutuhan Program

- Python
- Visual Studio Code
- Git
- GitHub

## Cara Menjalankan Program

Setelah tahap implementasi selesai, program direncanakan dapat dijalankan melalui terminal pada folder utama proyek dengan perintah:

```bash
python src/main.py
```

## Rencana Pengujian

| Kode | Skenario Pengujian | Hasil yang Diharapkan |
|---|---|---|
| TC01 | Data nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Nilai 0 | Nilai diterima |
| TC03 | Nilai 100 | Nilai diterima |
| TC04 | Nilai 105 | Nilai ditolak dengan pesan validasi |
| TC05 | File data tidak ditemukan | Program menangani kesalahan |
| TC06 | Semua nilai minimal 75 | Semua mahasiswa dinyatakan tuntas |

## Status Proyek

Tahap saat ini: **Implementasi, Pengujian, Debugging, dan Dokumentasi (Pertemuan 15)**.

Program telah diimplementasikan dan pengujian TC01–TC06 telah dilakukan. Hasil pengujian sesuai dengan hasil yang diharapkan.

Tahap selanjutnya adalah presentasi atau demonstrasi proyek pada Pertemuan 16.

## Repository GitHub

(https://github.com/auliarahmar13-ship-it/pertemuan-14-proyek-akhir-2225250001)
