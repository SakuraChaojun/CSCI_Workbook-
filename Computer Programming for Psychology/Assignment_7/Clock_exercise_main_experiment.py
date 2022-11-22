# Platform pycharm win11

# =====================
# IMPORT MODULES
# =====================
import os
import time
import numpy as np
from datetime import datetime
from psychopy import core, visual, monitors, gui, event

"""Edit your main experiment script so that the trials loop according to a clock timer. Also create and implement a 
block_timer and a trial_timer. """

if __name__ == '__main__':
    print('main_experiment ----\n')

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

# wait for 3 seconds
print('All variables have been created! Now ready to show the dialog box!')
time.sleep(3)

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
str_message = "Welcome to the experiment, Please press any key to start"

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
this_size = mon.getSizePix()
this_width = this_size[0]
this_height = this_size[1]

# -define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, fullscr=True, color=(-1, -1, -1))

# -define experiment start text using psychopy functions
start_text_stims = visual.TextStim(win, text=str_message)

# -define block (start)/end text using psychopy functions
str_block = "Next block will start"
block_sta_stims = visual.TextStim(win, text=str_block)
end_block = "End block"
block_end_stims = visual.TextStim(win, text=end_block)

# -define stimuli using psychopy functions
fix_stims = visual.TextStim(win, text="+")
my_image = visual.ImageStim(win, units="pix")

# -create response time clock
response_time_clock = core.Clock()

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

# =====================
# BLOCK SEQUENCE
# =====================
# define the timer
block_timer = core.Clock()
trial_timer = core.Clock()
wait_timer = core.Clock()
# -for loop for nBlocks *

for block in range(n_blocks):
    # -present block start message
    block_sta_stims.draw()
    win.flip()
    core.wait(1)
    # -randomize order of trials here *
    np.random.shuffle(stimulus_list)
    # -reset response time clock here
    block_timer.reset()
    block_start_time = block_timer.getTime()
    # =====================
    # TRIAL SEQUENCE
    # =====================
    # -for loop for nTrials *
    for trial in range(n_trials):
        # -set stimuli and stimulus properties for the current trial
        my_image.pos = (horiz_mult[trial] * this_width / 4,
                        vert_mult[trial] * this_height / 4)
        # TODO: -empty key presses

        # =====================
        # START TRIAL
        # =====================
        # -draw stimulus
        fix_stims.draw()
        # -flip window
        win.flip()
        my_image.image = os.path.join(image_dir, stimulus_list[trial])
        trial_timer.reset()
        # -wait time (stimulus duration)
        img_start_time = wait_timer.getTime()
        while trial_timer.getTime() <= 2:
            # -draw stimulus
            my_image.draw()
            win.flip()
        img_end_time = wait_timer.getTime()
        print("Trial" + str(trial) + " image Duration was {} seconds".format(img_end_time - img_start_time))

    block_end_time = block_timer.getTime()
    print("Block" + str(block) + "Duration was {} seconds".format(block_end_time - block_start_time))

block_end_stims.draw()
win.flip()
core.wait(.5)

# -collect subject response for that trial
# -collect subject response time for that trial
# -collect accuracy for that trial

# ======================
# END OF EXPERIMENT
# ======================
# -write data to a file
# -close window
win.close()
# -quit experiment
core.quit()
