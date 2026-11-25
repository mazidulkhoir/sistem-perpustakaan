import unittest
from models.buku import Buku

class TestBuku(unittest.TestCase):
    def setUp(self):
        self.buku = Buku(1, "Pemrograman Python", "John Doe", "Penerbit ABC", "Ilmu Komputer", 5)

    def test_tambah_buku(self):
        self.buku.tambah_buku()

    def test_ubah_buku(self):
        self.buku.ubah_buku()

    def test_hapus_buku(self):
        self.buku.hapus_buku()

    def test_cek_stok(self):
        stok = self.buku.cek_stok()
        self.assertEqual(stok, 5)

    def test_kurangi_stok(self):
        self.buku.kurangi_stok(2)
        self.assertEqual(self.buku.cek_stok(), 3)

    def test_tambah_stok(self):
        self.buku.tambah_stok(3)
        self.assertEqual(self.buku.cek_stok(), 8)

if __name__ == "__main__":
    unittest.main()