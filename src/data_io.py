
def baca_data(nama_file):
    """Membaca data nama dan nilai dari file."""
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                bagian = baris.strip().split(",")

                if len(bagian) != 2:
                    print(f"Baris {nomor_baris} tidak valid.")
                    continue

                nama = bagian[0].strip()

                try:
                    nilai = float(bagian[1].strip())
                except ValueError:
                    print(f"Nilai pada baris {nomor_baris} bukan angka.")
                    continue

                if not validasi_nilai(nilai):
                    print(f"Nilai {nilai:g} milik {nama} di luar rentang 0–100.")
                    continue

                if not nama:
                    print(f"Nama pada baris {nomor_baris} kosong.")
                    continue

                data.append({"nama": nama, "nilai": nilai})

    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
        return []

    return data


def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada pada rentang 0 sampai 100."""
    return 0 <= nilai <= 100
