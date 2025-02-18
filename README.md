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

## Alpha-Beta Pruning Optimization
The **Alpha-Beta pruning** is an optimization technique for the Minimax algorithm that significantly reduces the number of nodes evaluated in the game tree without affecting the final decision. This optimization makes the AI more efficient while maintaining the same level of gameplay intelligence.

Here's how Alpha-Beta pruning enhances the Minimax algorithm in Connect Four:

1. The algorithm maintains two values, **alpha** and **beta**, which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of, respectively.

2. During the tree search:
   - Alpha starts at negative infinity and increases as better moves are found
   - Beta starts at positive infinity and decreases as better opponent moves are found
   - When alpha becomes greater than or equal to beta, remaining branches can be "pruned" (skipped)

3. Pruning occurs because:
   - If the current position is already worse than what either player can force in another branch
   - The algorithm can prove no better outcome is possible in the remaining positions
   - Therefore, there's no need to explore those branches further

4. The optimization is most effective when:
   - The best moves are evaluated first (earlier pruning)
   - The game has a high branching factor (many possible moves)
   - Good moves tend to be clustered (allowing for more cutoffs)

5. Benefits of the optimization:
   - Reduces the number of positions evaluated
   - Allows for deeper search within the same time constraints
   - Maintains exactly the same move selection as regular Minimax
   - Particularly effective in games like Connect Four with many possible moves

For example, in a typical Connect Four position with depth 4, Alpha-Beta pruning might evaluate only 1000 positions instead of the 8000 positions that regular Minimax would examine, while reaching the same decision.

## Features

- **Human vs Computer**: Play against an AI opponent that uses the Minimax algorithm to make optimal decisions.
- **Human vs Human**: Challenge a friend in the classic two-player mode.
- **AI Difficulty**: Choose from multiple difficulty levels (Easy, Medium, Hard, Extreme Hard).
- **Real-Time Gameplay**: See the game board update after every move.
- **Responsive UI**: The game supports a simple yet interactive interface using **Pygame** for displaying the board and moves.

## Future Improvements
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
