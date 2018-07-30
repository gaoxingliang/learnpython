def add(a, b):
    return a+b

print(add(1, 2))
print(add(a=1, b=2))

# this is wrong
#print(add(c=1, d=2))


def addVec(a,b):
    return a+b, a+1

ca, cb = addVec(1, 3)
print(str(ca) + " " + str(cb))

# 默认参数
def sale(price, brand, color="red", second_hand=True):
    print("price", price, " brand:", brand)


sale(1000, "MBD", color="S")

obj = None
print(obj)