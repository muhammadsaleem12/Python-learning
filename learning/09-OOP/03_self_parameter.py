# for example 
# if you wanna define a function inside the class


# class Employee: 
#     language = "Python" # this a class attribute
#     salary = 50000 

#     # I want to make a function called getInfo() here, No matter what methods we create we must give a "self" whether we use it or not.

#     def getInfo(): # here we can accpet it with any name, but its usually done with "self" as an argument, that means the object that this method is runnign on. # 

#         print(f"The language is {language}. The salary is {salary}") # here well edit {self.language} and {self.salary}, taking the objects language and salary.
    


# kevin = Employee() 
# kevin.language = "JavaScript" # this is an instance attribute 
# print(kevin.language, kevin.salary)

# # now if you run the above function it will show an error that looks like this: 
# # TypeError: Employee.getInfo() takes 0 positional arguments but 1 was given


# kevin.getInfo() # but here we haven't given any arguemnet. # this call gets converted into:
# '''Employee.getInfo(kevin)''' # something like this. if you looks at it, you can might realize that we have indeed given an argument.




'''you might wanna comment out the above code in order to run the function below, after the changes made defined above.'''






# here is the fully functional modified version after the changes made. 


class Employee: 
    language = "Python" # this a class attribute
    salary = 50000 

    # I want to make a function called getInfo() here
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod # by using this @staticmethod we tell the program that this function doesn't work with objects and does not need any.
    # this way we wont have to put "self" or any other name to just to avoid the positional argument error.
    def greet():
        print("Good Morning")


kevin = Employee() 
kevin.language = "JavaScript" # this is an instance attribute 
# print(kevin.language, kevin.salary)


# both of the ways to define a fucntions works the same. 
kevin.getInfo() 
Employee.getInfo(kevin)
# here is an other function to test out.
kevin.greet()

