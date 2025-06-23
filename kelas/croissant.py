from superclass.produk import Produk
from interface.interface import Pengembangan

class Croissant(Produk, Pengembangan):
    def __init__(self, nama, kode, bahan, produk_produksi, biaya_produksi, harga):
        super().__init__(nama, kode, bahan, produk_produksi, biaya_produksi, harga)

    def tampildata(self):
        print(f"--- Data Croissant ---")
        print(f"Nama Produk: {self.nama}")
        print(f"Kode: {self.kode}")
        print(f"Bahan Utama: {self.bahan}")
        print(f"Produk Produksi: {self.produk_produksi}")
        print(f"Biaya Produksi: Rp {self.biaya_produksi}")
        print(f"Harga Jual: Rp {self.harga}")

    def adon(self):
        print(f"'{self.nama}' sedang dalam proses pengadonan berlapis.")

    def kembang(self):
        print(f"'{self.nama}' sedang dalam proses pengembangan (proofing).")

    def panggang(self):
        print(f"'{self.nama}' sedang dipanggang hingga renyah.")
