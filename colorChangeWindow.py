#Claire Yegian
#10/18/17
#colorChangeWindow.py - window changes to random color each time you click it

from random import randint

def mouseClick(event):
    num1 = randint(0,9)
    num2 = randint(0,9)
    num3 = randint(0,9)
    num4 = randint(0,9)
    num5 = randint(0,9)
    num6 = randint(0,9)
    
    color = Color(0xnum1num2num3num4num5num6,1)
    
    colorBox = RectangleAsset(1000,600,LineStyle(1,color),color)
    Sprite(colorBox)

App().listenKeyEvent('click',mouseClick)
App().run()