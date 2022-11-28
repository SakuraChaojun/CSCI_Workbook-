# platform win 11, pycharm

import os
import pandas as pd

if __name__ == "__main__":
    print("Assignment 8\n")

# =====================
# Question 1
# =====================

print("Question 1\n")

"""Create a short "read and analysis" script that loads a saved JSON file, performs rudimentary analyses on the data, 
and prints the means. """

file_name = 'save_json_example_block0.txt'
main_dir = os.getcwd()
data_dir = os.path.join(main_dir, "data", file_name)

df = pd.read_json(data_dir)

print("correct response mean: " + str((sum(df['corr_resp']) / len(df['corr_resp']))))
print("subject response mean: " + str((sum(df['sub_resp']) / len(df['sub_resp']))))
print("subject accuracy mean: " + str((sum(df['sub_acc']) / len(df['sub_acc']))))
print("response time mean: " + str((sum(df['resp_time']) / len(df['resp_time']))))

print("------")

# =====================
# Question 2
# =====================

print("Question 2\n")

"""Change your "read and analysis" script so that RTs for inaccurate responses are removed from analysis."""

# reload df
print("origin dataframe")
df = pd.read_json(data_dir)
print(df)

print("\nRTs for inaccurate responses are removed")
acc_trials = df.loc[df['sub_acc'] == 1]  # show only trials on which subject was correct
print(acc_trials)

print("------")

# =====================
# Question 3
# =====================
print("Question 3\n")

"""Change your "read and analysis" script so that any trials without a response (0 value) are removed from analysis."""

# reload df
print("origin dataframe")
df = pd.read_json(data_dir)
print(df)

print("\nwithout a response are removed")
without_response = df.loc[df['sub_resp'] != 0]
print(without_response)
