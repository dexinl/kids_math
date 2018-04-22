#!/usr/bin/python

import random

count = 20

test_set = []
sign_set = []
while count:
    a = random.randrange(3,100)
    b = random.randrange(3,100)
    c = random.randrange(0,2)
    if 1:
        if a > b and a - b > 1:
            if (b, a-b) not in test_set:
                test_set.append((b, a-b))
                sign_set.append(c)
                count -= 1
        elif b > a and b - a > 1:
            if (a, b-a) not in test_set:
                test_set.append((a, b-a))
                sign_set.append(c)
                count -= 1
    else:
        pass


i=0
for (a,b) in test_set:
    c = sign_set[i]
    i += 1
    if c:
        print "  %2d  + %2d  = " % (a,b)
    else:
        if a > b:
            print "  %2d  - %2d  = " % (a,b)
        else:
            print "  %2d  - %2d  = " % (b,a)

