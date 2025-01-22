#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import py_compile

print("Kompilyasiya Proqramı")
fayl_adı = input("\nFaylın adını daxil edin: ")  # Python 3-də input istifadə olunur
py_compile.compile(fayl_adı)

