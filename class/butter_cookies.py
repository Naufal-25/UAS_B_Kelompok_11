class ButterCookies(KueKering, Penopingan):
  def __init__(self, nama, kode, bahan, produk_produksi, biaya_produksi, harga):
        super().__init__(nama, kode, bahan, produk_produksi, biaya_produksi, harga)

  def adon(self):
        print(f"Adonan '{self.nama}' sedang dibuat.")

    def panggang(self):
        print(f"'{self.nama}' sedang dipanggang hingga matang sempurna.")

    def topping(self):
        print(f"Menambahkan topping pada '{self.nama}' (misal: taburan gula atau cokelat).")
