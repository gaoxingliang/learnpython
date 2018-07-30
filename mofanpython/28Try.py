# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 21:27:09 2018

@author: gaoxi
"""

try:
    file = open("NotExists", "r+")
except Exception as e:
    print(e)
    resp = input("create a file?")
    if resp == 'y':
        file=open("NotExists", "w")
    else:
        pass
    
else:
    print("open file success")
    file.write("QQ")
    
finally:
    print("Im in finally")
file.close()