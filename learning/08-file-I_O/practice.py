'''
To test the problems one must gotta uncomment each of the progrom by hand and test it out individually for better experience..

'''


# problem  1 = wirte3 a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

# f = open("poems.txt")
# content = f.read()
# if("twinkle" in content):
#     print("twinkle is present in the content")
# else:
#     print("The word twinkle is not present in the content")

    
# f.close()

# problem 2 = The game() function in a program lets a user play a game and returns the score as an integer. you need to read a file 'Hiscore.txt' which is either black or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

# import random

# def game():
#     print("Your are playing the game..")
#     score = random.randint(1, 62)
#     # fetch thehiscore
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore!=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#     print(f"Your score: {score}")

#     if(score>hiscore):
#         # write this hiscore to the file
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))

#     return score

# game()


# problem 3 = write a program to generate multiplication tables form 2 to 20 and wirte it to the different files. Place these files in a folder for a 13 - year old.

# def generateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} X {i} = {n*i}\n"

#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)


# for i in range(2, 21):
#     generateTable(i)



#problem 4 = A file contains a word "Donkey" multiple times. You need to write a program which replace this word with ##### by updating the same file.

# word = "Donkey"

# with open("donkey.txt", "r") as f:
#     content = f.read()

# contentNew = content.replace(word, "######")

# with open("donkey.txt", "w") as f:
#     content = f.write(contentNew)


# problem 5 = Repeat program 4 for a list of such words to be censored.

# words = ["Donkey", "Bad", "Ugly"]

# with open("bad_word.txt", "r") as f:
#     content = f.read()
# for word in words:
#     content = content.replace(word, "#" * len(word))

# with open("bad_word.txt", "w") as f:
#     content = f.write(content)


# problem 6 =  Write a program to mine a log file and find out whether it contains 'pyhton'.


# with open("log.txt") as f:
#     content = f.read()

# if("python" in content):
#     print("Yes python is present.")
# else:
#     print("No python is not present.")


# problem 7 = write a program to find out the line number where python is present from problem 6.


# with open("log.txt") as f:
#     lines = f.readlines()

# lineno = 1
# for line in lines:
#     if("python" in line):
#         print(f"Yes python is present. Line no: {lineno}")
#         break
#     lineno += 1

# else:
#     print("No python is not present")


#problem 8 = write a program to make a copy of text file "this.txt"

# with open("this.txt") as f:
#     content = f.read()

# with open("this_copy.txt", "w") as f:
#     f.write(content)


# problem 9 = write a program to find out whether a file is identical & matches the content of another file.             

# with open("this.txt") as f:
#     content1 = f.read()

# with open("this_copy.txt") as f:
#     content2 = f.read()

# if(content1 == content2):
#     print("Yes these files are identical")
# else:
#     print("No these files are not identical")


# problem 10 = write a program to wipe out the content of a file using python.

# with open("wipe_out.txt", "w") as f:
#     f.write("")  # leaving the str emtpty will wipe the while stuff out.




# problem 11 = write a python program to rename a file to "renamed_by_python.txt"

# with open("old.txt") as f:
#     content = f.read()

# with open("renamed_by_python.txt", "w") as f:
#     f.write(content)