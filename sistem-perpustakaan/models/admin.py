# Class Admin - Turunan dari Pengguna
# Inheritance: Admin -> Pengguna
# Admin dapat mengelola buku, anggota, peminjaman, dan laporan

from .pengguna import Pengguna

class Admin(Pengguna):
    def __init__(self, id_pengguna: int, username: str, password: str):
        super().__init__(id_pengguna, username, password)

    def tampilkan_menu(self) -> None:
        # Implementasi menu khusus administrator
        print("Menampilkan menu administrator")

    def kelola_buku(self) -> None:
        # Manajemen CRUD data buku
        print("Mengelola buku")

    def kelola_anggota(self) -> None:
        # Manajemen CRUD dan verifikasi status anggota
        print("Mengelola anggota")

    def kelola_peminjaman(self) -> None:
        # Memantau dan memproses transaksi peminjaman/pengembalian
        print("Mengelola peminjaman")

    def kelola_laporan(self) -> None:
        # Mencetak atau melihat rekapitulasi data perpustakaan
        print("Menampilkan laporan")