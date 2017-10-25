#Claire Yegian
#10/18/17
#printSquares.py - prints out grid of squares

def printSquares(rows,columns):
    n = 0
    while n<=columns:
        print('+--'*rows+'+')
        print('|  '*rows+'|')
    n += 1

printSquares(2,4)
