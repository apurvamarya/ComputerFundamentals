# Using break to exit early

for i in range(1, 11):
    if i == 7:
        break #Exit the loop when i = 7
    print(i)
    
# Using continue to skip itterations

for i in range(1, 11):
    if i%2 == 0: #if even number
        continue #Skip to next itteration
    print(f"Odd numbers: {i}")