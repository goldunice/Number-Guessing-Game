https://roadmap.sh/projects/number-guessing-game
# Number Guessing Game

A simple command-line-based number guessing game built with Python. In this game, the computer randomly selects a number, and the user must guess it within a limited number of attempts. The game includes difficulty levels, a timer, and a high score feature to make it more engaging.

## Features

1. Random Number Selection: The computer randomly selects a number between 1 and 100.
2. Difficulty Levels: 
   - Easy: 10 attempts
   - Medium: 5 attempts
   - Hard: 3 attempts
3. Hints: After each guess, the game will indicate whether the correct number is higher or lower than the user's guess.
4. Timer: Tracks the time taken by the user to guess the number.
5. High Score: Tracks and displays the fewest number of attempts it took to guess the number on each difficulty level.
6. Multiple Rounds: Allows the user to play multiple rounds without restarting the game.

## How to Play

1. Run the game, and you will be greeted with a welcome message and the game rules.
2. Choose a difficulty level:
   - Easy (10 attempts)
   - Medium (5 attempts)
   - Hard (3 attempts)
3. Start guessing the number by entering your guess.
4. After each guess, the game will tell you if the correct number is higher or lower.
5. If you guess correctly within the allowed attempts, you win the round! The game will display a congratulatory message, the number of attempts, and the time taken.
6. If you run out of attempts, the game ends, and you’ll have an option to play again.
7. At the end of each round, your high score will be displayed for the selected difficulty level.

## Example Output

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select a difficulty level:
1. Easy (10 attempts)
2. Medium (5 attempts)
3. Hard (3 attempts)

Enter your choice: 2

Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Enter your guess: 35
Incorrect! The number is less than 35.

Enter your guess: 30
Congratulations! You guessed the correct number in 4 attempts and took 12 seconds.
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/number-guessing-game.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd number-guessing-game
   ```

3. Run the game:
   ```bash
   python number_guessing_game.py
   ```

## Requirements

- Python 3.x

## Future Enhancements

- Leaderboard: Track high scores across multiple players.
- Graphical User Interface: Upgrade to a GUI version using `tkinter` or another framework.
- Custom Range: Allow the user to specify the range for guessing.
