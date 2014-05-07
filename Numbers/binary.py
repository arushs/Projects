import math
def toBinary(n):
    if n / 2 == 0:
        return n % 2
    else :
        return 10 * toBinary(n / 2) + toBinary(n % 2)
def toDec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return 2 * toDec(n/10) + toDec(n%10)

num = int(raw_input("Num to convert to binary? "))
print(toBinary(num))
coo = int(raw_input("Num to convert to Decimal? "))
print(toDec(coo))
