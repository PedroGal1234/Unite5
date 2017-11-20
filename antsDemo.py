#Pedro Gallino
#11/20/17
#antsDemo.py - how to use lists with graphics

from ggame import *
from random import randint

WIDTH = 800
HEIGHT = 500

if __name__ == '__main__':

    red = Color(0xFF0000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)
    for i in range(100):
        Sprite(ant,(randint(10,WIDTH),(randint(10,HEIGHT))))
    
    App().run()

