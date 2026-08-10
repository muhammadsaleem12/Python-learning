# lesson 6 practice set - conditional statements

# problem 1: find the greatest number among 4 numbers
a1 = int(input("Enter number1: "))
a2 = int(input("Enter number2: "))
a3 = int(input("Enter number3: "))
a4 = int(input("Enter number4: "))

if a1 > a2 and a1 > a3 and a1 > a4:
    print("The greatest number is:", a1)
elif a2 > a1 and a2 > a3 and a2 > a4:
    print("The greatest number is:", a2)
elif a3 > a1 and a3 > a2 and a3 > a4:
    print("The greatest number is:", a3)
else:
    print("The greatest number is:", a4)


# problem 2: check if student passed (needs >=40% overall and >=33% per subject)
marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

# check total percentage
total_percentage = (100) * (marks1 + marks2 + marks3) / 300

if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("You have passed:", total_percentage, "%")
else:
    print("You have failed:", total_percentage, "%")


# problem 3: spam message detector
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your message: ")

if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("This is a spam message.")
else:
    print("This is not a spam message.")


# problem 4: check if username has less than 10 characters
username = input("Enter your username: ")

if len(username) < 10:
    print("Username is valid.")
else:
    print("Username is not valid. It should be less than 10 characters.")


# problem 5: check if name is present in list
l = ["Saleem", "Ali", "Ahmed", "Zain", "Ayesha"]

name = input("Enter your name: ")

if name in l:
    print("Your name is present in the list.")
else:
    print("Your name is not present in the list.")


# problem 6: grade calculation
marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:
    grade = "A+"
elif 80 <= marks < 90:
    grade = "A"
elif 70 <= marks < 80:
    grade = "B"
elif 60 <= marks < 70:
    grade = "C"
elif 50 <= marks < 60:
    grade = "D"
elif marks < 50:
    grade = "F"

print("Your grade is:", grade)


# problem 7: case-insensitive keyword search in post
post = input("Enter your post: ")

# converting both post and keyword to lower() for case-insensitive matching
if "saleem".lower() in post.lower():
    print("The post is talking about saleem.")
else:
    print("The post is not talking about saleem.")