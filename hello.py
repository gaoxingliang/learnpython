"""

comment here
"""
hot = True
if hot == True :
    print("It's hot here");


a = True
b = False
if a and b :
    print("I should not print here")


if a or b :
    print("Yes it's right print me")

temp = 30
if temp < 10:
    print("Should not print here, it's colde")

if temp >= 30:
    print("Yes, it's hot")

temp2 = 20
if temp2 > 10:
    print("the temp 2 is larger than 10")
    if temp2 < 30:
        print("not so hot")


if temp > 20 and (a == True):
    print("Yes it's hot");


bb = True
if bb:
    message = "Hello world"
    print(message)


hot = 20
if hot > 10:
    print("large than 10")
elif hot > 20:
    print("large than 20")
elif hot > 30:
    print("large than 30")
else:
    print("unknown")


tempnow = 10
raining = False
if tempnow > 10:
    print("hot")
else:
    if raining:
        print("it's raining")
    else:
        print("not raining here")

print(True or False)
print(False and True)