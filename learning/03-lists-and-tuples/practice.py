# lesson 3 practice set - lists and tuples

# problem 1: store student marks and sort them
marks = []

f1 = int(input("Enter the marks: "))
marks.append(f1)
f2 = int(input("Enter the marks: "))
marks.append(f2)
f3 = int(input("Enter the marks: "))
marks.append(f3)
f4 = int(input("Enter the marks: "))
marks.append(f4)
f5 = int(input("Enter the marks: "))
marks.append(f5)
f6 = int(input("Enter the marks: "))
marks.append(f6)

# sort in ascending order
marks.sort()
print("sorted marks:", marks)


# problem 2: check that a tuple cannot be changed
a = (34, 364, "saleem")

# a[2] = "waseem" # TypeError: tuple object does not support item assignment!

print(a)


# problem 3: sum a list with 4 numbers
l = [34, 45, 5, 7]
print("sum of list:", sum(l))


# problem 4: count zeros in a tuple
a = (7, 0, 8, 0, 0, 9)

n = a.count(0)
print("number of zeros:", n)