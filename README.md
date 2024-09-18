# Connect Four Game with Minimax Algorithm

This is a Python implementation of the classic **Connect Four** game, enhanced with an AI opponent that uses the **Minimax algorithm** for decision-making.

## Table of Contents

- [About the Game](#about-the-game)
- [How the Minimax Algorithm Works](#how-the-minimax-algorithm-works)
- [Future Improvements](#future-improvements)
- [Photos](#photos)

## About the Game

Connect Four is a two-player connection game in which the players take turns dropping colored discs from the top into a vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four discs.

In this project, one player can compete against an AI opponent that uses the **Minimax algorithm** to play optimally, or you can play with another player.

## How the Minimax Algorithm Works

The Minimax algorithm is a recursive method used in decision-making and game theory. It simulates all possible moves in a game, considering both the player's and opponent's options, to determine the optimal move.

In the Connect Four game:

The AI evaluates all possible moves for both the AI and the human player.
Each move is given a score based on how favorable it is for the AI.
The algorithm selects the move that minimizes the possible loss (hence, minimax).


## Future Improvements

- Add a GUI for better user experience.
- Optimize the Minimax algorithm using Alpha-Beta pruning.

## Photos

- You can choose your gamemode:
- ![image](https://github.com/user-attachments/assets/6cfad1d1-d813-4350-86c9-047c5784823d)


- We can see the board after every move:
- ![image](https://github.com/user-attachments/assets/70a31f6c-835e-466c-bf65-1e21f4bbc301)

- It's very hard to beat the computer, but sometimes it's possible:
- ![image](https://github.com/user-attachments/assets/246cf12f-9a87-46ab-8e7c-c28d4bb1e284)

