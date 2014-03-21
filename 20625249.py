#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Suppose I have a vector (a_1, a_2, a_3, ... , a_n)

and I want to add a number to each element of my vector using the __add__ in python class.

Such that:

a = vector(7, 4, 2)

print a + 3

will output: (10, 7, 5)
"""
class Vector():

    def __init__(self,*args):
        self.args = args

    def __add__(self, other):
        return tuple(map(lambda x:x+other,self.args))
    
a = Vector(1,2,3)
print a+3
