#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("""
Port Tarama Seçimləri
1) Sürətli Tarama
2) Xidmət və Versiya Məlumatı
3) Əməliyyat Sistemi Məlumatı
4) Təhlükəsizlik Açığı Tarama
5) Dərin Tarama
6) Müəyyən Portları Tara
7) SYN Tarama (Gizli Tarama)
8) Tam Bağlantı Tarama
9) Ping Tarama
10) Firewal və Təhlükəsizlik Filtrləri Təhlili
11) UDP Tarama
12) Bütün Portları Tara
13) Profil Tarama
14) Tələ Portları (Decoy Scan)
15) Zamanlama Ayarları
""")

islem_no = input("Əməliyyat Nömrəsini Daxil Edin (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15): ")
hedef_ip = input("Hədəf IP və ya Domain Daxil Edin: ")

if islem_no == "1":
    os.system(f"nmap -T4 {hedef_ip}")

elif islem_no == "2":
    os.system(f"nmap -sS -sV {hedef_ip}")
    
elif islem_no == "3":
    os.system(f"nmap -O {hedef_ip}")
   
elif islem_no == "4":
    os.system(f"nmap --script vuln {hedef_ip}")

elif islem_no == "5":
    os.system(f"nmap -A -T4 {hedef_ip}")

elif islem_no == "6":
    portlar = input("Tarağınız portları vergüllə ayıraraq daxil edin (məsələn: 80,443,22): ")
    os.system(f"nmap -p {portlar} {hedef_ip}")

elif islem_no == "7":
    os.system(f"nmap -sS {hedef_ip}")

elif islem_no == "8":
    os.system(f"nmap -sT {hedef_ip}")

elif islem_no == "9":
    os.system(f"nmap -sn {hedef_ip}")

elif islem_no == "10":
    os.system(f"nmap -sA {hedef_ip}")

elif islem_no == "11":
    os.system(f"nmap -sU {hedef_ip}")

elif islem_no == "12":
    os.system(f"nmap -p- {hedef_ip}")

elif islem_no == "13":
    os.system(f"nmap -sV --script=default {hedef_ip}")

elif islem_no == "14":
    decoy_ip = input("Tələ IP ünvanlarını vergüllə ayıraraq daxil edin (məsələn: 192.168.1.1, 192.168.1.2): ")
    os.system(f"nmap -D {decoy_ip} {hedef_ip}")

elif islem_no == "15":
    timing = input("Zamanlama səviyyəsini daxil edin (0-5, daha yavaş və diqqətli üçün 0, sürətli üçün 5): ")
    os.system(f"nmap -T{timing} {hedef_ip}")

else:
    print("Xəta, səhv düyməni basdınız!")
