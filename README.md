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
     - [x] A 3x3 grid is generated at the start of each game with `?` filling the 9 spaces
 * User plays against the computer
     - [x] The computer generates a random integer from 1-9 each turn after the user
 * The game accepts the users inputs
 * Input validation
     - [x] Coordinates that are outside the size of the grid will not be accepted and the game must be restarted
     - [x] If a spot is already taken the user will not be able to place their symbol there, the game must be restarted
 * The game checks to see what the outcome of the game is and announces it
     - [x] The game will announce the winner
     - [x] The game will announce if it is a tie due to all the 9 spaces being filled without a winner
 
### Future features

* add the option to make it a user vs user game instead of just a user vs computer game
* Allow the players decide which symbol they would like to be, `X` or `O`

## Data Model

Whilst typing up this README.md before submission, I unfortunately realised that my project was missing a class data model, as I understand that this is stated as part of the pass criteria I will accept the result given by the assessment team.

## Testing

* I have given the console invalid data such as the same number twice or a numbe that is too large
* I have tested that the game works as expected on the Code Institute heroku terminal and on my local terminal
* I have been trying to source a valid python online validator as the link to the offical PEP8 validator we have been given brings you to a goDaddy domain [Here is the link that should bring me to the PEP8 validator](http://pep8online.com/)

## Bugs

### Solved Bugs

1. Since the board itself was zero indexed it took me a little while to realise that I would have to utilise a `-1` in the code for example on line 38 `int_input-1`

### Remaining Bugs

1. Each word where the global variable is being utilised is underlined in yellow and this is the error it displays, `Redefining name 'board' from outer scope (line 5)`

## Deployment

This project was deployed using Code Institute's mock terminal in Heroku.

* Steps for the deployment
    * Sign into your account on Heroku
    * Create a new Heroku app
    * Add a Config Var with a key of `PORT` and a value of `8000`
    * Ensure the buildpacks are set to `python` and `NodeJS` in that order
    * Link the Heroku app to the github repository
    * Deploy the game

### Credits

1. The Code institute deployment terminal
2. This is the link to the stack overflow article that helped me with the checking process in my project, specifically the `have_you_won` section, [click the link here](https://stackoverflow.com/questions/49160081/the-functions-for-this-python-tic-tac-toe-game-is-not-working)