class Muffin(KueKering, Pengembangan, Penopingan):
  def __init__(self, nama, kode, bahan, produk_produksi, biaya_produksi, harga):
        super().__init__(nama, kode, bahan, produk_produksi, biaya_produksi, harga)

  def adon(self):
        print(f"Adonan '{self.nama}' sedang dicampur.")

    def panggang(self):
        print(f"'{self.nama}' sedang dipanggang dalam cetakan.")

    def kembang(self):
        print(f"'{self.nama}' sedang mengembang saat dipanggang.")

    def topping(self):
        print(f"Menambahkan topping pada '{self.nama}' (misal: glaze atau crumble).")
