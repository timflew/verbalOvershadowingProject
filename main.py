#!/usr/bin/env python
from __future__ import division

import drawer
import timer
import time
from numpy import *
from inputter import *

def showFeedback(fbtext, xstart=5, ystart=100):
	drawer.fillScreen((0,0,0))
	for i in range(0,len(fbtext)):
		drawer.writeText(fbtext[i], (xstart,ystart+30*i))
	drawer.flip()
	waitforkey()


def instructions(insfile):
	insttext = ['show instructions here!']
	showFeedback(insttext)


drawer = drawer.Drawer()  
instructions('instructions.txt')


quit()
