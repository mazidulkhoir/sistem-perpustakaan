# Class Buku - Entitas inventaris buku
# Atribut private: id_buku, judul, penulis, penerbit, kategori, stok
# Method: CRUD operations dan management stok

class Buku:
    def __init__(self, id_buku: int, judul: str, penulis: str, penerbit: str, kategori: str, stok: int):
        self.__id_buku = id_buku
        self.__judul = judul
        self.__penulis = penulis
        self.__penerbit = penerbit
        self.__kategori = kategori
        self.__stok = stok

    def tambah_buku(self) -> None:
        # Menambah data buku ke inventory
        pass

    def ubah_buku(self) -> None:
        # Mengubah data buku yang sudah ada
        pass

    def hapus_buku(self) -> None:
        # Menghapus buku dari inventory
        pass

    def cek_stok(self) -> int:
        # Mengembalikan stok buku yang tersisa
        return self.__stok

    def kurangi_stok(self, jumlah: int) -> None:
        # Mengurangi stok buku setelah peminjaman
        if jumlah <= self.__stok:
            self.__stok -= jumlah

    def tambah_stok(self, jumlah: int) -> None:
        # Menambah stok buku (misal: pengembalian atau pembelian baru)
        self.__stok += jumlah