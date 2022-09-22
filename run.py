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
def showBoard():
    """
    Lays out the grid and 0 index system 
    """
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print("--+---+--")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print("--+---+--")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])


# takes the players input
def userInput(game_board):
    """
    Asks the user to enter an integer from 1-9, and ensuring that the space
    hasn't been taken already.
    ValueErrors raised if anything other than an integer from 1-9 is enetered.
    """
    integer_input = int(input("Please enter a number from 1-9: "))
    if integer_input >= 1 and integer_input <= 9 and game_board[integer_input-1] == "?":
        game_board[integer_input-1] = currentUser
    else:
        print("Sorry that spot is already taken")
        
  




showBoard()
userInput(game_board)