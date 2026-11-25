import unittest
from models.pengembalian import Pengembalian
from models.peminjaman import Peminjaman
from models.buku import Buku
from exceptions.custom_exceptions import *


class TestPengembalian(unittest.TestCase):
    def setUp(self):
        self.pengembalian = Pengembalian(1, "2024-01-30", 3, 0)
        self.peminjaman = Peminjaman(1, "2024-01-15", "2024-01-22", anggota_id=1)
        self.buku = Buku(1, "Judul Buku", "Penulis", "Penerbit", "Kategori", 3)

    def test_proses_pengembalian(self):
        # Test mode backward compatible (tanpa parameter)
        self.pengembalian.proses_pengembalian()
        self.assertEqual(self.pengembalian._Pengembalian__status, "selesai")

    def test_proses_pengembalian_dengan_validasi(self):
        # Test dengan parameter peminjaman dan buku
        self.pengembalian.proses_pengembalian(self.peminjaman, self.buku)
        self.assertEqual(self.peminjaman._Peminjaman__status, "selesai")
        self.assertEqual(self.buku.cek_stok(), 4)  # Stok bertambah 1

    def test_proses_pengembalian_ganda_ditolak(self):
        # Pertama kali proses pengembalian sukses
        self.pengembalian.proses_pengembalian(self.peminjaman, self.buku)
        # Sekali lagi, seharusnya dilempar exception
        with self.assertRaises(ValidasiPeminjamanException):
            self.pengembalian.proses_pengembalian(self.peminjaman, self.buku)

    def test_hitung_denda(self):
        pg = Pengembalian(1, "2024-01-30", 3, 0)
        denda = pg.hitung_denda()
        self.assertEqual(denda, 600)  # 3 hari x Rp200

    def test_hitung_keterlambatan(self):
        pg = Pengembalian(1, "2024-01-30", 3, 0)
        hari = pg.hitung_keterlambatan("2024-01-22")
        self.assertEqual(hari, 3)


if __name__ == "__main__":
    unittest.main()