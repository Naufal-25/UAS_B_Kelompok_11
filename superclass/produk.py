from abc import ABC, abstractmethod

class Produk(ABC):
      def __init__(self, nama, kode, bahan, produk_produksi, biaya_produksi, harga):
        self.nama = nama
        self.kode = kode
        self.bahan = bahan
        self.produk_produksi = produk_produksi
        self.biaya_produksi = biaya_produksi
        self.harga = harga

      @abstractmethod
      def tampil_data(self): 
        pass

