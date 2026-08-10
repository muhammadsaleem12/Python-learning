# lesson 1 variable and datatypes (practice problems)

# prob 1: add two numbers
a = 5
b = 10
sum = a + b
print("sum is:", sum)


# prob 2: find remainder when number is divided by z
num = 17
z = 5
rem = num % z
print("remainder:", rem)


# prob 3: check type of variable assigned using input()
val = input("enter something: ")
print(type(val)) # spoiler: input always gives str!


# prob 4: comparison operator
a = 34
b = 38
# is a greater than b?
print(a > b) # gives False


# prob 5: average of two numbers from user
# forgot to convert to int at first and it just glued the strings together lol
num1 = float(input("enter first num: "))
num2 = float(input("enter second num: "))
avg = (num1 + num2) / 2
print("average:", avg)


# prob 6: square of a number
x = int(input("enter number to square: "))
# square = x * x
square = x ** 2
print("square is:", square)