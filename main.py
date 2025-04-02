import pandas as pd
from time import sleep
import numpy as np
import pygame
import cv2



def getKey(KeyName):
    ans = False

    for event in pygame.event.get():pass
    keyinput=pygame.key.get_pressed()

    myKey=getattr(pygame,'K{}'.format(KeyName))
    if keyinput[myKey]:
        ans=True
    pygame.display.update()
    return ans
def getKeyboardInput():
    lr,fb,ud,yv=0,0,0,0
    speed=50
    if getKey("LEFT"):

        lr=-speed
    elif getKey("RIGHT"):lr=speed

    if getKey("up"):
        fr = speed
    elif getKey("down"):
        fr = -speed
    if getKey("w"):
        lr = speed
    elif getKey("s"):
        lr = -speed
    if getKey("a"):
        lr = speed
    elif getKey("d"):
        lr = -speed

    # if getKey("l"):
    #      me.load()
    #
    # elif getKey("t"):
    #     me.takeoff()

















