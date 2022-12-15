# Platform pycharm win11

# =====================
# IMPORT MODULES
# =====================
import os
import time
import numpy as np
from datetime import datetime
from psychopy import core, visual, monitors, gui, event

"""Adjust your experiment so that it follows frame-based timing rather than clock timing (comment out the clock-based 
timing code in case you want to use it again) using for loops and if statements.. """

if __name__ == '__main__':
    print('frame_timing_experiment ----\n')

# =====================
# PATH SETTINGS
# =====================
# -define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()
# -define the directory where you will save your data
data_dir = os.path.join(main_dir, 'data')
# -if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir, 'images')
# -check that these directories exist
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")
if not os.path.isdir(data_dir):
    raise Exception("could not find the path!")

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
file_name = str(exp_info['date']) + "_" + str(exp_info['subject_nr'])
print(file_name)

# =====================
# STIMULUS AND TRIAL SETTINGS
# =====================
# -number of trials and blocks *
n_trials = 4
n_blocks = 2

# -stimulus names (and stimulus extensions, if images) *
stimulus_list = os.listdir(image_dir)

# -stimulus properties like size, orientation, location, duration *
horiz_mult = [-1, 1, 1, -1]
vert_mult = [1, 1, -1, -1]

# -start message text *
start_message = "Welcome to the experiment, Please press any key to start"

# =====================
# PREPARE CONDITION LISTS
# =====================
# -check if files to be used during the experiment (e.g., images) exist
pics = ["face" + str(f'{i:02}') + ".jpg" for i in range(1, 9)]
for image in pics:
    if image in stimulus_list:
        print(image + ' was found!')
    else:
        raise Exception(image + ' not found!')

# -create counterbalanced list of all conditions *
np.random.shuffle(stimulus_list)

# =====================
# PREPARE DATA COLLECTION LISTS
# =====================
# -create an empty list for correct responses (e.g., "on this trial, a response of X is
# correct") *
correct_responses = []
# -create an empty list for participant responses (e.g., "on this trial, response was a
# X") *
participant_response = []
# -create an empty list for response accuracy collection (e.g., "was participant
# correct?") *
accuracy_collection = []
# -create an empty list for response time collection *
response_time = []
# -create an empty list for recording the order of stimulus identities *
stimulus_identities = []
# -create an empty list for recording the order of stimulus properties *
stimulus_properties = []

# =====================
# CREATION OF WINDOW AND STIMULI
# =====================
# -define the monitor settings using psychopy functions
mon = monitors.Monitor('my_monitor', width=21, distance=35)
this_size = (1920,1080)

this_width = this_size[0]
this_height = this_size[1]

# -define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, fullscr=True, color=(-1, -1, -1))

# -define experiment start text using psychopy functions
start_text_stims = visual.TextStim(win, text=start_message)

# -define block (start)/end text using psychopy functions
str_block = "Next block will start"
block_sta_stims = visual.TextStim(win, text=str_block)

end_block = "End block"
block_end_stims = visual.TextStim(win, text=end_block)

end_trial = "End trial"
trial_end_stims = visual.TextStim(win, text=end_trial)

# -define stimuli using psychopy functions
fix_stims = visual.TextStim(win, text="+")
my_image = visual.ImageStim(win, units="pix")

# -make mouse pointer invisible
event.Mouse(visible=False)

# =====================
# START EXPERIMENT
# =====================
# -present start message text
start_text_stims.draw()
win.flip()
# -allow participant to begin experiment with button press
event.waitKeys()

# =============================
# BLOCK SEQUENCE (FRAME TIMING)
# =============================

# Single frame duration in seconds
refresh_rate = 1.0 / 144.0

fix_dur = 1.0  # 1 sec
image_dur = 2.0  # 2 sec
text_dur = 1.5  # 1.5 sec

# make sure each frame is a whole number
fix_frames = int(fix_dur / refresh_rate)
image_frames = int(image_dur / refresh_rate)
text_frames = int(text_dur / refresh_rate)

# the total number of frames to be presented on a trial
total_frames = int(fix_frames + image_frames + text_frames)

# -for loop for nBlocks *
for block in range(n_blocks):
    # -present block start message
    block_sta_stims.draw()
    win.flip()
    core.wait(1)
    # -randomize order of trials here *
    np.random.shuffle(stimulus_list)
    # =====================
    # TRIAL SEQUENCE
    # =====================
    # -for loop for nTrials *
    for trial in range(n_trials):
        # -set stimuli and stimulus properties for the current trial
        my_image.pos = (horiz_mult[trial] * this_width / 4,
                        vert_mult[trial] * this_height / 4)
        my_image.image = os.path.join(image_dir, stimulus_list[trial])

        # =====================
        # START TRIAL
        # =====================
        for frame_n in range(total_frames):  # for the whole trial...
            # -draw stimulus
            # number of frames for fixation
            if 0 <= frame_n <= fix_frames:
                fix_stims.draw()
                win.flip()
                if frame_n == fix_frames:  # last frame for the fixation
                    print("End fix frame = ", frame_n)  # print frame number

            # number of frame for image after fixation
            if fix_frames < frame_n <= (fix_frames + image_frames):
                my_image.draw()
                win.flip()
                if frame_n == (fix_frames + image_frames):  # last frame for the image
                    print("End image frame = ", frame_n)

            # number of frames for the final text stimulus
            if(fix_frames + image_frames) < frame_n < total_frames:
                trial_end_stims.draw()
                win.flip()
                if frame_n == (total_frames - 1):
                    print("End text frame =", frame_n)

"""Add a "dropped frame" detector to your script to find out whether your experiment is dropping frames. How many 
total frames are dropped in the experiment? If 20 or fewer frames are dropped in the whole experiment (1 frame per 
trial), keep frame-based timing in your experiment. Otherwise, switch back to the CountdownTimer. """
print("overall, %i frames were dropped" % win.nDroppedFrames)

"""Answer: The 'stdout' shows 0 frames were dropped. According to the criteria, the researcher can continue to use 
the frame timing method. """

block_end_stims.draw()
win.flip()
core.wait(.5)

# ======================
# END OF EXPERIMENT
# ======================
# -close window
win.close()
# -quit experiment
core.quit()
