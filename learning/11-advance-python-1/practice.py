'''Problem 01 = Write a program to open three files 1.txt, 2.txt, 3.txt if any of these files are not present,
 a message without exiting the program must be printed promoting the same'''


try:
    with open("one.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("two.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("three.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)


print("Thank You")


'''Problem 02 = Write a program to print third, fifth, and seventh element from a list using enumerate fucntion'''


l = [1, 2, 3, 4, 5, 6, 7, 8]


for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)



'''Problem 03 = Write a list comprehension to print a list which contains the multiplication table of a user entered number.'''

n = 5

table = [n*i for i in range(1, 11)]

print(table)


'''Problem 04 = Write a program to display a/b where a and b are integers. if b=0, display infinite by handlingthe 'ZeroDivisionError'. '''

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError as z:
    print("Infinite")


'''Problem 05 = Store the multiplication tables generated in problem 3 in a file named Tables.txt'''


n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]

with open("Tables.txt", "a") as f:
    f.write(str(table) + "\n")
