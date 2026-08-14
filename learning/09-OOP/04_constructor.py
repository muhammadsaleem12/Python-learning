# INIT () CONSTRUCTOR
'''
__init__() is a special method which is first run as soon as the object is created.
__init__() method is also known as constructor
it takes self-argument and can also take further arguments.
'''
# __init__ # donder method those method that starts with underscores


class Employee:
    language = "python" # this is a class attribute
    salary = 50000

    # and here ill have to define the attributes as well
    def __init__(self, name, salary, language): # dunder method which is automatically called. its called with the help of the {kevin = Employee()}. it will be called everytime you call something like that. 
        # here ill have to pass those instance attributes.
        self.name = name 
        self.salary = salary
        self.language = language 
        print("I am creating an object")


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")
# what if i want to create an instance attribute. i would write my arguments inside the Employee()
kevin = Employee("Kevin", 70000, "JavaScript") # and this i would have to make changes above as well. to run what i pass here in the arguments here
kevin.name = "Kevin"
print(kevin.name, kevin.salary, kevin.language)


# before the changes the result was supposed to look like:
'''
I am creating and object
Kevin 50000 python'''

# and now its different as you can see by running
'''I am creating an object
Kevin 70000 JavaScript'''






# here is the same code without the comments to better understand the structure.

class Employee:
    language = "python" 
    salary = 50000

    
    def __init__(self, name, salary, language): 
        self.name = name 
        self.salary = salary
        self.language = language 
        print("I am creating an object")


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

kevin = Employee("Kevin", 70000, "JavaScript") 
kevin.name = "Kevin"
print(kevin.name, kevin.salary, kevin.language)