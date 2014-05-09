num = int(raw_input("amount of times to flip? "))
from random import randint
while num != 0:
    if randint(0,1) == 1:
        print "heads"
    else:
        print "tails"
    num-=1
