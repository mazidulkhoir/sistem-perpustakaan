import unittest
from models.anggota import Anggota
from models.mahasiswa import Mahasiswa

class TestAnggota(unittest.TestCase):
    def setUp(self):
        self.anggota = Anggota(1, "John Doe", "john@kampus.ac.id", "aktif")

    def test_cek_status_aktif(self):
        self.assertTrue(self.anggota.cek_status())

    def test_cek_status_nonaktif(self):
        anggota_nonaktif = Anggota(2, "Jane Doe", "jane@kampus.ac.id", "nonaktif")
        self.assertFalse(anggota_nonaktif.cek_status())

class TestMahasiswa(unittest.TestCase):
    def setUp(self):
        self.mhs = Mahasiswa(1, "Alice S.", "alice@kampus.ac.id", "aktif", "123456789")

    def test_tampilkan_identitas(self):
        identitas = self.mhs.tampilkan_identitas()
        self.assertIn("Alice S.", identitas)
        self.assertIn("123456789", identitas)

if __name__ == "__main__":
    unittest.main()