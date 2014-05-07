# The user enters a cost and then the amount of money given.
# The program will figure out the change and
# the number of quarters, dimes, nickels, pennies needed for the change.

cost = float(raw_input("cost? "))
money = float(raw_input("money? "))
remainder = 100* money - 100*cost
quarters = 0
dimes = 0
nickels = 0
pennies = 0
# remainder = remainder * 100
while remainder != 0:
    if remainder - 25 >= 0:
        remainder = remainder - 25
        quarters+= 1
    elif remainder - 10 >= 0:
        remainder = remainder - 10
        dimes+= 1
    elif remainder - 5 >= 0:
        remainder = remainder - 5
        nickels+= 1
    else:
        remainder = remainder - 1
        pennies+= 1
print("quarters = ")
print(quarters)
print("dimes = ")
print(dimes)
print("nickels = ")
print(nickels)
print("pennies = ")
print(pennies)
