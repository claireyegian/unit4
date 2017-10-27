#Claire Yegian
#10/27/17
#bubbles.py - random circle appears each time user clicks screen

from ggame import *
from random import randint

def mouseClick(event):
    addBubble()

def addBubble():
    num = randint(1,7)
    if num==1:
        bubblecolor = Color(0x00ff21,1)
    if num==2:
        bubblecolor = Color(0x321200,1)
    if num==3:
        bubblecolor = Color(0x000067,1)
    if num==4:
        bubblecolor = Color(0x5100ff,1)
    if num==5:
        bubblecolor = Color(0xf00032,1)
    if num==6:
        bubblecolor = Color(0x450081,1)
    if num==7:
        bubblecolor = Color(0x090909,1)
    
    bubble = CircleAsset(randint(5,200),LineStyle(1,bubblecolor),bubblecolor)
    Sprite(bubble,(randint(1,500),randint(1,500)))
    App().run()

App().listenMouseEvent('click',mouseClick)
App().run()
