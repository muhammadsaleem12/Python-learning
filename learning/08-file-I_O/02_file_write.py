# how to write in a file

# suppose we have a string 

st = "Hey there! Good afternoon." 

f = open("file2.txt", "w") # we have used the the mode "w"  in the second paramenter indicating to write. 

f.write(st) # assigned the string above to write into the new file created.

f.close # we closed it here.

# WHAT HAPPEND IF YOU RUN THE CODE!

# executing the code will immediately create a file named (file2.txt) and write the string assigned above in it for us. when you open the file you'll hopefully see the output.
# we were successfully able to write into the file.