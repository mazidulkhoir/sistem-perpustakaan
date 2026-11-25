# Class Mahasiswa - Turunan dari Anggota
# Inheritance: Mahasiswa -> Anggota -> Pengguna
# Atribut tambahan: nim
# Method: tampilkan_identitas

from .anggota import Anggota

class Mahasiswa(Anggota):
    def __init__(self, id_anggota: int, nama: str, email: str, status: str, nim: str):
        super().__init__(id_anggota, nama, email, status)
        self.__nim = nim

    def tampilkan_identitas(self) -> str:
        # Mengembalikan informasi nama dan NIM mahasiswa
        return f"Nama: {self._Anggota__nama}, NIM: {self.__nim}"