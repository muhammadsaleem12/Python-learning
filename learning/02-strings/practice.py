# lesson 2 practice - strings

# 1. display user name with Good Afternoon
name = input("enter your name: ")
print(f"Good Afternoon, {name}")
# or using + : print("Good Afternoon, " + name)


# 2. fill in letter template
letter = '''
          Dear <| Name |>,
          You are selected!
          <| Date |>
             '''

# replacing placeholders
letter = letter.replace("<| Name |>", "Alex")
letter = letter.replace("<| Date |>", "10 August 2026")
print(letter)


# 3. detect double space in a string
text = "this is a string with  double spaces in it"
# .find() returns index where it starts, or -1 if not found
double_space = text.find("  ")
print("double space index:", double_space) 


# 4. replace double from problem 3 spaces with single space
# string replaced:
clean_text = text.replace("  ", " ")
print(clean_text)


# 5. format letter using escape sequence characters
# \n for new line, \t for tab indent
formatted_letter = "Dear Alex,\n\tThis Python course is nice.\nThanks!"
print(formatted_letter)