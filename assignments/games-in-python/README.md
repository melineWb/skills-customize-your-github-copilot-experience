
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic Hangman word-guessing game using Python strings, loops, conditionals, and user input to practice string manipulation and game logic.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create a function that randomly selects a word from a predefined list and initializes the game state for the player.

#### Requirements
Completed program should:

- Define a list of words to choose from for the game
- Randomly select a word from the list at the start of each game
- Initialize tracking variables for guessed letters and attempts remaining
- Display the initial game state with underscores for each letter in the word

### 🛠️ Letter Guessing and Progress Tracking

#### Description
Implement the core gameplay loop where players guess letters and see their progress revealed.

#### Requirements
Completed program should:

- Accept letter guesses from the user via input
- Check if the guessed letter is in the word
- Update and display the current progress (e.g., `h_ll_`for word "hello" after guessing 'h', 'l')
- Track incorrect guesses and decrement the remaining attempts
- Prevent the player from guessing the same letter twice

### 🛠️ Game End Conditions and Messages

#### Description
Add logic to end the game when the player wins or loses, and display appropriate messages.

#### Requirements
Completed program should:

- End the game when the player guesses the complete word (win condition)
- End the game when attempts reach zero (lose condition)
- Display a win message showing the word and number of attempts remaining
- Display a lose message revealing the correct word
- Offer the player the option to play again
