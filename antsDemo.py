#Ray Tso
#4/30/18
#antsDemo.py

from ggame import *
from random import randint

ANTS=10
WIDTH=1000
HEIGHT=500

if __name__=='__main__':
    red=Color(0xFF0000,2)
    ant=CircleAsset(20,LineStyle(1,red),red)
    
    for i in range(ANTS):
        Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT)))
    
    App().run()
