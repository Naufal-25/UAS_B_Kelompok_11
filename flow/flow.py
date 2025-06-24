from fitur.data import Data
from fitur.print import Print
from fitur.proses import Proses
from fitur.profit import Profit

from kelas.roti_manis import RotiManis
from kelas.muffin import Muffin
from kelas.croissant import Croissant
from kelas.butter_cookies import ButterCookies

from example import get_sample_data

def input_produk():
    print("\n=== Input Produk Baru ===")
    nama = input("Nama Produk: ").strip()
    kode = input("Kode Produk: ").strip()
    bahan = input("Bahan Utama: ").strip()

    try:
        produksi = int(input("Jumlah Produk yang Dihasilkan per Batch: "))
        biaya = int(input("Total Biaya Produksi (Rp): "))
        harga = int(input("Harga Jual per pcs (Rp): "))
    except ValueError:
        print("Input angka tidak valid.")
        return None

    print("\nPilih Jenis Produk:")
    print("1. Roti Manis")
    print("2. Muffin")
    print("3. Croissant")
    print("4. Butter Cookies")

    jenis = input("Masukkan pilihan (1-4): ").strip()
    if jenis == "1":
        return RotiManis(nama, kode, bahan, produksi, biaya, harga)
    elif jenis == "2":
        return Muffin(nama, kode, bahan, produksi, biaya, harga)
    elif jenis == "3":
        return Croissant(nama, kode, bahan, produksi, biaya, harga)
    elif jenis == "4":
        return ButterCookies(nama, kode, bahan, produksi, biaya, harga)
    else:
        print("Jenis produk tidak dikenali.")
        return None

def main():
    data = Data()
    for item in get_sample_data():
        data.tambah(item)

    while True:
        print("\n=== MENU UTAMA TOKO ROTI ===")
        print("1. Tambah Produk")
        print("2. Lihat Semua Produk")
        print("3. Proses Produksi")
        print("4. Hitung Profit")
        print("5. Keluar")

        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            produk_baru = input_produk()
            if produk_baru:
                data.tambah(produk_baru)
                print("Produk berhasil ditambahkan.")

        elif pilihan == "2":
            print("\n=== Data Semua Produk ===")
            tampilkan = Print(data.produk)
            tampilkan.tampil()

        elif pilihan == "3":
            if not data.produk:
                print("Belum ada produk. Silakan tambah dulu.")
                continue

            for i, p in enumerate(data.produk, start=1):
                print(f"{i}. {p.nama}")
            try:
                index = int(input("Pilih produk untuk diproses: ")) - 1
                jumlah = int(input("Masukkan jumlah produksi: "))
                proses = Proses(data.produk[index], jumlah)
                proses.run()
            except (ValueError, IndexError):
                print("Input tidak valid.")

        elif pilihan == "4":
            if not data.produk:
                print("Belum ada produk.")
                continue
            for i, p in enumerate(data.produk, start=1):
                print(f"{i}. {p.nama}")
            try:
                index = int(input("Pilih produk untuk dihitung profit-nya: ")) - 1
                jumlah = int(input("Jumlah produksi (pcs): "))
                keuntungan = Profit(data.produk[index], jumlah)
                keuntungan.print_profit()
            except (ValueError, IndexError):
                print("Input tidak valid.")

        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
