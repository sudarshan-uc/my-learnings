import os
import datetime

f = open ("a.txt", "rt")
x = f.read(10)
print(x)
x = f.read(10)
print(x)

x = os.path.exists("a.txt")
print(x)

# THis is file handling program

x = input("Enter name of file : ")

if (os.path.exists(x)):
    print("Yes, I found the file")
else:
    print("there is no such file")

i = 1
while(i <= 100):
    f = "file" + str(i) + ".txt"
    x = open(f,"wt")
    i = i + 1
    x.close()

w = input("Waiting")

while(i <= 100 ):
    f = "file" + str(i) + ".txt"
    print("Deleting the file; ", f)
    os.rm(f)
    i = 1 + 1
    