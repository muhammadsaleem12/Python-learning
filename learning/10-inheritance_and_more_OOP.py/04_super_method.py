'''Super Method'''
# Super method is used to access the methods of a super class (parent) in derived class.

# what if i wanna run Manager class and along with that i wanna run its parent class what would i do, i would use the super() method



class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__() # here is the super method is used, along with the property that i wanna class which is init Construtor in this case
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__() # here as well
        print("Constructor of Manager")
    c = 3



'''even if the Employee and Programmer calls are commented out, and just Manager is running, we'll still be able to see their results.'''

# o = Employee()
# print(o.a) 
# o = Programmer() 
# print(o.a, o.b) 
o = Manager() 
print(o.a, o.b, o.c) 

# Output before 

# Constructor of Employee
# 1
# Constructor of Programmer
# 1 2
# Constructor of Manager
# 1 2 3

# Output after running the super method 

# Constructor of Employee
# Constructor of Programmer
# Constructor of Manager
# 1 2 3
