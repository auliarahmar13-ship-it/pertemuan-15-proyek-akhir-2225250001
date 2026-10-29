
import unittest
import os
import tempfile

from src.data_io import baca_data, validasi_nilai
from src.analisis import (
    hitung_statistik,
    tentukan_status,
    hitung_ketuntasan,
)


class TestProgram(unittest.TestCase):

    def test_nilai_batas_bawah(self):
        self.assertTrue(validasi_nilai(0))

    def test_nilai_batas_atas(self):
        self.assertTrue(validasi_nilai(100))

    def test_nilai_di_luar_rentang(self):
        self.assertFalse(validasi_nilai(105))

    def test_hitung_statistik(self):
        data = [
            {"nama": "Andi", "nilai": 80},
            {"nama": "Budi", "nilai": 70},
            {"nama": "Citra", "nilai": 90},
        ]

        hasil = hitung_statistik(data)

        self.assertEqual(hasil["rata_rata"], 80)
        self.assertEqual(hasil["nilai_minimum"], 70)
        self.assertEqual(hasil["nilai_maksimum"], 90)
        self.assertEqual(hasil["jumlah_data"], 3)

    def test_data_kosong(self):
        self.assertIsNone(hitung_statistik([]))

    def test_status_kkm(self):
        self.assertEqual(tentukan_status(75), "Tuntas")
        self.assertEqual(tentukan_status(74), "Tidak Tuntas")

    def test_hitung_ketuntasan(self):
        data = [
            {"nama": "Andi", "nilai": 80},
            {"nama": "Budi", "nilai": 70},
            {"nama": "Citra", "nilai": 75},
        ]

        hasil = hitung_ketuntasan(data)

        self.assertEqual(hasil["jumlah_tuntas"], 2)
        self.assertEqual(hasil["jumlah_tidak_tuntas"], 1)

    def test_file_tidak_ditemukan(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "file_tidak_ada.txt")
            self.assertEqual(baca_data(path), [])


if __name__ == "__main__":
    unittest.main()
