'''WHAT IS A CLASS METHOD'''
# A class method is a method which is bound to the class and not the object of the class.

# @classmethod decorator is used to create a class method.


# in the code below as we all know that because of this instance attribute that has preference over class attribute, so the output will be 45 ofcourse.

# but what if we want to have the result of the class attribute and not the instance attribute.

class Employee:
    a = 1

    @classmethod # for that we will use @classmethod, just like @staticmethod, this method will prevent the preference over the class method and will show the result of the class that we have set above.
    def show(cls): # self -> cls # @classmehtod will use "cls" that means the method that we have been working up.
        print(f"The class attribute of a is {cls.a}") # self.a -> cls.a




e = Employee()
e.a = 45 # instance attribute

e.show()