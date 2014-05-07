import math
digit = raw_input('What digit to go to?')
digit = int(digit)
if digit < 40:
    print(float(round(math.pi, digit)))
else:
    print("Sorry, digit is too large")
