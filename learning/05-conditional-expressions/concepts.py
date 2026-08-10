# lesson 5 - conditional expressions
# practicing if, elif, and else ladder

a = int(input("Enter your age: "))

if a >= 18:
    print("You are eligible to vote.")
    print("You can vote in the upcoming elections.")

elif a < 0:
    print("Invalid age entered. Please enter a valid age.")

elif a == 0:
    print("You're not born yet. Please enter a valid age.")

else:
    print("You are not eligible to vote.")
    print("Please try again when you are 18 or older.")

print("Thank you for using the voting eligibility checker.")