# lesson 1 - variables and data types
# testing basic types in python

# 1. Variables
# python doesn't need 'var' or 'let', just name = value
x = 10
age = 22
name = "Alex"
is_student = True
gpa = 3.8

# print everything out
print(x)
print(name)
print(is_student)

# 2. Checking types
# use type() to see what kind of data it is
print(type(age))        # <class 'int'>
print(type(gpa))        # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>

# 3. Changing types (casting)
# str to int
num_str = "100"
converted = int(num_str)
print(converted + 50)   # gives 150

# float conversion
pi = 3.14
print(int(pi))          # turns into 3 (drops decimals, doesn't round!)

# 4. Things that broke / notes
# print("Age: " + age)  # TypeError: can't add int to string!
# fix: print("Age: " + str(age)) or use f-strings:
print(f"My name is {name} and I am {age} years old.")

# variables can overwrite their type easily
data = 5
data = "now a string"
print(data)