#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

def run_command(command):
    """ Komutu işlədir və çıxışı qaytarır. """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Komut işlədilə bilmədi: {str(e)}"

def chkrootkit_scan():
    """ chkrootkit ilə rootkit taraması aparır. """
    print("[*] chkrootkit taraması başlayır...")
    result = run_command(["chkrootkit"])
    return result

def rkhunter_scan():
    """ rkhunter ilə rootkit taraması aparır. """
    print("[*] rkhunter taraması başlayır...")
    result = run_command(["rkhunter", "--checkall"])
    return result

def main():
    print("Rootkit Təsbit Proqramı\n")

    # chkrootkit taraması
    chkrootkit_result = chkrootkit_scan()
    print("\nchkrootkit Nəticələri:")
    print(chkrootkit_result)

    # rkhunter taraması
    rkhunter_result = rkhunter_scan()
    print("\nrkhunter Nəticələri:")
    print(rkhunter_result)

    # Digər rootkit təyinetmə alətləri əlavə edilə bilər

if __name__ == "__main__":
    main()
