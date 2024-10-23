# Wordle Game

This project is a React application that replicates the famous word-guessing game, **Wordle**, originally popularized by The New York Times. The game challenges players to guess a word, offering feedback on each guess. Unlike the original game, te user can choose the number of characters in the word.

## Features
- Simple and intuitive interface for word guessing.
- Feedback is provided for each guess: correct letters, correct positions, and incorrect letters.
- Tracks the number of attempts and ends the game after n + 1 wrong guesses or a correct guess.(n is the number of letters in a word chosen by the user.)
- Responsive design for mobile and desktop play.

## Requirements
- Node.js
- npm (Node package manager)

## Setup

1. Download the zip file of the project.
2. Unzip the file and navigate into the `client` directory.
3. Install the necessary libraries by running `npm install`.
4. Start the application in development mode with:

_The app should now be running at http://localhost:3000._

## How to Play Wordle
The game begins by selecting the number of letters in the word you need. The player has n + 1 chances to guess this word.
After each guess:

- Letters that are in the correct position will be highlighted in green.
- Letters that are in the word but in the wrong position will be highlighted in yellow.
- Letters that are not in the word at all will remain grey.

The goal is to guess the word in as few attempts as possible. If the word is guessed correctly or all attempts are used up, the game will end. 

Enjoy the challenge and sharpen your vocabulary skills!

