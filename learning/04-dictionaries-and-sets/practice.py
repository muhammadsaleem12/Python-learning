# lesson 4 practice set - dictionaries and sets

# problem 1: urdu to english dictionary lookup
words = {
    "madad": "help",
    "pyaar": "love",
    "kursi": "chair",
    "billi": "cat",
}

word = input("Enter a word in urdu: ")
print(words.get(word, "Word not found in dictionary"))


# problem 2: input 8 numbers and display unique ones using a set
s = set()

s.add(int(input("Enter a number: ")))
s.add(int(input("Enter a number: ")))
s.add(int(input("Enter a number: ")))
s.add(int(input("Enter a number: ")))
s.add(int(input("Enter a number: ")))
s.add(int(input("Enter a number: ")))
s.add(int(input("Enter a number: ")))
s.add(int(input("Enter a number: ")))

print("Unique numbers entered:", s)


# problem 3: can a set have 18 (int) and "18" (str)?
s3 = set()
s3.add(18)
s3.add("18")
print(s3)                   # {18, '18'} -> Yes, int and str are different types


# problem 4: length of set with int and float values
s4 = set()
s4.add(20)
s4.add(20.0)
s4.add('20')
print("Length of s4:", len(s4)) # prints 2 because 20 == 20.0 in Python!


# problem 5: check data types of {} and set()
d = {}                      # empty dictionary
s = set()                   # empty set
print(type(d))              # <class 'dict'>
print(type(s))              # <class 'set'>


# problem 6: create favorite language dictionary for 4 friends
fav_lang = {}

name = input("Enter your name: ")
lang = input("Enter your language: ")
fav_lang.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your language: ")
fav_lang.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your language: ")
fav_lang.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your language: ")
fav_lang.update({name: lang})

print(fav_lang)


# problem 9: can you have a list inside a set?
# s = {8, 7, 12, "Saleem", [1, 2]} 
# Error: TypeError: unhashable type: 'list'
# Lists are mutable and cannot be stored inside a set. 
# Also, sets are unindexed, so values inside cannot be modified by index anyway.