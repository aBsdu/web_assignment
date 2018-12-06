# to open the file
file = open("a.txt","rt")

#reading the file
'''read_file = file.read()'''


# line by line reading the file
'''read_file = file.readline()'''

# using for loop reading the file
'''for a in file:
    print a
'''

# reading file
read_file = file.readlines()
print read_file


# closing the file after all the process
file.close()
