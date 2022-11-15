# Platform pycharm win11

import os
import time
import numpy as np
from psychopy import visual, event, monitors, core

if __name__ == "__main__":
    print('Assignment 6 ----\n')

# =====================
# Question 1
# =====================

"""Write a short script that shows different face images from the image directory at 400x400 pixels in size. What 
does this do to the images? How can you keep the proper image dimensions and still change the size? """

"""Some figures will have been distorted in the fixed pixel condition (400,400). To resolve this problem, 
the researcher should normalize all picture resolution before conducting the Psychopy experiments. """

# image from https://www.boredpanda.com/objects-with-faces/?utm_source=google&utm_medium=organic&utm_campaign=organic

# init the directory
main_dir = os.getcwd()
image_dir = os.path.join(main_dir, 'images')
stims = os.listdir(image_dir)

# define the monitor and windows
mon = monitors.Monitor('my_monitor', width=21, distance=35)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, fullscr=True)

n_trials = 4
my_image = visual.ImageStim(win, units='pix', size=(400, 400))
np.random.shuffle(stims)

for trial in range(n_trials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image.draw()
    win.flip()
    event.waitKeys()

win.close()

# =====================
# Question 2
# =====================

"""Write a short script that makes one image appear at a time, each in a different quadrant of your screen (put the 
window in fullscreen mode). Think about how you can calculate window locations without using a trial-and-error 
method. """

print('Question 2 demo will start in 3 seconds ')
time.sleep(3)  # wait for 3 seconds

# Obtain the monitor info
this_size = mon.getSizePix()
this_width = this_size[0]
this_height = this_size[1]

# reinit the windows
win = visual.Window(monitor=mon, fullscr=True)
my_image = visual.ImageStim(win, units="pix")

horiz_mult = [-1, 1, 1, -1]
vert_mult = [1, 1, -1, -1]

for trial in range(n_trials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image.pos = (horiz_mult[trial] * this_width / 4,
                    vert_mult[trial] * this_height / 4)
    my_image.draw()
    win.flip()
    event.waitKeys()

win.close()

# =====================
# Question 3
# =====================

# Create a fixation cross stimulus (hint:text stimulus).
print('Question 3 demo will start in 3 seconds ')
time.sleep(3)  # wait for 3 seconds

# reinit the windows
win = visual.Window(monitor=mon, fullscr=True)

fix_text = visual.TextStim(win, text="+")
my_image = visual.ImageStim(win, units="pix")

for trial in range(n_trials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image.pos = (horiz_mult[trial] * this_width / 4,
                    vert_mult[trial] * this_height / 4)
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()

win.close()

# =====================
# Question 4
# =====================
# Fill in the following pseudocode with the real code you have learned so far:

print('Question 4 demo will start in 3 seconds ')
time.sleep(3)  # wait for 3 seconds

# =====================
# CREATION OF WINDOW AND STIMULI
# =====================
# reinit the windows
win = visual.Window(monitor=mon, fullscr=True)

# -define experiment start text using psychopy functions
start_msg = "Welcome to the experiment, Please press any key to start"
start_text = visual.TextStim(win, text=start_msg)
# -define block (start)/end text using psychopy functions
n_block = 2

block_start_text = "Next block"
block_end_text = "End block"

block_start = visual.TextStim(win, text=block_start_text)
block_end = visual.TextStim(win, text=block_end_text)

end_trail_text = "End the trial"
end_trial = visual.TextStim(win, text=end_trail_text)

# -define stimuli using psychopy functions (images, fixation cross)
main_dir = os.getcwd()
image_dir = os.path.join(main_dir, 'images')
stims = os.listdir(image_dir)

n_trials = 4
np.random.shuffle(stims)

fix_text = visual.TextStim(win, text="+")

# =====================
# START EXPERIMENT
# =====================
# -present start message text
start_text.draw()
win.flip()
# -allow participant to begin experiment with button press
event.waitKeys()

# =====================
# BLOCK SEQUENCE
# =====================
# -for loop for nBlocks
for block in range(n_block):
    # -present block start message
    block_start.draw()
    win.flip()
    event.waitKeys()
    # -randomize order of trials here
    np.random.shuffle(stims)
    # =====================
    # TRIAL SEQUENCE
    # =====================
    # -for loop for nTrials
    for trial in range(n_trials):
        # -set stimuli and stimulus properties for the current trial
        my_image = visual.ImageStim(win, units='pix', size=(400, 400))
        # =====================
        # START TRIAL
        # =====================
        # -draw fixation
        fix_text.draw()
        # -flip window
        win.flip()
        # -wait time (stimulus duration)
        core.wait(.5)
        # -draw image
        my_image.image = os.path.join(image_dir, stims[trial])
        my_image.draw()
        # -flip window
        win.flip()
        # -wait time (stimulus duration)
        core.wait(.5)
        # -draw end trial text
        end_trial.draw()
        # -flip window
        win.flip()
        # -wait time (stimulus duration)
        core.wait(.5)
# ======================
# END OF EXPERIMENT
# ======================
# - close window
win.close()
