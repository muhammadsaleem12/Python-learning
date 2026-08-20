'''TYPES DEFINITION IN PYTHON'''

n : int = 5 # telling python the value is int n. will bring up all the int functions for this. 

name : str = "Kevin" # here i did the same with string.

def sum(a: int, b: int) -> int: # doing the same as a function, define all as an int, a, b and the result. 
    return a + b

sum(4, 5) # here it will suggest the types its supposed to be.

# this function has been added recently. 
# this is a very best practice, whether you're using someone's code, or someone's running your's.


'''ADVANCED TYPE HINTS'''
# Python's typing module provides more advanced type hints, such as List, tuple, Dict, and Union. 
# you can import Lits, Tuple and Dict types from the typing module like this:

from typing import List, Tuple, Dict, Union

# The syntax of types looks something like this;

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with strings keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid

# These annotations help in making the code self-documenting and allow developers to understand the data structures used at a glance.