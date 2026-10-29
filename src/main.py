
from pathlib import Path

from data_io import baca_data
from analisis import hitung_statistik, hitung_ketuntasan
from utilitas import buat_laporan, simpan_laporan


FOLDER_PROYEK = Path(__file__).resolve().parent.parent
FILE_DATA = FOLDER_PROYEK / "data" / "nilai_contoh.txt"
FILE_LAPORAN = FOLDER_PROYEK / "output" / "laporan_nilai.txt"


def main():
    print("=== REKAP DAN ANALISIS NILAI MATEMATIKA ===")

    data = baca_data(FILE_DATA)

    if not data:
        print("Tidak ada data valid untuk dianalisis.")
        return

    statistik = hitung_statistik(data)
    ketuntasan = hitung_ketuntasan(data)

    laporan = buat_laporan(data, statistik, ketuntasan)

    print()
    print(laporan)
    print()

    FILE_LAPORAN.parent.mkdir(parents=True, exist_ok=True)
    simpan_laporan(laporan, FILE_LAPORAN)


if __name__ == "__main__":
    main()
