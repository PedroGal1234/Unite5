#Pedro Gallino
#11/17/17
#matrixDemo.py - how to create/use matrix


board = [['a','b','c'],['d','e','f'],['g','h','i']]
def printBoard():
    for row in range(0,3):
        for col in range(0,3):
            print(board[row][col],' ',end = '')
        print()

board = [['a','b','c'],['d','e','f'],['g','h','i']]
printBoard()

row = int(input('Enter a row Number: '))
col = int(input('Enter a column number: '))

board[row-1][col-1] = 'X'

printBoard()
