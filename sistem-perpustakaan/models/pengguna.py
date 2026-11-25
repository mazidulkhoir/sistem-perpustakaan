# Class Pengguna - Kelas abstrak dasar untuk semua pengguna
# Inheritance: Turunan dari tidak ada (kelas dasar)
# Penggunaan: Diwariskan oleh Admin dan Anggota

class Pengguna:
    def __init__(self, id_pengguna: int, username: str, password: str):
        self.__id_pengguna = id_pengguna
        self.__username = username
        self.__password = password

    def login(self) -> bool:
        # Memvalidasi kredensial pengguna
        return True

    def logout(self) -> None:
        # Mengakhiri sesi pengguna
        pass

    def tampilkan_menu(self) -> None:
        # Metode abstrak untuk menampilkan opsi menu sesuai peran
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini")