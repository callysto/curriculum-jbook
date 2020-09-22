![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/RatesRatiosAndProportionalReasoning/rates-ratios-and-proportional-reasoning.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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

import ipywidgets
from IPython.display import display, Math, Latex, HTML, IFrame, Javascript, clear_output
from ipywidgets import IntSlider, Label, widgets, interact, interact_manual, Button, Layout, interactive

# Rates, Ratios, and Proportional Reasoning

## Math 8

<img src="./images/ratioBars.gif">
*GIF taken from: https://patches.zone/compression-guide.* 

## Introduction
*Objects do not always appear in the same size.* This is true of everything in the universe. For example, what is the size of a human to an elephant? Or the size of our planet to the likes of Mars?

So, a need to compare quantities of things arises. This is needed to see how much bigger, or smaller, an amount is when compared to another. 

This notebook discusses three mathematical comparison concepts. These concepts are **ratios**, **rates**, and **proportional reasoning**. There will be interactive problems to help you understand these concepts. Let's start!

## Ratios
> **Ratios** are comparisons **between two things**. In its plainest form, *a ratio* says how much one thing is compared to another.

We will use the following illustration to help learn more about ratios:

<img src="./images/ratio.JPG" alt="Callysto" width=200  align = "center">

The illustration above contains $2$ *triangles* and $4$ *circles*. So, **the ratio of** *triangles* **to** *circles* would be $2$ to $4$. This is because you have exactly $2$ *triangles* and $4$ *circles*.

Now, let's think about ratios more generally:

> Let's say you have some quantity $a$ of object $A$. It doesn't matter what $A$ is; it could be potatoes, cats, pillows, you name it.
<br /><br />
Let's say you also have some quantity $b$ of object $B$. Again, it doesn't matter what $B$ is; it could be pennies or cars if you wanted.
<br /><br />
Then you can say that **the ratio of** $A$ **to** $B$ is *the number of $As$ you have* **to** *the number of $Bs$ you have*, ($a$ to $b$).

**Ratios** can also be written in different ways:

- Use a colon, ($a : b$), to separate the values.</h3>
- Use the word "to", ($a\textrm{ to }b$), to separate the values. </h3>
- Use a fraction, ($\frac{a}{b}$) to separate the values. </h3>

So, we can write the ratio of the example above in the following ways:

> a) $2 : 4$
<br /><br />
b) $2 \textrm{ to } 4$
<br /><br />
c) $\frac{2}{4}$

According to our definition of a ratio, for every $2$ *triangles*, there are $4$ *circles*. But, we can also compare *triangles* and *circles* by **scaling the ratio**. This is also known as an *equivalent of the ratio* or *equal ratio*. 

We can get an *equal ratio* by either multiplying or dividing each term in the ratio by the same number, (**Just not by zero**). So, since the ratio of *triangles* and *circles* is $2 : 4$, we can divide both sides of the ratio by $2$ to get $1 : 2$. This means there are $2$ *circles* for $each$ *triangle*, and it can be divided into $2$ groups.

<img src="./images/ratio_scale.JPG" alt="Callysto" width=350  align = "center">

Let's try the following problem:

#Used to ensure the description text doesn't get cut off.
style = {'description_width': 'initial'}

def q_1(val):
    #If the answer is correct:
    if val == "2 to 1":
        display("Correct!")
        display("If the values are flipped, then the ratio should also be flipped.")
        
    #If nothing is selected:
    elif val == None:
        None
    
    #Otherwise, if the answer is wrong:
    else:
        display("Please try again.")
        display("Remember, we are no longer looking at the ratio of triangles to circles.")

#a1, a2, and a3 are the possible inputs the user can put.
a1 = "2 to 4"
a2 = "2 to 1"
a3 = "1 to 2"

#Display the question.
#display(Latex("What is the ratio of circles to triangles?"))

#Create a drop down widget for answers.
interact(q_1, val = widgets.Dropdown(options=[a1 ,a2, a3],\
                                     value = None,\
                                     description = 'What is the ratio of circles to triangles?',\
                                     disabled = False,\
                                     style = style));

The following video, from [LearnAlberta](http://www.learnalberta.ca/content/mesg/html/math6web/index.html?page=lessons&lesson=m6lessonshell03.swf), demonstrates the idea of ratio with some interactive problems. You may need to enable the Adobe Flash Player for this site in your browser.

#lesson is the ratio lesson.
lesson = HTML('<center><embed width="500" height="400" src="InteractiveLesson.swf"\
frameborder="0" allow="autoplay"; encrypted-media"></center>')

#Construction of button to provide factored polynomial result.
buttonShowVideo = widgets.Button(description="Show Video")

def displayLesson(a):
    display(lesson)
    buttonShowVideo.close()

display(buttonShowVideo)
buttonShowVideo.on_click(displayLesson)

<font size = 2 > <center> *This work has been adapted from a learning resource originally owned by Alberta Education. (http://www.learnalberta.ca)* </center> </font>

### Ratio Related Problems

* **Problem 1:** Finding the equal ratios.

#Used to ensure the description text doesn't get cut off.
style = {'description_width': 'initial'}

#Create the box for options
a1=widgets.Checkbox(
    value=False,
    description="3 : 6",
    style=style
)

b1=widgets.Checkbox(
    value=False,
    description="6 : 8",
    style=style
)
c1=widgets.Checkbox(
    value=False,
    description="2 : 3",
    style=style
)
d1=widgets.Checkbox(
    value=False,
    description=r'36 : 48',
    style=style
)

#writtenQuestion is the question the user is asked.
writtenQuestion1 = 'Which of the following are equal ratios of 18:24 ?'
display(writtenQuestion1)

#Display the check box
display(a1)
display(b1)
display(c1)
display(d1)

#create a button to check the answer
button_check1 = widgets.Button(description="Check")
display(button_check1)

#Check the answer
def check_button1(x):
    #If answer is correct:
    if (a1.value==False and b1.value==True and c1.value==False and d1.value==True):
        clear_output()
        display(writtenQuestion1)
        display("Correct!")
        display(Latex(r"$18 : 24 = 6 : 8$ (Divide by 3)"))
        display(Latex(r"$18 : 24 = 36 : 48$ (Multiply by 2)"))
        
    #Otherwise, if the answer is wrong:
    else: 
        clear_output()
        display(writtenQuestion1)
        display(a1)
        display(b1)
        display(c1)
        display(d1)
        display("Please try again.")
        display("HINT: There is more than one answer. Make sure to divide or multiply both \
parts using the same number.")
        display(button_check1)
        
button_check1.on_click(check_button1)


* **Problem 2:** (Use the illustration below to answer the question)

<img src="./images/Car.gif" width="500" />
<font size = 1 > <center>*GIF taken from [NinetyEast](http://www.ninetyeast.net/physics/grade-9-10-gcse-hsc/forces/newtons-laws-of-motion/newtons-first-law-of-motion)*</center> </font>


#writtenQuestion is the question the user is asked.
writtenQuestion2 =  'What is the ratio of the speeds of the orange, green and blue cars?'
display(writtenQuestion2)

#Create the box for options
a2=widgets.Checkbox(
    value=False,
    description="4 : 2 : 1",
    style=style
)

b2=widgets.Checkbox(
    value=False,
    description='20 : 40 : 10',
    style=style
)
c2=widgets.Checkbox(
    value=False,
    description='10 : 20 : 40',
    style=style
)
d2=widgets.Checkbox(
    value=False,
    description=r'1 : 2 : 4',
    style=style
)

#Display the check box
display(a2)
display(b2)
display(c2)
display(d2)

#create a button to check the answer
button_check2 = widgets.Button(description="Check")
display(button_check2)

#Check the answer
def check_button2(x):
    #If answer is correct:
    if a2.value==True and b2.value==False and c2.value==False and d2.value==False:
        clear_output()
        display(writtenQuestion2)
        display("Correct!")
        display(Latex(r'Orange : Green : Blue $= 40 : 20 : 10 \
        = 4 : 2 : 1$ (Divide by 10)'))
        
    #Otherwise, if the answer is wrong:
    else: 
        clear_output()
        display(writtenQuestion2)
        display(a2)
        display(b2)
        display(c2)
        display(d2)
        display(button_check2)
        display("Please try again.")
        display("HINT: Make sure the order of your ratio is Orange : Green : Blue.")
                
button_check2.on_click(check_button2)

* **Problem 3:** Jack goes to the market and buys $8$ oranges, $6$ bananas, and $2$ pineapples.

#writtenQuestion is the question the user is asked.
writtenQuestion3 =  'What is the ratio of fruits to bananas?'
display(writtenQuestion3)

#Create the box for options
a3=widgets.Checkbox(
    value=False,
    description='16 : 6',
    style = style
)

b3=widgets.Checkbox(
    value=False,
    description='14 : 6',
    style = style
)

c3=widgets.Checkbox(
    value=False,
    description=r'8 : 3',
    style = style
)
d3=widgets.Checkbox(
    value=False,
    description=r'16 : 8',
    style = style
)

#Display the check box
display(a3)
display(b3)
display(c3)
display(d3)

#create a button to check the answer
button_check3 = widgets.Button(description="Check")
display(button_check3)

#Check the answer
def check_button3(x):
    #If answer is correct:
    if a3.value==True and b3.value==False and c3.value==True and d3.value==False:
        clear_output()
        display(writtenQuestion3)
        display("Correct!")
        display(Latex(r'Fruits : Bananas $= (8 + 6 + 2) : 6 \
        = 16 : 6 = 8 : 3$ (Divide by 2)'))
        
    #Otherwise, if the answer is wrong:
    else: 
        clear_output()
        display(writtenQuestion3)
        display(a3)
        display(b3)
        display(c3)
        display(d3)
        display(button_check3)
        display("Please try again.")
        display("HINT: There is more than one answer. Also, you should take note that\
 fruits means ALL fruits bought.")
                
button_check3.on_click(check_button3)

* **Problem 4:** Jack buys oranges and pineapples at a $4 : 3$ ratio.

#writtenQuestion is the question the user is asked.
writtenQuestion4 =  'If he buys 15 pineapples, how many oranges he will buy?'
display(writtenQuestion4)

#Create the box for options
a4=widgets.Checkbox(
    value=False,
    description='18 oranges',
    style = style
)
b4=widgets.Checkbox(
    value=False,
    description='24 oranges',
    style = style
)

c4=widgets.Checkbox(
    value=False,
    description='28 oranges',
    style = style
)
d4=widgets.Checkbox(
    value=False,
    description='20 oranges',
    style = style
)

#Display the check box
display(a4)
display(b4)
display(c4)
display(d4)

#create a button to check the answer
button_check4 = widgets.Button(description="Check")
display(button_check4)

#Check the answer
def check_button4(x):
    #If answer is correct:
    if a4.value== False and b4.value== False and c4.value== False and d4.value== True:
        clear_output()
        display(writtenQuestion4)
        display("Correct!")
        display(Latex(r'Oranges : Pineapples $= 4 : 3 \
        = 20 : 15$ (Multiply by 5)'))
        
    #Otherwise, if the answer is wrong:
    else: 
        clear_output()
        display(writtenQuestion4)
        display(a4)
        display(b4)
        display(c4)
        display(d4)
        display(button_check4)
        display("Please try again.")
        display("HINT: Multiply the ratio by the amount needed to get from 3\
 pineapples to 15 pineapples.")

button_check4.on_click(check_button4)

### Exercises

>**Question 1**: Jack has $16$ pens, $12$ pencils, and $6$ erasers. What is the ratio of supplies to erasers?

#Construction of button to provide answer to question 1.
buttonShowAnswer1 = widgets.Button(description="Show Answer")

def displayAnswer1(a):
    display(Latex(r"$34 : 6$ or $17 : 3$"))
    buttonShowAnswer1.close()

display(buttonShowAnswer1)
buttonShowAnswer1.on_click(displayAnswer1)

>**Question 2**: Jack has $16$ pens and $12$ pencils. If Jack gives $4$ pens to Jill, then how many pencils does Jack have to give Jill to keep an equal ratio?

#Construction of button to provide answer to question 2.
buttonShowAnswer2 = widgets.Button(description="Show Answer")

def displayAnswer2(a):
    display(Latex(r"$3$ pencils"))
    buttonShowAnswer2.close()

display(buttonShowAnswer2)
buttonShowAnswer2.on_click(displayAnswer2)

>**Question 3**: Jack delivers pizza. Fill up the following based on your ratio knowledge.

| Time (hour)   |Pizza delivered (quantity) |
|:-------------:|:-------------------------:|
|$6$            | $48$                      | 
|$ ?$           | $64$                      | 
|$7$            | $?$                       | 

#Construction of button to provide answer to question 3.
buttonShowAnswer3 = widgets.Button(description="Show Answer")

def displayAnswer3(a):
    display(Latex(r"$8$ and $56$"))
    buttonShowAnswer3.close()

display(buttonShowAnswer3)
buttonShowAnswer3.on_click(displayAnswer3)

## Rates

<img src="./images/GirlRunning.gif" width="300" height="200">

GIF taken from [Giphy](https://giphy.com/gifs/happy-girl-QKUTD5lAgpgrSHpbMB/fullscreen), October 27, 2018

> **Rates** are somewhat different than ratios. A rate is a ratio that compares two quantities of different units.

Suppose the girl in the figure above runs $2$ kilometers in $1$ hour. Then, the **rate** of the girl's running is $2$ km per hour, (Or $ 2 \frac{\textrm{km}}{\textrm{hour}}$). In this example, *a kilometer is the unit of distance*, and *hour is the unit of time*. So, the **running rate** of the girl is comparing two quantities of different units.

Rates occur in many areas of our life:

* How fast are you running? $\rightarrow$ *Kilometers per hour*
* What is the unit price of one of your pens? $\rightarrow$ *Price per unit*
* How fast are you typing? $\rightarrow$ *Words per minutes*

> Keep in mind that the denominator would be $1$ during rate calculation. 

Below is a video which demonstrates the real-life scenarios of rate:

from IPython.display import YouTubeVideo
YouTubeVideo('tT9A2jlL1s8')

<font size = 1 > <center> *This video was created by the YouTube channel LearningGamesLab and can be found at: (https://www.youtube.com/embed/tT9A2jlL1s8)* </center> </font>

### Rate Related Problems

* **Problem 1:** Jack writes $84$ words in $7$ minutes. He writes at a constant speed.

#writtenQuestion is the question the user is asked.
writtenQuestion11 =  'How many words can Jack write per minute?'
display(writtenQuestion11)

def q_11(val11):
    #If answer is correct:
    if val11 == "12 words per minute":
        display("Correct!")
        display(Latex(r'Words per minute $= \
        \frac{84}{7} = 12$ words per minute'))
    
    #If nothing is selected:
    elif val11 == None:
        None
        
    #Otherwise, if the answer is wrong:
    else:
        display("Please try again.")
        display(Latex(r'HINT: Words per minute $= \
        \frac{\textrm{Total number of words}}{\textrm{Total minutes}}$'))

a11 = '12 words per minute'
a21 = "13 words per minute"
a31 = "11 words per minute"
interact(q_11, val11 = widgets.Dropdown(options=[a11, a21, a31],\
                                     value = None,\
                                     description = 'Choose One:',\
                                     disabled = False));

* **Problem 2:** Jack delivers $16$ pizzas in $2$ hours.

#writtenQuestion is the question the user is asked.
writtenQuestion12 =  'How many pizzas can Jack deliver per hour?'
display(writtenQuestion12)

def q_12(val12):
    #If answer is correct:
    if val12 == "8 pizzas per hour":
        display("Correct!")
        display(Latex(r'Pizzas per hour $= \frac{16}{2} = 8$ pizzas per hour'))
    
    #If nothing is selected:
    elif val12 == None:
        None
        
    #Otherwise, if the answer is wrong:
    else:
        display("Please try again.")
        display(Latex(r'HINT: Pizzas per hour $= \
        \frac{\textrm{Total number of pizza deliveries}}{\textrm{Total hours}}$'))

a12 = "4 pizzas per hour"
a22 = "10 pizzas per hour"
a32 = "8 pizzas per hour"
interact(q_12, val12 = widgets.Dropdown(options=[a12, a22, a32],\
                                     value = None,\
                                     description = 'Choose One:',\
                                     disabled = False));

* **Problem 3:** There are three delivery workers at a Canadian Pizza shop. The table below shows how many pizzas has been delivered.

| Name  | Time (hour)   |Pizza delivered (quantity) |
|:------|:-------------:|:-------------------------:|
| Jack  |$6$            | $42$                      | 
| Robin |$ 5$           | $20$                      | 
|  Jill |$7$            | $35$                      | 

#writtenQuestion is the question the user is asked.
writtenQuestion13 =  'Which delivery worker delivers the fewest pizzas per hour?'
display(writtenQuestion13)

def q_13(val13):
    #If answer is correct:
    if val13 == "Robin":
        display("Great!")
        display(Latex(r'Pizzas per hour for Jack $= \
        \frac{42}{6} = 7$ pizzas per hour'))
        display(Latex(r'Pizzas per hour for Robin $= \
        \frac{20}{5} = 4$ pizzas per hour'))
        display(Latex(r'Pizzas per hour for Jill $= \
        \frac{35}{7} = 5$ pizzas per hour'))
        display(Latex("So, Robin delivers the fewest pizzas!"))
    
    #If nothing is selected:
    elif val13 == None:
        None
        
    #Otherwise, if the answer is wrong:
    else:
        display("Please try again.")
        display(Latex(r'HINT: Pizzas per hour for a person $= \
        \frac{\textrm{Total number of pizza deliveries}}{\textrm{Total hours}}$'))

a13 = "Jack"
a23 = "Robin"
a33 = "Jill"
interact(q_13, val13 = widgets.Dropdown(options=[a13, a23, a33],\
                                     value = None,\
                                     description = 'Choose One:',\
                                     disabled = False));

* **Problem 4:** Jack delivers $16$ pizzas in $4$ hours. How many pizzas can he deliver in $7$ hours?

> Let's solve this problem step by step:
 1. Calculate the rate of pizzas he can deliver in $1$ hour.
 2. Calculate the quantity of pizza he can deliver in $7$ hours.

#writtenQuestion1 is the question the user is asked.
writtenQuestion14 =  "What is the rate of Jack can deliver pizzas at (how many pizzas per hour)?"

def q_14(val14):
    #If answer is correct:
    if val14 == "4 pizza per hour":
        display("Great!")
        display(Latex(r'Pizzas per hour for Jack $= \
        \frac{16}{4} = 4$ pizzas per hour'))
        
        #Display the second question once the first question has been succesfully answered.
        display(writtenQuestion24)
        interact(q_24, val24 = widgets.Dropdown(options=[a44, a54, a64],\
                                     value = None,\
                                     description = 'Choose One:',\
                                     disabled = False));
    
    #If nothing is selected:
    elif val14 == None:
        None
        
    #Otherwise, if the answer is wrong:
    else:
        display("Sorry! Please try again.")
        display(Latex(r'HINT: Pizzas per hour $= \
        \frac{\textrm{Total number of pizzas delivered}}{\textrm{Total hours}}$'))

#The following is a list of answers for question 1.
a14 = "5 pizza per hour"
a24 = "4 pizza per hour"
a34 = "3 pizza per hour"

#Display the first question.
display(writtenQuestion14)
interact(q_14, val14 = widgets.Dropdown(options=[a14, a24, a34],\
                                     value = None,\
                                     description = 'Choose One:',\
                                     disabled = False));


#writtenQuestion2 is the question the user is asked.
writtenQuestion24 =  "How many pizzas can Jack deliver in 7 hours?"

def q_24(val24):
    #If answer is correct:
    if val24 == "28 pizzas":
        display("Great!")
        display(Latex(r'Jack delivers $4 \times 7 = 28$ pizzas per 7 hours!'))
    
    #If nothing is selected:
    elif val24 == None:
        None
    
    #Otherwise, if the answer is wrong:
    else:
        display("Sorry! Please try again.")
        display(Latex(r'HINT: (Pizzas per hour) $\times$ ($n$ amount of hours) $=$ Number of pizzas per $n$ hours'))

#The following is a list of answers for question 2.
a44 = "36 pizzas"
a54 = "32 pizzas"
a64 = "28 pizzas"

* **Problem 5:** Jack can deliver $16$ pizzas in $4$ hours. Jill can also deliver $64$ pizzas in $8$ hours. How many hours will they take to deliver $120$ pizzas if they work together?

> Let's solve this problem step by step:
 1. Calculate the rate of pizzas delivered by Jack and Jill.
 2. Calculate the combined pizza delivery rate.
 3. Calculate the amount of hours they take to deliver $120$ pizzas.

#writtenQuestion1 is the question the user is asked.
writtenQuestion15 =  "What is the rate of pizzas Jack and Jill can deliver in 1 hour?"
display(writtenQuestion15)

def q_15(val15):
    #If answer is correct:
    if val15 == "4 pizzas for Jack and 8 pizzas for Jill":
        display("Great!")
        display(Latex(r'Pizzas per hour for Jack $= \frac{16}{4} = 4$ pizzas'))
        display(Latex(r'Pizzas per hour for Jill $= \frac{64}{8} = 8$ pizzas'))
    
        #Display the second question once the first question has been succesfully answered.
        display(writtenQuestion25)
        interact(q_25, val25 = widgets.Dropdown(options=[a45, a55, a65],\
                                     value = None,\
                                     description = 'Choose One:',\
                                     disabled = False));

    #If nothing is selected:
    elif val15 == None:
        None
    
    #Otherwise, if the answer is wrong:
    else:
        display("Sorry! Please try again.")
        display(Latex(r'HINT: Pizzas per hour $= \
        \frac{\textrm{Total number of pizzas delivered}}{\textrm{Total hours}}$'))
        
a15 = "5 pizzas for Jack and 7 pizzas for Jill"
a25 = "4 pizzas for Jack and 8 pizzas for Jill"
a35 = "2 pizzas for Jack and 5 pizzas for Jill"

interact(q_15, val15 = widgets.Dropdown(options=[a15 ,a25, a35],\
                                     value = None,\
                                     description = 'Choose One:',\
                                     disabled = False));

#writtenQuestion2 is the question the user is asked.
writtenQuestion25 =  "How many pizzas can Jack and Jill deliver per hour?"

def q_25(val25):
    #If answer is correct:
    if val25 == "12 pizzas":
        display("Great!")
        display(Latex(r'Jack and Jill can deliver $4 + 8 = 12$ pizzas per hour!'))
        
        #Display the third question once the second question has been succesfully answered.
        display(writtenQuestion35)
        interact(q_35, val35 = widgets.Dropdown(options=[a75, a85, a95],\
                                     value = None,\
                                     description = 'Choose One:',\
                                     disabled = False));
    
    #If nothing is selected:
    elif val25 == None:
        None
    
    #Otherwise, if the answer is wrong:
    else:
        display("Sorry! Please try again.")
        display('HINT: Try adding the amount of pizzas Jack and Jill can do in an hour.')

#The following is a list of answers for question 2.
a45 = "12 pizzas"
a55 = "10 pizzas"
a65 = "24 pizzas"

#writtenQuestion3 is the question the user is asked.
writtenQuestion35 =  "How many hours would it take Jack and Jill to deliver 120 pizzas?"

def q_35(val35):
    #If answer is correct:
    if val35 == "10 hours":
        display("Great!")
        display(Latex(r'Hours taken $= \
        \frac{120}{12} = 10$ hours to deliver 120 pizzas'))
    
    #If nothing is selected:
    elif val35 == None:
        None
    
    #Otherwise, if the answer is wrong:
    else:
        display("Sorry! Please try again.")
        display(Latex(r'HINT: Hours taken $= \
        \frac{\textrm{Total number of pizzas they have to delivery}}{\textrm{Combined pizza delivery rate}}$'))

#The following is a list of answers for question 3.
a75 = "12 hours"
a85 = "10 hours"
a95 = "24 hours"

### Exercises

>**Question 1**: 
A car travels $88$ miles in $11$ hours. What is the rate of speed the car travels at?

#Construction of button to provide answer to question 1.
buttonShowAnswer11 = widgets.Button(description="Show Answer")

def displayAnswer11(a):
    display(Latex(r"$8$ miles per hour."))
    buttonShowAnswer11.close()

display(buttonShowAnswer11)
buttonShowAnswer11.on_click(displayAnswer11)

>**Question 2**: 
A car travels $72$ miles in $9$ hours. How many miles can the car can travel in $25$ hours?

#Construction of button to provide answer to question 2.
buttonShowAnswer12 = widgets.Button(description="Show Answer")

def displayAnswer12(a):
    display(Latex(r"$200$ miles"))
    buttonShowAnswer12.close()

display(buttonShowAnswer12)
buttonShowAnswer12.on_click(displayAnswer12)

>**Question 3**: 
A sedan can travel $64$ miles in $4$ hours. However, an SUV can travels $48$ miles in $3$ hours. Which car is faster?

#Construction of button to provide answer to question 3.
buttonShowAnswer13 = widgets.Button(description="Show Answer")

def displayAnswer13(a):
    display(Latex(r"They travel at equal speeds"))
    buttonShowAnswer13.close()

display(buttonShowAnswer13)
buttonShowAnswer13.on_click(displayAnswer13)

>**Question 4**:
Jack can deliver $100$ newspapers in $5$ hours, but Jill can deliver $125$ newspapers in $5$ hours. How many newspaper can both Jack and Jill deliver in $7$ hours?

#Construction of button to provide answer to question 4.
buttonShowAnswer14 = widgets.Button(description="Show Answer")

def displayAnswer14(a):
    display(Latex(r"$315$ newspapers in $7$ hours"))
    buttonShowAnswer14.close()

display(buttonShowAnswer14)
buttonShowAnswer14.on_click(displayAnswer14)

## Proportional Reasoning

Before beginning **proportional reasoning**, we will become familiar with proportions first. **A proportion** is a statement that two *ratios*, or *fractions*, equal:

> $\Large \frac{\textrm{a}} {\textrm{b}}  = \frac{\textrm{c}} {\textrm{d}} \hspace{2cm} \textrm{or} \hspace{2cm} {\textrm{a}} : {\textrm{b}} = {\textrm{c}} : {\textrm{d}}$

If *two ratios are equal*, then the cross product of the ratios is also equal:

> $\Large \textrm{a} \times {\textrm{d}}  = \textrm{b} \times {\textrm{c}}$

Let's say you run $20$ meters in $4$ seconds. How many seconds will it take you to run $100$ meters?

Assume that you wil need $x$ seconds to run $100$ meters. From our definition of proportion, we will get:

> $\frac{(20\textrm{ meters})} {(4\textrm{ seconds})} = \frac{(100\textrm{ meters})} {(x\textrm{ seconds})}$ 
<br /> <br />
$\Rightarrow (20\textrm{ meters}) \times (x\textrm{ seconds}) = (100{\textrm{ meters}}) \times (4\textrm{ seconds})$
<br /> <br />
$\Rightarrow (x\textrm{ seconds}) = \frac{(100\textrm{ meters}) \times (4\textrm{ seconds})} {(20\textrm{ meters})}$
<br /> <br />
$\Rightarrow (x\textrm{ seconds}) = 20\textrm{ seconds to run 100 meters.}$

We can view this problem visually:

<img src="./images/run.jpg" width="400" >

Running image taken and modified from [VectorStock](https://www.vectorstock.com/royalty-free-vector/kid-running-vector-20339619), October 27, 2018

Now, we can begin discussing what *proportional reasoning* is:

> **Proportional reasoning** is the ability to compare two quantities and predict the value of one based on the values of another. We do this using multiplication.

In the example above, the distance of $100$ meters is $5$ **times** larger than the initial distance, ($20$ meters). This is the case since:

> $ 5 \times  (20\textrm{ meters}) = (100 \textrm{ meters}) $

So, the time required to travel $100$ meters will be $5$ times of the initial time:

> $ 5 \times (4\textrm{ seconds}) = (20 \textrm{ seconds})$

This problem is a proportional reasoning problem.

Below is a video that demonstrates the idea of proportional reasoning:

%%html
<iframe width="560" height="315" src="https://www.youtube.com/embed/TTsLGvHve2E" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

*This video was created by the YouTube channel Program Innovation and can be found at: [https://youtu.be/TTsLGvHve2E](https://youtu.be/TTsLGvHve2E)* 

### Proportional Reasoning Related Problems

* **Problem 1:** For every 2 red candies in a package, there are 3 green candies. 
This problem is taken from [TapIntoTeenMinds](https://tapintoteenminds.com/progression-of-proportional-reasoning/).


#writtenQuestion1 is the question the user is asked.
writtenQuestion17 =  "How many red candies would there be if you had 12 green candies?"
display(writtenQuestion17)

def q_17(val17):
    #If answer is correct:
    if val17 == "8 red candies":
        display("Great!")
        display(Latex(r'$\frac{12}{2} = 6$ times as many red candies. So, $2 \times 6 \
        = 12$ red candies in the bag.'))
        
    #If nothing is selected:
    elif val17 == None:
        None
    
    #Otherwise, if the answer is wrong:
    else:
        display("Sorry! Please try again.")
        display('HINT: Try finding how many times more green candies there are in the bag.\
 Then, multiply the ratio by that amount. ')

a17 = "8 red candies"
a27 = "6 red candies"
a37 = "10 red candies"
interact(q_17, val17 = widgets.Dropdown(options=[a17, a27, a37],\
                                     value = None,\
                                     description = 'Choose One:',\
                                     disabled = False));

Let's see the visualization of this problem to give you clear idea what is exactly happening here:

<img src="./images/Candy_problem.gif" width="500" height="400">

*GIF from https://tapintoteenminds.com/progression-of-proportional-reasoning/, October 27, 2018.

* **Problem 2:** Below are two investment scenarios. Which investment is better? (This problem is taken from [TapIntoTeenMinds](https://tapintoteenminds.com/progression-of-proportional-reasoning/))

> Scenario 1 : An investment of $100$ dollars grows to $400$ dollars. 
<br /> <br />
Scenario 2 : An investment of $1000$ dollars grows to $1500$ dollars.

If you think this problem is about profit, then you will get $(400-100) = 300$ dollars profit from Scenario 1. But, you will get $(1500-1000) = 500$ dollars profit from scenario 2. So, in this case, scenario 2 is better than scenario 1. Let's visualize this way of thinking:

<img src="./images/invesment_absolute.gif" width="500" height="400">

*GIF from https://tapintoteenminds.com/progression-of-proportional-reasoning/, October 27, 2018.

#writtenQuestion1 is the question the user is asked.
writtenQuestion18 =  "We can think of this question in terms of profit."
display(writtenQuestion18)

def q_18(val18):
    #If answer is correct:
    if val18 == "False":
        display("Great!")
        display("This is because we didn't implement the proportional thinking in above explanation")
        
    #If nothing is selected:
    elif val18 == None:
        None
        
    #Otherwise, if the answer is wrong:
    else:
        display("Sorry! Please try again.")
        display("We want to look at this question using proportional thinking instead of just profit. \
This is the case since we are interested in how fast our money will grow.")


a18 = "True"
a28 = "False"

interact(q_18, val18 = widgets.Dropdown(options=[a18 ,a28],\
                                     value = None,\
                                     description = 'Choose One:',\
                                     disabled = False));

Now, let's think about this problem in a **proportional way**. 

We will get $(100 \times 4)$ in Scenario 1 and $(1000 \times 1.5)$ in Scenario 2. So, we will get $4$ times our initial investment in Scenario 1, and $1.5$ times our initial investment in Scenario 2. So, Scenario 1 is *better* than Scenario 2.

Below is a visualization that demonstrates the idea of multiplicative thinking:

<img src="./images/invesment_multiplicative.gif" width="500" >

*GIF taken from https://tapintoteenminds.com/progression-of-proportional-reasoning/, October 27,2018 

* **Problem 3:** Jack went to a store to buy oranges. He found that a pack of $8$ oranges cost $2$ dollars, and a pack of $20$ oranges cost $5.5$ dollars.

#writtenQuestion1 is the question the user is asked.
writtenQuestion19 =  "Which pack of oranges is cheaper?"
display(writtenQuestion19)

def q_19(val19):
    #If answer is correct:
    if val19 == "8 Oranges":
        display("Great!")
        display(Latex(r"$8$ oranges $\times$ $0.25 = 2$ dollars"))
        display(Latex(r"$20$ oranges $\times$ $0.275 = 5.5$ dollars"))
        display(Latex(r"So, since $0.25$ is less than $0.275$, buying $8$ oranges is cheaper."))

    #If nothing is selected:
    elif val19 == None:
        None
    
    #Otherwise, if the answer is wrong:
    else:
        display("Sorry! Please try again.")
        display("HINT: Check how much each orange costs.")

a19 = "8 Oranges"
a29 = "20 Oranges"

interact(q_19, val19 = widgets.Dropdown(options=[a19, a29],\
                                     value = None,\
                                     description = 'Choose One:',\
                                     disabled = False));

### Exercise

>**Question 1**: 
Jack has $8$ pens and $4$ pencils. Jill has $10$ pens. If both have the same proportion of pens to pencils, how many pens does Jill have?

#Construction of button to provide answer to question 1.
buttonShowAnswer77 = widgets.Button(description="Show Answer")

def displayAnswer77(a):
    display(Latex(r"Jill has $20$ pencils"))
    buttonShowAnswer77.close()

display(buttonShowAnswer77)
buttonShowAnswer77.on_click(displayAnswer77)

>**Question 2**: 
A Sedan car drives $4$ km in $2$ hours, while an SUV drives $36$ km. If the SUV drives at the same proportional rate as the Sedan, how many hours will it take the SUV to drive $36$ km?

#Construction of button to provide answer to question 1.
buttonShowAnswer88 = widgets.Button(description="Show Answer")

def displayAnswer88(a):
    display(Latex(r"It will take the SUV $18$ hours to drive 36 km."))
    buttonShowAnswer88.close()

display(buttonShowAnswer88)
buttonShowAnswer88.on_click(displayAnswer88)

>**Question 3**: 
A cobra grows $2$ meters in $18$ days, while a python grows $9.5$ meters in $81$ days. Which types of snake has faster growth? 

#Construction of button to provide answer to question 1.
buttonShowAnswer99 = widgets.Button(description="Show Answer")

def displayAnswer99(a):
    display(Latex(r"The python grows faster."))
    buttonShowAnswer99.close()

display(buttonShowAnswer99)
buttonShowAnswer99.on_click(displayAnswer99)

## Conclusion

In this notebook, we introduced three important concepts of mathematics: *Ratio*, *Rate* and *Proportional Reasoning*. 

Let's review what we have learned:

- **A ratio** is the comparison between two things.
- **A rate** is a type of ratio that also compares two things but in different units.
- **Proportional Reasoning** also compares two things based on multiplicative thinking.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)