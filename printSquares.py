#Claire Yegian
#10/18/17
#printSquares.py - prints out grid of squares

def printSquares(rows,columns):
    n = 0
    while n<rows:
        print('+--'*columns+'+')
        print('|  '*columns+'|')
        n += 1
    print('+--'*columns+'+')

printSquares(4,9)
