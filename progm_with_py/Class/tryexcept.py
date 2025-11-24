def divide (x, y):
    try:
        result = x/y
        print("Result of division : ", result)
    except:
        print("Error: Division br zero")
    
# Test the function

divide(10, 2)
divide(5, 0)
