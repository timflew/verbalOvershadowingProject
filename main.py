#!/usr/bin/env python

# main verbal overshadowing code
from __future__ import division

import drawer
import timer
import time
from numpy import *
from inputter import *
from undergrad_tasks import *

# loadConfig(fName)-Loads configuration data from config.txt
# confData-A dictionary mapping the config values to names
confData = loadConfig('config.txt')

# selectStimuli(fName,numWedge,numPart)
# colors-List containing numTrial entries. Each entry contains a list where the first entry is a list of color angles
# and the second entry is the target color
colors=selectStimuli('stim.txt',numWedge,numPart,numTrial,numCols)


def showFeedback(fbtext, xstart=5, ystart=100):
	drawer.fillScreen((0,0,0))
	for i in range(0,len(fbtext)):
		drawer.writeText(fbtext[i], (xstart,ystart+30*i))
	drawer.flip()
	waitforkey()


def instructions(insfile):
    # Load instructions from instr.txt
    #instrText=loadInstructions('instr.txt')
	instrText = ['show instructions here!']
	showFeedback(instrText)


drawer = drawer.Drawer()  
instructions('instructions.txt')

#runExpt(confData['numTrial'])

quit()




