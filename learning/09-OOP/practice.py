# lets start the practice set for OOP (Object Oriented Programming)

'''Problem 01 = Create a Class "Programmer" for storing information of few programmers working at Microsoft.'''

class Programmer:
    company = "Microsoft"
    def  __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Kevin", 70000, 245001)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Robin", 50000, 245002)
print(r.name, r.salary, r.pin, r.company)


'''Problem 02 = Write a class "calculator" capable of finding square, cube and square root of a number'''

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is: {self.n * self.n}")

    def cube(self):
        print(f"The cube is: {self.n * self.n * self.n}")

    def square_root(self):
        print(f"The square root is: {self.n**1/2}")

a =  Calculator(4)
a.square()
a.cube()
a.square_root()


'''prblem 03 = Create a class with a class attribute a; create an object from it and set "a" directly using object. a = o. Does this change the class attribute? '''

class Demo:
    a = 4

o = Demo
print(o.a) # here it prints class attribute because instance attribute is not present.
o.a = 0 # here the instance attribute is set.
print(o.a) # then it prints instance attribute becuase instance is present above.
print(Demo.a) # hence the attribute doesn't change.


'''problem 04 = Add a static method in problem 2 , to greet the user with hello.'''

# copied from problem 02

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is: {self.n * self.n}")

    def cube(self):
        print(f"The cube is: {self.n * self.n * self.n}")

    def square_root(self):
        print(f"The square root is: {self.n**1/2}")

    @staticmethod
    def hello(): # dont need to access instance attribute hence we used a static method.
        print("Hello There!")

a =  Calculator(4)
a.hello()  # here it is.
a.square()
a.cube()
a.square_root()


'''problem 05 = Write a class Train which has methods to book a ticket , get status(no of seats) and get fare information of train running under National Railways.'''


from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} form {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} form {fro} to {to} is {randint(222, 5555)}")



t = Train(12399)
t.book("Karachi", "Islamabad")
t.getStatus()
t.getFare("Karachi", "Islamabad")


'''problem 06 = Can you change the self-parameter inside a class to soemthing else (say "kevin"). Try changing self to "slf" or "kevin" and see the effects'''


# here were gonna use the calculator program from problem 2 

class Calculator:
    def __init__(slf, n):
        slf.n = n

    def square(slf):
        print(f"The square is: {slf.n * slf.n}")

    def cube(slf):
        print(f"The cube is: {slf.n * slf.n * slf.n}")

    def square_root(slf):
        print(f"The square root is: {slf.n**1/2}")

a =  Calculator(4)
a.square()
a.cube()
a.square_root()

# as we already know that you can use any name as an argument, as long as you made changes everywhere where self is used.   what we usualy use is "self"  but you literally use any name, like "kevin", but that doesn't sounds good, the best practice is that you use "self"


'''with this our practice set for OOP is over.'''
