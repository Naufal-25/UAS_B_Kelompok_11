from kelas.butter_cookies import ButterCookies
from kelas.croissant import Croissant
from kelas.muffin import Muffin
from kelas.roti_manis import RotiManis

from fitur.data import Data
from fitur.print import Print
from fitur.proses import Proses
from fitur.profit import Profit



def main():
    data = Data()

    data.tambah(Croissant("Croissant Cokelat", "C001", "Tepung, Cokelat, Ragi", 100, 300000, 10000))
    data.tambah(Muffin("Muffin Blueberry", "M002", "Tepung, Blueberry, Telur", 120, 240000, 8000))
    data.tambah(RotiManis("Roti Manis Keju", "R003", "Tepung, Keju, Ragi", 150, 270000, 9000))
    data.tambah(ButterCookies("Butter Cookies Vanilla", "B004", "Tepung, Mentega, Gula", 200, 180000, 7000))

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
                pilih = int(input("\nMasukkan nomor produk: ")) - 1
                if pilih < 0 or pilih >= len(data.produk):
                    print("Pilihan tidak valid.")
                    continue
                jumlah = int(input("Masukkan jumlah produk yang akan diproduksi: "))
                produk_dipilih = data.produk[pilih]
                proses = Proses(produk_dipilih, jumlah)
                proses.run()
                hasil = Profit(produk_dipilih, jumlah)
                hasil.print_profit()
            except ValueError:
                print("Input harus berupa angka.")

        elif pilihan == "3":
            print("Terima kasih, program selesai.")
            break

        else:
            print("Menu tidak tersedia.")

if __name__ == "__main__":
    main()
