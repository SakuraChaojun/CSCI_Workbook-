### Final Project

---

#### Introduction

The main idea of this experiment is to explore the participant's visual search performance in the triangle shape. This experiment is a classic search task for a target among some number of distractors. The response time (RT, reaction time) increases roughly linearly with the number of shapes shown. However, locating the target presence objects and target absence objects is not exhibit the same performance (Wolfe, 2020). This experiment examined the participant's performance in the two groups: Group 1: locate the target-presence objects; group 2: locate the target-absence objects. 

<div class='imabox'>
   <img src = https://github.com/SakuraChaojun/selected-courses/blob/main/Computer%20Programming%20for%20Psychology/project/images/condition_2.png style="width:300px"> <img src = https://github.com/SakuraChaojun/selected-courses/blob/main/Computer%20Programming%20for%20Psychology/project/images/condition_4.png style="width:300px">
</div>

---

#### Methods [Project main code](https://github.com/SakuraChaojun/selected-courses/blob/main/Computer%20Programming%20for%20Psychology/project/project_505.py)
The experiment only has two blocks for demonstration, and each block has four trials. Participants need to locate the target shape as soon as possible. Press 'Q' means they found the target shape and 'P' for not. The odd number block is the target shape that appears, and the even number block is the target shape that disappears. The stimulus will not refresh until the participants press the keyboard. The fixation time is about 0.25 seconds. 

In each trial, the shape, position and number are random, but the size and orientation are fixed. 

<div class='imabox'>
   <img src = https://github.com/SakuraChaojun/selected-courses/blob/main/Computer%20Programming%20for%20Psychology/project/images/condition_1_demo.gif style="width:300px"> <img src = https://github.com/SakuraChaojun/selected-courses/blob/main/Computer%20Programming%20for%20Psychology/project/images/condition_2_demo.gif style="width:300px">
</div>

```
for blocks in range(n_blocks):
    //Each block round appears different conditions
    if blocks % 2 == 0:
        alltrials = alltrials1  # condition 1
    elif blocks % 2 != 0:
        alltrials = alltrials2  # condition 2 `
```

---

#### Results

The experiment records the participant's response and the corresponding time. The standard output includes the number of blocks and trials, this trial type (whether the target appears or not) and, accuracies, response time. [Example of output files, click here](https://github.com/SakuraChaojun/selected-courses/blob/main/Computer%20Programming%20for%20Psychology/project/dataFiles/505_outputFile.csv).Before the experiment starts, a dialogue box will pop up and require the participant to fill up the personal information. The file name will be generated basis on the participant input. 

 <div class='imabox'>
   <img src = https://github.com/SakuraChaojun/selected-courses/blob/main/Computer%20Programming%20for%20Psychology/project/images/project_1.png style="width:300px"> <img src = https://github.com/SakuraChaojun/selected-courses/blob/main/Computer%20Programming%20for%20Psychology/project/images/output_1.png style="width:300px">
</div>

---

#### Data Analysis [Data Analysis Code](https://github.com/SakuraChaojun/selected-courses/blob/main/Computer%20Programming%20for%20Psychology/project/project_505_data_analysis.py)

In order to show the saved data file, the program conducts a brief [exploratory data analysis](https://sakurachaojun.github.io/PSYO3505/data/EDA.html). (Although this part may be beyond the course scope). First, the program converts the format to the millisecond and then plots the histogram to show the data distribution. Next, the program operated the data frame to generate the table showing different conditions' mean reaction time. The results suggest that locating the target-appear shape is fast than the target-disappear shape, even though the sample is small. 

 <div class='imabox'>
   <img src = https://github.com/SakuraChaojun/selected-courses/blob/main/Computer%20Programming%20for%20Psychology/project/data_images/Figure_1.png style="width:300px"> <img src = https://github.com/SakuraChaojun/selected-courses/blob/main/Computer%20Programming%20for%20Psychology/project/data_images/Figure_3.png style="width:300px">
</div>

---

#### References 
1. Background article:[Jeremy M.](https://search.bwh.harvard.edu/new/pubs/Wolfe2020_VisualSearch_annurev-vision.pdf)
2. The code framework (skeleton): [Reshanne Reeder](https://kylemath.github.io/pytutorial/level3.html)
3. The code algorithms of stimulus presentation: [AhaOlaDad](https://zhuanlan.zhihu.com/p/143266583)
4. The code algorithms of recording data: [Kyle Mathewson](https://kerblooee.github.io/pytutorial/level6.html)
5. Exploratory data analysis techniques: [Chaojun Ma](https://sakurachaojun.github.io/PSYO3505/data/EDA.html)
6. Course assignment 8: [homework](https://github.com/SakuraChaojun/selected-courses/tree/main/Computer%20Programming%20for%20Psychology/Assignment_8)

---

Thank you 




