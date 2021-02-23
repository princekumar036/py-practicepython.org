'''
https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
26 - Check Tic Tac Toe
As you may have guessed, we are trying to build up to a full tic-tac-toe board. 
However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:
game = [[1, 2, 0],
	    [2, 1, 0],
	    [2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. 
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
'''


def check_winner(game):
    # for rows
    for i in range(3):
        row = set([game[i][0], game[i][1], game[i][2]])
        if len(row) == 1 and game[i][0] != 0:
            return game[i][0]
    # for columns
    for i in range(3):
        column = set([game[0][i], game[1][i], game[2][i]])
        if len(column) == 1 and game[0][i] != 0:
            return game[0][i]
    # for diagonals
    diag1 = set([game[0][0], game[1][1], game[2][2]])
    diag2 = set([game[0][2], game[1][1], game[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and game[1][1] != 0:
        return game[1][1]