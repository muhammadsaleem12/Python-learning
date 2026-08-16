'''Operator Overloading'''

# Operators in python can be overloaded using dunder methods.
# These methods are called when a given operator is used on the objects.
# Operators in Python can be overloaded using the following methods:

'''
p1+p2 # p1.__add__(p2)
p1-p2 # p1.__sub__(p2)
p1*p2 # p1.__mul__(p2)
p1/p2 # p1.__truediv__(p2)
p1//p2 # p1.__floordiv__(p2)
'''
# Other dunder/magic methods in python:
# __str__() # used to set what gets displayed upon calling str(obj)
# __len__() # used to set what gets displayed upon calling.__len() or len(obj)


# for instance

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num): # here we are providing Python with a precise recipe or set of instructions on how to combine two objects of your custom class. without this python i basicaly blind to the operators.
        return self.n + num.n 

n = Number(1)
m = Number(2)

print(n + m)


