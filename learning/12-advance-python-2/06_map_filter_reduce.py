'''MAP, FILTER & REDUCE'''
from functools import reduce


'''MAP EXAMPLE'''
# Map applies a function to all the items in an input_list.


l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList)) # to print we must convert it into list.


'''FILTER EXAMPLE'''
# basically filters

def even(n):
    if (n%2 == 0):
        return True
    return False

only_even = filter(even, l)
print(list(only_even))


'''REDUCE EXAMPLE'''

def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print(reduce(sum, l)) # to use reduce we gotta import reduce form functools
print(reduce(mul, l)) 

# the sum here works using with "Sequential Computation" that means form the list of [1, 2, 3, 4, 5]  
# it calculates two numbers at one time like: 1+2 =3 -> 3+3 => 6+4 => 10+5 = 15.  
# same goes if you do multiplication like above, substraction, and division.
# this is called sequential computation. 