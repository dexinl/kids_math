#!/usr/bin/python

import random

count = 20

test_set = []
while count:
    a = random.randrange(3,20)
    b = random.randrange(3,20)
    if a > b and a - b > 1:
        if (b, a-b) not in test_set:
            test_set.append((b, a-b))
            count -= 1
    elif b > a and b - a > 1:
        if (a, b-a) not in test_set:
            test_set.append((a, b-a))
            count -= 1
    else:
        continue


for (a,b) in test_set:
    print "  %2d  + %2d  = " % (a,b)
