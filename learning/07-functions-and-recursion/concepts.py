# lesson 7 - functions & recursion
# practicing def, arguments, return values, default parameters, and recursion

# 1. FUNCTION DEFINITION AND CALL

def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c) / 3
    print(average)

# function calls
avg()
print("thankyou")


# 2. ARGUMENTS AND RETURN VALUES

def good_day(name, ending):
    print(f"Good Day, {name}!")
    print(ending)
    return "OK!"

# store returned value in variable 'a'
a = good_day("Saleem", "Thank you")
print(a)


# 3. DEFAULT ARGUMENTS

def greet(name, ending="Thank you!"):  # ending has a default value
    print(f"Good Day, {name}.")
    print(ending)

greet("Saleem", "Thanks")   # overrides default parameter
greet("Waseem")            # uses default parameter ("Thank you!")

    
# 4. RECURSION (Function calling itself: narrowing down the problem until it meets base condition)

def factorial(n):
    # base condition
    if n == 1 or n == 0:
        return 1 
    # recursive call
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(num)}")