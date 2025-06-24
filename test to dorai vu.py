from abc import ABC, abstractmethod
import time

# === Abstract Base Class Produk ===
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


# === Interface Khusus Produk yang Mengembang ===
class Pengembangan(ABC):
    @abstractmethod
    def kembang(self):
        pass


# === Subclass: Kue Kering ===
class KueKering(Produk):
    def __init__(self, nama, kode, bahan, produk_produksi, biaya_produksi, harga):
        super().__init__(nama, kode, bahan, produk_produksi, biaya_produksi, harga)

    def tampil_data(self):
        print(f"--- Data Kue Kering ---")
        print(f"Nama Produk: {self.nama}")
        print(f"Kode: {self.kode}")
        print(f"Bahan Utama: {self.bahan}")
        print(f"Produk Produksi: {self.produk_produksi}")
        print(f"Biaya Produksi: Rp {self.biaya_produksi}")
        print(f"Harga Jual: Rp {self.harga}")

    def topping(self):
        pass


# === Produk Turunan ===
class ButterCookies(KueKering):
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


class Croissant(Produk, Pengembangan):
    def tampil_data(self):
        print(f"--- Data Croissant ---")
        print(f"Nama Produk: {self.nama}")
        print(f"Kode: {self.kode}")
        print(f"Bahan Utama: {self.bahan}")
        print(f"Produk Produksi: {self.produk_produksi}")
        print(f"Biaya Produksi: Rp {self.biaya_produksi}")
        print(f"Harga Jual: Rp {self.harga}")

    def adon(self):
        print(f"'{self.nama}' sedang dalam proses pengadonan berlapis.")

    def kembang(self):
        print(f"'{self.nama}' sedang dalam proses pengembangan (proofing).")

    def panggang(self):
        print(f"'{self.nama}' sedang dipanggang hingga renyah.")


class Muffin(KueKering, Pengembangan):
    def tampil_data(self):
        print(f"--- Data Muffin ---")
        print(f"Nama Produk: {self.nama}")
        print(f"Kode: {self.kode}")
        print(f"Bahan Utama: {self.bahan}")
        print(f"Produk Produksi: {self.produk_produksi}")
        print(f"Biaya Produksi: Rp {self.biaya_produksi}")
        print(f"Harga Jual: Rp {self.harga}")

    def adon(self):
        print(f"Adonan '{self.nama}' sedang dicampur.")

    def kembang(self):
        print(f"'{self.nama}' sedang mengembang saat dipanggang.")

    def panggang(self):
        print(f"'{self.nama}' sedang dipanggang dalam cetakan.")

    def topping(self):
        print(f"Menambahkan topping pada '{self.nama}' (misal: glaze atau crumble).")


class RotiManis(Produk, Pengembangan):
    def tampil_data(self):
        print(f"--- Data Roti Manis ---")
        print(f"Nama Produk: {self.nama}")
        print(f"Kode: {self.kode}")
        print(f"Bahan Utama: {self.bahan}")
        print(f"Produk Produksi: {self.produk_produksi}")
        print(f"Biaya Produksi: Rp {self.biaya_produksi}")
        print(f"Harga Jual: Rp {self.harga}")

    def adon(self):
        print(f"'{self.nama}' sedang dalam proses pengadonan.")

    def kembang(self):
        print(f"'{self.nama}' sedang dalam proses pengembangan (fermentasi).")

    def panggang(self):
        print(f"'{self.nama}' sedang dipanggang.")


# === Proses Produksi ===
class Proses:
    def __init__(self, produk, jumlah):
        self.produk = produk
        self.jumlah = jumlah

    def run(self):
        print(f"\n=+= Memulai Proses Produksi: {self.produk.nama} =+=")
        time.sleep(self.jumlah)

        if hasattr(self.produk, 'adon'):
            self.produk.adon()
            time.sleep(self.jumlah+6)

        if hasattr(self.produk, 'kembang'):
            self.produk.kembang()
            time.sleep(self.jumlah+1)

        if hasattr(self.produk, 'panggang'):
            self.produk.panggang()
            time.sleep(5)

        if hasattr(self.produk, 'topping'):
            self.produk.topping()
            time.sleep(self.jumlah-10)

        print(f"=+= Proses Produksi {self.produk.nama} Selesai =+=\n")


# === Perhitungan Profit ===
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
        return self.harga_total() - self.biaya_total()

    def print_profit(self):
        print(f"Harga produksi satuan dari '{self.produk.nama}' adalah: Rp {self.biaya_min():,.0f}")
        print(f"Harga total produksi sebanyak {self.jumlah} pcs adalah: Rp {self.biaya_total():,.0f}")
        print(f"Harga total jual sebanyak {self.jumlah} pcs adalah: Rp {self.harga_total():,.0f}")
        print(f"Profit untuk {self.jumlah} pcs adalah: Rp {self.profit():,.0f}\n")


# === Manajemen Data Produk ===
class Data:
    def __init__(self):
        self.produk = []

    def tambah(self, kue):
        self.produk.append(kue)


# === Tampilan Produk ===
class Print:
    def __init__(self, list_produk):
        self.produk = list_produk

    def tampil(self):
        if not self.produk:
            print("[[ DATA PRODUK KOSONG ]]")
        else:
            for i, r in enumerate(self.produk, start=1):
                print(f"\nProduk {i}:")
                r.tampil_data()


# === Main Flow ===
def main():
    data = Data()


    # Tambahkan produk ke daftar data
    data.tambah(Croissant("Croissant Cokelat", "C001",
                          "Tepung, Cokelat, Ragi",
                          100, 300000, 10000))
    data.tambah(Muffin("Muffin Blueberry", "M002",
                       "Tepung, Blueberry, Telur",
                       120, 240000, 8000))
    data.tambah(RotiManis("Roti Manis Keju", "R003",
                          "Tepung, Keju, Ragi",
                          150, 270000, 9000))
    data.tambah(ButterCookies("Butter Cookies Vanilla",
                              "B004", "Tepung, Mentega, Gula",
                              200, 180000, 7000))



    while True:
        print("\n===== SISTEM PRODUKSI TOKO ROTI =====")
        print("1. Lihat Data Produk")
        print("2. Produksi Produk")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            Print(data.produk).tampil()

        elif pilihan == "2":
            Print(data.produk).tampil()
            try:
                pilih = int(input("\nMasukkan nomor produk yang ingin diproduksi: ")) - 1
                if pilih < 0 or pilih >= len(data.produk):
                    print("Pilihan tidak valid.")
                    continue

                jumlah = int(input("Masukkan jumlah produk yang akan diproduksi: "))
                produk_dipilih = data.produk[pilih]

                # Proses dan profit
                proses = Proses(produk_dipilih, jumlah)
                proses.run()

                hasil = Profit(produk_dipilih, jumlah)
                hasil.print_profit()

            except ValueError:
                print("Input tidak valid. Harus angka.")

        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem.")
            break

        else:
            print("Pilihan tidak tersedia.")

# === Jalankan Program ===
if __name__ == "__main__":
    main()
