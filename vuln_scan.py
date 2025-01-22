#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print("Zəiflik Təhlil Aləti")
hedef_ip = input("Hədəf IP: ")
os.system("nikto -h " + hedef_ip)
