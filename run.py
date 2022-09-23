
# Global variables
board = [
    "?", "?", "?",
    "?", "?", "?",
    "?", "?", "?"
]
CURRENTUSER = "X"
WINNER = None
GAMERUNNING = True

# displaying the game board to the console


def show_board(board):
    """
    Lays out the grid and 0 index system .strip()
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | " + board[8])

# takes the players input


def user_input(board):
    """
    Asks the user to enter an integer from 1-9, and ensuring that the space
    hasn't been taken already.
    """
    int_input = int(input("Please enter a number from 1-9: "))
    if int_input >= 1 and int_input <= 9 and board[int_input-1] == "?":
        board[int_input-1] = CURRENTUSER
    else:
        print("Something went wrong, please enter a valid integer from 1-9")

# checking for the winner


while GAMERUNNING:
    show_board(board)
    user_input(board)
