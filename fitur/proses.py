class Profit:
    def __init__(self, produk, jumlah):
        self.produk = produk
        self.jumlah = jumlah

    def biaya_min(self):
        return self.produk.biaya_produksi / self.produk.produk_produksi
    
    def biaya_total(self):
        return self.biaya_min() * self.jumlah

    def harga_total(self):
        return self.produk.harga * self.jumlah
    
    def profit(self):
        return self.biaya_total - self.harga_total