'''Problem_05 = Write a program to find the maximun of the numbers in a list using the reduce function.'''
from functools import reduce


l = [1, 2, 334, 53, 625, 654, 645, 342]


def greater(a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, l))