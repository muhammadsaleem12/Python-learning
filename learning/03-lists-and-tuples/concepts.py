# lesson 3 - lists and tuples
# practicing mutable lists and immutable tuples

# 1. LISTS (Mutable - can be modified)

# basic list creation and append method
friends = ["Alice", "Bob", "Charlie", "David"]
print(friends) 

# append adds element to the end
friends.append("Eve")
print(friends) 


# list methods practice
l1 = [1, 4, 6, 4, 7, 3, 7, 3]

# l1.sort()         # sorts the list in ascending order
# l1.reverse()      # reverses the list order
# l1.insert(2, 10)  # inserts 10 at index 2
# l1.pop(2)         # removes the element at index 2 

l1.remove(4)        # removes the first occurrence of 4
print(l1)


# 2. TUPLES (Immutable - cannot be modified)

a = (1, 2, 5, 6, False, "Saleem", "Waseem")

# a[0] = 453        # TypeError: tuples are immutable and cannot be changed!
print(type(a))      # <class 'tuple'>
print(a)


# tuple methods practice
a = (1, 2, 5, 6, 6, False, "Saleem", "Waseem")
print(a)

# count occurrences of an item
no = a.count(6)     # returns 2 (6 appears twice)
print(no)

# find index of first occurrence
i = a.index(6)      # returns 3 (index of first 6)
print(i)