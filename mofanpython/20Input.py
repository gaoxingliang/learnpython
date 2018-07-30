# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:03:17 2018

@author: gaoxi
"""

n = input("give a number")
print("what you input is ", n)
n = int(n)
if n >= 10:
    print("a > 10 number")
elif n >= 5:
    print(">5")
else:
    print("last one")