![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/InterpretAndAssessOdds/interpret-and-assess-odds.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, Math, Latex, HTML, clear_output, Markdown, Javascript, clear_output
import ipywidgets as widgets
from ipywidgets import interact, FloatSlider, IntSlider, interactive, Layout, ButtonStyle, HBox
from traitlets import traitlets


import plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)


# Function: executes next cell on button widget click event 

def run_cells(ev):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,IPython.notebook.get_selected_index()+2)'))
    return

# Interpret and Assess the Odds
    
## and the validity of a probability statement
---

In this Jupyter Notebook, you will be looking at examples of probabilistic statements that we encounter in our daily lives and some errors in our judgment that can arise when we try to reason with probabilistic statements. We will be looking at:

- Examples of statements of probability and odds.
- Expressing odds as a probability and vice versa.
- Determining the probability of, or the odds on and against, an outcome in a situation.
- Explain, using examples, how decisions may be based on probability or odds and on subjective judgments.
- Solving a contextual problem that involves odds or probability.


## Probability and Odds

Let's begin with some definitions. Having a clear understanding of these definitions will help with the rest of the notebook, as these concepts will be used often. 

<div class="alert alert-warning">
<font color="black"><b>Event:</b> 
An outcome of an experiment. These are the outcomes that are possible. 
</div>

For example, when rolling a die, the possible events are the die landing on the numbers 1 to 6.

<div class="alert alert-warning">
<font color="black"><b>Probability:</b> 
The likelihood that an event will occur. In a very large amount of trials, it is the fraction of times you expect the event to happen. This is expressed as a number between 0 and 1, with 1 being 100% likelihood.  
</div>

For example, after a large number of coin flips you would expect a properly weighted coin to land on heads half of the time. Therefore the probability of said event is $0.5$.

<div class="alert alert-warning">
<font color="black"><b>Odds:</b> 
The odds of an event X is expressed as a ratio X to Y. This the ratio between the probability that the event will occur and the probability that it will not occur. 
</div>

For example, what are the odds of rolling a $1$ for a fair die? 

Well, the probability of rolling a $1$ is $(\frac{1}{6})$ and the probability of not rolling a $1$ is $1-(\frac{1}{6}) = (\frac{5}{6})$ . Therefore the odds are: 
     
$$
\frac{1}{6}:\frac{5}{6} = 1:5
$$

**Note**: You would express the probability of an event *not* happening as: $1-p$, where $p$ is the probability of the event occurring. It will be useful to think in the negative case sometimes. 

### Different types of Odds

<div class="alert alert-warning">
<font color="black"><b>Odds Against:</b> 
This happens when the probability of the event not happening are higher than the event happening. Odds against are expressed with the larger number first.
</div>
    
For example, the odds against rolling a 1 on a fair dice are 5:1.

<div class="alert alert-warning">
<font color="black"><b>Odds-on:</b> 
These are the opposite of odds against, (i.e. The probability of the event happening are greater than it not happening).
</div>
    
For example, the odds for rolling an even number or a 1 on a fair dice is 4:2

<div class="alert alert-warning">
<font color="black"><b>Even Odds:</b> 
This occurs when the probability of an event happening is equal to that of the event not happening. 
</div>
    
For example, tossing a fair coin as an even odds of landing on heads or tails. 

### Dependent vs. Independent Events


<div class="alert alert-warning">
<font color="black"><b>Independent Events:</b> 
Events that, if they occurs, do not influence the likelihood of any other event happening.  
</div>

For example, tossing a coin. The fact that one coin toss lands on heads does not affect the probability of the next coin toss. 

<div class="alert alert-warning">
<font color="black"><b>Dependent Events:</b> 
Events that, if they occurs, change the future probability of the other events happening. 
</div>

The most classic example is pulling cards at random from a deck of cards. If you take a card out and don't put it back in, then there are fewer cards in the deck. If you pulled an *ace of spades* from a standard deck of cards, with probability $(\frac{1}{52})$, the probability of pulling an *ace of hearts* is now $(\frac{1}{51})$. The first event of pulling a card at random *and not replacing it* influenced the probability of the next card being pulled. When evaluating probabilities, it is important to consider whether the events are *dependent or independent*.


Let's try some true or false questions on what you have learned about odds and probability so far!

#trueFalseQuestion1 stores the true or false question that is being asked:
trueFalseQuestion1 = 'The probability of rolling an even number on a fair die is 0.5'
display(trueFalseQuestion1)

#a1 is the input button widget for true and false.
a1 = widgets.RadioButtons(
    options=['True', 'False'],
    value= None,
    disabled=False
)
display(a1)

#bt1 is a button labeled "Check Answer".
bt1 = widgets.Button(description = "Check Answers", 
                    layout = Layout(width = '25%', height = '60px'),
                    button_style = 'info'
                    )

#Check if answer is correct.
def check_answer(b):
    #If the answer is correct:
    if a1.value == 'True':
        clear_output()
        display(trueFalseQuestion1)
        display(Latex("$\;$ True"))
        display(Latex("$\;$ Correct! A die has equal parts odd and even numbers."))
        display()
    
    #Otherwise:
    else:
        clear_output()
        display(trueFalseQuestion1)
        display(a1)
        display(bt1)
        display(Latex("$\;$ Not quite, please try again."))
        display(Latex("$\;$ Remember, a die is made up of equal part odd and even numbers."))

bt1.on_click(check_answer)
display(bt1)

#trueFalseQuestion2 stores the true or false question that is being asked:
trueFalseQuestion2 = 'The odds of rolling an even number are 2:1.'
display(trueFalseQuestion2)

#a2 is the input button widget for true and false.
a2 = widgets.RadioButtons(
    options=['True', 'False'],
    value= None,
    disabled=False
)
display(a2)

#bt2 is a button labeled "Check Answer".
bt2 = widgets.Button(description = "Check Answers", 
                    layout = Layout(width = '25%', height = '60px'),
                    button_style = 'info'
                    )

#Check if answer is correct.
def check_answer(b):
    #If the answer is correct:
    if a2.value == 'False':
        clear_output()
        display(trueFalseQuestion2)
        display(Latex("$\;$ False"))
        display(Latex("$\;$ Correct! A die has equal parts odd and even numbers."))
        display()
    
    #Otherwise:
    else:
        clear_output()
        display(trueFalseQuestion2)
        display(a2)
        display(bt2)
        display(Latex("$\;$ Not quite, please try again."))
        display(Latex("$\;$ Remember, a dece is made up of equal part odd and even numbers."))

bt2.on_click(check_answer)
display(bt2)

#trueFalseQuestion3 stores the true or false question that is being asked:
trueFalseQuestion3 = 'The odds against rolling a 4 are 1:5.'
display(trueFalseQuestion3)

#a3 is the input button widget for true and false.
a3 = widgets.RadioButtons(
    options=['True', 'False'],
    value= None,
    disabled=False
)
display(a3)

#bt3 is a button labeled "Check Answer".
bt3 = widgets.Button(description = "Check Answers", 
                    layout = Layout(width = '25%', height = '60px'),
                    button_style = 'info'
                    )

#Check if answer is correct.
def check_answer(b):
    #If the answer is correct:
    if a3.value == 'False':
        clear_output()
        display(trueFalseQuestion3)
        display(Latex("$\;$ False"))
        display(Latex("$\;$ Correct! The odds against rolling any number once is 5 : 1."))
        display()
    
    #Otherwise:
    else:
        clear_output()
        display(trueFalseQuestion3)
        display(a3)
        display(bt3)
        display(Latex("$\;$ Not quite, please try again."))
        display(Latex("$\;$ Remember, the odds against has the larger number in the front."))

bt3.on_click(check_answer)
display(bt3)

#trueFalseQuestion4 stores the true or false question that is being asked:
trueFalseQuestion4 = Latex('The odds of rolling an uneven number are $1:1$.')
display(trueFalseQuestion4)

#a4 is the input button widget for true and false.
a4 = widgets.RadioButtons(
    options=['True', 'False'],
    value= None,
    disabled=False
)
display(a4)

#bt4 is a button labeled "Check Answer".
bt4 = widgets.Button(description = "Check Answers", 
                    layout = Layout(width = '25%', height = '60px'),
                    button_style = 'info'
                    )

#Check if answer is correct.
def check_answer(b):
    #If the answer is correct:
    if a4.value == 'True':
        clear_output()
        display(trueFalseQuestion4)
        display(Latex("$\;$ True"))
        display(Latex("$\;$ Correct! A die has equal parts odd and even numbers."))
        display()
    
    #Otherwise:
    else:
        clear_output()
        display(trueFalseQuestion4)
        display(a4)
        display(bt4)
        display(Latex("$\;$ Not quite, please try again."))
        display(Latex("$\;$ Remember, dice are usually made up of equal part odd and even numbers."))

bt4.on_click(check_answer)
display(bt4)

#trueFalseQuestion5 stores the true or false question that is being asked:
trueFalseQuestion5 = 'The probability of not rolling a 5 is 5/6 (or 0.833).'
display(trueFalseQuestion5)

#a5 is the input button widget for true and false.
a5 = widgets.RadioButtons(
    options=['True', 'False'],
    value= None,
    disabled=False
)
display(a5)

#bt5 is a button labeled "Check Answer".
bt5 = widgets.Button(description = "Check Answers", 
                    layout = Layout(width = '25%', height = '60px'),
                    button_style = 'info'
                    )

#Check if answer is correct.
def check_answer(b):
    #If the answer is correct:
    if a5.value == 'True':
        clear_output()
        display(trueFalseQuestion5)
        display(Latex("$\;$ True"))
        display(Latex("$\;$ Correct! The probability of not rolling a $5 = 1 - ({1\\over6}) = {5\\over6}.$"))
        display()
    
    #Otherwise:
    else:
        clear_output()
        display(trueFalseQuestion5)
        display(a5)
        display(bt5)
        display(Latex("$\;$ Not quite, please try again."))
        display(Latex(r"$\;$ Remember, the odds of not rolling a number $n = 1 - P(\textrm{Rolling }n).$"))

bt5.on_click(check_answer)
display(bt5)

#trueFalseQuestion6 stores the true or false question that is being asked:
trueFalseQuestion6 = 'The probability of rolling a 7 on a regular die is 1.'
display(trueFalseQuestion6)

#a6 is the input button widget for true and false.
a6 = widgets.RadioButtons(
    options=['True', 'False'],
    value= None,
    disabled=False
)
display(a6)

#bt5 is a button labeled "Check Answer".
bt6 = widgets.Button(description = "Check Answers", 
                    layout = Layout(width = '25%', height = '60px'),
                    button_style = 'info'
                    )

#Check if answer is correct.
def check_answer(b):
    #If the answer is correct:
    if a6.value == 'False':
        clear_output()
        display(trueFalseQuestion6)
        display(Latex("$\;$ False"))
        display(Latex("$\;$ Correct! A regular die only has numbers between $1$ and $6$. So, the probability\
        of rolling a 7 is 0."))
        display()
    
    #Otherwise:
    else:
        clear_output()
        display(trueFalseQuestion6)
        display(a6)
        display(bt6)
        display(Latex("$\;$ Not quite, please try again."))
        display(Latex(r"$\;$ Remember, a regular die only goes from $1$ to $6$."))

bt6.on_click(check_answer)
display(bt6)

**Wording** plays a crucial role in evaluating these statements. This last exercise demonstrated that there are many ways to phrase these questions. It is important to pay attention to the structure of these statements when evaluating and assessing them.

## Converting between Odds and Probability


Now that we understand what odds and probabilities mean, we can look at how they are related. We can also look at how we can express one as the other. 

To describe odds in favour of an event $E$, we have to think about what we are writing a ratio of. We are writing the ratio of $E$ happening versus that of $E$ not happening. This we write as $P(E)$ and $1-P(E)$ respectively.

We can write this as an equation:

$$
\text{Odds for the event $E$ occurring} = {P(E) \over 1-P(E)}
$$

As a ratio, we would write this as $P(E):1-P(E).$  

If the odds are $r:s$ in favour of an event $E$, we write this as:

$$
\text{Odds for the event $E$ occurring} =  {{r \over s} \over {1 + {r \over s} }} .
$$

However, if the odds are against the event $E$ occurring, we would write the equation:

$$
\text{Odds against the event $E$ occurring} = {1-P(E) \over P(E)}
$$

As a ratio, we would write this as $1-P(E):P(E).$

#question is the question the user is asked.
question = 'If the odds against an event happening are N:1, where N is a whole number, what is the \
probability of the event happening? (Use p for the probability of the event occurring)'
display(question)

#Steps for the answer:
prob_button= widgets.Button(description = "Show Answer", 
                            layout = Layout(width = '25%', height = '60px'),
                            button_style = 'info'
                            )
display(prob_button)

#If "Show Answer" is clicked:
def prob_answer(b):
    clear_output()
    display(question)
    display(Latex("$\;$ The formula we need here is $N = {1-p \\over p}$"))
    display(Latex("$\;$ Why? This is because odds against is the reciprocal ratio of odds on."))
    display(Latex("$\;$ Rearrange the formula: $Np + p = 1$"))
    display(Latex("$\;$ Isolate for the value you're looking for: $p(1+N) = 1$"))
    display(Latex("$\;$ $\\Rightarrow p = {1 \\over N+1}$"))
    return

prob_button.on_click(prob_answer)

Check to make sure this works for the dice roll!

---

## <center> Bayesian vs. Frequentist Reasoning </center>
    
These two schools of thinking are the foundation of modern probability theory. Since you are not taking a course in probability theory, we won't delve too deep into these subjects. Still, learning their basic principles will help you check the validity of statements about odds and probability.

<div class="alert alert-warning">
<font color="black"><b>Frequentist School:</b> 
Focuses on large amounts of data to assess probabilities. 
</div>
    
<div class="alert alert-warning">
<font color="black"><b>Bayesian School:</b> 
The Bayesian approach was named after the 18th century Reverend Thomas Bayes. It employs the use of conditional probabilities. They look at large amounts of data but also want to consider the conditional probabilities. These are the likelihoods of a certain event occurring in the first place.
</div>

It's easiest to understand their differences through an example:
> Say you have a bird feeder hung from a stand which keeps track of how many and what type of birds come to feed. At some point, it is noted that 2 Emperor Penguins have come to feed. If there were $N$ birds over 1 day:
- *The Frequentist* would say that there is a $\frac{2}{N}$ probability that an Emperor Penguin will fly up to the bird feeder in a day. 
- *The Bayesian*, with their conditional probabilities, disagrees. The Bayesian knows the percentage of all the birds in Canada that are Emperor Penguins. This percentage happens to be very small (some might say $0$). So, the Bayesian says this is an incredibly rare event.
<br /><br />
By considering a prior probability, the Bayesian drew a more educated conclusion. 

Before you decide which approach is better to use, we must note a couple very important points:

- What if the conditional probabilities are incorrect? Where did the Bayesian get their data from? What were the methods used? Were they biased? The Bayesian can sometimes unknowingly introduce biases with their prior knowledge. This may make the interpretation of the probability values somewhat subjective.

- The Frequentist would rely only on the data collected. This means they would remain as unbiased as possible.

It is crucial to understand the pros and cons of each school of thought. Using one approach or the other can be useful based on the context of the problem and data set.  

## Dartboard Exercise

Let's do a bit more of an applied exercise for the concepts you have learned thus far. Consider the dartboard simulation below. If a dart is thrown at random, what are the odds on it hitting inside the green circle?

# import matplotlib.pyplot as plt
%matplotlib inline
import random

circle_centerx=1
circle_centery=1
circle_radius=0.5

darts_number=widgets.IntText(value=0,disabled=False)
submit_button3=widgets.Button(description='Throw',button_style='info',disabled=False)
reset_button3=widgets.Button(description='Restart',disabled=False)
warning3=widgets.HTML(value=" ")

def on_button_submit3_clicked(b):
    global circle_centerx,circle_centery,circle_radius
    x_green=[]
    y_green=[]
    x_inside=[]
    y_inside=[]
    x_outside=[]
    y_outside=[]
    if darts_number.value >0:
        if darts_number.value>100000:
            darts_number.value=100000
        warning3.value=""
        for i in range(darts_number.value):
            x=random.random()*2
            y=random.random()*2
            if (x-circle_centerx)**2+(y-circle_centery)**2<circle_radius**2:
                x_green.append(x)
                y_green.append(y)
            elif (x-circle_centerx)**2+(y-circle_centery)**2<(circle_radius*2)**2:
                x_inside.append(x)
                y_inside.append(y)
            else:
                x_outside.append(x)
                y_outside.append(y)

        circle1 = plt.Circle((circle_centerx, circle_centery), circle_radius,color='g',fill=False)
        circle2 = plt.Circle((circle_centerx, circle_centery), circle_radius*2,color='black',fill=False)
        fig, ax = plt.subplots(figsize=(10,10)) 

        ax.plot(x_green,y_green, 'o', color='g',alpha=0.4)
        ax.plot(x_inside,y_inside, 'o', color='y',alpha=0.4)
        ax.plot(x_outside,y_outside, 'o', color='r',alpha=0.4)
        
        ax.add_artist(circle2)
        ax.add_artist(circle1)
        

        plt.ylim(0, 2) 
        plt.xlim(0, 2) 
        plt.show()
        ###################b.disabled=True
        darts_number.disabled=True
        display(Latex("Number of  darts inside the green circle: "+str(len(x_green))))
        display(Latex("Number of  darts that hit the dart board: "+str(len(x_green)+len(x_inside))))
        display(Latex("Total number of darts thrown: "+str(darts_number.value)))
        display(reset_button3)
    else:
        warning3.value="Please enter number greater than zero"
    
submit_button3.on_click(on_button_submit3_clicked)

def restart_cell(b):
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index(), IPython.notebook.get_selected_index()+1)'))

reset_button3.on_click(restart_cell)

display(Markdown("**Number of darts to throw** (up to 100000):"))
display(widgets.HBox([darts_number,submit_button3]))
display(warning3)

*Approach to solving this problem*: We need to understand how to calculate a probability in this context. We must calculate the areas of the inner and outer circles, calculate the probability, and then the odds!

*For our current problem*: Take $r_1=1$ to be the radius of the inner (green) circle and $r_2=2$ as the radius of the dartboard (the outer circle). Calculate the probability of a dart thrown at random will land within the inner circle. For now we will ignore the darts that do not hit the dart board.

#Dartboard exercise part 1 answer
dboard1 = widgets.Button(description = "Check Answer", 
                         layout = Layout(width = '25%', height = "60px"),
                         button_style = 'info'
                        )
display(dboard1)

def check_dboard1(b):
    clear_output()
    display(Latex("$\;$ The area of the inner circle is given by: $\pi (r_1)^2$"))
    display(Latex("$\;$ The area of the dartboard is given by: $\pi (r_2)^2$"))
    display(Latex("$\;$ The ratio of the areas is given by: $\\frac{\pi (r_1)^2}{\pi (r_2)^2}$"))
    display(Latex("$\;$ Simplifying and substituting in values we obtain: $\\frac{(r_1)^2}{(r_2)^2}=\\frac{1^2}{2^2}=\\frac{1}{4}$"))
    display(Latex("$\;$ Thus the probability of darts that hit the dartboard \
                  landing in the inner circle is $\\frac{1}{4}$"))
    
    return

dboard1.on_click(check_dboard1)

Now, what are the odds against landing in the inner cirle?

#dartboard exercise part 2

dboard2_button = widgets.Button(description = "Check Answer", 
                                layout = Layout(width = '25%', height = '60px'),
                                button_style = 'info'
                               )
display(dboard2_button)

def check_dboard2(b):
    clear_output()
    display(Latex("$\;$ The probability of landing in the inner circle is $(\\frac{\pi}{4})$, \
                  therefore the probability of not landing in the inner circle is $1-(\\frac{\pi}{4}) \
                  = (\\frac{3}{4})$."))
    display(Latex("$\;$ As explained above, we take the ratio $(\\frac{3}{4}):(\\frac{1}{4})$."))
    display(Latex("$\;$ Thus the odds against landing in the inner circle are $3:1$. \
                  Again ignoring the darts that missed the dartboard."))
    
    return
dboard2_button.on_click(check_dboard2)
                            

Now, let's try some more difficult questions with the dartboard. These may take a bit more time to work through. If you would like to review some more material, please go through the rest of the notebook and then come back to these! Try taking the time to solve the questions on paper before pressing the "Show Answer" button. While it may be tempting, it is always more rewarding to attempt to solve it yourself.

question1 = widgets.Button(description = "Question #1", 
                           layout = Layout(width = '25%', height = '60px'),
                           button_style = 'info'
                          )
display(question1)

q1answer = widgets.Button(description = "Show Answer")

def q1check(b):
    clear_output()
    display(Latex("If we consider all of the darts, what is the probability of not hitting the dartboard?"))
    display(q1answer)
    return
question1.on_click(q1check)

def q1ans(b):
    clear_output()
    display(Latex("If we consider all of the darts, what is the probability of not hitting the dartboard?"))
    display(Latex("$\;$ We start with the area of the square, $A_s = (b)(h) = (2)(2) = 4$"))
    display(Latex("$\;$ The area of the dartboard is $A_d = \pi (r_2)^2 = \pi (1)^2 = \pi$"))
    display(Latex("$\;$ Thus the probability of hitting the dartboard is $\\frac{\pi}{4}$ \
                  and the probability of not hitting the dartboard is $1-\\frac{\pi}{4} \\approx 0.215$."))
    return

q1answer.on_click(q1ans)
    

question2 = widgets.Button(description = "Question #2", 
                           layout = Layout(width = '25%', height = '60px'),
                           button_style = 'info'
                          )
display(question2)

q2answer = widgets.Button(description = "Show Answer")

def q2check(b):
    clear_output()
    display(Latex("What is the probability of hitting the inner circle twice in a row?"))
    display(q2answer)
    return
question2.on_click(q2check)

def q2ans(b):
    clear_output()
    display(Latex("What is the probability of hitting the inner circle twice in a row?"))
    display(Latex("$\;$ First off, we note that the two events are independent of \
                  one another. The probability of each is $\\frac{1}{4}$"))
    display(Latex("$\;$ Finally, we multiply these two probabilities together. This gives us the \
                  probability of these events happening in succession to get \
                  $ \\frac{1}{4} \\times \\frac{1}{4} = \\frac{1}{16}$."))
    return

q2answer.on_click(q2ans)
    

question3 = widgets.Button(description = "Question #3", 
                           layout = Layout(width = '25%', height = '60px'),
                           button_style = 'info'
                          )
display(question3)

q3answer = widgets.Button(description = "Show Answer")

def q3check(b):
    clear_output()
    display(Latex("What is the probability of hitting the outer circle and then the outer circle?"))
    display(q3answer)
    return
question3.on_click(q3check)

def q3ans(b):
    clear_output()
    display(Latex("$What is the probability of hitting the outer circle and then the outer circle?"))
    display(Latex("$\;$ Again the two events are independent of one another. We have to calculate the \
                  probability of each event."))
    display(Latex("$\;$ The probability of hitting the inner circle is $\\frac{1}{4}$ and \
                  the probability of hitting the outer circle but not the inner circle is \
                  $\\frac{3}{4}-\\frac{1}{4}=\\frac{1}{2}$."))
    display(Latex("$\;$ Finally we multiply the two probabilities together. This gives us the \
                  probability of these events happening in succession to get \
                  $\\frac{1}{2} \\times \\frac{1}{4} = \\frac{1}{8}$."))

    
    return

q3answer.on_click(q3ans)
    

This dartboard example can also be used to see the different ways of assessing validity.

Use the frequentist approach to determine the probability of landing in the inner circle or on a certain number. Remember that the frequentist assumes no prior knowledge about the dartboard. They must collect data. Note where the random throws lands. Keep track of both the number of throws, $N$, and the number of times, $m$, they land on the red circle. How many throws until $\frac{m}{N} \approx \frac{1}{4}$? 

Remember, the frequentist approach relies on large data sets! See if there is a convergence towards $\frac{1}{4}$ after 20 throws. 

---
## Making Decisions Based on Odds & Probability


One topic we may hear in the news that uses odds and probability is that of lottery winners. According to the CBC, approximately a quarter of all Canadians play the lottery weekly. We can buy a ticket and choose three sets of seven numbers for $5.00. Now, how do we calculate the odds of winning?

Consider [Lotto Max](http://lotto.bclc.com/lotto-max-and-extra/prizes-and-odds.html). In this lottery game, the player selects 7 distinct numbers from 1 to 49. We can count the number of ways to do this by using the  _Choose Function_ (Also known as the [Binomial Coefficients](https://en.wikipedia.org/wiki/Binomial_coefficient)). This gives us the number of ways to choose $k$ non-ordered elements from a fixed set of $n$ elements, which we write as follows: 

$${n \choose k} = {n! \over {k!(n-k)!}}$$

Here, $n$ and $k$ are both positive integers and $n!$ means $n\cdot(n-1)\cdot(n-2)\cdots 3\cdot 2\cdot 1$, (Some positive integer $n$ multiplied by every positive integer less than it). Now, back to the lottery. 

We have $k=7$ numbers to choose from a total of $n=49$ numbers. The number of ways to do this is given by:

$${49 \choose 7} = {49! \over {7!(49-7)!}} = {49! \over {7!42!}} = {49\cdot 48\cdot 47\cdot 46\cdot 45\cdot 44\cdot 43\cdot 42! \over {7!42!}} = {49\cdot 48\cdot 47\cdot 46\cdot 45\cdot 44\cdot 43 \over {7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot 1}} = 85,900,584$$

To win the lottery, we must hold a winning ticket, where one of the sets of numbers we chose matches all 7 of the winning numbers. Note that there is exactly one set of winning numbers.

Since a $5.00 ticket allows us to choose three sets of seven numbers, our chances of winning are slightly better. This is assuming that we don't choose exactly the same seven numbers for two or three of our sets.

So, we have three of the possible $85,900,584$ seven number configurations. This makes the odds for holding a winning ticket as $3:85,900,584$, (Or $1:28,633,528$).

**Exploration:** Every ticket comes with three sets of seven numbers we can choose from. We saw that the odds of having a winning ticket is $3:85,900,584$, (Or $1:28,633,528$ simplified). If we had only one set of seven numbers to choose from in a single ticket, the odds of winning would be much lower: $1:85,900,584$. So, in comparing having one set of numbers to having three sets of numbers, our chances seem to have improved.

**Exploration Question 1:** Would buying more tickets improve our chances of winning?

decision_q1_ctr = 0

# Exercise 2 widgets

decision_q1_button = widgets.Button(button_style='info', description="Save & View Answer", \
                                    layout=Layout(width='50%', height='30px') )
decision_q1_text = widgets.Textarea( placeholder='Enter your answer here.', description='', \
                                    disabled=False , layout = Layout(width='50%',height='250px')  )

display(decision_q1_text)
display(decision_q1_button)

decision_q1_button.on_click( run_cells )

decision_q1_ctr += 1

# Explanation to display in markdown format

exp_q1_line1 = "Would buying more tickets improve our chances of winning? **Yes.**"
exp_q1_line2 = "From a technical perspective, buying more tickets would improve our chance of winning. \
For example, if we buy two tickets, we now have a $6:89,900,584$ chance of winning. That is \
approximately a $1$ out of $14,983,430$ chance."
exp_q1_line3 = "Let $n$ be the number of tickets. Then every $n$ tickets gives us $3n$ sets of seven \
numbers to choose from. We can see that as we increase $n$, the fraction ${89,900,584 \over 3n}$ becomes \
smaller. This makes our chances of winning approximately $1$ out of ${89,900,584 \over 3n}.$ For instance, \
if we buy $n=7$ tickets, then our chance of winning is approximately 1 out of ${89,900,594 \over 21}$. \
That is, approximately a $1$ out of $4,280,980$ chance."

# Executes when user saves answer

if(decision_q1_ctr >= 2):
    decision_q1_button.close()
    user_decision_q1_text = decision_q1_text.value
    
    display(Markdown("**You wrote: **"))
    display(Markdown(user_decision_q1_text))
    
    display(Markdown("**Explanation: **"))
    display(Markdown(exp_q1_line1))
    display(Markdown(exp_q1_line2))
    display(Markdown(exp_q1_line3))

**Exploration Question 2.** Would this be a sound financial strategy?

decision_q2_ctr = 0

# Exercise 2 widgets

decision_q2_button = widgets.Button(button_style='info',description="Save & View Answer", layout=Layout(width='50%', height='30px') )
decision_q2_text = widgets.Textarea( placeholder='Enter your answer here.', description='', disabled=False , layout = Layout(width='50%',height='250px')  )

display(decision_q2_text)
display(decision_q2_button)

decision_q2_button.on_click( run_cells )

decision_q1_ctr = 0

decision_q2_ctr += 1

# Explanation to display in markdown format

exp_q2_line1 = "Would this be a sound financial strategy? **No.**"
exp_q2_line2 = "While it would technically increase your chances, buying more tickets would not be a good\
financial strategy. For example, if we bought 1000 tickets, we would have a $1000:89,900,584$ chance of winning. \
That is approximately a $1$ out of $29,967$ chance."
exp_q2_line3 = "So, the odds of you winning if you bought 1000 tickets are still not great. Plus, for every $n$ \
tickets you buy, you pay $5n$ dollars. That means that you would have spent $5000 dollars to get 1000 tickets. "

# Executes when user saves answer

if(decision_q2_ctr >= 2):
    decision_q2_button.close()
    user_decision_q2_text = decision_q2_text.value
    
    display(Markdown("**You wrote: **"))
    display(Markdown(user_decision_q2_text))

    display(Markdown("**Explanation: **"))
    display(Markdown(exp_q2_line1))
    display(Markdown(exp_q2_line2))
    display(Markdown(exp_q2_line3))

---
## Conclusion

In this Jupyter Notebook by Callysto, you learned about assessing the validity of odds and probability statements. We first outlined the concepts of:

* *Events*, 
* *Probability*, 
* And *Odds*. 

Thereafter, we defined some commonly used types of odds:

* *Odds on*,
* *Odds against*, 
* And *Even odds*.

We learnt the differences between *Dependent* and *Independent events*. We also elucidated the perspectives of Bayesian and Frequentist reasoning. These two schools of thought, along with an understanding of the concepts outlined throughout this Notebook, will give the reader a necessary toolset to interpret and assess the validity of odds and probability statements.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)