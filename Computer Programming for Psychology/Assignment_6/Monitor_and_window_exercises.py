# Platform pycharm win11

from psychopy import event, visual, monitors

if __name__ == '__main__':
    print('Assignment 6 ----\n')

# How does changing "units" affect how you define your window size?
"""The 'units' parameter has several values: height, norm, deg, cm and pix. The researcher can fix the stimulus 
window sizes irrespective of the monitor. For all units, the centre of the screen is represented by coordinates (0,
0). Negative values mean down/left, and positive values mean up/right. The researcher can Use the height value to 
define the stimulus windows height. This unit can be helpful because it scales with window size. In normalized (
'norm') units, the window ranges in both x and y from -1 to +1. Moreover, use degrees of visual angle to set the size 
and location of the stimulus. Finally, the researcher may want to specify the size and location of the stimulus in 
pixels. The 'pix' values can work it. """

# How does changing colorSpace affect how you define the color of your window? Can you define colors by name?

"""Psychopy supports three different colour spaces: RGB, DKL and LMS. The researcher can use the three-digit numbers 
to define their desired colour in stimulus windows. However, the same number does not represent the same colour in 
the different spaces. For example, in RGB, the array [1,1,1] represents white and in HSV is red. Therefore, 
changing the colour space also can change the colour most of the time. Additionally, researchers can use hexadecimal 
string or natural language to define the colour, such as 'DarkSalmon' or '#00FF00'. """

# Fill in the following pseudocode with the real code you have learned so far:

# =====================
# CREATION OF WINDOW AND STIMULI
# =====================

# - define the monitor settings using psychopy functions
mon = monitors.Monitor('my_monitor', width=21, distance=35)
mon.setSizePix([1920, 1080])

# - define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size=(800, 600), color='#0F75E0', units='height', fullscr=True)
win.flip()
event.waitKeys()
win.close()
