import os
import numpy as np
from psychopy import core,event,visual,monitors

#=====================
#START TRIAL

#switch to the workspace
main_dir = os.getcwd()
image_dir = os.path.join(main_dir,"images")
stims = os.listdir(image_dir)
np.random.shuffle(stims)
print(stims)

#define the monitor and windows
mon = monitors.Monitor("my_monitor", width=21, distance=35)
mon.setSizePix(mon.getSizePix())
win = visual.Window(monitor=mon,fullscr=True)

#-draw fixation
fix_text = visual.TextStim(win, text="+")
fix_text.draw()
#-flip window
win.flip()
#-wait time (stimulus duration)
core.wait(1)

#-draw image
my_image = visual.ImageStim(win,units="pix")
my_image.image = os.path.join(image_dir,stims[0])
my_image.draw()
#-flip window
win.flip()
#-wait time (stimulus duration)
core.wait(1)

#-draw end trial text
end_trial = "END TRIAL"
end_text = visual.TextStim(win,text = end_trial)
end_text.draw()
#-flip window
win.flip()
#-wait time (stimulus duration)
core.wait(1)

win.close()
core.quit()
