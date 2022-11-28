# platform win 11, pycharm

import numpy as np
from psychopy import event, visual, monitors, core

if __name__ == "__main__":
    print("Assignment_8\n")

# define the monitors first (global variable)
mon = monitors.Monitor("my_monitor", width=21, distance=35)
mon.setSizePix(mon.getSizePix())

# =====================
# Question
# =====================

"""Instead of collecting key name, subject RT, subject accuracy, and correct responses in lists, create a dictionary 
containing those variables. Then, during response collection, append the data to the dictionary instead of filling 
lists. """

"""Keep in mind that you can pre-define dictionaries or lists for the whole experiment (in which case you have to use 
[block][trial] indexing to collect responses) or you can do it block-by-block (in which case you can use [trial] 
indexing). Create your lists (or dictionary, if you prefer) within the block loop and switch to [trial] indexing. """

# init the windows
win = visual.Window(monitor=mon, size=(400, 400), color=[-1, -1, -1])

n_blocks = 2
n_trails = 3
my_text = visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer()  # add countdown timer

# create problems and solutions to show
# write a list of simple arithmetic
math_problems = ['1+3=', '1+1=', '3-2=', '4-1=']
solutions = [4, 2, 1, 3]
prob_sol = list(zip(math_problems, solutions))

# Algorithm from lecture
sub_resp = dict()
sub_acc = dict()
prob = dict()
corr_resp = dict()
resp_time = dict()

for block in range(n_blocks):
    sub_resp[block] = [-1] * n_trails
    sub_acc[block] = [-1] * n_trails
    prob[block] = [-1] * n_trails
    corr_resp[block] = [-1] * n_trails
    resp_time[block] = [-1] * n_trails

    for trial in range(n_trails):
        # what problem will be shown and what is the correct response
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]

        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(2)

        event.clearEvents(eventType="keyboard")

        count = -1  # for counting keys
        while cd_timer.getTime() > 0:  # for 2 seconds
            my_text.text = prob[block][trial][0]  # present the problem for that trial
            my_text.draw()
            win.flip()

            # collect key presses after first flip
            keys = event.getKeys(keyList=['1', '2', '3', '4', 'escape'])

            if keys:
                count = count + 1  # count up the number of times a key is pressed

                if count == 0:  # if this is the first time a key is pressed
                    #  get RT for first response in the loop
                    resp_time[block][trial] = rt_clock.getTime()
                    # get key for only the first response in the loop
                    sub_resp[block][trial] = keys[0]  # remove from the list

            # record subject accuracy
            # correct remembers keys are saved as Strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1  # arbitrary number for accurate response
            # incorrect remembers keys are saved as Strings
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2  # arbitrary number for inaccurate response
            # should be something other than 0 to distinguish from non responses

        # print results
        print("problem =", prob[block][trial], "correct response = ",
              corr_resp[block][trial], "subject response = ", sub_resp[block][trial],
              "subject accuracy = ", sub_acc[block][trial])

print(sub_resp)
print(sub_acc)
print(prob)
print(corr_resp)
print(resp_time)

# quit demo
win.close()
core.quit()
