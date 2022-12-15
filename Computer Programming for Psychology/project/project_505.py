# Platform pycharm win 11
# Prepare for Project 505

"""
introductory comments:

"""

# =====================
# IMPORT MODULES
# =====================
# -import numpy and/or numpy functions *
# -import psychopy functions
# -import file save functions
# -(import other functions as necessary: os...)
import os
import time
import random
import itertools
import numpy as np
import pandas as pd
from datetime import datetime
from psychopy import core, visual, event, monitors, gui

# main start here
if __name__ == "__main__":
    print("project demo \n")

# =====================
# PATH SETTINGS
# =====================
main_dir = os.getcwd()
path = os.path.join(main_dir, 'dataFiles')
# -check that these directories exist
if not os.path.exists(path):
    os.makedirs(path)

# =====================
# COLLECT PARTICIPANT INFO
# =====================
# -create a dialogue box that will collect current participant number, age, gender, handedness
exp_info = {"subject_nr": (), "age": (),
            "gender": (), "handedness": ('left', 'right', 'ambi'),
            "session": ()
            }

# wait for 2 seconds
print('All variables have been created! Now ready to show the dialog box!')
time.sleep(2)
# Customize my_dlg so that you have a title for your dialog box: "subject info"
my_dlg = gui.DlgFromDict(dictionary=exp_info, title='subject_info')

# get date and time
date = datetime.now()
exp_info['date'] = str(date.day) + str(date.month) + str(date.year)

# -create a unique filename for the data
filename = (str(exp_info['subject_nr']) + '_outputFile.csv')
# print(filename)

# =====================
# STIMULUS AND TRIAL SETTINGS
# =====================
# -number of trials and blocks *
n_trials = 4
n_blocks = 2
totalTrials = n_trials * n_blocks

# -stimulus properties like size
position_raw = np.arange(-0.4, 0.5, 0.1)
position = np.around(position_raw, decimals=2)

# -stimulus properties position
position_stim = list(itertools.product(position, repeat=2))
# print(position_stim)

# number of shape per trial
stims_number = [4, 8, 8, 10, 12, 14, 16]

# define the monitor settings using psychopy functions
mon = monitors.Monitor('my_monitor', width=21, distance=35)
mon.setSizePix(mon.getSizePix())

# -define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, units='height', fullscr=False, color='grey')

# -start message text *
start_message = visual.TextStim(win, text="Welcome to the experiment, Please press any key to start", height=.04)
wait_message = visual.TextStim(win, text="press space to continue", height=.04)

# =====================
# PREPARE CONDITION LISTS
# =====================
# two conditions
condition1 = [0, 1] * 4  # triangle with line
condition2 = [2, 3] * 4  # triangle without line

# zip the number of shapes and conditions together
alltrials1 = list(zip(stims_number, condition1))
alltrials2 = list(zip(stims_number, condition2))

# -create counterbalanced list of all conditions *
random.shuffle(alltrials1)
random.shuffle(alltrials2)

# =====================
# PREPARE DATA COLLECTION LISTS
# =====================
# record the trial and block number
# as well as their response, accuracy, and reaction time
types = [0] * totalTrials
accuracies = [0] * totalTrials
response = [0] * totalTrials
responseTimes = [0] * totalTrials
trialNumbers = [0] * totalTrials
blockNumbers = [0] * totalTrials

# =====================
# CREATION OF WINDOW AND STIMULI
# =====================
# windows and monitor define above
# define the fixations
fix_stims = visual.TextStim(win, text="+", height=0.05, color=[255, 255, 255])

# -define experiment start text using psychopy functions
instruction_message = visual.TextStim(win, text="Visual search task \n"
                                                "Your task is to identify whether exists a unique shape in the screen\n"
                                                "Press space to start when you are ready ", height=.04)
line_presence = visual.TextStim(win, text="If the unique shape appears on the screen \n press q otherwise, press p"
                                          "\nPress space to start when you are ready ",
                                height=.04)

# -define block (start)/end text using psychopy functions
block_text = visual.TextStim(win, text="Block start", height=.04)
end_block = visual.TextStim(win, text="Block end \nPress space", height=.04)
end_experiment = visual.TextStim(win, text="Experiment End \n \nThanks for your participation", height=.04)

# define stimuli using psychopy functions
line_stims = visual.Line(win)

# -create response time clock
trial_timer = core.Clock()

# -make mouse pointer invisible
win.mouseVisible = False

# =====================
# START EXPERIMENT
# =====================
# -present start message text
start_message.draw()
win.flip()
# -allow participant to begin experiment with button press
event.waitKeys(keyList=['space'])

instruction_message.draw()
win.flip()
event.waitKeys(keyList=['space'])

line_presence.draw()
win.flip()
event.waitKeys(keyList=['space'])

# =====================
# BLOCK SEQUENCE
# =====================
# -for loop for nBlocks *
for blocks in range(n_blocks):

    # Each block round appears different conditions
    if blocks % 2 == 0:
        alltrials = alltrials1  # condition 1
    elif blocks % 2 != 0:
        alltrials = alltrials2  # condition 2

    # -present block start message
    block_text.text = 'Begin Block ' + str(blocks + 1)
    block_text.draw()
    win.flip()
    core.wait(1)

    # -randomize order of trials here *
    random.shuffle(alltrials)

    # -reset response time clock here
    trial_timer.reset()

    # =====================
    # TRIAL SEQUENCE
    # =====================
    # -for loop for nTrials *
    for trials in range(n_trials):
        # -set stimuli and stimulus properties for the current trial
        overallTrial = blocks * n_trials + trials
        blockNumbers[overallTrial] = blocks + 1
        trialNumbers[overallTrial] = trials + 1
        # -empty key presses
        event.clearEvents(eventType='keyboard')

        # =====================
        # START TRIAL
        # =====================
        # draw fixations
        fix_stims.draw()
        win.flip()
        core.wait(0.5)

        # current shape positions
        StimPos = random.sample(position_stim, alltrials[trials][0])
        for i in StimPos:
            # -draw stimulus
            tri_stim = visual.ShapeStim(win, vertices=((0, 0.025), (0, -0.025), (0.05, 0)), pos=i)
            tri_stim.draw()

        # if the shape identifier == 1 the target stimulus is the triangle with line
        if alltrials[trials][1] == 1:
            # obtain the position for the line
            HlinePos1 = random.sample(StimPos, 1)
            # elements convert to list
            HlinePos1 = HlinePos1[0]
            HlinePos2 = [HlinePos1[0] - 0.03, HlinePos1[1]]
            line_stims.start = HlinePos1
            line_stims.end = HlinePos2
            line_stims.draw()

        # if the shape identifier == 2 No target stimulus appear
        elif alltrials[trials][1] == 2:
            for j in StimPos:
                HlinePos1 = j
                HlinePos2 = [j[0] - 0.03, j[1]]
                line_stims.start = HlinePos1
                line_stims.end = HlinePos2
                line_stims.draw()

        # if the shape identifier == 3 the target stimulus is the triangle without line
        elif alltrials[trials][1] == 3:
            for k in random.sample(StimPos, alltrials[trials][0] - 1):
                HlinePos1 = k
                HlinePos2 = [k[0] - 0.03, k[1]]
                line_stims.start = HlinePos1
                line_stims.end = HlinePos2
                line_stims.draw()

        # -flip window
        win.flip()
        trial_timer.reset()
        keys = event.waitKeys(keyList=['q', 'p', 'escape'])

        if keys:
            # record the response time and relevant data
            responseTimes[overallTrial] = trial_timer.getTime()
            # -collect subject response for that trial
            response[overallTrial] = keys[0]
            # -collect accuracy for that trial
            if alltrials[trials][1] == 0 or alltrials[trials][1] == 2:
                types[overallTrial] = 'No unique shape'
                if keys[0] == 'q':
                    accuracies[overallTrial] = 'Incorrect'
                else:
                    accuracies[overallTrial] = 'Correct'

            if alltrials[trials][1] == 1 or alltrials[trials][1] == 3:
                types[overallTrial] = 'unique shape appear'
                if keys[0] == 'q':
                    accuracies[overallTrial] = 'correct'
                else:
                    accuracies[overallTrial] = 'Incorrect'

        print(
            'Block:',
            blocks + 1,
            ', Trial:',
            trials + 1,
            ', Types:',
            types[overallTrial],
            ", response:",
            response[overallTrial],
            ', accuracies',
            accuracies[overallTrial],
            ', RT:',
            responseTimes[overallTrial]
        )

    event.clearEvents()

    if blocks != n_blocks - 1:
        end_block.draw()
        win.flip()
        event.waitKeys(keyList=['space'])

    else:
        end_experiment.draw()
        win.flip()
        core.wait(2)

# ======================
# END OF EXPERIMENT
# ======================
# -write data to a file
df = pd.DataFrame(data={
    'Block Number': blockNumbers,
    'Trial Number': trialNumbers,
    'Types': types,
    'Response': response,
    'Accuracy': accuracies,
    'Response Time': responseTimes
})
# save to csv file
df.to_csv(os.path.join(path, filename), sep=',', index=False)

# -close window
win.close()
# -quit experiment
# core.quit()

# ======================
# Example saved file
# ======================
# read the data from the path
data_dir = os.path.join(main_dir, 'dataFiles', filename)
# generate the dataframe
df = pd.read_csv(data_dir)

# The script should print the entire dataframe
print(df)

