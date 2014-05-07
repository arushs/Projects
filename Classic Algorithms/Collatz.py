n = int(raw_input("Number to find steps to reach 1? "))

steps = 0
while n != 1:
    if n % 2 == 0:
        steps+=1
        n = n / 2
    else:
        steps+=1
        n = n * 3 + 1
print steps
