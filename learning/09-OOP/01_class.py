# Lesson 09 - OOP

# what is OOP (Objected Oriented Programming)

# solving a problem by creating object is one of the most popular approaches in programming. This is called Object-Oriented-Programming.

# The concept focuses on using reusable code (DRY (DON'T REPEAT YOUSELF) principle.)

'''01 WHAT IS A CLASS'''
# Class is a blueprint to creating object.
# for instance : there is a form to be filled and empty form, someone filled it, I did, so the form will be called mine, like its my form, if leo has filled the form, it will be called leo's form, and when it was empty, it wasn't anyones. 
# HENCE the empty form is know as a CLASS in OOP and the filled one is called the OBJECT.




# basic class example:
class Employee: 
    name = "Kevin" # this is an object/instance attribute.
    language = "Python" # this is a class attribute.
    salary = 50000 # this is also a class attribute.

kevin = Employee() # kevin here is an object.
print(kevin.name, kevin.language, kevin.salary)

# this is a very basic way to make classes and objects.

# lets get things a little further. 


'''02 OBJECT''' 
# there is s perticular information in an OBJECT, 
# an OBJECT is an instantiation of a class. when class is defined, a template (info) is defined. memory is allocated only after object instantiation.

# OBJECT of a given class can invoke the methods available to it without revealing the implementation detailed to the user, - Abstraction & Encapsulation

'''MODELING A PROBLEM IN OOPS'''
# we identify the following in our problem
    # Noun -> Class -> Employee
    # Adjective -> Attributes -> name, age , salary.
    # Verbs -> Methods -> getSalary(), increment().

'''CLASS ATTRIBUTES'''
# An attribute that belongs to the class rather than a perticular object.
# Example:
class Employee: 
    language = "Python" 
    salary = 50000 
    # lanugage and salary are both class attribute (becuase this directly belongs to the class called Employee:)

kevin = Employee() 
print(kevin.language, kevin.salary)

ben = Employee()
print(ben.language, ben.salary)
    # the objects like above (kevin, ben) when they fill up the class, (Employee) will get the values from the class, such as salary and language.


'''WHAT if you wanna print their names along'''

class Employee: 
    language = "Python" 
    salary = 50000 

kevin = Employee() 
kevin.name = "Kevin"
print(kevin.name, kevin.language, kevin.salary)

ben = Employee()
ben.name = "Ben"
print(ben.name, ben.language, ben.salary)

# to sum things up:  Here the name is object attribute also known as (instance attributes) and salary and language are class attributes as they directly belong to the class.








