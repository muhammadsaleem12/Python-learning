'''Multilevel Inheritance'''
# When a child class becomes a parent for another child class.
#       Parent
#         |
#       Child1 -> parent2 for Child2
#         |
#       Child2

class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3


o = Employee()
print(o.a) # Prints the a attribute we can print o.b and o.c but that will show error as they are not presnet in Employee # output 1
o = Programmer() 
print(o.a, o.b) # Prints both a and b attribute since there is exist both Employee and Programmer properties but now the Manager's # output 1 2 
o = Manager() 
print(o.a, o.b, o.c) # prints all the three properties since all of the above exists in the Manager class. # output 1 2 3



