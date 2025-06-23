from superclass.produk import Produk

class KueKering(Produk):
  def __init__(self, nama, kode, bahan, produk_produksi, biaya_produksi, harga):
        super().__init__(nama, kode, bahan, produk_produksi, biaya_produksi, harga)

  def tampildata(self):
        print(f"--- Data Kue Kering ---")
        print(f"Nama Produk: {self.nama}")
        print(f"Kode: {self.kode}")
        print(f"Bahan Utama: {self.bahan}")
        print(f"Produk Produksi: {self.produk_produksi}")
        print(f"Biaya Produksi: Rp {self.biaya_produksi}")
        print(f"Harga Jual: Rp {self.harga}")
