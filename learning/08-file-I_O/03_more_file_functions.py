f = open("file3.txt",)


# lines = f.readlines() # reads a single line from a file and returns it as a string 
# print(lines, type(lines))  # this functions contains all the str and returns a list 

# seperately printing the strings 

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5, type(line5))


# how can we do the same using WHILE loop

line= f.readline()
while(line != ""):
    print(line)
    line = f.readline()



f.close


# Mode of opening a file 

# r = open for reading 

# w = open for writing 

# a = open for appending (addding at the end of something perticular)

# + = open for updating 

# 'rb' will open for read in binary mode 

# 'rt' will open for read in text mode