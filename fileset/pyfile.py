# Program to read from a file and print the contents line by line
# and raise an exception if file not found

import sys

try:
    file1 = input("Enter a filename :")
    f = open(file1, 'r+t')
    contents = f.read()
    print(contents)

    mycont = input("Enter a text here:")
    f.write(mycont)
    f.write("\n")
    f.close()

    f = open(file1, 'r+t')
    contents = f.read()
    print(contents)
    f.close()

except FileNotFoundError:
    print("File does not exist!")
except PermissionError:
    print("You don't have the permissions")
except IsADirectoryError:
    print("Name given is a directory")
except:
    print("Error is ", sys.exc_info()[0])
