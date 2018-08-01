# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:55:52 2018

@author: gaoxi
"""

# with as  与try with resource 类似
# 比如打开文件
file1 = open("afile", "r")
data1 = file1.read()
file1.close()

