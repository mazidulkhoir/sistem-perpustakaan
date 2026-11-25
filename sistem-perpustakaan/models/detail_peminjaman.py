# Class DetailPeminjaman - Komposisi dari Peminjaman
# Atribut private: id_detail, jumlah
# Method: tambah_detail

class DetailPeminjaman:
    def __init__(self, id_detail: int, jumlah: int):
        self.__id_detail = id_detail
        self.__jumlah = jumlah

    def tambah_detail(self, jumlah_tambahan: int) -> None:
        # Menambahkan item buku ke dalam transaksi peminjaman
        self.__jumlah += jumlah_tambahan