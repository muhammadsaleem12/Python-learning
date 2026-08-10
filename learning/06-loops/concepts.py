# lesson 6 - loops in python
# practicing while loops, for loops, break, continue, and pass


# 1. WHILE LOOPS

# basic counter
i = 1 
while i < 5:
    print("SALEEM")
    i = i + 1

# printing numbers 1 to 50
i = 1 
while i < 51:
    print(i)
    i += 1 

# iterating over a list using while loop
l = [1, "Saleem", False, "this", "Python", True, 3.14]
i = 0 
while i < len(l):
    print(l[i])
    i += 1


# 2. FOR LOOPS

# range function range(start, stop)
for i in range(1, 6):
    print(i)

# iterating over list
l = [1, 3, 5, 7, 9]
for i in l:
    print(i)

# iterating over tuple
t = (6, 7, 8, 9, 10)
for i in t:
    print(i)

# iterating over string
s = "Saleem"
for i in s:
    print(i)


# 3. FOR LOOP WITH ELSE

# else block executes after the loop completes naturally
l = [1, 2, 3, 4, 5]
for item in l:
    print(item)
else:
    print("Loop is completed")


# 4. BREAK, CONTINUE, AND PASS

# break: exits loop immediately
for i in range(100):
    if i == 50:
        break 
    print(i)

# continue: skips current iteration
for i in range(100):
    if i == 50:
        continue 
    print(i)

# pass: placeholder statement (prevents IndentationError)
for i in range(645):
    pass