import random
import time

# Initialize high scores for each difficulty level
high_scores = {"Easy": None, "Medium": None, "Hard": None}


def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Your goal is to guess the number within a limited number of attempts.")

    while True:
        difficulty = select_difficulty()
        max_attempts = get_attempts(difficulty)
        number_to_guess = random.randint(1, 100)

        play_round(difficulty, max_attempts, number_to_guess)

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break


def select_difficulty():
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        return "Easy"
    elif choice == '2':
        return "Medium"
    elif choice == '3':
        return "Hard"
    else:
        print("Invalid choice! Defaulting to Medium difficulty.")
        return "Medium"


def get_attempts(difficulty):
    return {"Easy": 10, "Medium": 5, "Hard": 3}.get(difficulty, 5)


def play_round(difficulty, max_attempts, number_to_guess):
    print(f"\nGreat! You've selected the {difficulty} difficulty level.")
    print(f"You have {max_attempts} chances to guess the correct number.")
    attempts = 0
    start_time = time.time()

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: ").strip())
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        attempts += 1
        if guess == number_to_guess:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            print(f"Time taken: {elapsed_time} seconds.")
            update_high_score(difficulty, attempts)
            return

        elif guess < number_to_guess:
            print("Incorrect! The number is greater than your guess.")
        else:
            print("Incorrect! The number is less than your guess.")

        if attempts == max_attempts:
            print(f"\nYou've run out of chances! The correct number was {number_to_guess}. Better luck next time.")


def update_high_score(difficulty, attempts):
    global high_scores
    current_score = high_scores[difficulty]

    if current_score is None or attempts < current_score:
        high_scores[difficulty] = attempts
        print(f"New high score for {difficulty} difficulty: {attempts} attempts!")
    else:
        print(f"High score for {difficulty} difficulty: {current_score} attempts.")


if __name__ == "__main__":
    start_game()
