#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

def run_command(command):
    """ Komut çalışdırır və nəticəni qaytarır. """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Komut çalışdırıla bilmədi: {str(e)}"

print("VPN Nəzarət Aləti")
hedef_ip = input("Hedef IP: ")


print("[*] VPN taraması başlayır...")
tarama_sonucu = run_command(["ike-scan", hedef_ip])


print("[*] Tarama Nəticələri:")
print(tarama_sonucu)


with open("vpn_tarama_nəticələri.txt", "w") as file:
    file.write(tarama_sonucu)
    print("[*] Nəticələr vpn_tarama_nəticələri.txt faylına qeyd edildi.")
