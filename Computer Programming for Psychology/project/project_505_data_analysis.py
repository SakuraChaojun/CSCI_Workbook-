# Platform pycharm win 11
# Prepare for Project 505

"""introductory comments:
Name of the file: project_505.py, project_505_data_analysis.py
Name: Chaojun M.

Explanation of what your experiment does:
This experiment tests the participant's visual search task performance. There are two
conditions: one needs the participant to find the triangle with the line in the several triangle shapes. Another
condition requires the participant to find the triangle without the line in the several triangle shapes.

Explanation of why your experiment: We want to know how fast the participant can locate the unique shape (i.e. unique
triangle) in the 'normal' triangle background.

"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("project demo 2 \n")

# ======================
# Example saved file
# ======================
# read the data from the path
main_dir = os.getcwd()
data_dir = os.path.join(main_dir, 'dataFiles', '505_outputFile.csv')
# generate the dataframe
df = pd.read_csv(data_dir)

# The script should print the entire dataframe
print(df)

print('----')

# convert to milliseconds
df['Response Time'] = df['Response Time'] * 1000
print(df)
print('----')

# describe the data
print(df['Response Time'].describe())
print('----')

# plot the graph
df['Response Time'].plot(kind='hist')

# add a solid line at the median and dashed lines at the 25th and 75th percentiles (done for you)
plt.axvline(df['Response Time'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['Response Time'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['Response Time'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

plt.show()

# group the mean
rt_mean = df.groupby(by='Block Number').agg('mean')
print(rt_mean)

