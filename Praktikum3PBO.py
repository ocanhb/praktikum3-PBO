# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:14:43 2024

@author: ocanh
"""

class Praktikan:
    def __init__(self, nama, nim, fakultas, hobi):
        self.nama = nama  
        self.nim = nim    
        self.fakultas = fakultas  
        self.hobi = hobi  
    
    def mahasiswa_nama(self):
        return self.nama   
    
    def mahasiswa_nim(self):
        return self.nim    
    
    def mahasiswa_fakultas(self):
        return self.fakultas  
    
    def mahasiswa_hobi(self):
        return self.hobi   

praktikan1 = Praktikan("Hasanul Bashori", "064002300041", "Teknik Informatika", "Nonton anime")  

print("----Program menampilkan identitas---")
print("Nama saya adalah", praktikan1.mahasiswa_nama())    
print("NIM saya", praktikan1.mahasiswa_nim())              
print("Saya dari fakultas", praktikan1.mahasiswa_fakultas())  
print("Hobi saya adalah", praktikan1.mahasiswa_hobi())     