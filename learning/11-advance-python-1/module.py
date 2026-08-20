# here we have defined a function that we will try and call from another file like 10_main.py
# by using the (from module import myFunc) on that file, doing that well be able to access this files code from there..

# let's Try

def myFunc():
    print("Hello World!")

myFunc()
print(__name__) # what does __name__ do, this will tell us which file is this function is being called from.

# for instance if you run the code the output here will be

# Hello World!
# __main__

# ofcourse the __name__ will print __main here becuase we are running it from the main file, 
# but what if we run it from the another file like 10_main.py

# the output will be 

# Hello World!
# module 

# since we will be calling out myFunc() from module it should be printing this.
# lets try it from that file, shall we.


'''Note: '''

if __name__ == "__main__":
    # if this code is directly executed by running the file its present in, only then run this code.
    print("We are directly running the code.")

# now the above code as writtin above will only be executed if this file is directly running it, 
# this will not be executed from any other file by importing, just like we did with the above function.
