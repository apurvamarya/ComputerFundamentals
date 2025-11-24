def factorial():
    try:
        n = int(input("Enter a Number "))
        if (n == 0 or n == 1):
            print("Factorial of number is 1")
        elif (n<0):
            print("Invalid Input")
        else:
            fact = 1
            for i in range(1, n+1):
                fact *= i
            print(fact)
    except:
        print("Invalid Input")

factorial()