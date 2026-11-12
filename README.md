# Tic-Tac-Toe

A simple two-player Tic-Tac-Toe game that runs in the terminal, written in Python.

## Requirements

- Python 3.6 or newer
- No external dependencies

## Running the game

```bash
python3 tictactoe.py
```

## How to play

- Two players take turns: **X** goes first, then **O**.
- On your turn, enter a number from 1 to 9 to place your mark on that square.
- Squares are numbered left to right, top to bottom:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

- The first player to get three marks in a row (horizontally, vertically, or diagonally) wins.
- If all nine squares are filled and nobody has won, the game is a draw.
- After each game you can choose to play again (`y`) or quit (`n`).

## Example

```
 X | O |  
---+---+---
   | X |  
---+---+---
   |   | O

Player X, choose a square (1-9):
```

## Features

- Input validation: rejects non-numeric input, numbers outside 1-9, and occupied squares
- Automatic win and draw detection
- Replay option without restarting the program

## Project structure

| File           | Description                      |
| -------------- | -------------------------------- |
| `tictactoe.py` | The game logic and terminal UI   |
| `README.md`    | Project documentation            |
