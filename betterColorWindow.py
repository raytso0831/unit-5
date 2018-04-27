#Ray Tso
#4/27/18
#betterColorWindow.py

from random import randint
from ggame import*
def mouseClick(event):
    
    red=Color(0xFF0000,1) #this is the color red
    green=Color(0x00FF00,1)
    blue=Color(0x0000FF,1)
    black=Color(0x000000,1)
    
    colors = [red, blue, green, black]
    line = LineStyle(1,colors[0])
    square = RectangleAsset(1000,1000,line,colors[randint](0,3))
    Sprite(square)
    
App().listenMouseEvent('click',mouseClick)
App().run()

