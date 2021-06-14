# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:27:28 2021

@author: asus
"""

"SOAL NO. 8 APLIKASI 6a"
"PERHITUNGAN NILAI TOTAL TRANSAKSI PEMBELIAN PRINTER"


""
ulang="y"
while ulang=="y" or ulang =="Y":
#Siapkan variabel
    print("===========================")
    print(" APLIKASI 6a")
    print(" Pembelian printer")
    print("===========================")
    u=1
    #Hitung
    u =input(" Masukkan Banyak Printer = ")
    n=int(u)
    harga = n * 660000
    print(" Total Harga Pembelian Printer= Rp.",harga)
    ulang = input("\n Ulang program? y/t = ")
    if ulang=="t" or ulang=="T":
        break