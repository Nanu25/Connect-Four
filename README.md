# Connect Four Game with Minimax Algorithm

This is a Python implementation of the classic **Connect Four** game, featuring an AI opponent powered by the **Minimax algorithm**. The AI plays optimally, providing a challenging experience for human players.

## Table of Contents

- [About the Game](#about-the-game)
- [How the Minimax Algorithm Works](#how-the-minimax-algorithm-works)
- [Features](#features)
- [Future Improvements](#future-improvements)
- [Screenshots](#screenshots)

## About the Game

**Connect Four** is a two-player connection game where players take turns dropping colored discs into a vertically suspended grid. The objective is to be the first to form a horizontal, vertical, or diagonal line of four discs. The game ends when one player wins or when the grid is filled without a winner, resulting in a draw.

In this implementation, you can play **Human vs Human** or **Human vs AI**. The AI opponent uses the **Minimax algorithm** to evaluate and choose optimal moves. The game provides a visual representation of the board and updates after every move, allowing you to easily track progress.

## How the Minimax Algorithm Works

The **Minimax algorithm** is a decision-making algorithm commonly used in two-player games. It works by simulating all possible moves and choosing the one that maximizes the player's chances of winning while minimizing the opponent's chances.

Here’s how the Minimax algorithm works in Connect Four:

1. The AI evaluates all possible moves for both the AI and the human player.
2. For each move, a **score** is assigned based on how favorable the move is for the AI. Winning moves have higher scores, while moves leading to a loss have lower scores.
3. The algorithm recursively simulates all potential future moves, considering the opponent's counter-moves.
4. The AI chooses the move with the best score, ensuring that it plays optimally.
5. The algorithm operates by assuming both players are playing optimally, aiming to minimize the AI’s potential loss.

## Features

- **Human vs Computer**: Play against an AI opponent that uses the Minimax algorithm to make optimal decisions.
- **Human vs Human**: Challenge a friend in the classic two-player mode.
- **AI Difficulty**: Choose from multiple difficulty levels (Easy, Medium, Hard, Extreme Hard).
- **Real-Time Gameplay**: See the game board update after every move.
- **Responsive UI**: The game supports a simple yet interactive interface using **Pygame** for displaying the board and moves.

## Future Improvements

- **Alpha-Beta Pruning**: Optimize the Minimax algorithm to make it more efficient by reducing the number of nodes evaluated.
- **Graphical Enhancements**: Improve the visual experience with animations and better UI components.

## Screenshots

### 1. Choose Your Game Mode
Select between playing against the AI or another human player.
![Game Mode](https://github.com/Nanu25/Connect-Four/blob/main/GameMode)

### 2. Player Setup
Enter your player names to start the game.

![Player Setup](https://github.com/Nanu25/Connect-Four/blob/main/PlayerSetup)
### 3. The Game in Action
Here is an example of the board after a few moves.
![Game Run](https://github.com/Nanu25/Connect-Four/blob/main/gamerun.png)

### 4. The AI Plays Well, But You Can Win
The AI is tough to beat, but it's not impossible to win. Here's an example of the human player winning.
![Win](https://github.com/Nanu25/Connect-Four/blob/main/Win)
