def Fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

number = int(raw_input())
print(Fibonacci(number))
