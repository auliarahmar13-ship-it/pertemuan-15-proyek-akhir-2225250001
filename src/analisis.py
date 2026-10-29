
KKM = 75


def hitung_statistik(data):
    """Menghitung rata-rata, nilai minimum, dan maksimum."""
    if not data:
        return None

    daftar_nilai = [mahasiswa["nilai"] for mahasiswa in data]

    statistik = {
        "rata_rata": sum(daftar_nilai) / len(daftar_nilai),
        "nilai_minimum": min(daftar_nilai),
        "nilai_maksimum": max(daftar_nilai),
        "jumlah_data": len(daftar_nilai),
    }

    return statistik


def tentukan_status(nilai):
    """Menentukan ketuntasan berdasarkan KKM."""
    if nilai >= KKM:
        return "Tuntas"
    return "Tidak Tuntas"


def hitung_ketuntasan(data):
    """Menghitung jumlah mahasiswa tuntas dan tidak tuntas."""
    jumlah_tuntas = 0
    jumlah_tidak_tuntas = 0

    for mahasiswa in data:
        status = tentukan_status(mahasiswa["nilai"])

        if status == "Tuntas":
            jumlah_tuntas += 1
        else:
            jumlah_tidak_tuntas += 1

    return {
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_tidak_tuntas": jumlah_tidak_tuntas,
    }
