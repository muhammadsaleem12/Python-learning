

myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

# above can be simplified using list comprehension

squaredList = [i*i for i in myList]

print(squaredList)

#  output will be the same 