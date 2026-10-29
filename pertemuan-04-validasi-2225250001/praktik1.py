# Praktik 1 - Penilaian Mahasiswa
# Nama  : Aulia Rahma Ramadhani
# NIM   : 2225250001

print("=== Praktik 1 Penilaian Mahasiswa ===")

# Input (dibaca sebagai teks terlebih dahulu)
teks_ujian = input("Nilai ujian (0-100): ").strip()
teks_tugas = input("Nilai tugas (0-100): ").strip()
teks_hadir = input("Kehadiran (%): ").strip()

# Validasi tipe data
try:
    ujian = float(teks_ujian)
    tugas = float(teks_tugas)
    hadir = float(teks_hadir)
except ValueError:
    print("Pesan penolakan: data harus berupa angka.")
    exit()

# Validasi rentang
if not (0 <= ujian <= 100):
    print("Pesan penolakan: nilai ujian di luar rentang 0 sampai 100.")
elif not (0 <= tugas <= 100):
    print("Pesan penolakan: nilai tugas di luar rentang 0 sampai 100.")
elif not (0 <= hadir <= 100):
    print("Pesan penolakan: kehadiran di luar rentang 0 sampai 100.")
else:
    # Hitung nilai akhir
    akhir = (0.6 * ujian) + (0.4 * tugas)

    # Menentukan predikat
    if akhir >= 85:
        predikat = "A"
    elif akhir >= 70:
        predikat = "B"
    elif akhir >= 60:
        predikat = "C"
    elif akhir >= 50:
        predikat = "D"
    else:
        predikat = "E"

    # Menentukan status kelulusan
    if hadir < 80:
        status = "Tidak memenuhi syarat kehadiran"
    elif predikat in ["A", "B", "C"]:
        status = "Lulus"
    else:
        status = "Belum Lulus"

    # Output
    print("\n===== HASIL =====")
    print(f"Nilai Akhir : {akhir:.2f}")
    print(f"Predikat    : {predikat}")
    print(f"Status      : {status}")