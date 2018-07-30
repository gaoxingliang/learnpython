text="ThisIs aA fil\nThis is next line"
myfile=open("myfile.txt", "w")
myfile.write(text)
myfile.close()


appendtext = "\nappend file"
myfile=open("myfile.txt", "a")
myfile.write(appendtext)
myfile.close()


rfile = open("myfile.txt", "r")
content = rfile.read()
print(content)



rfile = open("myfile.txt", "r")
lines = rfile.readlines()

# with \n for the first and second line
print(lines)


rfile = open("myfile.txt", "r")
lines = rfile.readlines()

print(lines)