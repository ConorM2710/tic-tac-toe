#-----Global Variables-----
currentUser = "X"
winner = None
gameRunning = True


# Layout of the 3 x 3 game board
game_board = [
    "?", "?", "?",
    "?", "?", "?",
    "?", "?", "?"
]



# displaying the game board to the console
def show_board():
    """
    Lays out the grid and 0 index system 
    """
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print("--+---+--")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print("--+---+--")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])


# takes the players input



show_board()