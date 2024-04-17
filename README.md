# Nim Game with AI Opponents

This project implements the classic game of Nim with multiple AI opponents using different algorithms and strategies. The game is built using Flask for the web application and Python for the backend logic.

## Table of Contents
- [Game Rules](#game-rules)
- [AI Opponents](#ai-opponents)
  - [Evaluation Function](#evaluation-function)
  - [Minimax](#minimax)
  - [Fail-Soft Alpha-Beta Pruning](#fail-soft-alpha-beta-pruning)
  - [Fail-Hard Alpha-Beta Pruning](#fail-hard-alpha-beta-pruning)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Game Rules
- The game starts with multiple piles of stones.
- Two players take turns removing stones from the piles.
- On each turn, a player must remove at least one stone from a single pile.
- The player who removes the last stone loses the game.

## AI Opponents
The project includes several AI opponents that use different algorithms and strategies to play the game of Nim optimally. The available AI opponents are:

### Evaluation Function
The evaluation function AI opponent uses a heuristic approach based on the nim-sum concept. It calculates the nim-sum of the current game state and makes a move that reduces the nim-sum to zero, ensuring a winning position. If the nim-sum is already zero, it makes a random move.

### Minimax
The minimax AI opponent uses the minimax algorithm to determine the best move. It recursively explores the game tree, considering all possible moves and counter-moves, and selects the move that maximizes its score while minimizing the opponent's score. The algorithm assumes that both players play optimally.

### Fail-Soft Alpha-Beta Pruning
The fail-soft alpha-beta pruning AI opponent is an optimized version of the minimax algorithm. It employs alpha-beta pruning to reduce the number of nodes evaluated in the game tree. The fail-soft variation allows the search to continue even if a node's value exceeds the current alpha or beta bounds, potentially exploring better moves.

### Fail-Hard Alpha-Beta Pruning
The fail-hard alpha-beta pruning AI opponent is similar to the fail-soft variant but strictly limits the returned value to be within the alpha and beta bounds. If a node's value exceeds the bounds, the search is immediately terminated for that branch. This approach can lead to earlier cutoffs and faster search but may miss potentially better moves.

## Getting Started
To run the Nim game locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/nim-game.git
   ```

2. Install the required dependencies:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

4. Open your web browser and navigate to `http://localhost:5000` to play the game.

## Project Structure
The project structure is as follows:
```
nim-game/
├── templates/
│   ├── index.html
│   ├── game.html
│   └── result.html
├── app.py
├── evaluation_function.py
├── minimax.py
├── fail_soft.py
├── fail_hard.py
├── requirements.txt
└── README.md
```

- The `templates` directory contains the HTML templates and styling for the game pages.
- `app.py` is the main Flask application file that handles the game logic and routes.
- `evaluation_function.py`, `minimax.py`, `fail_soft.py`, and `fail_hard.py` contain the implementations of the different AI opponents.
- `requirements.txt` lists the required Python dependencies.
- `README.md` provides an overview of the project and instructions for running the game.