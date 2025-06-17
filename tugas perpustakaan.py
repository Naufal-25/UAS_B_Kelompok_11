# nama  :Cristian Alex Mulyawan
# nomor :K3524024
from abc import ABC, abstractmethod
from datetime import datetime

# Interface
class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass


class Borrowable(ABC):
    @abstractmethod
    def borrow(self, member):
        pass

    @abstractmethod
    def return_book(self):
        pass


class Searchable(ABC):
    @abstractmethod
    def search(self, keyword):
        pass


# Entity
class Book(Borrowable, Displayable):
    MAX_COPIES = 2

    def __init__(self, base_code, title, author):
        self.base_code = base_code  
        self.code = None            
        self.title = title
        self.author = author
        self.borrowed_by = None
        self.borrow_date = None

    def borrow(self, member):
        if not self.borrowed_by:
            self.borrowed_by = member
            self.borrow_date = datetime.now()
            return True
        return False

    def return_book(self):
        self.borrowed_by = None
        self.borrow_date = None

    def display(self):
        status = f"(Dipinjam oleh {self.borrowed_by.name})" if self.borrowed_by else "(Tersedia)"
        print(f"{self.code:<12} | {self.title:<30} | {self.author:<20} {status}")


class Member(Displayable):
    MAX_BOOKS = {'A': 5, 'B': 10, 'C': 3}  # A = Mahasiswa, B = Dosen, C = Umum

    def __init__(self, member_id, name, member_type):
        self.member_id = member_id
        self.name = name
        self.member_type = member_type.upper()
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if len(self.borrowed_books) >= self.MAX_BOOKS[self.member_type]:
            return False, "Melebihi kapasitas pinjaman"
        if book.borrow(self):
            self.borrowed_books.append(book)
            return True, "Buku berhasil dipinjam"
        return False, "Buku sedang dipinjam"

    def return_book(self, book_code):
        for book in self.borrowed_books:
            if book.code == book_code:
                book.return_book()
                self.borrowed_books.remove(book)
                return True
        return False

    def display(self):
        print(f"{self.member_id:<10} | {self.name:<25} | {self.member_type:<2}")
        for book in self.borrowed_books:
            days = (datetime.now() - book.borrow_date).days
            status = " (Terlambat)" if days > 14 else ""
            print(f"  - {book.title}, {days} hari sejak pinjam{status}")


#Repository
class IRepository(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def list_all(self):
        pass


class BookRepository(IRepository, Searchable):
    def __init__(self):
        self.books = {}

    def add(self, book: Book):
        existing = [k for k in self.books.keys() if k.startswith(book.base_code)]
        count = len(existing)
        if count < Book.MAX_COPIES:
            new_key = f"{book.base_code}-{count + 1}"
            book.code = new_key  
            self.books[new_key] = book
            print(f"Buku berhasil ditambahkan dengan kode: {new_key}")
        else:
            print("Sudah mencapai batas maksimal untuk buku ini.")

    def delete(self, code):
        if code in self.books and self.books[code].borrowed_by is None:
            del self.books[code]
            return True
        return False

    def get(self, code):
        return self.books.get(code)

    def list_all(self):
        return self.books.values()

    def search(self, keyword):
        keyword_lower = keyword.lower()
        results = [b for b in self.books.values()
                   if keyword_lower in b.title.lower() or keyword_lower in b.author.lower()]
        return results


class MemberRepository(IRepository, Searchable):
    def __init__(self):
        self.members = {}

    def add(self, member: Member):
        if member.member_id in self.members:
            print("ID anggota sudah ada.")
            return False
        self.members[member.member_id] = member
        print(f"Anggota '{member.name}' berhasil ditambahkan.")
        return True

    def delete(self, member_id):
        member = self.members.get(member_id)
        if member and not member.borrowed_books:
            del self.members[member_id]
            return True
        return False

    def get(self, member_id):
        return self.members.get(member_id)

    def list_all(self):
        return self.members.values()

    def search(self, keyword):
        keyword_lower = keyword.lower()
        return [m for m in self.members.values() if keyword_lower in m.name.lower()]


#Manager
class LibraryManager:
    def __init__(self, book_repo: BookRepository, member_repo: MemberRepository):
        self.books = book_repo
        self.members = member_repo

    def borrow_book(self, member_id, book_code):
        member = self.members.get(member_id)
        book = self.books.get(book_code)
        if member and book:
            success, msg = member.borrow_book(book)
            print(msg)
            if success:
                print(f"Buku yang sedang dipinjam oleh {member.name}:")
                member.display()
        else:
            print("Anggota atau buku tidak ditemukan.")


# Application
def main():
    book_repo = BookRepository()
    member_repo = MemberRepository()
    manager = LibraryManager(book_repo, member_repo)

    while True:
        print("\n=== SELAMAT DATANG DI SISTEM PERPUSTAKAAN ===")
        print("+----+------------------------+")
        print("| No | Login Sebagai          |")
        print("+----+------------------------+")
        print("| 1  | Admin                  |")
        print("| 2  | Anggota                |")
        print("| 3  | Keluar                 |")
        print("+----+------------------------+")
        role = input("Pilih: ")

        if role == "1":
            pwd = input("Masukkan password admin: ")
            if pwd != "333":
                print("Password salah.")
                continue

            while True:
                print("\n=== MENU ADMIN ===")
                print("+----+-------------------------+")
                print("| No | Menu                    |")
                print("+----+-------------------------+")
                print("| 1  | Tambah Buku             |")
                print("| 2  | Lihat Buku              |")
                print("| 3  | Cari Buku               |")
                print("| 4  | Hapus Buku              |")
                print("| 5  | Tambah Anggota          |")
                print("| 6  | Hapus Anggota           |")
                print("| 7  | Cari Anggota            |")
                print("| 8  | Lihat Semua Anggota     |")
                print("| 9  | Kembali                 |")
                print("+----+-------------------------+")
                admin_choice = input("Pilih: ")

                if admin_choice == "1":
                    code = input("Kode Buku (misal BK001): ").strip()
                    title = input("Judul Buku: ").strip()
                    author = input("Penulis: ").strip()
                    if not code or not title or not author:
                        print("Data buku tidak boleh kosong.")
                        continue
                    book_repo.add(Book(code, title, author))

                elif admin_choice == "2":
                    print("\nDAFTAR BUKU:")
                    print(f"{'Kode':<12} | {'Judul':<30} | {'Penulis':<20} Status")
                    print("-" * 80)
                    for book in book_repo.list_all():
                        book.display()

                elif admin_choice == "3":
                    keyword = input("Masukkan identitas buku: ").strip()
                    if not keyword:
                        print("Kata kunci tidak boleh kosong.")
                        continue
                    results = book_repo.search(keyword)
                    print(f"\nHasil pencarian buku untuk '{keyword}':")
                    if results:
                        print(f"{'Kode':<12} | {'Judul':<30} | {'Penulis':<20} Status")
                        print("-" * 80)
                        for book in results:
                            book.display()
                    else:
                        print("Tidak ditemukan buku yang sesuai.")

                elif admin_choice == "4":
                    code = input("Kode Lengkap Buku (misal BK001-1): ").strip()
                    if not code:
                        print("Kode buku tidak boleh kosong.")
                        continue
                    if book_repo.delete(code):
                        print("Buku dihapus.")
                    else:
                        print("Gagal hapus buku (mungkin sedang dipinjam atau kode tidak ditemukan).")

                elif admin_choice == "5":
                    mid = input("ID Anggota: ").strip()
                    name = input("Nama: ").strip()
                    tipe = input("Tipe Anggota (A: Mahasiswa / B: Dosen / C: Umum): ").strip().upper()
                    if not mid or not name or tipe not in Member.MAX_BOOKS:
                        print("Data anggota tidak valid.")
                        continue
                    member_repo.add(Member(mid, name, tipe))

                elif admin_choice == "6":
                    mid = input("ID Anggota: ").strip()
                    if not mid:
                        print("ID anggota tidak boleh kosong.")
                        continue
                    if member_repo.delete(mid):
                        print("Anggota dihapus.")
                    else:
                        print("Gagal hapus anggota (mungkin masih meminjam buku atau ID tidak ditemukan).")

                elif admin_choice == "7":
                    keyword = input("Masukkan nama anggota: ").strip()
                    if not keyword:
                        print("Kata kunci tidak boleh kosong.")
                        continue
                    results = member_repo.search(keyword)
                    print(f"\nHasil pencarian anggota untuk '{keyword}':")
                    if results:
                        print("Keterangan Tipe: A = Mahasiswa, B = Dosen, C = Umum")
                        print(f"{'ID':<10} | {'Nama':<25} | Tipe")
                        print("-" * 50)
                        for member in results:
                            member.display()
                    else:
                        print("Tidak ditemukan anggota yang sesuai.")

                elif admin_choice == "8":
                    print("\nDAFTAR ANGGOTA:")
                    print("Keterangan Tipe: A = Mahasiswa, B = Dosen, C = Umum")
                    print(f"{'ID':<10} | {'Nama':<25} | Tipe")
                    print("-" * 50)
                    for member in member_repo.list_all():
                        member.display()

                elif admin_choice == "9":
                    break

                else:
                    print("Pilihan tidak valid.")

        elif role == "2":
            while True:
                print("\n=== MENU ANGGOTA ===")
                print("+----+-------------------------+")
                print("| No | Menu                    |")
                print("+----+-------------------------+")
                print("| 1  | Lihat Anggota           |")
                print("| 2  | Pinjam Buku             |")
                print("| 3  | Kembalikan Buku         |")
                print("| 4  | Cari Buku               |")
                print("| 5  | Kembali                 |")
                print("+----+-------------------------+")
                choice = input("Pilih: ")

                if choice == "1":
                    print("\nDAFTAR ANGGOTA:")
                    print("Keterangan Tipe: A = Mahasiswa, B = Dosen, C = Umum")
                    print(f"{'ID':<10} | {'Nama':<25} | Tipe")
                    print("-" * 50)
                    for member in member_repo.list_all():
                        member.display()

                elif choice == "2":
                    mid = input("ID Anggota: ").strip()
                    code = input("Kode Lengkap Buku: ").strip()
                    if not mid or not code:
                        print("ID anggota dan kode buku tidak boleh kosong.")
                        continue
                    manager.borrow_book(mid, code)

                elif choice == "3":
                    mid = input("ID Anggota: ").strip()
                    if not mid:
                        print("ID anggota tidak boleh kosong.")
                        continue
                    member = member_repo.get(mid)
                    if member:
                        code = input("Kode Buku yang dikembalikan: ").strip()
                        if not code:
                            print("Kode buku tidak boleh kosong.")
                            continue
                        if member.return_book(code):
                            print("Buku dikembalikan.")
                            print(f"Buku yang masih dipinjam oleh {member.name}:")
                            member.display()
                        else:
                            print("Buku tidak ditemukan.")
                    else:
                        print("Anggota tidak ditemukan.")

                elif choice == "4":
                    keyword = input("Masukkan kata kunci judul/penulis: ").strip()
                    if not keyword:
                        print("Kata kunci tidak boleh kosong.")
                        continue
                    results = book_repo.search(keyword)
                    print(f"\nHasil pencarian buku untuk '{keyword}':")
                    if results:
                        print(f"{'Kode':<12} | {'Judul':<30} | {'Penulis':<20} Status")
                        print("-" * 80)
                        for book in results:
                            book.display()
                    else:
                        print("Tidak ditemukan buku yang sesuai.")

                elif choice == "5":
                    break

                else:
                    print("Pilihan tidak valid.")

        elif role == "3":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
