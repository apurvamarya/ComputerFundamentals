def checkEven(number):
    try:    
        if number % 2 == 0:
            print(number, " is an Even number")
        else:
            print(number, " is an Odd number") 
    except ValueError:
        print("Value Error")

def checkGReaterThanFive(n):
    if n>5:
        print("Number is grater than 5")
    else:
        print("Number is not grater than 5")
        
num = int(input("Enter a Number "))
checkEven(num)
checkGReaterThanFive(5)