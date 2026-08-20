'''RAISING EXCEPTION'''

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))


# when dividing with 0 the function crashs and shows a ZeroDivisionError.
# here we dont want that ugly ZeroDivisionError: so we created out own with the raise exception.

if(b == 0):
    raise ZeroDivisionError("Hey! our program is not meant to divide numbers by zero.") # raise raises an error and have the function crashes.
else:
    print(f"The division a/b is {a/b}")