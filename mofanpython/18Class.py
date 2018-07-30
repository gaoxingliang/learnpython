# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 20:44:22 2018

@author: gaoxi
"""

class Calculator:
    name="Good cal"
    price= 20
    
    def __init__(self, name, price, height, width):
        self.name = name
        self.price = price
        self.h = height
        self.w = width
    
    def add(self, a, b):
        result = a + b
        print(result)
        print(self.price)
        
        
    def substract(self, x, y):
        return x - y
    
    # must has a self
    def wrong(self, x,m):
        print(x+m)
        


cal = Calculator()
cal.wrong(3, 2)


print(cal.name)
