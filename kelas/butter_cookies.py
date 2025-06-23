from superclass.kue_kering import KueKering

class ButterCookies(KueKering):
    def __init__(self, nama, kode, bahan, produk_produksi, biaya_produksi, harga):
        super().__init__(nama, kode, bahan, produk_produksi, biaya_produksi, harga)

    def tampil_data(self):
        print(f"--- Data Butter Cookies ---")
        print(f"Nama Produk: {self.nama}")
        print(f"Kode: {self.kode}")
        print(f"Bahan Utama: {self.bahan}")
        print(f"Produk Produksi: {self.produk_produksi}")
        print(f"Biaya Produksi: Rp {self.biaya_produksi}")
        print(f"Harga Jual: Rp {self.harga}")

    def adon(self):
        print(f"Adonan '{self.nama}' sedang dibuat.")
    def panggang(self):
        print(f"'{self.nama}' sedang dipanggang hingga matang sempurna.")

    def topping(self):
        print(f"Menambahkan topping pada '{self.nama}' (misal: taburan gula atau cokelat).")
