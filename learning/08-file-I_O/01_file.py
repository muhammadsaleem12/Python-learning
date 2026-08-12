# The random-access memory is volatile, and all its contents are lost once a program terminates in order to persist the data forever, we use files

# A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it. 

#RAM  = volatile 
# HDD = Non volatile

#  we can read a file and write a file.

'''
a = "a very long string with emails"

emails = []
tooks 3 seconds generated a bundle of emails, after the execution of the code, it doesn't get stored anywhere. it disappears.

to store the data somewhere, you gotta use FILE.  Mp3, Mp4, Pdf, etc. to persist the data. using (NON VOLATILE MEMORY)

so why dont we use a NON-VOLATILE memory instead of RAMS, the answer is that we don't because RAMS are faster relative to HDD/SDD (Non- volatiles)

'''

# Types of files 
# 1. text files (.txt, .py, .c, etc) 
# 2. binary file (.jpg, .dat, etc)

# python has a lot of fucntions for reading, updating and deleting file.

# to read a file

f = open("file.txt") # helps open the files its a buitl-in function that takes two parameters (filename,  mode("r" by default))
data = f.read() # basically the function to read.
print(data) # printed data 
f.close # whenever you open a file, its a must to close it back.