#Claire Yegian
#10/27/17
#bouncingBall.py - bouncing ball

from ggame import *

back = Color(0x000000,1)
ball = Color(0xf000f0,1)
"""
def moveBall:
    ballBounce.x = ba

def moveBanana():
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE
    data['frames'] = 0

def updateScore():
    data['score'] += 10
    data['scoreText'].destroy()
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))

def step():
    data['frames'] += 1
    if data['frames'] == 300:
        moveBanana()

data = {}
data['score'] = 0
data['frames'] = 0"""

    
"""
def changeDirectionRight:
    if ballBounce.x>1000:"""
        

ballBounce = CircleAsset(50,LineStyle(1,ball),ball)
background = RectangleAsset(1000,600,LineStyle(1,back),back)

Sprite(background)
Sprite(ballBounce)

App().run()
