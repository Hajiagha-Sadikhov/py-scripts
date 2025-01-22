#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

def detect_waf():
    print("Təhlükəsizlik Divarı Aşkar Etmə Proqramı")
    target = input("Sayt ünvanını daxil edin: ") 
    try:
        subprocess.run(["wafw00f", target], check=True)  
    except FileNotFoundError:
        print("wafw00f aləti tapılmadı. Zəhmət olmasa quraşdırın.")
    except subprocess.CalledProcessError as e:
        print(f"Xəta baş verdi: {e}")

detect_waf()
