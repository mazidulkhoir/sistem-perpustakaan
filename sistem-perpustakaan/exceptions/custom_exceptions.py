# Custom Exception untuk Sistem Informasi Perpustakaan Kampus
# Berisi exception khusus untuk validasi bisnis perpustakaan

class BukuTidakTersediaException(Exception):
    """Dipicu ketika stok buku habis saat dicoba dipinjam"""
    pass

class PeminjamanMelebihiBatasException(Exception):
    """Dipicu ketika anggota melebihi batas 2 buku aktif"""
    pass

class DurasiPeminjamanMelebihiException(Exception):
    """Dipicu ketika durasi peminjaman melebihi 7 hari"""
    pass

class AnggotaTidakAktifException(Exception):
    """Dipicu ketika status anggota tidak aktif"""
    pass

class BukuTidakDitemukanException(Exception):
    """Dipucu ketika ID buku tidak ditemukan di inventory"""
    pass

class ValidasiPeminjamanException(Exception):
    """Wrapper exception untuk kesalahan validasi peminjaman"""
    pass