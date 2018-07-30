# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:10:07 2018

@author: gaoxi
"""

# tuple can't be changed
atuple=(12, 2 ,3 ,4,56, 56)

alist=[1213, 423,565,43]


for x in atuple:
    print(x)
    
print("list....")
for index in range(len(alist)):
    print(alist[index])
    
print("tuple")
for index in range(len(atuple)):
    print(atuple[index])
    
    
# place 666 to index 1    
alist.insert(1, 666)
print(alist)

# remove a value -> throw error if the value not exists
#alist.remove(33)
alist.remove(1213)
print(alist)



print(alist[:2])

print(alist.index(565))
alist.sort()
print(alist)
alist.sort(reverse=True)
print(alist)

mult_dim_a=[
        [1,2,3],
        [2,3,4]
        ]

print(mult_dim_a[1][2])