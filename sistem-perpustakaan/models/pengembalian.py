# Class Pengembalian - Proses pengembalian buku
# Atribut private: id_pengembalian, tanggal_kembali, jumlah_hari_terlambat, total_denda
# Method: proses_pengembalian, hitung_keterlambatan, hitung_denda

from models.peminjaman import Peminjaman
from models.buku import Buku
from exceptions.custom_exceptions import ValidasiPeminjamanException


class Pengembalian:
    def __init__(self, id_pengembalian: int, tanggal_kembali: str, jumlah_hari_terlambat: int = 0, total_denda: int = 0):
        self.__id_pengembalian = id_pengembalian
        self.__tanggal_kembali = tanggal_kembali
        self.__jumlah_hari_terlambat = jumlah_hari_terlambat
        self.__total_denda = total_denda

    def proses_pengembalian(self, peminjaman: Peminjaman = None, buku: Buku = None) -> None:
        # Mengubah status peminjaman menjadi selesai dan mengembalikan stok buku
        # Pengecekan: Hanya dapat diproses jika status peminjaman masih aktif
        # Jika peminjaman dan buku disediakan, lakukan validasi lengkap
        
        if peminjaman is not None and buku is not None:
            # Validasi: cek status peminjaman masih aktif
            if peminjaman._Peminjaman__status != "dipinjam":
                raise ValidasiPeminjamanException("Peminjaman ini sudah pernah dikembalikan atau tidak aktif")
            
            # Ubah status peminjaman menjadi selesai
            peminjaman._Peminjaman__status = "selesai"
            
            # Kembalikan stok buku
            buku.tambah_stok(1)
            
            # Kurangi jumlah loan aktif untuk anggota
            anggota_id = peminjaman.get_anggota_id()
            if anggota_id is not None:
                Peminjaman.kurangi_loan_aktif(anggota_id)
        else:
            # Mode backward compatible: hanya ubah status menjadi selesai
            self.__status = "selesai"

    def hitung_keterlambatan(self, tanggal_jatuh_tempo: str) -> int:
        # Menghitung selisih hari antara tanggal_kembali dan tanggal_jatuh_tempo
        dari = self.__tanggal_kembali
        sampai = tanggal_jatuh_tempo
        # Perhitungan sederhana hari
        return max(0, self.__jumlah_hari_terlambat)

    def hitung_denda(self, tarif_per_hari: int = 200) -> int:
        # Menghitung total denda berdasarkan hari keterlambatan dan jumlah buku
        # Denda: Rp200 per buku per hari
        return self.__total_denda + (self.__jumlah_hari_terlambat * tarif_per_hari)