![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/IndependentProbability/IndependentProbability.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

%%html
<button onclick="run_all()">CLICK HERE TO BEGIN</button> 
<script>
function run_all(){
    Jupyter.actions.call('jupyter-notebook:run-all-cells-below');
    Jupyter.actions.call('jupyter-notebook:save-notebook');
}
</script>

# Probability of Independent Events

<img style="float: left;" src="Images/FirstDicePic.svg" height="1800" width="700">


## Introduction

Our lives are full of random events! To be an informed and successful person, it is important to get a "feel" for randomness. What is a random event? Flipping a coin, rolling dice, shuffling cards, and lottery draws are all examples of random events. There are **two basic types** of random events: **dependent** random events, and **independent** random events.
    
What are **dependent** random events? Sometimes the occurrence of an event can affect the probability of the next event occurring. For example, consider removing a playing card from a deck of cards. As you take each card, there are fewer cards left in the deck, and so the probability of drawing a particular card changes on later draws.

This notebook will focus on **independent** events. As you've probably guessed, these are events that are **not affected** by previous events.

**Note:** To express the likelihood of an event occurring, we assign a **probability** to it, usually expressed as a decimal or fraction that is between zero and one.

### Die Simulator

Click the "Roll Dice!" button as many times as you'd like. Do you think that the current number on the die affects the likelihood of the next number occurring? 


from ipywidgets import Output, VBox
from random import choice
import time
from IPython.display import Image, display, clear_output
from ipywidgets import widgets

Animation = Image(filename="Images/DiceAnimationInfinite.gif", width = 80, height = 80)
N1 = Image(filename="Images/Dice1.gif", width = 50, height = 50)
N2 = Image(filename="Images/Dice2.gif", width = 50, height = 50)
N3 = Image(filename="Images/Dice3.gif", width = 50, height = 50)
N4 = Image(filename="Images/Dice4.gif", width = 50, height = 50)
N5 = Image(filename="Images/Dice5.gif", width = 50, height = 50)
N6 = Image(filename="Images/Dice6.gif", width = 50, height = 50)

### Widgets ###
out1 = Output()
button1 = widgets.Button(description = "Roll Die!")

### Functions ###
def on_button1_clicked(b):
    subj = [N1, N2, N3, N4, N5, N6]
    with out1:
        clear_output()
        display(Animation)
        time.sleep(2.5)
        clear_output(wait=True)
        display(choice(subj))
    
### Display Widgets ###
display(VBox([button1, out1]))

### Initialize Button Click Action ###
button1.on_click(on_button1_clicked)

### Experimental Probability

One way of estimating the probability of an event is to do so experimentally.  If we do an experiment $x$ times and the event we want occurs $n$ times, then the **experimental probability** of the event is just: 

\begin{equation}
\text{Probability of an event happening} = \dfrac{\text{Number of occurrences of event}}{\text{Number of experiments done}}=\dfrac{n}{x}
\end{equation}

#### Question

Consider the event of rolling a particular number (say 3) on the above six-sided die.  Roll the above die $x$ times (say 20 times) and count how many times ($n$) the particular number occurs.

*What is your experimental estimate for the probability of rolling a given number on a six-sided die?  Would you get the same estimate if you did it again?*

### Experimental Die Simulator

Experimental estimates of probability improve if the number of times the experiment is done ($x$) is large. Let's demonstrate this through an example. The slider below allows you to choose how many times the die is rolled. The chart below keeps track of the value of each roll. Start at the bottom of the slider and make your way to the top. Do you see any pattern forming?

from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np
import random

def f(x=50):
    min = 1
    max = 6
    D1, D2, D3, D4, D5, D6 = 0, 0, 0, 0, 0, 0
    for i in range(x):
        num1 = random.randint(min, max)
        if num1 == 1:
            D1 += 1
        elif num1 == 2:
            D2 += 1
        elif num1 == 3:
            D3 += 1
        elif num1 == 4:
            D4 += 1
        elif num1 == 5:
            D5 += 1
        elif num1 == 6:
            D6 += 1
    
    
    plt.figure()
    plt.bar([1,2,3,4,5,6],[D1,D2,D3,D4,D5,D6])
    plt.ylim(0, (x/6)*2)
    plt.ylabel('Total Number of Occurences ($n$)')
    plt.xlabel('Die Value')
    plt.show()

    
interactive_plot = interactive(f, x=widgets.IntSlider(min=50,max=5000,step=495, continuous_update=False))
output = interactive_plot.children[-1]
output.layout.height = '300px'
interactive_plot

### Review Questions

*What pattern emerges when the number of rolls increases? In other words, what happens to the graph when you move the slider to 5000 rolls?*

def multiple_choice(O1, O2, O3, O4):
    question_prompts = [O1, O2, O3, O4]
    answer = question_prompts[0]
    letters = ["a)", "b)", "c)", "d)"]

    #Starts and ends bolded letters
    start = "\033[1m"
    end = "\033[0;0m"

    #Randomly shuffles the options
    random.shuffle(question_prompts)

    #Prints the letters a) - d) in sequence with randomly chosen options
    for i in range(4):
        selection = question_prompts.pop()
        print(start + letters[i] + end + selection)

        #Stores the correct answer
        if selection == answer:
            letter_answer = letters[i]

    button1 = widgets.Button(description="a)")
    button2 = widgets.Button(description="b)")
    button3 = widgets.Button(description="c)")
    button4 = widgets.Button(description="d)")
    
    button1.style.button_color = 'Whitesmoke'
    button2.style.button_color = 'Whitesmoke'
    button3.style.button_color = 'Whitesmoke'
    button4.style.button_color = 'Whitesmoke'
    
    container = widgets.HBox(children=[button1,button2,button3,button4])
    display(container)

    def on_button1_clicked(b):
        if "a)" == letter_answer:
            print("Correct! 👏", end='\r')
            button1.style.button_color = '#abffa8'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again! ", end='\r')
            button1.style.button_color = '#ffbbb8'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button2_clicked(b):
        if "b)" == letter_answer:
            print("Correct! 👏", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = '#abffa8'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again! ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = '#ffbbb8'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button3_clicked(b):
        if "c)" == letter_answer:
            print("Correct! 👏", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = '#abffa8'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again! ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = '#ffbbb8'; button4.style.button_color = 'Whitesmoke'

    def on_button4_clicked(b):
        if "d)" == letter_answer:
            print("Correct! 👏", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = '#abffa8'
        else:
            print("Try again! ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = '#ffbbb8'

    button1.on_click(on_button1_clicked)
    button2.on_click(on_button2_clicked)
    button3.on_click(on_button3_clicked)
    button4.on_click(on_button4_clicked)
    
Option1 = "The total for each dice value becomes roughly the same as the number of rolls increases."
Option2 = "The graph will look like a staircase; i.e. 1 has the lowest total and 6 has the highest."
Option3 = "The graph will look like a hill; i.e. the middle values (3 and 4) will have the highest totals."
Option4 = "No pattern emerges."

multiple_choice(Option1, Option2, Option3, Option4)

*Read the number of number of occurrences ($n$) of a particular die value (say 3) and calculate the experimental probability as the number of experiments ($x$) increases.  To what value does the experimental probability trend?*

#import random

#Assign each question to these four variables. Note: there must be 4 questions and 1 answer.
Option1 = "Probability = 1/6" #Make this the answer. It'll be randomized later.
Option2 = "Probability = 1/2"
Option3 = "Probability = 1/3"
Option4 = "Probability = 1/4"

multiple_choice(Option1, Option2, Option3, Option4)

### Experimental Coin Simulator

Let's switch from dice to coins as a further example. A coin has two sides: "Head" and "Tails".  The following simulator counts the number of occurrences of each when a fair coin is flipped experimentally $x$ times.

**Question:** *Similar to the dice bar chart above, what shape/pattern emerges if you toss a coin thousands of times?*

def g(x=10):
    min = 1
    max = 2
    Heads, Tails = 0,0
    for i in range(x):
        num1 = random.randint(min, max)
        if num1 == 1:
            Heads += 1
        elif num1 == 2:
            Tails += 1

    plt.figure()
    plt.bar(["Heads","Tails"],[Heads, Tails])
    plt.ylim(0, (x/2)*2)
    plt.ylabel('Total')
    plt.xlabel('Coin Value')
    plt.show()

    
interactive_plot = interactive(g, x=widgets.IntSlider(min=10,max=5000,step=499, continuous_update=False))
output = interactive_plot.children[-1]
output.layout.height = '300px'
interactive_plot

Option1 = "The two columns become more and more similar in height."
Option2 = "No pattern!"
Option3 = "The 'Tails' column becomes twice as big as the 'Heads' column."
Option4 = "'Heads' is more likely and so its column becomes bigger."

multiple_choice(Option1, Option2, Option3, Option4)

**Question:** *Calculate the experimental probability of the event of getting a "Head" on a single coin toss using your data for a large number of experiments.  What do you think the exact probability is?*

### Independence and the Gambler's Fallacy

We have seen, based on experiment, that a fair coin has probability of $\frac{1}{2}$ of resulting in "Heads".

**Question:** *Suppose you toss a fair coin and it comes up "Heads" **nine times** in a row. What is the chance that **the next toss** will also be a "Head"?*

Option1 = "1/2 chance (50%)"
Option2 = "Nearly zero percent chance!"
Option3 = "1/6 chance"
Option4 = "1/4 chance (25%)"

multiple_choice(Option1, Option2, Option3, Option4)

**Note:** It is common for people to think that a Tail is "overdue", but the next toss of the coin is **totally independent** of any previous tosses.

Saying "a Tail is due" is called **The Gambler's Fallacy**. Don't fall for it!

## Calculating the Probability of Independent Events Theoretically

We have seen how to estimate the probability of an event experimentally.  In many cases we can calculate an exact **theoretical probability** using the following formula:

\begin{equation}
\text{Probability of an event happening} = \dfrac{\text{Number of ways it can happen}}{\text{Total number of possible outcomes}}
\end{equation}

**Example:** What is the probability of getting a "Tail" when tossing a coin?

- **Number of ways it can happen: 1** (Tail)
- **Total number of possibly outcomes: 2** (Head and Tail)


Therefore, the probability of getting a "Tail" = $\dfrac{1}{2}=0.5$

**Example:** What is the probability of getting a "3" or "6" when rolling a die?

- **Number of ways it can happen: 2** ("3" and "6")
- **Total number of possibly outcomes: 6** ("1", "2", "3", "4", "5", "6")


Therefore, the probability = $\dfrac{2}{6}=\dfrac{1}{3}=0.333...$

**Notes:** 
- Probabilities are often shown as a **decimal**, **fraction**, or a **percentage**. Here are **three** ways of showing the probability of flipping a "Head":

    - As a decimal: **0.5**
    - As a fraction: **1/2**
    - As a percentage: **50%**


- The **theoretical probability formula** looks similar to the **experimental formula**, but both formulas are quite different.  Using the theoretical formula, no experiment is done. We simply consider the possible outcomes and count those corresponding to the event of interest. Unlike an experimental probability, we will always get the **exact same answer** when we calculate the theoretical probability! *The theoretical probability is the true probability*.  Experimental probabilities *approximate* the true probability. The approximations improve as the number of experiments ($x$) is increased.

### Review Questions

*What is the probability of getting a "3" or "5" when rolling a die?*

Option1 = "Probability = 1/3"
Option2 = "Probability = 1/6"
Option3 = "Probability = 1"
Option4 = "Probability = 3/6 or 5/6"

multiple_choice(Option1, Option2, Option3, Option4)

*What is the probability of getting a "1", "2", or "3" when rolling a die?*

Option1 = "Probability = 3/6 or 1/2"
Option2 = "Probability = 1/6"
Option3 = "Probability = 1/3"
Option4 = "Probability = 0"

multiple_choice(Option1, Option2, Option3, Option4)

## The Probability of Multiple Independent Events

What if we wish to compute the probability of **multiple** independent events happening? For example, what is the probability of getting **three "Heads" in a row**?  Or, equivalently, if we **flip three coins**, what is the probability of getting exactly **three "Heads"**?

The following chart does the experiment of flipping three coins $x$ times and keeps track of the number of times ($n$) that three "Heads" occurs.

repeated_heads = 3

def h(n):
    sum1 = 0
    for i in range(n):
        num = random.randint(0,1)
        sum1 += num
    
    if sum1 == n:
        return True
    else:
        return False

def a(x=1000):
    good = 0
    bad = 0
    for j in range(x):
        y = h(repeated_heads)
        if y == True:
            good += 1
        else:
            bad += 1
    
    plt.figure()
    plt.bar(["Total Tosses","3 Heads in a Row"],[bad+good, good])
    plt.ylim(0, x + 10000)
    plt.ylabel('Total number of occurrences ($n$)')
    plt.xlabel('')
    plt.show()
    #print("After flipping a coin three times for " + str(x) + " iterations, the probability of getting three heads in a row can be approximated as: (Number of 3 Heads in a row) / (Total number of trials) = ", str(good) + "/" + str(good+bad) + " =", round(good/(good+bad), 5))
    print("After flipping three coins " + str(x) + " times, the probability of getting three heads is experimentally:\n (Number of times 3 Heads occurs) / (Total number of trials) = n/x =", str(good) + "/" + str(good+bad) + " =", round(good/(good+bad), 5))


interactive_plot = interactive(a, x=widgets.IntSlider(min=1000,max=100000,step=9900, continuous_update=False))
output = interactive_plot.children[-1]
output.layout.height = '300px'
interactive_plot

### Review Question

*As you move the slider to the right, what theoretical probability do your experimental results approach?*

Option1 = "0.125"
Option2 = "0.5"
Option3 = "1.5"
Option4 = "0.25"

multiple_choice(Option1, Option2, Option3, Option4)

### Computing Multiple Independent Event Probabilities Theoretically

**Question:** How do we quickly compute the theoretical probability of getting three Heads on a flip of three coins?

**Answer:** We can calculate the chances of two or more **independent** events by **multiplying** the chances. For each toss of a coin, a "Head" has a probability of 0.5. And so the chance of getting **three Heads in a row is**: 

\begin{equation}
0.5 \times 0.5 \times 0.5 = \boldsymbol{0.125}
\end{equation}

<img style="float: center;" src="Images/TREEFINAL.svg" width="50%">

Another way of seeing this is to write out all of the possibilities. We call this the *sample space* of the random trial. In this example, the random trial is flipping three coins. Below is this sample space:

<img style="float: center;" src="Images/SampleSpace.svg" width="50%">

Observe that only **one** of the **eight** possibilities is "HHH". Hence, the probability of getting three Heads on a flip of three coins is **1/8 = 0.125**.

**Notes:** 
- If you multiply probabilities in this way you must express them in decimal form first, not as percents!  If you want to express the final result as a percent, you can convert it to a percent by multiplying by 100%. Here for example, 0.125 becomes 12.5%.
- Computing multiple independent events theoretically in this manner (through multiplication) requires that each outcome is **equally likely**.

### Review Questions

*What is the probability of 7 heads in a row? (Hint: use a calculator).*

Option1 = "0.0078125"
Option2 = "0.03125"
Option3 = "0.015625"
Option4 = "0.5"

multiple_choice(Option1, Option2, Option3, Option4)

*Given that **we have just got 6 heads in a row**, what is the probability that **the next toss** is also a head?  Or equivalently, suppose we **flip 7 coins** and find that the **first six are heads**, what is the probability the last coin is a **head**? *

Option1 = "0.5"
Option2 = "0.03125"
Option3 = "0.015625"
Option4 = "0.0078125"

multiple_choice(Option1, Option2, Option3, Option4)

### A Cleaner Notation

Typically, we use "P" to mean "Probability Of". For Independent Events, we have

\begin{equation}
    \text{P(A and B) = P(A)} \times \text{P(B)}
\end{equation}

So we denote "the probability of getting 2 heads in a row" by

\begin{equation}
    \text{P(Heads and Heads) = P(Heads)} \times \text{P(Heads) = 0.5} \times \text{0.5 = 0.25}. 
\end{equation}

### Review Questions

*How would you denote: "the probability of rolling a "1" twice in a row and then rolling a "5" on a die"? Or equivalently when rolling three dice that the first two are "1" and the last one is a "5"?*

Option1 = "P('1' and '1' and '5')"
Option2 = "P('1' and '5')"
Option3 = "P('1')P('5')"
Option4 = "P('1' and '1' or '5')"

multiple_choice(Option1, Option2, Option3, Option4)

*For a coin, let H = "Heads" and T = "Tails". What is P(H and T and T and H)? Input your exact decimal answer in the textbox bellow.*

text = widgets.Text(
    value='',
    placeholder='Type probability (decimal)',
    description="Probability =",
    disabled=False
)

button = widgets.Button(description="Hint")
hint = [widgets.Label("P(H and T and T and H) = P(H) \u00D7 P(T) \u00D7 P(T) \u00D7 P(H). Recall that P(H) = P(T)=0.5")]
display(text)

def on_button_clicked(b):
    widgets.Box(hint)
    #print("P(H and T and T and H) = P(H) \u00D7 P(T) \u00D7 P(T) \u00D7 P(H). Recall that P(H) = P(T)=0.5")
    
            
def callback(wdgt):
    if (wdgt.value == "0.0625") or (wdgt.value == ".0625") or (wdgt.value == "1/16"):
        print("Correct! 👏                                                                                                    ", end='\r')
        text.on_submit(callback)
    else:
        print("Try again! Hint: P(H and T and T and H) = P(H) \u00D7 P(T) \u00D7 P(T) \u00D7 P(H). Recall that P(H) = P(T) = 0.5", end='\r')
        text.on_submit(callback)
        #display(button)
        #button.on_click(on_button_clicked)

text.on_submit(callback)

## Application Example

Suppose we have two groups:
- A member of each group gets randomly chosen for the winners' circle
- Then, one of those gets randomly chosen to get the grand prize.

**Question:** *What is your chance of winning the grand prize if:*
- *there is a **1/5 chance** of going to the winners' circle, and*
- *there is a **1/2** chance of winning the big prize?*

<img style="float: center;" src="Images/Lottery.svg" width="55%">

text2 = widgets.Text(
    value='',
    placeholder='Type probability (decimal)',
    description="Probability =",
    disabled=False
)


display(text2)

           
def callback2(wdgt):
    if (wdgt.value == "0.1") or (wdgt.value == ".1") or (wdgt.value == "1/10"):
        print("Correct! 👏                                                                ", end='\r')
        text2.on_submit(callback2)
    else:
        print("Try again! Hint: You have a 1/5 chance followed by a 1/2 chance of winning.", end='\r')
        text2.on_submit(callback2)

text2.on_submit(callback2)



## Conclusion

- Experimental Probability = (Number of occurrences of event)/(Number of experiments done)
- Theoretical Probability = (Number of ways event can happen)/(Total number of possible outcomes)
- Dependent events (removing cards from a deck of cards) are affected by **previous events**
- Independent events (such as rolling a die) are **not** affected by previous events
- Calculate the probability of 2 or more **independent** events by **multiplying**

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
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)