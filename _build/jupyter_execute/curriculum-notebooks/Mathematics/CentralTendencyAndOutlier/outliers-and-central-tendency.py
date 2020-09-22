![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/CentralTendencyAndOutlier/outliers-and-central-tendency.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

%%html

<script>
  function code_toggle() {
    if (code_shown){
      $('div.input').hide('500');
      $('#toggleButton').val('Show Code')
    } else {
      $('div.input').show('500');
      $('#toggleButton').val('Hide Code')
    }
    code_shown = !code_shown
  }

  $( document ).ready(function(){
    code_shown=false;
    $('div.input').hide()
  });
</script>
<p> Code is hidden for ease of viewing. Click the Show/Hide button to see. </>
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from ipywidgets import interact, widgets, Button, Layout
from scipy import stats
from collections import Counter
from array import array
from statistics import mode
import IPython
import pandas
import sys
from astropy.table import Table
import tkinter
import csv
import pandas as pd
from pandas import DataFrame

def display(question, answerList):
    print(question)
    IPython.display.display(answerList)

# Central Tendency and Outliers

This notebook focuses on what an outlier is and how it affects central tendency. Remember central tendency means the mean, median, and mode of some data. If you need review on central tendency, check out this previous notebook.

Things you will learn in this notebook:
* What an outlier is
* How an outlier affects mean
* How an outlier affects median
* How an outlier affects mode
* Why outliers can be a problem

<img style="float: right;" src="images/PunnyOutlier.jpg" width="400" height="300">

## What is an outlier?

An outlier is a value that "lies outside" (is much smaller or larger than) most of the other values in a set of data.

Let's look at an example: <br>
Here is a data set: $26, 23, 27, 25, 28, 29, 24, 99 $ <br>
Lets put it in order: $23, 24, 25, 26, 27, 28, 29, 99$ <br> 
$99$ is larger than all the other data, by a lot. <br> 
Therefore, we can call $99$ an outlier.

An outlier is also data that is out of place, or that might be a mistake when it was collected.

## Central tendency

First let's look at the central tendency of the example above. 

Mean = $\frac{23+24+25+26+27+28+29+99}{8} = \frac{281}{8} = 35.125$. <br>
The median is found between 26 and 27, so the median is 26.5. <br>
There is no mode because none are repeated more than once.

Then we will remove the outlier (99) and recalculate the central tendency.

Mean = $\frac{23+24+25+26+27+28+29}{7} = \frac{182}{7} = 26$. <br>
The median is the middle number so the median is 26. <br>
There is no mode because none are repeated more than once.

What changes do you notice? What changed the most?

### Try it yourself

Here are the ratings of a new restaurant out of 10:

$4.5, 7, 15, 3.5, 6, 5, 9, 10, 1$

answer622 = widgets.RadioButtons(options=['Yes', 'No'], value = None)
answernext = widgets.RadioButtons(options=['1', '10', '15', '-1'], value = None)

question622 = 'Is there an outlier?'
questionnext = 'Which value is the outlier?'

def checknext(d):
    IPython.display.clear_output(wait=False)
    display(question622, answer622)
    display(questionnext, answernext)
    if answernext.value == '15':
        print("You're right! 15 is an outlier because the ratings are only supposed to be out of 10.")
    else:
        print("Not quite, try again.")


def check622(d):
    IPython.display.clear_output(wait=False)
    display(question622, answer622)
    if answer622.value == 'Yes':
        print("Correct!")
    else:
        print("Actually there is an outlier.")
    display(questionnext, answernext)
    answernext.observe(checknext, 'value')
        
IPython.display.clear_output(wait=False)
display(question622,answer622 )
answer622.observe(check622, 'value')

%%html
<html>
<head>
<script type="text/javascript">
<!--
function toggle(id) {
var e = document.getElementById(id);
if(e.style.display == 'none')
e.style.display = 'block';
else
e.style.display = 'none';
}
//-->
</script>
</head>

<body>
<div id="question622">
 <button id = "622"
onclick="toggle('answer622');">Solution</button> 
</div>
<div style="display:none" id="answer622">
An outlier is a value that does not seem to fit with the rest of the data. <br/>
In this case, we are looking at ratings that should be between 0 and 10. <br/>
All the values in this data set are within that range except for 15. <br/>
So 15 must be the outlier. <br/>

Also -1 would be an outlier if it was in the data set, but because it's not then it's not the right answer. <br/>

</div>

</body>
</html>

## A bigger set of data

Let's look at some data about the sodium content (amount of salt) in different common foods. Is there an outlier?

<img style="float: center;" src="images/walking-food.jpg" width="500" height="200">

df = pd.read_csv('sources/exampleDataSource.csv')
print(df)

OriginalData = []
with open('sources/exampleData.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        OriginalData.append(int(row[1]))

Now let's calculate the mean, median, and mode using the computer.

def computeCenTendency(dataset):
    
    #mean value
    mean= np.mean(dataset)
    print("Mean: ", round(mean,3))

    #median value
    # First we need to sort the data in ascending order
    dataset.sort()
    median = np.median(dataset)
    print("Median: ", round(median,3))
    
    # Mode
    hits = []
    for item in dataset:
        tally = dataset.count(item)
        #Makes a tuple that is the number of huts paired with the relevant number
        values = (tally, item)
        # Only add one entry for each number in the set
        if values not in hits:
            hits.append(values)
    hits.sort(reverse=True)
    if hits[0][0]>hits[1][0]:
        print("Mode:", round(hits[0][1],3), "(appeared", hits[0][0], "times.)")
    else:
        print("There is no mode")

    Counter(dataset)
    return mean, median, hits[0][1]

centralTendency = []
centralTendency = computeCenTendency(OriginalData)

Now let's show this data in a graph. But not just any graph. We will display it in a histogram. This way we can group together foods that have a similar sodium content into "bins". You can control how many bins are on the graph by using the slider below. Look how the graph changes.

Can you tell if there's an outlier when there's only a couple bins? How about when there's a lot of bins?

def plotHistogram(x_values, num_bins, xLabel, yLabel, histTitle):
    n, bins, patches = plt.hist(x_values, num_bins, facecolor='blue', alpha=0.5)

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(histTitle)
    plt.show()
    
def callPlottingFunction(num_bins):
    print("Generating... plot for :", num_bins)
    #n, bins, patches = plt.hist(data, num_bins, facecolor='blue', alpha=0.5)
    #plt.xlabel('Numberof values')
    #plt.ylabel('Sodium Content')
    #plt.title('Histogram of 30 products in Australian supermarkets')
    #plt.show()
    plotHistogram(OriginalData, num_bins , 'Sodium Content', 'values', 'Histogram of 30 products in Australian supermarkets')

interact(callPlottingFunction, num_bins=widgets.IntSlider(min=0,max=100,step=1,value=50));

When there are a lot of bins, it's really easy to see that there's an outlier. If we look at the data, we know that's soy sauce. So let's remove it and see how the central tendency is affected.

dataWithoutOutlier = []
with open('sources/exampleData_NoOutlier.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        dataWithoutOutlier.append(int(row[1]))
#print("Sodium content read from the file: ", dataWithoutOutlier)

centralTendencyWithoutOutlier = []
centralTendencyWithoutOutlier = computeCenTendency(dataWithoutOutlier)

def callPlottingFunctionNoOutlier(num_bins):
    print("Generating... plot for :", num_bins)
    plotHistogram(dataWithoutOutlier, num_bins , 'Sodium Content', 'values', 'Histogram of 30 products in Australian supermarkets')

interact(callPlottingFunctionNoOutlier, num_bins=widgets.IntSlider(min=0,max=100,step=1,value=50));

Should soy sauce be excluded though? It is a common food that many people own, so it's not out of place in the data. It's just very salty.

**An outlier should really be out of place in your data set, not just a large or small value.**

-------

#### Now try adding your own data points into this set. 

Try adding really big and/or really small numbers. You can also add many repeating numbers to change the mode. <br>
**Restart**: press to remove all your outliers to start again.<br>
**Add Outlier**: press to add a new outlier. You can add as many as you want. (value has to be less than 10,000) <br>
**Compute**: press to calculate the central tendency and see a histogram of the dataset with your outlier(s).<br>
**Compare**: press to see the central tendency before and after your outliers are added. How do your outliers change the central tendency?

global datasetWithOutlier
global centralTendencyWithOutlier
datasetWithOutlier = dataWithoutOutlier.copy()

add = widgets.Button(description='Add Outlier',disabled=False,button_style='')
remove = widgets.Button(description='Restart',disabled=False,button_style='')
outlier = widgets.BoundedIntText(value=None,max=10000,description='Outlier:',disabled=False)
compute = widgets.Button(description='Calculate',disabled=False,button_style='')
compare = widgets.Button(description='Compare',disabled=False,button_style='')

def displayButtons():
    IPython.display.clear_output()
    IPython.display.display(remove)
    IPython.display.display(add)
    IPython.display.display(compute)
    IPython.display.display(compare)

def addOutlier(a):
    global datasetWithOutlier
    IPython.display.clear_output()
    IPython.display.display(remove)
    IPython.display.display(add)
    IPython.display.display(outlier)
    IPython.display.display(compute)
    IPython.display.display(compare)
    datasetWithOutlier.append(outlier.value)
    print("Current Dataset:")
    print(datasetWithOutlier)

def showOutlier(a):
    IPython.display.clear_output()
    IPython.display.display(remove)
    IPython.display.display(add)
    IPython.display.display(outlier)
    IPython.display.display(compute)
    IPython.display.display(compare)
    outlier.observe(addOutlier, 'value')
    print("Current Dataset:")
    print(datasetWithOutlier)
    
def reset(a):
    displayButtons()
    datasetWithOutlier = dataWithoutOutlier.copy()
    print("Current Dataset:")
    print(datasetWithOutlier)
    
def callPlottingFunctionWithOutlier(num_bins):
    print("Generating... plot for :", num_bins)
    plotHistogram(datasetWithOutlier, num_bins, 'Sodium Content', 'values', 'Histogram with Outliers')

def calculate(a):
    global centralTendencyWithOutlier
    centralTendencyWithOutlier = computeCenTendency(datasetWithOutlier)
    print(centralTendencyWithOutlier)
    interact(callPlottingFunctionWithOutlier, num_bins=widgets.IntSlider(min=0,max=100,step=1,value=50));
    
def compareTendencies(a):
    centralTendencyWithoutOutlierArray = np.around(np.asarray(centralTendencyWithoutOutlier), 3)
    centralTendencyWithOutlierArray = np.around(np.asarray(centralTendencyWithOutlier), 3) 
    arr = { 'Central Tendency ':  np.array(['Mean','Median','Mode' ]),
            'Before adding outlier ':  np.array([centralTendencyWithoutOutlierArray[0],  centralTendencyWithoutOutlierArray[1], 
                                            centralTendencyWithoutOutlierArray[2] ]),
            'After adding outlier ': np.array([centralTendencyWithOutlierArray[0], centralTendencyWithOutlierArray[1],
                                           centralTendencyWithOutlierArray[2]])}
    print(Table(arr))
    

displayButtons()
print("Current Dataset:")
print(datasetWithOutlier)
compare.on_click(compareTendencies)
compute.on_click(calculate)
add.on_click(showOutlier)
remove.on_click(reset)


### Effects of Outliers 

##### Mean
From the above results and histogram, we see that adding outliers can change the mean dramatically.<br>
This is because we need to add all the values to determine the mean value.<br>
Outliers are often values that are much larger or smaller than the other values.<br>
When we add these values to the sum, the average can change a lot.

##### Median
For the median, we need to consider the middle number(s).<br>
Adding one outlier adds a single point at the far end of our data set, so everything else shifts over only one spot. <br>
The median might change or might not.

##### Mode
The mode is very unlikely to change, because mode is the most repeated value.<br>
Unless you add many outliers, all with the same value, the mode probably won't change.<br>
And if there are multiple outliers with the same value, then maybe they should be kept in the dataset, they might be important.


### What should we use to represent data?

<img style="float: right;" src="images/median-over-mean.jpg" width="350" height="200">

The reason we use central tendency is to tell important information about the data set we want to talk about. We want to know what this data is like without saying every value in the set. Usually mean is used to represent data as it is affected by all points, but that's not always a good thing. If there's an outlier in the data, maybe mean is not the best way to represent the middle of the data in general. Median might be a more truthful representation of the middle in that case. 

In the food data, we might want to represent how much sodium is in food we eat nearly every day. If we don't eat soy sauce often, then it would be an outlier. Then the mean will tell us we eat a lot more sodium every day than the median would tell us. If we use the mean to represent this data, someone could argue that we eat too much sodium. But its not true since we don't eat it often. So if we use the median to represent this data, we can still include soy sauce in the data, but it would represent what we eat more truthfully.

-------------- 

## Test yourself 

### Question 1

The Purple Tornadoes played 8 games this season and these are their scores.<br>
15, 10, 18, 11, 1, 18, 25, 12

answer642 = widgets.RadioButtons(options=['25 and 18', '1', '25 and 1', '1 and 10', '25', 'None of these'],
                             value = None,  description='Choices:')

question642 = "Which of these values could be outliers?"

def check642(g):
    IPython.display.clear_output(wait=False)
    display(question642, answer642)
    if answer642.value == '25 and 1':
        print("That's right!")
    else:
        print("Not quite. Try again.")

IPython.display.clear_output(wait=False)
display(question642, answer642)
answer642.observe(check642, 'value')

%%html
<html>
<head>
<script type="text/javascript">
<!--
function toggle(id) {
var e = document.getElementById(id);
if(e.style.display == 'none')
e.style.display = 'block';
else
e.style.display = 'none';
}
//-->
</script>
</head>

<body>
<div id="question642">
 <button id = "642"
onclick="toggle('answer642');">Solution</button> 
</div>
<div style="display:none" id="answer642">
Outliers are values which are much bigger or smaller than the rest of the data.<br />
Since there is only one value in the 20s, which is 25, that might be an outlier.<br/>
Also there is only one value less than 10, which is 1, so that might also be an outlier.<br/>

Everything else is pretty close together.<br>
<br>
We do not know for sure if these are real outliers, but they could be, so we call them potential outliers. <br>

</div>

</body>
</html>

### Question 2

Sam's class recorded the height of 10 the students in the class in centimeters. This is the data they got:<br>
120, 125, 133, 146, 180, 152, 154, 138, 122, 140<br>
The current mean height of these 10 students is 141 cm.<br>
The current median height is 139 cm. <br>

question611 = " If we say that 180 cm is an outlier, what will happen to the central tendency?"
answer611 = widgets.RadioButtons(options=['mean will increase', 'median will stay the same', 'mean will decrease', 'None of the above'],
                             value= None, description='Choices:')


def checkAnswer(a):
    IPython.display.clear_output(wait=False)
    display(question611, answer611)
    if answer611.value == 'mean will decrease':
        print("Correct Answer!")
    else:
        print("Sorry, that's not right! Try again.")

display(question611, answer611)

answer611.observe(checkAnswer, 'value')

%%HTML
<html>
<head>
<script type="text/javascript">

<!--
function toggle(id) {
var e = document.getElementById(id);
if(e.style.display == 'none')
e.style.display = 'block';
else
e.style.display = 'none';
}
//-->
</script>
</head>

<body>
<div id="question611">
 <button id = "611"
onclick="toggle('answer611');">Solution</button> 
</div>
<div style="display:none" id="answer611">
Since we are saying that the outlier is 180 cm and that is larger than the rest of the data, the mean will decrease.  <br/>
If the outlier was smaller than the rest of the data, the mean would increase. <br/>
<br/>
Since there was 10 values, the median was the average between the 5th and 6th values when the list is sorted. <br/>
But if we remove one value, then the median will become the 5th value which is smaller than the average of the 5th and 6th values. <br/>
This is only because those 2 values are not the same number, or else the median would stay the same.


</div>

</body>
</html>

### Question 3

A teacher collected the grades of one test and these are the results:
100, 78, 98, 78, 78, 75, 55, 86, 100.

Also 4 students missed the test so they got a grade of zero.

question612 = " What is the mode grade for all the students in the test? "

answer612 = widgets.RadioButtons(options=['78', '100', '0', '78 and 100', 'There is none'],
                              value = None, description='Choices:')

def check612(b):
    IPython.display.clear_output(wait=False)
    display(question612, answer612)
    if answer612.value == '0':
        print("That's right!")
    else:
         print("Sorry, that's not right, try again. Don't forget the mode is the value that repeats the most.")

IPython.display.clear_output(wait=False)
display(question612, answer612)
answer612.observe(check612, 'value')

%%html
<html>
<head>
<script type="text/javascript">
<!--
function toggle(id) {
var e = document.getElementById(id);
if(e.style.display == 'none')
e.style.display = 'block';
else
e.style.display = 'none';
}
//-->
</script>
</head>

<body>
<div id="question612">
 <button id = "612"
onclick="toggle('answer612');">Solution</button> 
</div>
<div style="display:none" id="answer612">
Since there is 3 78s, you might think that 78 would be the mode. <br/>
But we are also counting the 4 studetns who got a zero. <br/>
Therefore theres 4 zeros in the dataset, so the mode is 0. <br/>


</div>

</body>
</html>

answer613 = widgets.RadioButtons(options=['Yes, to 100', 'Yes, to 78', 'Yes, to 0', 'No, it stays the same'],
                             value =None, description='Choices:')

question613 = "If we don't count the students who missed the test, does the mode change? If so, to what?"

def check613(e):
    IPython.display.clear_output(wait=False)
    display(question613, answer613)
    if answer613.value == 'Yes, to 78':
        print("You are correct!")
    else:
        print("Not quite, Try again.")
        
IPython.display.clear_output(wait=False)
display(question613, answer613)
answer613.observe(check613, 'value')

%%html
<html>
<head>
<script type="text/javascript">
<!--
function toggle(id) {
var e = document.getElementById(id);
if(e.style.display == 'none')
e.style.display = 'block';
else
e.style.display = 'none';
}
//-->
</script>
</head>

<body>
<div id="question613">
 <button id = "613"
onclick="toggle('answer613');">Solution</button> 
</div>
<div style="display:none" id="answer613">

When we remove the students who missed the test, since they made the mode 0, the mode will definitely change. <br />
Since there is 3 78s and only 2 100s, the new mode will be 78. <br/>
If there were 3 100s, then the mode would change to 78 and 100.

</div>

</body>
</html>

### Extra Hard Question

A student has gotten the following marks on his tests: 87, 95, 76, and 88. He wants a mean that is at least 85 and only has one more test.

answer631 = widgets.RadioButtons(options=['60', '70', '80', '90'],
                             value =None, description='Choices:')

question631 = "What is the minimum mark he must get on the last test in order to achieve that average?"

def check631(e):
    IPython.display.clear_output(wait=False)
    display(question631, answer631)
    if answer631.value == '80':
        print("Correct Answer!")
    else:
        print("Wrong answer! Try again.")
        
IPython.display.clear_output(wait=False)
display(question631, answer631)
answer631.observe(check631, 'value')

%%html
<html>
<head>
<script type="text/javascript">
<!--
function toggle(id) {
var e = document.getElementById(id);
if(e.style.display == 'none')
e.style.display = 'block';
else
e.style.display = 'none';
}
//-->
</script>
</head>

<body>
<div id="question631">
 <button id = "631"
onclick="toggle('answer631');">Solution</button> 
</div>
<div style="display:none" id="answer631">
To find which mark he needs, we can just try these 4 numbers and see how the mean changes.</br>
First, if he got 60 on the last test, his new mean would be:</br>
(87 + 95 + 76 + 88 + 60) ÷ 5 = 81.2 </br>
Getting a 60 would mean he finished with an average of 81.2, so he needs something higher than that.</br>
Now what if he got 70 on the last test? The new mean would be:</br>
(87 + 95 + 76 + 88 + 70) ÷ 5 = 83.2 </br>
Getting a 70 would bring the average closer to 85 than getting a 60, but still not there.</br>
How about if he got 80 on the last test? The new mean would be:</br>
(87 + 95 + 76 + 88 + 80) ÷ 5 = 85.2 </br>
Getting an 80 would bring his average us past 85!</br>
<b>And since the next option is larger than 80, this is the smallest mark he would need to finish with 85.</b></br>
We can still check what the mean would be if he got 90:</br>
(87 + 95 + 76 + 88 + 90) ÷ 5 = 87.2 </br>
Getting a 90 would be even better for the final mean, but he does not have to get 90 to finsih with at least 85.</br>
</br>
**You can use this with your own grades too to see how future tests can effect your final grade, if you want.
</div>

</body>
</html>

## Conclusion

In this notebook, we learned how an outlier affects central tendency. 

When an outlier is added to (or removed from) a data set:
* Mean changes the most 
* Median changes a little bit
* Mode doesn't change unless there are multiple outliers with the same value

Also, not all larger or smaller values should be called outliers and excluded from data. That depends more on context if some is given. 

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)