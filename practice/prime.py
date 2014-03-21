#!/usr/bin/env python
#-*-coding:utf-8-*-

def is_prime(number):
    for i in range(2,number-1):
        if number%i == 0:
            return False
        else:
            pass
    return True
l=[]
for n in range(2,100):
    if is_prime(n):
        l.append(n)
print l
        


