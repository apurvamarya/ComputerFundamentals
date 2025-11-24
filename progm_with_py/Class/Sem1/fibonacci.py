def fibonacci(n):
  a, b = 0, 1
  result = []
  for _ in range(n):
    result.append(a)
    # print("A = ",a,"B = ",b)
    a, b = b, a + b
  print(result)
  # return result
fibonacci(5)
# Only shows the value at that term
# def fibo(n):
#   if (n == 0):
#     print("Invalid Input")
#   elif (n == 1):
#     return 0
#   elif (n==2):
#     return 1
#   elif (n <= 1):
#     return 1
#   else:
#     return fibo(n-1) + fibo(n-2)

# n = int(input("Enter a Number "))
# for i in range(1, n+1):
#   print(fibo(i), end=" ")
#fib = fibonacci(num)
#print(f"Fibonacci sequence up to {num} terms: {fib}")
