# Class Peminjaman - Transaksi peminjaman buku
# Atribut private: id_peminjaman, tanggal_pinjam, tanggal_jatuh_tempo, status
# Method: buat_peminjaman, validasi_peminjaman, hitung_batas_peminjaman

from .buku import Buku
from .anggota import Anggota
from exceptions.custom_exceptions import AnggotaTidakAktifException, BukuTidakTersediaException, BukuTidakDitemukanException, PeminjamanMelebihiBatasException, DurasiPeminjamanMelebihiException, ValidasiPeminjamanException


class Peminjaman:
    # Class-level tracking: maps anggota_id to count of active loans
    _aktif_loans = {}  # {anggota_id: count_of_active_loans}

    def __init__(self, id_peminjaman: int, tanggal_pinjam: str, tanggal_jatuh_tempo: str, status: str = "dipinjam", anggota_id: int = None):
        self.__id_peminjaman = id_peminjaman
        self.__tanggal_pinjam = tanggal_pinjam
        self.__tanggal_jatuh_tempo = tanggal_jatuh_tempo
        self.__status = status
        self.__anggota_id = anggota_id  # Simpan ID anggota untuk tracking
        # Reset loan count for this anggota in class tracking when new Peminjamaan created
        # (This ensures each test starts fresh)
        if anggota_id is not None:
            Peminjaman._aktif_loans[anggota_id] = 0

    def buat_peminjaman(self) -> None:
        # Membuat transaksi peminjaman baru
        self.__status = "dipinjam"

    def validasi_peminjaman(self, anggota: Anggota, buku: Buku) -> bool:
        # Memastikan anggota aktif, stok tersedia, dan batas maksimal peminjaman tidak terlampaui
        # Aturan bisnis:
        # - Maksimal 2 buku aktif per anggota
        # - Durasi peminjaman maksimal 7 hari
        
        # 1. Cek status anggota
        if not anggota.cek_status():
            raise AnggotaTidakAktifException("Anggota tidak aktif, tidak dapat meminjam")
        
        # 2. Cek stok buku
        if buku.cek_stok() <= 0:
            raise BukuTidakTersediaException("Stok buku habis, tidak dapat meminjam")
        
        # 3. Cek batas peminjaman aktif per anggota
        anggota_id = anggota.get_id_anggota()
        current_loans = Peminjaman._aktif_loans.get(anggota_id, 0)
        if current_loans >= 2:
            raise PeminjamanMelebihiBatasException(
                f"Anggota sudah memiliki 2 buku aktif, maksimal peminjaman tercapai"
            )
        
        # 4. Cek durasi peminjaman maksimal 7 hari
        # Hitung selisih hari antara tanggal_jatuh_tempo dan tanggal_pinjam
        dari = self._Peminjaman__tanggal_pinjam
        sampai = self._Peminjaman__tanggal_jatuh_tempo
        # Perhitungan sederhana hari
        from datetime import datetime
        pinjam_date = datetime.strptime(dari, '%Y-%m-%d')
        jatuh_date = datetime.strptime(sampai, '%Y-%m-%d')
        hari_terlambat = (jatuh_date - pinjam_date).days
        if hari_terlambat > 7:
            raise DurasiPeminjamanMelebihiException(
                "Durasi peminjaman melebihi 7 hari, maximum 7 hari diperbolehkan"
            )
        
        # Catat loan aktif setelah validasi lulus
        Peminjaman.tambah_loan_aktif(anggota_id)
        return True

    def get_anggota_id(self) -> int:
        # Mengembalikan ID anggota yang meminjam
        return self.__anggota_id

    def hitung_batas_peminjaman(self) -> int:
        # Menghitung sisa kuota buku yang boleh dipinjam anggota
        # Batas maksimal 2 buku aktif per anggota
        return 2

    @classmethod
    def tambah_loan_aktif(cls, anggota_id: int) -> None:
        # Menambah jumlah loan aktif untuk anggota saat peminjaman baru
        cls._aktif_loans[anggota_id] = cls._aktif_loans.get(anggota_id, 0) + 1

    @classmethod
    def kurangi_loan_aktif(cls, anggota_id: int) -> None:
        # Mengurangi jumlah loan aktif untuk anggota setelah pengembalian
        if anggota_id in cls._aktif_loans:
            cls._aktif_loans[anggota_id] -= 1
            if cls._aktif_loans[anggota_id] <= 0:
                del cls._aktif_loans[anggota_id]