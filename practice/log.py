#!/usr/bin/env python
#-*-coding:utf-8-*-

def log(func):
    def wrapper(*args, **kw):
        print 'enter', func.__name__
        func(*args, **kw)
        print 'exit', func.__name__
    return wrapper

@log
def test(a, b):
    print a,b

test(1,2)