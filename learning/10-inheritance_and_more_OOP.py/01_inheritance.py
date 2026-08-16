# Inheritance (how does it exactly works)
'''Inheritance is a way of creating a new class from an existing class.'''
# TYPES OF INHERITANCE
# Single inheritance
# Multiple inheritance
# Multilevel inheritance

# this is a type of single inheritance.
# based -> drived 


class Employee:
    company = 'Microsoft'
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
# if i want to have the methods from the class Employee to the class Programmer, I'd simply copy the method and paste in the class Programmer below. thats possible, it wont be best practice if you have about 10s of method, would you still want to copy paste things up, even if you would, that would be very troublesome and the code will be very prone to errors.

# so the best practice is that we use something called:
'''inheritance'''
class Programmer: # here we will put Employee in the parentheses, like this: class Programmer(Employee):
    company = "Microsoft Infotech"
    def show(self): # then we wont be needing this method since its already defined in the Employee class above, we will use it using the inheritance method.
        print(f"The name is {self.name} and the salary is {self.salary}")

    def showLangauge(self):
        print(f"The name is {self.name} and he is good with {self.language} langauge")


a = Employee()
b = Programmer()

print(a.company, b.company)






# this is the neat version of how the code exactly works
# while both the code produces the same output, you will see how effiently the code below actually is.

class Employee:  # this is called the base class or a parent class.
    company = 'Microsoft'
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")


'''inheritance'''

class Programmer(Employee): # and this is known as the inherited class.
    company = "Microsoft Infotech"
def showLangauge(self):
        print(f"The name is {self.company} and he is good with {self.language} langauge")


a = Employee()
b = Programmer()

print(a.company, b.company)