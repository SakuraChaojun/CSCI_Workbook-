# platform win 11, pycharm
from psychopy import event, visual, monitors, core

if __name__ == "__main__":
    print("Assignment_8\n")

# define the monitors first (global variable)
mon = monitors.Monitor('my_monitor', width=21, distance=35)
mon.setSizePix(mon.getSizePix())

# =====================
# Question
# =====================

"""event.getKeys is prone to collect as many responses as you can make in a trial, but often times you only want to 
collect one response for a trial. Come up with a solution so that only a single response is recorded from 
event.getKeys (e.g., ignoring all responses after the first response). Hint: one solution is used somewhere else in 
level6. """

print("Question 1 demo will start")
# init the windows
win = visual.Window(monitor=mon, size=(400, 400), color=[-1, -1, 1])

n_trials = 5
my_text = visual.TextStim(win)
fix = visual.TextStim(win, text='+')
sub_resp = []

for trial in range(n_trials):
    my_text.text = "trial %i" % trial  # insert integer into the string with %i

    fix.draw()
    win.flip()
    core.wait(2)
    event.clearEvents(eventType="keyboard")

    my_text.draw()
    win.flip()
    core.wait(1)

    keys = event.getKeys()  # put get keys HERE

    print("keys that were pressed", keys)  # which keys were pressed

    if keys:
        sub_resp = keys[0]  # only take first response

    print("response that was counted", sub_resp)

# event.clearEvents(eventType="keyboard")
"""Answer: Put the "clear event" statement outside the trial loop, and the program will collect all responses from 
the participant, even in the fixation scenario. We don't want to collect the response during "fixation time,
" so putting the statement within the trial loop will resolve the problem. The output only includes the "trial 
scenario" instead of all experiments. """

"""Statement placement in your script is very important when collecting responses and refreshing key-presses. What 
happens if you put event.ClearEvents within the trial loop instead of outside the trial loop? What happens if you 
un-indent the "if keys:" line? """

"""Answer: Suppose I un-indent the if line. The following block will never execute. Hence the 'keys' variable is the 
local variable, and after the for loop, the value will be clear away. """

# if keys:
#      sub_resp = keys[0]  # only take first response
#
# print("response that was counted", sub_resp)

# close the windows
win.close()
# quit the demo
core.quit()
