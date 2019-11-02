# snake tutorial in python from you-tube copied by Brian L

import math
import random
import pygame
import tkinter as tk 
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    pass


def redrawWindow(surface):
    pygame.display.update()

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    width = 800
    height = 800
    rows = 40
    win = pygame.display.set_mode((width, height))
    s = snake((255, 0, 0), (10, 10))
    flag = True

    clock = pygame.time.Clock()


    while flag:
        pygame.time.delay(50)  #!#!#!# this lower equals slower
        clock.tick(10)  ###!!! this lower equals faster

        redrawWindow(win)


    pass





main()
