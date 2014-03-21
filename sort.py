#!/usr/bin/env python
#-*-coding:utf-8-*-
l=range(0,888)

def qsort(lst):
    if not lst:
        return []
    return qsort([x for x in lst[1:] if x > lst[0]])+lst[0:1]+qsort([x for x in lst[1:] if x < lst[0]])

def main(l):
    l=qsort(l)
    l.reverse()
    l1,l2=[],[]
    l1.append(l.pop())
    l2.append(l.pop())
    sum_l1 = sum(l1)
    sum_l2 = sum(l2)
    while l:
        value = l.pop()
        if sum_l1>sum_l2:
            l2.append(value)
            sum_l2+=value
        else:
            l1.append(value)
            sum_l1+=value
    print l1
    print l2
    print sum(l1)-sum(l2)

if __name__=="__main__":
    main(l)