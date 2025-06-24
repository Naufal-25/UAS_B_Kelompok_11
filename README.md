=== SISTEM PRODUKSI "Hanari Bakery" KELOMPOK 11 KELAS B ===
Anggota:
Cristian Alex Mulyawan [[ K3524024 ]]          Bertugas dalam pembuatan flow program
Naufal Hanif Satria Wijayanto [[ K3524064 ]]   Bertugas dalam pembuatan fitur-fitur program
Wava Al Qudsi [[ K3524084 ]]                   Bertugas dalam pembuatan class program

Fitur Utama

Menampilkan daftar produk roti dan kue
Menambahkan produk baru (Croissant, Muffin, Roti Manis, Butter Cookies)
Simulasi proses produksi (adon, kembang, panggang, topping)
Perhitungan estimasi profit berdasarkan biaya dan harga jual

Struktur Program

main.py # Titik eksekusi utama
example.py # Data sample produk
interface/
    interface.py # Interface untuk produk dengan topping dan pengembangan
superclass/
    produk.py # Abstract class Produk
    kue_kering.py # Subclass Produk untuk jenis kue kering
kelas/
    croissant.py
    muffin.py
    roti_manis.py
    butter_cookies.py
fitur/
    data.py # Manajemen data produk
    print.py # Fitur tampilan data produk
    proses.py # Simulasi proses produksi
    profit.py # Kalkulasi keuntungan
flow/
    flow.py # Logika menu dan interaksi pengguna