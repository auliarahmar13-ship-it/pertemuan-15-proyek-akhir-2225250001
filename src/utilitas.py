
def buat_laporan(data, statistik, ketuntasan):
    """Menyusun laporan hasil analisis nilai."""
    laporan = []

    laporan.append("LAPORAN REKAP DAN ANALISIS NILAI MATEMATIKA")
    laporan.append("=" * 45)
    laporan.append(f"Jumlah mahasiswa : {statistik['jumlah_data']}")
    laporan.append(f"Rata-rata nilai  : {statistik['rata_rata']:.2f}")
    laporan.append(f"Nilai minimum    : {statistik['nilai_minimum']:g}")
    laporan.append(f"Nilai maksimum   : {statistik['nilai_maksimum']:g}")
    laporan.append(f"Jumlah tuntas    : {ketuntasan['jumlah_tuntas']}")
    laporan.append(f"Jumlah tidak tuntas: {ketuntasan['jumlah_tidak_tuntas']}")
    laporan.append("")
    laporan.append("RINCIAN NILAI MAHASISWA")
    laporan.append("-" * 45)

    for mahasiswa in data:
        nama = mahasiswa["nama"]
        nilai = mahasiswa["nilai"]
        status = "Tuntas" if nilai >= 75 else "Tidak Tuntas"
        laporan.append(f"{nama}: {nilai:g} - {status}")

    return "\n".join(laporan)


def simpan_laporan(isi_laporan, nama_file):
    """Menyimpan laporan ke dalam file teks."""
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write(isi_laporan)
        print(f"Laporan berhasil disimpan ke '{nama_file}'.")
        return True
    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")
        return False
