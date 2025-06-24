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
        return self.biaya_total() - self.harga_total()
    
    def print_profit(self):
        print(f"Harga produksi satuan dari '{self.produk.nama}' adalah: Rp {self.biaya_min()}")
        print(f"Harga total produksi sebanyak {self.jumlah} pcs adalah: Rp {self.biaya_total()}")
        print(f"Harga total jual sebanyak {self.jumlah} pcs adalah: Rp {self.harga_total()}")
        print(f"Profit untuk {self.jumlah} pcs adalah: Rp {self.profit()}")