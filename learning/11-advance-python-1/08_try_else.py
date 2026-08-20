'''TRY WITH ELSE:'''

# try with else: only works with the condition with try: successfully runs,
# if not then the except: will do its thing, and else: wont run at all. 

try:
    a = int(input("Hey! Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyy")

else:
    print("I am inside else")