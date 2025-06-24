from kelas.croissant import Croissant
from kelas.muffin import Muffin
from kelas.roti_manis import RotiManis
from kelas.butter_cookies import ButterCookies

def get_sample_data():
    return [
        Croissant("Croissant Classic", "C002", "Tepung, Air, Susu, Gula, Ragi, Garam, Mentega, Telur", 15, 60000, 5000),
        Muffin("Muffin Classic", "M003", "Tepung, Gula, Garam, Baking Powder, Telur, Margarin, Vanili", 15, 30000, 4000),
        RotiManis("Roti Manis Susu", "R004", "Tepung, Ragi, Gula, Telur, Susu, Mentega, Garam", 20, 50000, 2500),
        ButterCookies("Butter Cookies Chocochip", "B005", "Tepung, Mentega, Gula, Telur, Vanilla Extract, Garam, Choccochips", 15, 30000, 4000)
    ]
