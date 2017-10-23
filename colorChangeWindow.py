#Claire Yegian
#10/18/17
#colorChangeWindow.py - window changes to random color each time you click it

from ggame import *
from random import randint

def mouseClick(event):
    changeColor()

def changeColor():
    num1 = randint(1,4)
    if num1 == 1:
        color = Color(0x00ff63,1)
        colorBox = RectangleAsset(1000,600,LineStyle(1,color),color)
        Sprite(colorBox)
    elif num1 == 2:
        color = Color(0xff4563,1)
        colorBox = RectangleAsset(1000,600,LineStyle(1,color),color)
        Sprite(colorBox)
    elif num1 == 3:
        color = Color(0x004300,1)
        colorBox = RectangleAsset(1000,600,LineStyle(1,color),color)
        Sprite(colorBox)
    elif num1 == 4:
        color = Color(0xff00ff,1)
        colorBox = RectangleAsset(1000,600,LineStyle(1,color),color)
        Sprite(colorBox)

App().listenMouseEvent('click',mouseClick)
App().run()