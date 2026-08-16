'''Multiple Inheritance'''
# Multiple inheritance occurs when the child class inherits from more than one parent classes.

# parent1   parent2
#   |____ ____|
#        |
#      Child

class Employee:  # parent1 class
    company = 'Microsoft'
    name = 'Micheal'
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")



class Coder: # parent2 class
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")




class Programmer(Employee, Coder): # inherited class
    company = "Microsoft Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} langauge")


b = Programmer()


b.show()
b.printLanguage()
b.showLanguage()


# as you can see how multiple inheritance works, we created 2 parent classes and inherited the properties to the Child (class Programmer).