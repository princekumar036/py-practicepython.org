'''
https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
24 - Draw A Game Board 1
Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
'''
def draw_board(sz):
    for i in range(sz):
        print(" ---" * sz)
        print("|   " * (sz + 1))
    print(" ---" * sz)

# # other solution
# a = '---'.join('    ')
# b = '   '.join('||||')
# print('\n'.join((a, b, a, b, a, b, a)))