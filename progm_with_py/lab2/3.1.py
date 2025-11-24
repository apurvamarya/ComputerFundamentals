import random
# Genrate random number
secret_number = random.randint(1, 100)
attempts = 0
max_attempt = 7

print("Welcome to the Number Guessing Game")
print(f"I'm pf a number between 1 nad 100.")
print(f"You have {max_attempt} to guess it.")

while attempts < max_attempt:
    try:
        guess = int(input(f"\nAttempts {attempts + 1}: Enter your guess:"))
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations You guess it in {attempts} attempts")
            break
        elif guess < secret_number:
            print("Too low Try a higher number.")
        else:
            print("Too high Try a lower number.")
        
        remaining = max_attempt - attempts
        if remaining > 0:
            print(f"You have {remaining} attempts left.")
    except ValueError:
        print("Please enter a valid number")
        attempts -= 1 # Dont count invalid input as an attempt
if attempts >= max_attempt and guess != secret_number:
    print(f"\nGame over The number was {secret_number}")