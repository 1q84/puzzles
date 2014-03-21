#!/usr/bin/env python
#-*-coding:utf-8-*-

def outer(n):
    def inner(m):
        return n+m
    return inner

print outer(1)(2)