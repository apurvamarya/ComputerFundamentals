# Count from 5

count = 5
while count >0:
    print(f"Countdown: {count}")
    count = count - 1
print("Blast off")

# Keep asking until valid input

while True:
    password = input("Enter password: ")
    if len(password) >= 8:
        print("Password accepted")
        break
    else:
        print("Password too short. Must be atlest 8 characters.")
