# lesson 2 - strings basics
# practicing string operations and indexing

# 1. basic strings and quotes
name = "alex"
greeting = 'hello'
multiline = '''this is a 
multiline string'''

print(greeting + " " + name)


# 2. string slicing and indexing (0-based)
text = "python"
print(text[0])     # 'p' (first letter)
print(text[-1])    # 'n' (last letter)
print(text[0:3])   # 'pyt' (from index 0 up to 3, excludes 3)
print(text[2:])    # 'thon' (index 2 to end)


# 3. useful string methods
msg = "  hello world  "
print(msg.upper())         # "  HELLO WORLD  "
print(msg.strip())         # removes spaces from start/end
print(msg.replace("l", "z")) # "  hezzo worzd  "


# 4. f-strings (easiest way to print variables inside text)
age = 22
print(f"my name is {name} and i am {age}")


# 5. string length & escape chars
word = "python"
print(len(word))   # 6

# \n for new line, \t for tab
print("line1\nline2")


# note: strings are immutable! 
# text[0] = 'z' # TypeError: can't change letters directly