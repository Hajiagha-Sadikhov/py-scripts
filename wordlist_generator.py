#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def wordlist_yarat(min_uzunluq, max_uzunluq, simvollar, output_file):
    """Verilən parametrlərə əsasən wordlist yaradır və fayla qeyd edir."""
    command = f"crunch {min_uzunluq} {max_uzunluq} '{simvollar}' -o {output_file}"
    os.system(command)
    print(f"Wordlist '{output_file}' adlı fayla qeyd edildi!")

def main():
    print("Wordlist Yaradıcı Proqramı\n")

    try:
        min_uzunluq = int(input("Minimum uzunluq sayını daxil edin: "))
        max_uzunluq = int(input("Maksimum uzunluq sayını daxil edin: "))
    except ValueError:
        print("Xahiş olunur, düzgün bir rəqəm daxil edin.")
        return

    simvollar = input("İstədiyiniz simvolları daxil edin (məsələn: abc123): ")

    output_file = input("Wordlist'in saxlanacağı fayl adını daxil edin (məsələn: wordlist.txt): ")

    wordlist_yarat(min_uzunluq, max_uzunluq, simvollar, output_file)

if __name__ == "__main__":
    main()
