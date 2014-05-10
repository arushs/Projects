import math
def factorial(n):
    if n < 0:
        print "error, number is below, 0"
    elif(n < 2):
        return 1
    else :
        return factorial(n-1) * n
n = input("Number to find factorial? ")
num = n
sum = 1;
print factorial(num)
if n < 0:
    print "error, number is below, 0"
else:
    while n > 0:
        sum = sum*n
        n-=1
    print sum
