'''
https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
27 - Tic Tac Toe Draw
In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information about a tic tac toe game. 
In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board, to know whether player 1 or player 2 (or whoever is X and O won).

The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal. 
So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:

game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3.
Then the game would print out
game = [[0, 0, X],
	    [0, 0, 0],
	    [0, 0, 0]]
And ask Player 2 for their move, printing an O in that place.

Things to note:
# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). 
To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1
This is not required, but whichever way you choose to implement this, it should be explained to the player.
# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number.
Then you can use your Python skills to figure out which row and column they want their piece to be in.
# Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.

Bonus:
For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full. 
In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.
'''
game_board =    [[0,0,0],
                [0,0,0],
                [0,0,0]]

def draw_board():
    for row in game_board:
        print(" ---" * 3)
        for elem in row:
            if elem == 0:
                print("|   ", end="")
            elif elem == 1:
                print("| X ", end="")
            elif elem == 2:
                print("| O ", end="")
        print("|   ")
    print(" ---" * 3)

def p1_move():
    p1_inp = input("Player 1, enter coordinates (row, col): ").split(",")
    r = int(p1_inp[0]) - 1
    c = int(p1_inp[1]) - 1
    if game_board[r][c] == 0:
        game_board[r][c] = 1
    else:
        print("Invalid!!")

def p2_move():
    p2_inp = input("Player 2, enter coordinates (row, col): ").split(",")
    r = int(p2_inp[0]) - 1
    c = int(p2_inp[1]) - 1
    if game_board[r][c] == 0:
        game_board[r][c] = 2
    else:
        print("Invalid!!")

no_of_moves = 0
draw_board()
while True:
    p1_move()
    draw_board()
    p2_move()
    draw_board()