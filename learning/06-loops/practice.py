# lesson 6 practice set - loops

# problem 1: multiplication table of a number using for loop
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")


# problem 2: greet people in list whose names start with 'S'
l = ["Saleem", "Waseem", "Zuko", "Ali"]

for name in l:
    if name.startswith("S"):
        print(f"Hello {name}")


# problem 3: multiplication table using while loop
n = int(input("Enter a number: "))
i = 1 

while i < 11:
    print(f"{n} X {i} = {n * i}")
    i += 1


# problem 4: check if a number is prime
n = int(input("Enter a Number: "))

for i in range(2, n):
    if (n % i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")


# problem 5: sum of first n natural numbers using while loop
n = int(input("Enter the number: "))
i = 1
sum_val = 0

while i <= n:
    sum_val += i
    i += 1

print("Sum:", sum_val)


# problem 6: factorial of a given number using for loop
n = int(input("Enter the number: "))
product = 1

for i in range(1, n + 1):
    product = product * i 

print(f"The factorial of {n} is {product}")


# problem 7: pyramid pattern
# for n = 3:
#   *
#  ***
# *****
n = int(input("Enter the number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))


# problem 8: right-triangle star pattern
# *
# **
# ***
n = int(input("Enter the number: "))

for i in range(1, n + 1):
    print("*" * i)


# problem 9: hollow square star pattern
n = int(input("Enter the number: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*")


# problem 10: multiplication table in reverse order
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} X {11 - i} = {n * (11 - i)}")