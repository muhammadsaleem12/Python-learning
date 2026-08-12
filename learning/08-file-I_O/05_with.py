# what is WITH statement

f = open("file5.txt")

print(f.read())

f.close() # what if we dont always want to close the file.


# The same can be written using with statement like this:

with open("file5.txt") as f:
    print(f.read())


# you dont have to explicityly close the file.
# outside the with statement the file will be closed automatically.

