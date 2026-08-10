# lesson 7 practice set - functions and recursion

# problem 1: find greatest of 3 numbers
a = 100
b = 23
c = 3

def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c 

print("Greatest number is:", greatest(a, b, c))


# problem 2: fahrenheit to celsius conversion
def f_to_c(f):
    return 5 * (f - 32) / 9

f_temp = int(input("Enter temperature in F: "))
c_temp = f_to_c(f_temp)
print(f"Degree °C: {round(c_temp, 2)}")


# problem 3: prevent print() from adding new line using end=""
print("a")
print("b")
print("c", end="")
print("d", end="\n")


# problem 4: recursive function to calculate sum of first n natural numbers
# sum(n) = sum(n-1) + n
def sum_recursive(n):
    if n == 1:
        return 1
    return sum_recursive(n - 1) + n

print("Sum of first 4 numbers:", sum_recursive(4))


# problem 5: recursive pattern printing
# ***
# **
# *
def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)

pattern(3)


# problem 6: inches to cm conversion (1 inch = 2.54 cm)
def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inch_to_cms(n)}")


# problem 7: remove a given word from a list and strip spaces
def rem(l, word):
    n = []
    for item in l:
        for item in l:
            if not(item == word):
                n.append(item.strip(word))
        return n

l = ["Saleem", "Zuko", "Waseem", "ko"]


print(rem(l, "ko"))


# problem 8: function to print multiplication table
def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

multiply(4)