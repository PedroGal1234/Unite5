#Pedro Gallino
#11/15/17
#/betterColoredWindow.py - a better colored window from unit 2.5

from ggame import *
from random import randint

def mouseClick(event):    
    colors = ['0xff0000','0x000ff','0xffff00','0xff33ff','0x66cc00','0xff8000']
    num = randint(1,6)
    color = Color(colors[num-1],1)
    line = LineStyle(3,color)
    rectangle = RectangleAsset(1000,1000,line,color)
    Sprite(rectangle)

App().listenMouseEvent('click',mouseClick)
App().run()

