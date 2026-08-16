'''Problem 01 =  Create a class (2-D Vector) and use it to create another class representing a 3-D vector'''
print("Problem_01:")

class twoDVector:
    def __init__(self, i , j):
        self.i = i    
        self.j = j    


    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class threeDVector(twoDVector):
    def __init__(self, i , j, k):
        super().__init__(i, j)
        self.k = k    


    def show(self):
            print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = twoDVector(1, 2)
a.show()
b = threeDVector(1, 2, 3)
b.show()


'''Problem 02 = Create a class "Pets" from a class "Animals" and further create a class "Dog" from "Pets" .Add a method "bark" to class "Dog". '''
print("Problem_02:")


class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow!")


d = Dog()

d.bark()


'''Problem 03 = Create a class "Employee" and add salary and increament properties to it.
Write  a method "salaryAfterIncrement" method with a @property decorator with a setter 
which changes the value of increment based on the salary'''
print("Problem_03:")


class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)* 100



e = Employee()
print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 280.8
print(e.increment)



'''problem 04 = Write a class "Complex" to represent complex numbers, along with overloaded operators "+" and "*" which adds and multiples them.'''
print("Problem_04:")

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)

    def __str__(self):  # without using this __str__() method, the output was <__main__.Complex object at 0x0000028860388910>.
        return f"{self.r} + {self.i}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1 * c2)


'''Problem 05 = Write a class vector representing a vector of n dimensions. 
Overload the + and * operator which calculates the sum and the dot(.) product of them'''
print("Problem_05:")
        
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9) # same dimension vector

print(v1 + v2) 
print(v1 * v2)

print(v1 + v3) 
print(v1 * v3) 


'''problem 06 = Write __str__() method to print the vector as follows:
            7i + 8j + 10k
Assume vector of dimension 3 for this problem.'''
print("problem_06:")

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)" # literally just added i, j, k in the str method of the problem 5

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9) # same dimension vector

print(v1 + v2) 
print(v1 * v2)

print(v1 + v3) 
print(v1 * v3) 


'''problem 07 = Override the __len__() method on vector of problem 5 to display the dimension of the vector. '''
print("Problem_07:")

# from problme 05
 
class Vector:
    def __init__(self, l): # taking list
        self.l = l


    def __len__(self):
        return len(self.l)

# Test the implementation
v1 = Vector([1, 2, 3]) # if vectors length was variable, id pass a list like this.
print(len(v1)) # python doesn't whats the len of a vector, its blind again. so we gotta define some above.

# output should be 3
