# Platform pycharm win11

import time
from psychopy import gui
from datetime import datetime

if __name__ == '__main__':
    print('Assignment 6 ----\n')

# =====================
# COLLECT PARTICIPANT INFO
# =====================

# -create a dialogue box that will collect current participant number, age, gender, handedness
# Edit the dictionary "exp_info" so you have a variable called "session", with "1" preset as the session number.

exp_info = {'session': 1,
            'subject_nr': 0,
            'age': 0,
            'handedness': ('right', 'left', 'ambi'),
            'gender': ''
            }

# Tell your experiment to print "All variables have been created!
# Now ready to show the dialog box!". Then, show the dialog box.

print('All variables have been created! Now ready to show the dialog box!')
time.sleep(3)  # wait for 3 seconds

# Customize my_dlg so that you have a title for your dialog box: "subject info".
# Set the order of the variables as session, subject_nr, age, gender, handedness.

# TODO: answer the question :
# If passing the value for the 'session' is fixed, the session field cannot change and keep the number 1 all the time.
# Set the variable "session" as fixed. What happens?

my_dlg = gui.DlgFromDict(dictionary=exp_info, title='subject info',  # fixed=['session'],
                         order=['session', 'subject_nr', 'age', 'gender', 'handedness'])

# get date and time
date = datetime.now()
# what time is it right now?
print(date)

# -create a unique filename for the data
exp_info['date'] = str(date.day) + str(date.month) + str(date.year)
file_name = str(exp_info['date']) + '-' + str(exp_info['subject_nr'])
print(file_name)
