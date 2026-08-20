'''TRY WITH FINALLY'''
# finally runs anyway, no matter what you do the finally would run.
'''
try:
    a = int(input("Hey! Enter a number: "))
    print(a)

except Exception as e:
    print(e)

finally:  
    print("I am inside finally")
'''

# so you must be wondering, why just not just simply use, print, that works just the same. 
# and thats actually true in the above case you can just print the message you wont have to use finally.

# so what excatly is the purpose of finally. lets see 

def main():
    try:
        a = int(input("Hey! Enter a number: "))
        print(a)
        return

    except Exception as e :
        print(e)
        return

    finally:
        print("Hey I am inside of finally.")


main()

# now in this above case with the function, you see if you dont put finally there the message wont be printed.
# the finally overwrites almost every other conditio, ignoring others, it will run eventually at any cost.