# Class Anggota - Kelas abstrak turunan dari Pengguna
# Inheritance: Anggota -> Pengguna
# Atribut private: id_anggota, nama, email, status
# Method: tampilkan_menu, cek_status

from .pengguna import Pengguna

class Anggota(Pengguna):
    def __init__(self, id_anggota: int, nama: str, email: str, status: str):
        super().__init__(id_anggota, "", "")  # Username/password not primary for anggota
        self.__id_anggota = id_anggota
        self.__nama = nama
        self.__email = email
        self.__status = status

    def tampilkan_menu(self) -> None:
        # Implementasi menu khusus anggota
        print("Menampilkan menu anggota")

    def cek_status(self) -> bool:
        # Mengecek apakah anggota berstatus aktif dan layak meminjam
        return self.__status == "aktif"

    def get_id_anggota(self) -> int:
        # Mengembalikan ID anggota
        return self.__id_anggota