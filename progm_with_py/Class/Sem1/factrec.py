def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1) 

num = int(input("Enter a Number "))
print(factorial(num))

''' fact(9)
    9 * fact(8)
    8 * fact(7)
    7 * fact(6)
    6 * fact(5)
    5 * fact(4)
    4 * fact(3)
    3 * fact(2)
    2 * fact(1)
    fact(1) = 1
    1*2
    2*3
    ...'''
