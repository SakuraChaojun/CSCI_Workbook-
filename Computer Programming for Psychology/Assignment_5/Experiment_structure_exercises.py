# -*- coding: utf-8 -*-
# OS platform: WIN 11,i7

#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os

print(os.getcwd())
#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')
print(data_dir)

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')
print(image_dir)

#-check that these directories exist
print(os.path.isdir(image_dir))
print(os.path.isdir(data_dir))

#alternatively we can throw a exception 
#if not os.path.isdir(image_dir):    
    #raise Exception('Could not find the path-image!')

#if not os.path.isdir(data_dir):
   #raise Exception('Could not find the path-data!')
   
   
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
n_trials = 10
n_blocks = 2

#-stimulus names (and stimulus extensions, if images) *
cats = ['faces'] * 10
imgs = ['im1.png','im2.png','im3.png','im4.png','im5.png',
        'im6.png','im7.png','im8.png','im9.png','im10.png']

#-stimulus properties like size, orientation, location, duration *
stimSize = [200,200]
stimDur = 1
stimOrien = [10]

#-start message text *
start_message = 'Welcome to the experiment, press any key to begin'

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
ims_in_dir = sorted(os.listdir(image_dir))
if not imgs == ims_in_dir:
    # raise Exception('The image lists do not match up! Check the files')
    print ('The image lists do not match up! Check the files')
    #for loop verison plese refer 'Directory_exercises'
    
#-create counterbalanced list of all conditions *
cat_images = list(zip(cats,imgs))
print(cat_images)

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
correct_response = []
#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
participant_response = []
#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
response_accuracy = []
#-create an empty list for response time collection *
response_time = []
#-create an empty list for recording the order of stimulus identities *
stimulus_identities = []
#-create an empty list for recording the order of stimulus properties *
stimulus_properties = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
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
for block in range(n_blocks):
    #-present block start message
    #-randomize order of trials here *
    np.random.shuffle(cat_images)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in range(n_trials):
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        print(trial)
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

