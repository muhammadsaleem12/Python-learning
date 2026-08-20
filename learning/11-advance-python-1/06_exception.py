'''EXCEPTION'''

'''
a = int(input("Hey! Enter a number: ")) # if the user writes something else, instead of an int then the program would crash.
print(a)
'''

# but if you wanna show the user the error message without crashing the code, then we can use try: and except:

try:
    a = int(input("Hey! Enter a number:"))
# except only runs we the try: fails
except Exception as e:  # now we are printing the error itself, like where did the user go wrong, our code would not crash at all.
    print(e)   


# and since the code is not crashing we can run further code after printing the error. like this:
print("Thank You!")

# # OUTPUT
# Hey! Enter a number:kevin
# invalid literal for int() with base 10: 'kevin'
# Thank You!




# this is another example of how to handle try and exceptions.
'''
try:
    # Code
except: ZeroDivisionError:
    # Code
except: TypeError:
    # Code
except:
    # Code  # All other exceptions are handled here.
'''