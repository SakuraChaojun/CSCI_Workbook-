#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np
#-import psychopy functions
from psychopy import visual,core,gui,event
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os
#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
os.chdir('/Users/chaojunma/Desktop/Alberta')
#-define the directory where you will save your data

#-if you will be presenting images, define the image directory

#-check that these directories exist

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time

#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *

#-stimulus names (and stimulus extensions, if images) *

#-stimulus properties like size, orientation, location, duration *

#-start message text *

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist

#-create counterbalanced list of all conditions *


#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
#-create an empty list for response time collection *
#-create an empty list for recording the order of stimulus identities *
#-create an empty list for recording the order of stimulus properties *

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window([800 * 600],allowGUI = True, 
foil = visual.GratingStim [ 

#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
    #-present block start message
    #-randomize order of trials here *
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment