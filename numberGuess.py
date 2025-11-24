import random

def play_game():
    print("====================================")
    print("      Welcome to Guess The Number   ")
    print("====================================")
    print("I am thinking of a number between 1 and 100.")
    print("Try to guess it!\n")

    # Computer chooses a random number
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100. Try again.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f" Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempts.\n")
            break

def main():
    while True:
        play_game()
        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thanks for playing! Goodbye")
            break

if __name__ == "__main__":
    main()
