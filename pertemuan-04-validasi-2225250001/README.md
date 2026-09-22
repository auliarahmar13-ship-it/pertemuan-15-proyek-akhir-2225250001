# Pertemuan 04 — Seleksi Multi-Kondisi dan Validasi Input

**Nama:** Aulia Rahma Ramadhani
**NIM:** 2225250001
**Kelas:** 3A

---

# Tujuan

Praktikum Pertemuan 04 bertujuan mempelajari penggunaan **percabangan if, elif, dan else**, serta penerapan **validasi input** pada program Python. Selain menentukan keputusan berdasarkan beberapa kondisi, praktikum ini juga melatih penanganan kesalahan input agar program lebih aman, mudah digunakan, dan menghasilkan keluaran yang sesuai dengan aturan yang telah ditentukan.

Materi yang dipraktikkan meliputi klasifikasi nilai, kategori bilangan, validasi rentang angka, validasi tipe data, klasifikasi segitiga berdasarkan sudut, serta penggabungan seluruh konsep tersebut pada satu program praktik.

---

# Struktur Folder

```
pertemuan-04-validasi-2225250001/
│
├── README.md
│
├── latihan/
│   ├── 01_predikat_nilai.py
│   ├── 02_kategori_bilangan.py
│   ├── 03_validasi_rentang.py
│   ├── 04_validasi_tipe.py
│   └── 05_klasifikasi_segitiga_sudut.py
│
└── praktik/
    └── validasi_klasifikasi_nilai.py
```

---

# Cara Menjalankan Program

1. Buka folder **pertemuan-04-validasi-2225250001** di VS Code.
2. Buka menu **Terminal → New Terminal**.
3. Pastikan posisi terminal berada pada folder proyek.
4. Jalankan program menggunakan perintah berikut.

**Latihan 1**

```bash
python latihan/01_predikat_nilai.py
```

**Latihan 2**

```bash
python latihan/02_kategori_bilangan.py
```

**Latihan 3**

```bash
python latihan/03_validasi_rentang.py
```

**Latihan 4**

```bash
python latihan/04_validasi_tipe.py
```

**Latihan 5**

```bash
python latihan/05_klasifikasi_segitiga_sudut.py
```

**Praktik 1**

```bash
python praktik/validasi_klasifikasi_nilai.py
```

---

# Algoritma Setiap Program

## Latihan 1 — Predikat Nilai

**Input:** Nilai akhir (0–100)

**Proses:**

* Membaca nilai bertipe float.
* Memeriksa nilai menggunakan rantai `if-elif-else`.
* Menentukan predikat A, B, C, D, atau E.
* Menampilkan nilai beserta predikatnya.

**Output:** Predikat nilai mahasiswa.

---

## Latihan 2 — Kategori Bilangan

**Input:** Satu bilangan bulat.

**Proses:**

* Memeriksa apakah bilangan negatif.
* Jika tidak, memeriksa apakah bernilai nol.
* Jika positif, memeriksa sisa bagi 2.
* Menentukan kategori genap atau ganjil.

**Output:** Negatif, Nol, Positif Genap, atau Positif Ganjil.

---

## Latihan 3 — Validasi Rentang

**Input:** Nilai ujian.

**Proses:**

* Memastikan nilai berada pada rentang 0–100.
* Jika valid, menentukan predikat.
* Jika di luar rentang, menampilkan pesan kesalahan.

**Output:** Predikat atau pesan validasi.

---

## Latihan 4 — Validasi Tipe

**Input:** Jumlah soal benar.

**Proses:**

* Menggunakan `try-except`.
* Mengubah input menjadi integer.
* Menghitung persentase benar.
* Menentukan status tuntas jika ≥75%.

**Output:** Persentase dan status tuntas.

---

## Latihan 5 — Klasifikasi Segitiga Berdasarkan Sudut

**Input:** Tiga besar sudut.

**Proses:**

* Memastikan semua sudut positif.
* Memastikan jumlah sudut = 180°.
* Menentukan sudut terbesar.
* Mengklasifikasikan segitiga menjadi lancip, siku-siku, atau tumpul.

**Output:** Jenis segitiga atau pesan penolakan.

---

## Praktik 1 — Validasi Klasifikasi Nilai

**Input:** Nilai ujian, tugas, dan kehadiran.

**Proses:**

1. Membersihkan spasi menggunakan `.strip()`.
2. Memvalidasi tipe data dengan `try-except`.
3. Memastikan nilai berada pada rentang 0–100.
4. Menghitung nilai akhir = 0.6 × ujian + 0.4 × tugas.
5. Menentukan predikat A–E.
6. Memeriksa syarat kehadiran minimal 80%.
7. Menentukan status Lulus atau Belum Lulus.

**Output:** Nilai akhir, predikat, dan status kelulusan.

---

# Tabel Keputusan

| Kondisi             | Hasil                 |
| ------------------- | --------------------- |
| Nilai ≥ 85          | Predikat A            |
| 70 ≤ Nilai < 85     | Predikat B            |
| 60 ≤ Nilai < 70     | Predikat C            |
| 50 ≤ Nilai < 60     | Predikat D            |
| Nilai < 50          | Predikat E            |
| Kehadiran ≥ 80%     | Memenuhi syarat hadir |
| Kehadiran < 80%     | Belum lulus           |
| Jumlah sudut = 180° | Segitiga valid        |
| Jumlah sudut ≠ 180° | Ditolak               |

---

# Hasil Pengujian

## Latihan 1 — Predikat Nilai

| Input | Keluaran yang Diharapkan | Status   |
| ----- | ------------------------ | -------- |
| 92    | Predikat A               | Berhasil |
| 85    | Predikat A               | Berhasil |
| 84.9  | Predikat B               | Berhasil |
| 70    | Predikat B               | Berhasil |
| 60    | Predikat C               | Berhasil |
| 50    | Predikat D               | Berhasil |
| 49.9  | Predikat E               | Berhasil |

### Kesimpulan

Program berhasil mengelompokkan nilai ke dalam lima predikat sesuai batas yang diberikan menggunakan rantai `if-elif-else`.

---

## Latihan 2 — Kategori Bilangan

| Input | Keluaran                | Status   |
| ----- | ----------------------- | -------- |
| -5    | Bilangan negatif        | Berhasil |
| 0     | Bilangan nol            | Berhasil |
| 8     | Bilangan positif genap  | Berhasil |
| 13    | Bilangan positif ganjil | Berhasil |

### Kesimpulan

Setiap bilangan hanya masuk ke satu kategori sehingga kondisi saling lepas dan tidak bertumpuk.

---

## Latihan 3 — Validasi Rentang

| Input | Keluaran              | Status   |
| ----- | --------------------- | -------- |
| 95    | Predikat A            | Berhasil |
| 75    | Predikat B            | Berhasil |
| 40    | Predikat E            | Berhasil |
| 120   | Nilai di luar rentang | Berhasil |
| -10   | Nilai di luar rentang | Berhasil |

### Kesimpulan

Validasi berhasil mencegah nilai yang tidak berada pada rentang 0–100 diproses lebih lanjut.

---

## Latihan 4 — Validasi Tipe

| Input     | Keluaran             | Status   |
| --------- | -------------------- | -------- |
| 15        | 75% dan Tuntas       | Berhasil |
| 14        | 70% dan Belum Tuntas | Berhasil |
| 20        | 100% dan Tuntas      | Berhasil |
| 0         | 0% dan Belum Tuntas  | Berhasil |
| 21        | Pesan rentang        | Berhasil |
| dua belas | Pesan tipe           | Berhasil |

### Kesimpulan

Penggunaan `try-except` berhasil menangani input yang bukan angka tanpa menyebabkan program berhenti.

---

## Latihan 5 — Klasifikasi Segitiga

| Input     | Keluaran                | Status   |
| --------- | ----------------------- | -------- |
| 60,60,60  | Segitiga lancip         | Berhasil |
| 90,45,45  | Segitiga siku-siku      | Berhasil |
| 120,30,30 | Segitiga tumpul         | Berhasil |
| 100,50,40 | Jumlah sudut tidak 180° | Berhasil |
| 0,90,90   | Sudut harus positif     | Berhasil |

### Kesimpulan

Program melakukan validasi terlebih dahulu sebelum menentukan jenis segitiga sehingga hasil lebih akurat.

---

## Praktik 1 — Validasi Klasifikasi Nilai

| Ujian | Tugas | Hadir | Nilai Akhir | Hasil                   | Status      |
| ----- | ----- | ----- | ----------- | ----------------------- | ----------- |
| 90    | 80    | 85    | 86.00       | A                       | Lulus       |
| 75    | 70    | 85    | 73.00       | B                       | Lulus       |
| 60    | 60    | 80    | 60.00       | C                       | Lulus       |
| 50    | 50    | 80    | 50.00       | D                       | Belum Lulus |
| 40    | 30    | 100   | 36.00       | E                       | Belum Lulus |
| 90    | 90    | 75    | 90.00       | A                       | Belum Lulus |
| 105   | 80    | 90    | -           | Nilai ujian tidak valid | Berhasil    |
| 80    | -6    | 90    | -           | Nilai tugas tidak valid | Berhasil    |
| 80    | 80    | abc   | -           | Kehadiran bukan angka   | Berhasil    |

### Kesimpulan

Seluruh test case berhasil dijalankan sesuai spesifikasi. Program mampu menangani kesalahan tipe data, kesalahan rentang nilai, menghitung nilai akhir, menentukan predikat, serta menetapkan status kelulusan berdasarkan dua syarat sekaligus.

---

# Refleksi

Pada praktikum Pertemuan 04 saya mempelajari bahwa penyusunan kondisi harus dilakukan secara berurutan agar keputusan yang dihasilkan benar. Saya juga memahami pentingnya validasi sebelum melakukan proses perhitungan, karena data yang tidak valid dapat menyebabkan hasil menjadi salah atau program mengalami error.

Kesalahan yang sempat saya temui adalah menjalankan file Python dari direktori yang salah sehingga muncul pesan **No such file or directory**. Masalah tersebut berhasil diperbaiki dengan memastikan terminal berada pada folder proyek dan menjalankan file menggunakan lokasi yang benar.

Selain itu, saya belajar menggunakan `try-except` untuk menangani kesalahan input, sehingga ketika pengguna memasukkan teks seperti **abc**, program tidak berhenti tetapi menampilkan pesan bahwa input harus berupa angka. Hal ini membuat program menjadi lebih aman, lebih mudah digunakan, dan sesuai dengan prinsip validasi input yang dipelajari pada pertemuan ini.

---

# Kesimpulan Praktikum

Praktikum ini berhasil menggabungkan konsep percabangan, operator logika, nested if, validasi rentang, serta penanganan kesalahan tipe data ke dalam berbagai studi kasus. Seluruh latihan dan praktik dapat dijalankan dengan baik, menghasilkan keluaran yang sesuai dengan spesifikasi, dan memberikan pemahaman mengenai pembuatan program yang lebih terstruktur serta lebih andal dalam menerima masukan dari pengguna.
