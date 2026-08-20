a = 40 # global variable

def fun():
    global a # by using this method we basically overwrites the above a's value of 40 to 3 with the local variable. output: 3
    a = 3 # local variable
    print(a)

fun()
print(a)