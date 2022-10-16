# Tic Tac Toe

Tic Tac Toe is a python terminal game, which runs in the Code Institute mock terminal on Heroku.

The objective of the game is for the user "X" to beat the computer "O", by attempting to score three of 
their symbols in a row vertically, diagonally or horizontally.

[Here is a link to the live site]()

![image of the game on multiple devices]()

## How to play the game

Tic Tac Toe is a game of ancient origins which you can find out more about here on [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe)

In this version the user "X" will be playing against the computer "O".
1. The user "X" goes first and must enter a valid integer from 1 to 9.
2. The board is a three by three grid with the nine spaces consisting of a `?`.
3. When the user enters a valid integer the `?` will disappear and be replaced by that players symbol,
either an `X` or an `O`.
4. The player and the computer then takes turns to occupy spaces on the grid.
5. The first player to occupy three spaces such that theyr'e symbol aligns vertically, horizontally or diagonally, wins the game.
6. In the event of a draw match, the players must reset the board and start again.

## Features

### Existing features

 * Board generation at the start of each game
     * A 3x3 grid is generated at the start of each game with `?` filling the 9 spaces
 * User plays against the computer
     * The computer generates a random integer from 1-9 each turn after the user
 * The game accepts the users inputs
 * Input validation
     - [x] Coordinates that are outside the size of the grid will not be accepted and the game must be restarted
     - [x] If a spot is already taken the user will not be able to place their symbol there, the game must be restarted
 * The game checks to see what the outcome of the game is and announces it
     - [x] The game will announce the winner
     - [x] The game will announce if it is a tie due to all the 9 spaces being filled without a winner
 
