#Claire Yegian
#10/27/17
#bubbles.py - random circle appears each time user clicks screen

from ggame import *
from random import randint

num = randint(1,7)
color1 = Color(0x00ff21,1)
color2 = Color(0x00ff21,1)
color1 = Color(0x00ff21,1)
color1 = Color(0x00ff21,1)
color1 = Color(0x00ff21,1)
color1 = Color(0x00ff21,1)
color1 = Color(0x00ff21,1)

bubblecolor = Color(0x004566,1)

bubble = CircleAsset(randint(1,200),LineStyle(1,bubblecolor),bubblecolor)

Sprite(bubble,(randint(1,500),randint(1,500)))
App().run()
