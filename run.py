
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

# checking for the winner or a draw, across all three directions
# Rows


def check_rows(board):
    """
    Checking the horizontals to see if there has been a win
    """
    global WINNER
    if board[0] == board[1] == board[2] and board[1] != "?":
        WINNER = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "?":
        WINNER = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "?":
        WINNER = board[6]
        return True


# Columns


def check_columns(board):
    """
    Checking the verticals to see if there has been a win, utilising
    the same method as the check_rows
    """
    global WINNER
    if board[0] == board[3] == board[6] and board[0] != "?":
        WINNER = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "?":
        WINNER = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "?":
        WINNER = board[2]
        return True


# Diagonal


def check_diagonal(board):
    """
    Checking the diagonals to see if there has been a win
    """
    global WINNER
    if board[0] == board[4] == board[8] and board[0] != "?":
        WINNER = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "?":
        WINNER = board[2]
        return True

# Draw


def check_draw(board):
    """
    Checking for a tie in the game by checking if all 9 spaces
    have been filled and there is no more moves to make
    """
    global GAMERUNNING
    if "?" not in board:
        show_board(board)
        print("Uh Oh there is no more space letf, It's a tie!\n")
        GAMERUNNING = False


while GAMERUNNING:
    show_board(board)
    user_input(board)
