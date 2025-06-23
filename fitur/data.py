from kelas.butter_cookies import ButterCookies
from kelas.croissant import Croissant
from kelas.muffin import Muffin
from kelas.roti_manis import RotiManis

class Data:
    def __init__(self):
        self.produk=[]
    
    def tambah(self, kue):
        self.produk.append(kue)

class Print:
    def tampil(self):
        if not self.produk:
            print ("[[ KOSONG ]]")
        else:
            for i, crew in enumerate(self.produk, start=1):
                print(f"\nProduk {i}:")
                crew.tampildata()