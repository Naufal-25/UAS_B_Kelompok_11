import time

class Proses:
    def __init__(self, produk, jumlah):
        self.produk = produk
        self.jumlah = jumlah
    
    def run(self):
        print(f"\n=+= Memulai Proses Produksi: {self.produk.nama} =+=")
        time.sleep(2)

        if hasattr(self.produk, 'adon'):
            self.produk.adon()
            time.sleep(2)

        if hasattr(self.produk, 'kembang'):
            self.produk.kembang()
            time.sleep(2)

        if hasattr(self.produk, 'panggang'):
            self.produk.panggang()
            time.sleep(2)

        if hasattr(self.produk, 'topping'):
            self.produk.topping()
            time.sleep(2)
        
        print(f"=+= Proses Produksi {self.produk.nama} Selesai =+=\n")
