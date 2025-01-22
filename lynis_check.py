#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

print("Sistem Zəiflik Analiz Proqramı")

def check_lynis_installed():
    try:
        subprocess.run(["lynis", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_lynis():
    """Lynis alətini quraşdırır."""
    print("Lynis aləti sisteminizdə quraşdırılmayıb. Quraşdırma başlayır...")
    os.system("sudo apt update && sudo apt install lynis -y")
    print("Lynis uğurla quraşdırıldı!")

if not check_lynis_installed():
    while True:
        user_input = input("Lynis aləti sisteminizdə quraşdırılmayıb. Quraşdırmaq istəyirsiniz? (y/n): ").lower()
        if user_input == "y":
            install_lynis()
            break
        elif user_input == "n":
            print("Proqram sonlandırılır.")
            exit(0)
        else:
            print("Yanlış giriş. Xahiş olunur 'y' və ya 'n' daxil edin.")

output_file = "lynis_output.txt"
os.system(f"lynis audit system > {output_file}")
print(f"Nəticələr {output_file} faylına qeyd edildi.")
