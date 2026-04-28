import random

def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    
    for turn in range(9):
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins! Congratulations!")
                    return
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue
            
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    play_game()
