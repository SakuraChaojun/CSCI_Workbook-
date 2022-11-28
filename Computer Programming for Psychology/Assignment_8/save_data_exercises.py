# platform win 11, pycharm
import csv
import os
import numpy as np
from psychopy import event, visual, monitors, core

if __name__ == "__main__":
    print("Assignment_8\n")

# define the monitors first (global variable)
mon = monitors.Monitor('my_monitor', width=21, distance=35)
mon.setSizePix(mon.getSizePix())

main_dir = os.getcwd()
data_dir = os.path.join(main_dir, 'data', 'save_csv_example.csv')
# =====================
# Question
# =====================

"""Using csv.DictWriter (use your favorite search engine to find the help page), save your dictionary (that you 
created above) as a .csv file. """

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

data_as_dict = [prob, corr_resp, sub_resp, sub_acc, resp_time]

try:
    with open(data_dir, mode='w', newline='') as csvfile:  # "sub_data" is arbitrary, but stay consistent
        field_names = ['Block', 'Trial', 'prob', 'Subject_response', 'Response_time', 'Subject_accuracy']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writeheader()
        for num_block in range(n_blocks):
            for num_trial in range(n_trails):
                writer.writerow({'Block': num_block, 'Trial': num_trial,
                                 'prob': prob[num_block][num_trial],
                                 'Subject_response': sub_resp[num_block][num_trial],
                                 'Response_time': resp_time[num_block][num_trial],
                                 'Subject_accuracy': sub_acc[num_block][num_trial]})

        print("Successfully write the file !")

except IOError as e:
    print("IOError", e)

# quit demo
win.close()
core.quit()
