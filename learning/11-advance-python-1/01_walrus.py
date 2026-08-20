'''NEWLY ADDED FEATURES IN PYTHON'''
# following are some of the newly added faetures in python programming language

'''WALRUS OPERATOR'''
# The walrus operator(:=) introduced in Python 3.8, allows you to assign values to variables as part of an expression. This operator, named for its resemblance to the eyes of tusks of walrus, is officially called the "assignment expressioin".

# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3: # does 2 things at the same time, very convenient
    print(f"List is too long ({n} elements, expected <= 3)") # OUTPUT: List is too long (5 elements, expected <= 3)