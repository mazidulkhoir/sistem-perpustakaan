# Class Dosen - Turunan dari Anggota
# Inheritance: Dosen -> Anggota -> Pengguna
# Atribut tambahan: nip
# Method: tampilkan_identitas

from .anggota import Anggota

class Dosen(Anggota):
    def __init__(self, id_anggota: int, nama: str, email: str, status: str, nip: str):
        super().__init__(id_anggota, nama, email, status)
        self.__nip = nip

    def tampilkan_identitas(self) -> str:
        # Mengembalikan informasi nama dan NIP dosen
        return f"Nama: {self._Anggota__nama}, NIP: {self.__nip}"