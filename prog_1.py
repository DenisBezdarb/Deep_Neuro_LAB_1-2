# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:19:22 2025

@author: user
"""

from random import randint

s = []
summ = 0
for i in range(10):
    s.append(0)
    s[i] = randint(0, 10)
    if s[i] % 2 == 0:
        summ += s[i]

print(summ)
