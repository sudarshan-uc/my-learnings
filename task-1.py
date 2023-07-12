import os
import shutils

# Create two folders:
def create_dir(dirName):
    os.mkdir(dirName)
    print("Directiory created" dirName)

def main():
    userName = input("Your Name please : ")
    userCity = input("Your Current City : ")
    create_dir('a.txt')
    create_dir('b.txt')
    if(os.path.exists(a.txt)):
        print("a.txt directory exists, creating a file and writing the message.")
        f = open("a.txt/c.txt", "wt")
        f.write("My name is {userName}. I am from {userCity}.")
        f.close()
        if(os.path.exists(a.txt/c.txt)):
            print("file is created successfully in a.txt directory")
        else:
            print("File does not exist")
            exit()
    else:
        print("Directory a.txt does not exist")
        exit()
    os
    print("copying the file")
    shutils.copy('a.txt/c.txt', 'b.txt/')
    

if __name__ == '__main__':
    main()