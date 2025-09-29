import random

def play_round(low=1, high=100):
    secret = random.randint(low, high)
    attempts = 0
    print(f"\nI'm thinking of a number between {low} and {high}.")
    print("Type 'q' to quit this round.")

    while True:
        guess = input("Your guess: ").strip().lower()
        if guess == 'q':
            print(f"You quit! The number was {secret}.")
            return None  # round ended early

        # Validate input
        if not guess.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess)
        if guess < low or guess > high:
            print(f"Stay within {low}-{high}.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low! 📉")
        elif guess > secret:
            print("Too high! 📈")
        else:
            print(f"🎉 Correct! The number was {secret}. You took {attempts} attempts.")
            return attempts

def main():
    print("=== Number Guess Game ===")
    while True:
        result = play_round()
        # Ask to play again unless user quit mid-round
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
