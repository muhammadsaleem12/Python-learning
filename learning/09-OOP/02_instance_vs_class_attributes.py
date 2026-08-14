# for example

class Employee: 
    language = "Python" # this a class attribute
    salary = 50000 

kevin = Employee() 
kevin.language = "JavaScript" # this is an instance attribute # if I comment out this instance attribute obv the result will have python written in it.
print(kevin.language, kevin.salary)

# now you might ask that we have already assigned a class language above, why assign it again as an instance, (I'd say thats Arbitrary haha!)
# so what do you think the result will be, is it gonna be python or javascript.

#ofcourse it will be JavaScript, becuase of the "note" below

# note: Instance attributes take preference over class attributes during assignment & retrieval