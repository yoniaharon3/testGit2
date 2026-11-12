"""Simple two-player Tic-Tac-Toe for the terminal."""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def print_board(board):
    print()
    for row in range(3):
        cells = board[row * 3:row * 3 + 3]
        print(" " + " | ".join(cells))
        if row < 2:
            print("---+---+---")
    print()


def get_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def ask_move(board, player):
    while True:
        raw = input(f"Player {player}, choose a square (1-9): ").strip()
        if not raw.isdigit() or not 1 <= int(raw) <= 9:
            print("Please enter a number from 1 to 9.")
            continue
        index = int(raw) - 1
        if board[index] != " ":
            print("That square is taken. Try another.")
            continue
        return index


def play_game():
    board = [" "] * 9
    player = "X"
    print("Tic-Tac-Toe! Squares are numbered 1-9, left to right, top to bottom.")

    while True:
        print_board(board)
        board[ask_move(board, player)] = player

        winner = get_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return
        if " " not in board:
            print_board(board)
            print("It's a draw!")
            return

        player = "O" if player == "X" else "X"


def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
