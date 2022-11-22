# Platform pycharm win11
import os
import numpy as np
from psychopy import core, visual, monitors

if __name__ == '__main__':
    print('Assignment 7 ----\n')

# switch to the main workspace (global environment)
# image from https://www.boredpanda.com/objects-with-faces/?utm_source=google&utm_medium=organic&utm_campaign=organic
main_dir = os.getcwd()
image_dir = os.path.join(main_dir, 'images')
stims = os.listdir(image_dir)

# define the monitor
mon = monitors.Monitor('my_monitor', width=21, distance=35)
mon.setSizePix(mon.getSizePix())

"""Create a "wait_timer" to find out exactly how long core.wait(2) presents each image. Make sure this is not 
counting the time of the whole trial, but only the duration of each image. How precise is core.wait? """

"""Answer: According to the timer function, each image duration is 2 seconds, approximately. However, the exact time 
is more than 2 seconds, from 2.016 to 2.008. That means the "core. wait" method does not provide a precise showing 
time. """

# =====================
# Question 1
# =====================

# define the windows
win = visual.Window(monitor=mon, fullscr=False)

# define the number of trials and counterbalance the stim list
n_trials = 5
my_image = visual.ImageStim(win)
np.random.shuffle(stims)

# define a timer
wait_timer = core.Clock()

for trial in range(n_trials):
    wait_timer.reset()
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image.draw()
    win.flip()
    core.wait(2)
    print('Trial' + str(trial) + ' time =', wait_timer.getTime())

win.close()

"""Create a "clock_wait_timer" to find out exactly how long each image is presented when you use a clock + while 
loops. How precise is this? """

"""Answer: This time, each image duration is roughly two seconds and more precise than only applying the "core. wait" 
method. However, the range is 2.006 to 2.001, not exactly 2 seconds. """

# =====================
# Question 2
# =====================
print('------\nQuestion 2 demo will start\n------')
# define the windows
win = visual.Window(monitor=mon, fullscr=False)

# override the trials definition
n_trials = 5
my_image = visual.ImageStim(win)
np.random.shuffle(stims)

# define the timer
clock_wait_timer = core.Clock()
wait_timer = core.Clock()

for trial in range(n_trials):
    # set stimuli and stimulus properties for the current trial
    my_image.image = os.path.join(image_dir, stims[trial])
    clock_wait_timer.reset()
    # draw stimulus
    img_start_time = wait_timer.getTime()
    while clock_wait_timer.getTime() <= 2:
        my_image.draw()
        win.flip()
    img_end_time = wait_timer.getTime()

    print("Trial" + str(trial) + " image Duration was {} seconds".format(img_end_time - img_start_time))

win.close()

"""Create a "countdown_timer" to find out exactly how long each image is presented when you use a CountdownTimer + 
while loops. How precise is this? """

"""Answer: The counter-down timer precise is similar to the clock timer, ranging from 2.002 to 2.004. Also is not 
precisely an exact 2 seconds. """

# =====================
# Question 3
# =====================
print('------\nQuestion 3 demo will start\n------')

# define the windows
win = visual.Window(monitor=mon, fullscr=False)

# override the trials definition
n_trials = 4
my_image = visual.ImageStim(win)
np.random.shuffle(stims)

# define the timer
countdown_timer = core.CountdownTimer()
wait_timer = core.Clock()

for trial in range(n_trials):
    # set stimuli and stimulus properties for the current trial
    my_image.image = os.path.join(image_dir, stims[trial])
    countdown_timer.reset()
    countdown_timer.add(2)

    # draw stimulus
    img_start_time = wait_timer.getTime()
    while countdown_timer.getTime() > 0:
        my_image.draw()
        win.flip()
    img_end_time = wait_timer.getTime()

    print("Trial" + str(trial) + " image Duration was {} seconds".format(img_end_time - img_start_time))

win.close()
core.quit()
