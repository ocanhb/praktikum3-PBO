# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:35:40 2024

@author: ocanh
"""

class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def ukuran_panjang(self):
        return self.panjang

    def ukuran_lebar(self):
        return self.lebar

    def hitung_luas(self):
        return self.panjang * self.lebar
        
print("Hasanul Bashori 064002300041 Teknik informatika")
print("---program menghitung luas persegi panjang---")

panjang_persegi_panjang = float(input("Masukkan panjang persegi panjang: "))
lebar_persegi_panjang = float(input("Masukkan lebar persegi panjang: "))

persegi_panjang = PersegiPanjang(panjang_persegi_panjang, lebar_persegi_panjang)

print("panjang persegi panjang:", persegi_panjang.ukuran_panjang())

print("lebar persegi panjang:", persegi_panjang.ukuran_lebar())

luas = persegi_panjang.hitung_luas()
print("persegi panjang dengan panjang", persegi_panjang.ukuran_panjang(), "cm dan lebar", persegi_panjang.ukuran_lebar(), "cm memiliki luas sebesar", luas, "cm^2")
