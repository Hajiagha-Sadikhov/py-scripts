#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print("""
MAC Ünvanını Dəyişdirmək
1) MAC Ünvanını Təsadüfi Seç
2) MAC Ünvanını Əl İlə Seç
3) MAC  Ünvanı Orijinal Hala Geri Döndür!

""")

islem_no = input("Əməliyyat Nömrəsini Daxil Edin (1,2,3): ")

if(islem_no == "1"):
    os.system("ifconfig eth0 down")
    os.system("macchanger -r eth0")
    os.system("ifconfig eth0 up")
    print("\nMAC Ünvanı Təsadüfi Seçildi!")

elif(islem_no == "2"):
    mac_adres = input("Yeni MAC Ünvanını Daxil Edin: ")
    os.system("ifconfig eth0 down")
    os.system("macchanger --mac " + mac_adres + " eth0")
    os.system("ifconfig eth0 up")
    print("\nMAC Ünvanı Əl İlə Seçildi!")

elif(islem_no == "3"):
    os.system("ifconfig eth0 down")
    os.system("macchanger -p eth0")
    os.system("ifconfig eth0 up")
    print("\nMAC  Ünvanı Orijinal Hala Geri Döndü!")

else:
    print("Xəta, səhv düyməni basdınız!")

