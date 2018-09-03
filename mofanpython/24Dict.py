# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 20:02:29 2018

@author: gaoxi
"""

dict = {"apple" : 1, "pear": 3, "orange": 34}

print(dict["apple"])

del dict["pear"]

print(dict)



char_list=['a', 'b', 'b', 'a']
print(set(char_list))

unique_char = set(char_list)
unique_char.add("Q")
print(unique_char)
print("remove it", unique_char.remove('a'))
print("discard ", unique_char.discard('Y'))

sentence = "welcome to this demo"
print(set(sentence))


