# lesson 4 - dictionaries & sets
# practicing key-value pairs and unique collections

# 1. DICTIONARIES (Key-Value pairs, mutable, indexed by keys)

marks = {
    "Saleem": 100,
    "Waseem": 56,
    "Ali": 23,
    0: "Zero"
}

# accessing values
print(marks["Ali"])         # returns 23

# dictionary methods
print(marks.items())        # returns dict_items([('Saleem', 100), ...])
print(marks.keys())         # returns dict_keys(['Saleem', 'Waseem', 'Ali', 0])
print(marks.values())       # returns dict_values([100, 56, 23, 'Zero'])

# updating dictionary
marks.update({"Saleem": 99, "Zuko": 90})
print(marks)

# .get() vs direct lookup []
print(marks.get("Saleem"))  # prints value or None if key is missing (no error)
print(marks["Saleem"])      # prints value, but throws KeyError if key is missing


# 2. SETS (Unordered, unindexed, unique values only)

# empty set declaration
e = set()                   # use set(), because {} creates an empty dict!
print(type(e))              # <class 'set'>

# sets auto-remove duplicates
s = {1, 5, 32, 54, 5, 5, 5, "Harry"}
print(s, type(s))

# adding elements
s.add(5566)
print(s)


# 3. SET OPERATIONS (Union, Intersection, Subset)

s1 = {1, 45, 6, 8, 9}
s2 = {7, 8, 9, 1}

print("Union:", s1.union(s2))            # combines unique items from both
print("Intersection:", s1.intersection(s2)) # items common to both
print("Difference:", s1.difference(s2))    # items in s1 but not in s2
print("Is subset:", s1.issubset(s2))       # False

# subset & superset checks
a = {1, 2, 3}
b = {1, 2}

print(b.issubset(a))        # True (all items of b are in a)
print(a.issuperset(b))      # True (a contains all items of b)