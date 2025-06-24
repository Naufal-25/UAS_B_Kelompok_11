class Print:
    def __init__(self, list):
        self.produk = list

    def tampil(self):
        if not self.produk:
            print ("[[ KOSONG ]]")
        else:
            for i, r in enumerate(self.produk, start=1):
                print(f"\nProduk {i}:")
                r.tampil_data()