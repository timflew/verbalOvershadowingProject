#!/Library/Frameworks/Python.framework/Versions/Current/bin/python
from __future__ import division
import OpenGL.GL as gl
import pygame
from pygame.locals import *
import pygame.image
from numpy import *
import colorsys
pygame.font.init()
        
class Drawer(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 1024))#, pygame.FULLSCREEN)#16)
        pygame.mouse.set_visible(False)
        self.center = (512,368)
        self.deg2pix = 30
        self.xlim = (0, 1024)
        self.ylim = (0,768)
        self.gainmag = 40
        self.font = pygame.font.Font(None, 36)
        self.textDic = {}

    def writeText(self, text, pos, col=(255,255,255)):
        if not self.textDic.has_key(text):
            self.textDic[text] = self.font.render(text, 1, col)
        self.screen.blit(self.textDic[text], pos)

    def drawLine(self,stapos,endpos,width,col):
        pygame.draw.line(self.screen, col, stapos, endpos, 5)


    def fillScreen(self, col=(255,255,255)):
        self.screen.fill(col)
        
    def flip(self):
        pygame.display.flip()

