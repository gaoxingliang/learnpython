from numpy import shape,tile
a = [[1,2], [2,3], [3,4]]
print(shape(a)[0])
b = tile(a, (2,1))
print(b)