![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/StoichiometryAndLimitingReactants/stoichiometry-and-limiting-reactants.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

(Click **Cell** > **Run All** before proceeding.)

%matplotlib inline

#----------

#Import modules and packages 
import ipywidgets as widgets
import random
import math
import matplotlib.pyplot as plt
from ipywidgets import Output, IntSlider, VBox, HBox, Layout
from IPython.display import clear_output, display, HTML, Javascript, SVG, YouTubeVideo

#----------

#ipywidgets as widgets
#import random

#This function produces a multiple choice form with four options
def multiple_choice(option_1, option_2, option_3, option_4):
    option_list = [option_1, option_2, option_3, option_4]
    answer = option_list[0]
    letters = ["(A) ", "(B) ", "(C) ", "(D) "]

    #Boldface letters at the beginning of each option
    start_bold = "\033[1m"; end_bold = "\033[0;0m"

    #Randomly shuffle the options
    random.shuffle(option_list)
    
    #Prints the letters (A) to (D) in sequence with randomly chosen options
    for i in range(4):
        option_text = option_list.pop()
        print(start_bold + letters[i] + end_bold + option_text)

        #Stores the correct answer
        if option_text == answer:
            letter_answer = letters[i]

    button1 = widgets.Button(description="(A)"); button2 = widgets.Button(description="(B)")
    button3 = widgets.Button(description="(C)"); button4 = widgets.Button(description="(D)")
    
    button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
    button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
    
    container = widgets.HBox(children=[button1,button2,button3,button4])
    display(container)
    print(" ", end='\r')

    def on_button1_clicked(b):
        if "(A) " == letter_answer:
            print("Correct! 👏", end='\r')
            button1.style.button_color = '#abffa8'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again! ", end='\r')
            button1.style.button_color = '#ffbbb8'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button2_clicked(b):
        if "(B) " == letter_answer:
            print("Correct! 👏", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = '#abffa8'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again! ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = '#ffbbb8'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button3_clicked(b):
        if "(C) " == letter_answer:
            print("Correct! 👏", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = '#abffa8'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again! ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = '#ffbbb8'; button4.style.button_color = 'Whitesmoke'

    def on_button4_clicked(b):
        if "(D) " == letter_answer:
            print("Correct! 👏", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = '#abffa8'
        else:
            print("Try again! ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = '#ffbbb8'

    button1.on_click(on_button1_clicked); button2.on_click(on_button2_clicked)
    button3.on_click(on_button3_clicked); button4.on_click(on_button4_clicked)

# Stoichiometry and Limiting Reactants

<br />
<img style="float: left;" src="images/StoichiometryLimiting.svg" height="300" width="600">

## Stoichiometry

**Stoichiometry** is founded on the Law of Conservation of Mass. Note that "stoichio" comes from the Greek word "stoikheion" which means "element" and "metry" means "measure". So "stoichiometry" is the calculation of relative quantities of reactants and products in chemical reactions.

**Stoichiometry allows us to:**

- Predict how much product will form in chemical reactions.
- Determine which reactant is in excess and which is limiting.

### Mole - Mole Relationships in Chemical Reactions

The coefficients in a balanced chemical equation indicate both the relative numbers of molecules in the reaction and the relative number of moles.

<br />
<img style="float: left;" src="images/3DMolecules.svg" height="300" width="500">

### Examples

**1)** Consider the following chemical equation: 

<center>____ Al + ____ Br$_2$ $\rightarrow$ ____ AlBr$_3$</center>

Given 15 moles of aluminum (Al), how many moles of bromine (br) are needed for this reaction to occur (with no excess reactant)? Round to two significant figures.

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out1 = Output()
button1_step1 = widgets.Button(description="Step One", layout=Layout(width='20%', height='100%'), button_style='primary')
count1 = 1

text1_1 = widgets.HTMLMath(value=r"First, we balance the above equation: 2Al + 3Br$_2$ $\rightarrow$ 2AlBr$_3$")
text1_2 = widgets.HTMLMath(value="Note: The coefficients from the above balanced chemical equation give us the molar ratios.")

def on_button1_step1_clicked(b):
    global count1
    count1 += 1
    with out1:
        clear_output()
        if count1 % 2 == 0:
            display(text1_1, text1_2)
            
display(VBox([button1_step1, out1]))
button1_step1.on_click(on_button1_step1_clicked)

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out2 = Output()
button1_step2 = widgets.Button(description="Step Two", layout=Layout(width='20%', height='100%'), button_style='primary')
count2 = 1

text2_1 = widgets.HTMLMath(value=r"Now, we use these coefficients to convert mol of Al to mol of Br$_2$:")
text2_2 = widgets.HTMLMath(value=r"$15 \text{ mol Al} \bigg(\dfrac{3\text{ mol Br}_2}{2\text{ mol Al}}\bigg)=22.5=23 \text{ mol Br}_2$")
text2_3 = widgets.HTMLMath(value=r"Therefore, given 15 moles aluminum, 23 moles bromine are needed. This is the merit of balancing.")

def on_button1_step2_clicked(b):
    global count2
    count2 += 1
    with out2:
        clear_output()
        if count2 % 2 == 0:
            display(text2_1, text2_2, text2_3)
            
display(VBox([button1_step2, out2]))
button1_step2.on_click(on_button1_step2_clicked)

**2)** Consider the following chemical equation:

<center>____ H$_2$ + ____ N$_2$ $\rightarrow$ ____ NH$_3$</center>

How many moles of NH$_3$ are formed when 3.6 mol of H$_2$ are reacted with an excess of N$_2$?

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out3 = Output()
button2_step1 = widgets.Button(description="Step One", layout=Layout(width='20%', height='100%'), button_style='primary')
count3 = 1

text3_1 = widgets.HTMLMath(value=r"As usual, we balance the equation: 3H$_2$ + 2N$_2$ $\rightarrow$ 2NH$_3$")

def on_button2_step1_clicked(b):
    global count3
    count3 += 1
    with out3:
        clear_output()
        if count3 % 2 == 0:
            display(text3_1)
            
display(VBox([button2_step1, out3]))
button2_step1.on_click(on_button2_step1_clicked)

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out4 = Output()
button2_step2 = widgets.Button(description="Step Two", layout=Layout(width='20%', height='100%'), button_style='primary')
count4 = 1

text4_1 = widgets.HTMLMath(value=r"We write what we are given. We place the unit and the element that we wish to cancel in the denominator of the molar ratio. We write what we wish to convert to (moles of NH$_3$) in the numerator:")
text4_2 = widgets.HTMLMath(value=r"$3.6 \text{ mol H}_2 \bigg(\dfrac{2\text{ mol NH}_3}{3\text{ mol H}_2}\bigg)=2.4 \text{ mol NH}_3$")

def on_button2_step2_clicked(b):
    global count4
    count4 += 1
    with out4:
        clear_output()
        if count4 % 2 == 0:
            display(text4_1, text4_2)
            
display(VBox([button2_step2, out4]))
button2_step2.on_click(on_button2_step2_clicked)

### Practice

Use the chemical equation below to answer the following question(s). Remember to balance it before proceeding.

<br />
<center>____ KClO$_3$ + ____ KCl $\rightarrow$ ____ O$_2$</center>

#from IPython.display import Javascript, display
#from ipywidgets import widgets

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Randomize variables
mole_amount = round(random.uniform(10.0, 50.0), 1)

#Determine question type
question_type = random.randint(1,3)

if question_type == 1:
    #Print question
    question = "If the reaction produced {} moles of oxygen, how many moles of potassium chlorate decomposed?".format(mole_amount)
    print(question)
    #Answer
    substance_choice = "potassium chlorate"
    answer = mole_amount * (2/3)
elif question_type == 2:
    question = "Given {} moles of potassium chlorate, how many moles of potassium chloride will be produced?".format(mole_amount)
    print(question)
    #Answer
    substance_choice = "potassium chloride"
    answer = mole_amount * (2/2)
elif question_type == 3:
    question = "If the reaction produced {} moles of potassium chloride, how many moles of oxygen were produced?".format(mole_amount)
    print(question)
    #Answer
    substance_choice = "oxygen"
    answer = mole_amount * (3/2)


#Define range of values for random multiple choices
mini = 100
maxa = 1000

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(round(answer, 1)) + " moles " + substance_choice
option_2 = str(round(choice_list[0]/10, 1)) + " moles " + substance_choice
option_3 = str(round(choice_list[1]/10,1)) + " moles " + substance_choice
option_4 = str(round(choice_list[2]/10,1)) + " moles " + substance_choice

multiple_choice(option_1, option_2, option_3, option_4)

### Additional Resource

If you're still confused regarding the material above, this video should clear things up.

from IPython.display import YouTubeVideo
YouTubeVideo('7qoR8jmmnYQ')

### Stoichiometry Involving Mass, Particles, and Volume

Converting from moles of one substance to moles of another is the fundamental goal of stoichiometry. We now use the mole ratio to convert between particles, grams, and litres.

### Example

**1)** Consider the combustion of butane (C$_4$H$_{10}$):

<br />
<center>____ C$_4$H$_{10}$ + ____ O$_2$ $\rightarrow$ &nbsp; &nbsp; &nbsp; &nbsp; ?</center>

Calculate the mass of CO$_2$ produced when 1.00 g of C$_4$H$_{10}$ is burned.

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out6 = Output()
button3_step1 = widgets.Button(description="Step One", layout=Layout(width='20%', height='100%'), button_style='primary')
count5 = 1

text5_1 = widgets.HTMLMath(value=r"First, we predict the products (a combustion reaction) and balance the above equation: 2C$_4$H$_{10}$ + 13O$_2$ $\rightarrow$ 10H$_2$O + 8CO$_2$")
text5_2 = widgets.HTMLMath(value=r"Recall: H$_2$O and CO$_2$ are always the products of a combustion reaction.")

def on_button3_step1_clicked(b):
    global count5
    count5 += 1
    with out6:
        clear_output()
        if count5 % 2 == 0:
            display(text5_1, text5_2)
            
display(VBox([button3_step1, out6]))
button3_step1.on_click(on_button3_step1_clicked)

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out7 = Output()
button3_step2 = widgets.Button(description="Step Two", layout=Layout(width='20%', height='100%'), button_style='primary')
count6 = 1

text6_1 = widgets.HTMLMath(value=r"We wish to move from grams of C$_4$H$_{10}$ to grams of CO$_2$. On the diagram above, put your finger on where we should begin and trace to where we should end: grams (C$_4$H$_{10}$) $\rightarrow$ moles (C$_4$H$_{10}$) $\rightarrow$ moles (CO$_2$) $\rightarrow$ grams (CO$_2$).")
text6_2 = widgets.HTMLMath(value=r"$1.00 \text{ g }C_4H_{10} \bigg(\dfrac{1\text{ mol}}{52.07\text{ g}}\bigg)\bigg(\dfrac{8 \text{ mol CO}_2}{2 \text{ mol }C_4H_{10}}\bigg)\bigg(\dfrac{44.01 \text{ g}}{1 \text{ mol}}\bigg)=3.38 \text{ g CO}_2$")
text6_3 = widgets.HTMLMath(value=r"Recall: To move between grams and moles we require the molar mass, which is 52.07 g/mol for C$_4$H$_{10}$ and 44.01 g/mol for CO$_2$.")
def on_button3_step2_clicked(b):
    global count6
    count6 += 1
    with out7:
        clear_output()
        if count6 % 2 == 0:
            display(text6_1, text6_2, text6_3)
            
display(VBox([button3_step2, out7]))
button3_step2.on_click(on_button3_step2_clicked)

**2)** The decomposition of potassium chlorate is often used to prepare small amounts of oxygen in many labs.

<br />
<center>____ KClO$_3$ $\rightarrow$ &nbsp; &nbsp; &nbsp; &nbsp; ?</center>

How many millilitres of oxygen gas can be prepared from 4.50 g of potassium chlorate?

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out8 = Output()
button4_step1 = widgets.Button(description="Step One", layout=Layout(width='20%', height='100%'), button_style='primary')
count7 = 1

text7_1 = widgets.HTMLMath(value=r"First, we predict the products (a decomposition reaction) and balance the above equation: 2KClO$_3$ $\rightarrow$ 2KCl + 3O$_2$")
text7_2 = widgets.HTMLMath(value=r"Recall: If 'M' represents a metal, then MClO$_3$ $\rightarrow$ MCl + O$_2$.")

def on_button4_step1_clicked(b):
    global count7
    count7 += 1
    with out8:
        clear_output()
        if count7 % 2 == 0:
            display(text7_1, text7_2)
            
display(VBox([button4_step1, out8]))
button4_step1.on_click(on_button4_step1_clicked)

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out9 = Output()
button4_step2 = widgets.Button(description="Step Two", layout=Layout(width='20%', height='100%'), button_style='primary')
count8 = 1

text8_1 = widgets.HTMLMath(value=r"Following the above diagram, the order of conversions is as follows: g (O$_2$) $\rightarrow$ mol (O$_2$) $\rightarrow$ mol (KClO$_3$) $\rightarrow$ L (KClO$_3$) $\rightarrow$ mL (KClO$_3$).")
text8_2 = widgets.HTMLMath(value=r"$4.50 \text{ g KClO}_3 \bigg(\dfrac{1\text{ mol}}{122.55\text{ g}}\bigg)\bigg(\dfrac{3 \text{ mol O}_2}{2 \text{ mol KClO}_3}\bigg)\bigg(\dfrac{22.4 \text{ L}}{1 \text{ mol}}\bigg)\bigg(\dfrac{1000 \text{ mL}}{1 \text{ L}}\bigg)=1230 \text{ mL O}_2$")
text8_3 = widgets.HTMLMath(value=r"Recall: To move between litres and moles (assuming that the reaction takes place at standard temperature and pressure (STP) we use the conversion 22.4 L/mol.")
def on_button4_step2_clicked(b):
    global count8
    count8 += 1
    with out9:
        clear_output()
        if count8 % 2 == 0:
            display(text8_1, text8_2, text8_3)
            
display(VBox([button4_step2, out9]))
button4_step2.on_click(on_button4_step2_clicked)

### Practice

Mixing solid zinc with a solution of hydrochloric acid is used to produce hydrogen gas (remember to balance):

<br />
<center>____ Zn + ____ HCl $\rightarrow$ ____ ZnCl$_2$ + ____ H$_2$</center>

#from IPython.display import Javascript, display
#from ipywidgets import widgets

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Randomize variables
particle_amount = round(random.uniform(5.0, 9.9), 2)
exact_amount = particle_amount * 10**23
#Determine question type
question_type = random.randint(1,2)

if question_type == 1:
    #Print question
    question = "If you had {} ".format(particle_amount) + chr(0x2A09) + " 10" + chr(0x00B2) + chr(0x00B3) + " atoms of zinc, how many millilitres of hydrogen would be produced?"
    print(question)
    #Answer
    substance_choice = " mL hydrogen"
    answer = (exact_amount / (6.02 * 10**23)) * 22.4 * 1000
elif question_type == 2:
    question = "If you had {} ".format(particle_amount) + chr(0x2A09) + " 10" + chr(0x00B2) + chr(0x00B3) + " molecules of hydrochloric acid, how many grams of zinc are required for this reaction to take place?"
    print(question)
    #Answer
    substance_choice = " g Zn"
    answer = (exact_amount / (6.02 * 10**23)) / 2 * 65.41


#Define range of values for random multiple choices
mini = 10
maxa = 20000

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)

#Round options to the specified number of significant figures
def round_sf(number, significant):
    return round(number, significant - len(str(number)))

#Assign each multiple choice to these four variables
#Option_1 contains the answer
if answer < 100:
    option_1 = str("%0.1f" % answer) + substance_choice
else:
    option_1 = str(round_sf(int(answer), 3)) + substance_choice
    
option_2 = str(round_sf(int(choice_list[0]), 3)) + substance_choice
option_3 = str(round_sf(int(choice_list[1]),3)) + substance_choice
option_4 = str(round_sf(int(choice_list[2]),3)) + substance_choice

multiple_choice(option_1, option_2, option_3, option_4)

### Additional Resource

If you're still confused regarding the material above, this video should clear things up.

from IPython.display import YouTubeVideo
YouTubeVideo('Auq_tXHKXW8')

## Limiting Reactants

Before defining what a limiting reactant is, we first present a very simple example to demonstrate the concept.

**Silly (but useful) example:** Suppose you wish to make several extremely boring sandwiches using one slice of cheese and two slices of bread for each. Then, let

- Bd = bread
- Ch = cheese
- Bd$_2$Ch = sandwich

<img style="float: center;" src="images/BreadCheese.PNG" height="300" width="200">

So then we have the following equation:
<br />
<center> 2Bd + Ch $\rightarrow$ Bd$_2$Ch</center>

**Problem:** *If you have 10 slices of bread and 7 slices of cheese, how many sandwiches can you make? What will be leftover?*

**Solution:** This can be done mentally; however, here's the basic computation that is required:

<br />
<div style="text-align: left"> 10 Bd$\bigg(\dfrac{1\: \text{Bd}_2\text{Ch}}{2\: \text{Bd}}\bigg) =$ 5 Bd$_2$Ch </div>

Therefore, we can make 5 sandwiches and so 2 slices of cheese are leftover.

A **limiting reactant** is the reactant that is completely consumed in a reaction. It will determine, or limit, the amount of product formed. The other reactants are called **excess reactants**. These reactants are added to a reaction in larger than necessary amounts.

In the previous question, which was limiting? Will the *bread* run out first or will the *cheese* run out first? Answer: The bread is the limiting reactant and the cheese is in excess. *How do we know?*

**Key Steps**: Given the information (10 slices of bread and 7 slices of cheese in this case) we must do the following:

1. *Choose one of the values to work with. It doesn't matter which.* 

Let's choose the first value to work with. So we'll start with 10 slices of bread.
2. *Using stoichiometry, start with your chosen value and convert that value (using the appropriate molar ratio) into the other reactant.*

<div style="text-align: left"> 10 Bd$\bigg(\dfrac{1\: \text{Ch}}{2\: \text{Bd}}\bigg) =$ 5 Ch </div>

3. *Compare the result from Step 2 with the corresponding value that you are given in the question. Step 2 tells us **how much we need** of the other reactant for a perfect reaction; i.e. if we are given **more** than what Step 2 gives us, then that reactant is in excess.*

We are given **7 slices of cheese**. From Step 2, we calculated that (given 10 slices of bread) we **only need 5 slices of cheese**. Since $7 > 5$, **cheese is in excess** and **bread** is the **limiting reactant (LR)**.

### Example

Consider the following synthesis reaction:

<br />
<center>____ Fe + ____ Cl$_2$ $\rightarrow$ ____ FeCl$_3$</center>

If 11.2 g of iron is reacted with 23.4 g of chlorine, iron (III) chloride is formed.

**1)** *Which reactant is in excess? Which reactant is limiting?*

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out11 = Output()
button5_step1 = widgets.Button(description="Step One", layout=Layout(width='20%', height='100%'), button_style='primary')
count9 = 1

text9_1 = widgets.HTMLMath(value=r"First, we balance the above equation: 2Fe + 3Cl$_2$ $\rightarrow$ 2FeCl$_3$")
text9_2 = widgets.HTMLMath(value=r"Next, we follow the 'Key Steps' above. Choose one of the reactants to work with, say Fe.")


def on_button5_step1_clicked(b):
    global count9
    count9 += 1
    with out11:
        clear_output()
        if count9 % 2 == 0:
            display(text9_1, text9_2)
            
display(VBox([button5_step1, out11]))
button5_step1.on_click(on_button5_step1_clicked)

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out12 = Output()
button5_step2 = widgets.Button(description="Step Two", layout=Layout(width='20%', height='100%'), button_style='primary')
count10 = 1

text10_1 = widgets.HTMLMath(value=r"With 11.2 g of Fe, how much Cl$_2$ is required for a perfect reaction?")
text10_2 = widgets.HTMLMath(value=r"11.2 g Fe $\bigg(\dfrac{1\text{ mol}}{55.85\text{ g}}\bigg)\bigg(\dfrac{3\text{ mol Cl}_2}{2\text{ mol Fe}}\bigg)\bigg(\dfrac{70.90\text{ g}}{1\text{ mol}}\bigg)=$ 21.3 g Cl$_2$")
text10_3 = widgets.HTMLMath(value=r"Note: 21.3 g Cl$_2$ is exactly how much Cl$_2$ you NEED for a PERFECT reaction (i.e. reacting 11.2 g Fe with 21.3 g Cl$_2$ would result in NO EXCESS reactant).")


def on_button5_step2_clicked(b):
    global count10
    count10 += 1
    with out12:
        clear_output()
        if count10 % 2 == 0:
            display(text10_1, text10_2, text10_3)
            
display(VBox([button5_step2, out12]))
button5_step2.on_click(on_button5_step2_clicked)

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out13 = Output()
button5_step3 = widgets.Button(description="Step Three", layout=Layout(width='20%', height='100%'), button_style='primary')
count11 = 1

text11_1 = widgets.HTMLMath(value=r"Compare that value (21.3 g Cl$_2$) with the given Cl$_2$ value (from the question): 23.4 g $>$ 21.3 g $\implies$ Cl$_2$ is in excess. Therefore, Fe is the LR.")

def on_button5_step3_clicked(b):
    global count11
    count11 += 1
    with out13:
        clear_output()
        if count11 % 2 == 0:
            display(text11_1)
            
display(VBox([button5_step3, out13]))
button5_step3.on_click(on_button5_step3_clicked)

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out14 = Output()
button5_step4 = widgets.Button(description="NOTE", layout=Layout(width='20%', height='100%'), button_style='warning')
count12 = 1

text12_1 = widgets.HTMLMath(value=r"What if we started with 23.4 g of Cl$_2$ instead of 11.2 g of Fe? The stategy is exactly the same. We show the work below:")
text12_2 = widgets.HTMLMath(value=r"23.4 g Cl$_2$ $\bigg(\dfrac{1\text{ mol}}{70.90\text{ g}}\bigg)\bigg(\dfrac{2\text{ mol Fe}}{3\text{ mol Cl}_2}\bigg)\bigg(\dfrac{55.85\text{ g}}{1\text{ mol}}\bigg)=$ 12.3 g Fe")
text12_3 = widgets.HTMLMath(value=r"Since 11.2 g Fe $<$ 12.3 g Fe, we don't start with enough Fe for a perfect reaction $\implies$ Fe is the LR and Cl$_2$ must be excess.")
                            
def on_button5_step4_clicked(b):
    global count12
    count12 += 1
    with out14:
        clear_output()
        if count12 % 2 == 0:
            display(text12_1, text12_2, text12_3)
            
display(VBox([button5_step4, out14]))
button5_step4.on_click(on_button5_step4_clicked)

**2)** *Calculate the mass of the excess.*

Because we chose to work with Fe first (which was a completely random choice) we calculated that we require exactly 21.3 g of Cl$_2$ for a perfect reaction. Also, it worked out that Cl$_2$ is in excess, which means that we simply perform the following subtraction:

<br />
<center> 23.4 g - 21.3 g = 2.1 g Cl$_2$ </center>

Note: If we chose to work with Cl$_2$ first (instead of Fe) then, while we would still have been able to find which is limiting (see "NOTE" above), we would have to perform the calculation to find 21.3 g of Cl$_2$ required for a perfect reaction.

**3)** *Calculate the mass of the product.*

The whole point of determining which reactant is limiting is precisely to find how much product will be produced. *Always use the mass of the **limiting reactant** to calculate the mass of the product!*

Since Fe is the LR, we must start with that mass and convert it to the mass of the product (FeCl$_3$):

<br />
<center> 11.2 g Fe $\bigg(\dfrac{1\text{ mol}}{55.85\text{ g}}\bigg)\bigg(\dfrac{2\text{ mol FeCl}_3}{2\text{ mol Fe}}\bigg)\bigg(\dfrac{162.2\text{ g}}{1\text{ mol}}\bigg)=$ 32.5 g FeCl$_3$ </center>

### Interactive Example

Recall the chemical reaction (from above):

<br />
<center> 2Fe + 3Cl$_2$ $\rightarrow$ 2FeCl$_3$</center>

Use the sliders below to dynamically adjust the mass of both reactants. As you adjust the mass of the reactants, observe the changes in limiting reactant, mass of excess, and the mass of product.

out_text = Output()

################ Widgets #################
style = {'description_width': 'initial'}
reactant1_slider = widgets.FloatSlider(continuous_update=False, wait=True, value=11.2, min=10, max=100, step=0.1, description="Fe (g)", style=style)
reactant2_slider = widgets.FloatSlider(continuous_update=False, wait=True, value=21.3, min=10, max=100, step=0.1, description="Cl" + chr(0x2082) + " (g)", style=style)
calc = widgets.Button(description="Calculate LR and Excess", layout=Layout(width='20%', height='88%'),button_style='success')
###########################################

display(VBox([reactant1_slider, reactant2_slider, calc]))

#############################################

def on_submit_button_clicked(b):
    #Answers
    Fe_first = reactant1_slider.value * (1/55.85) * (3/2) * (70.9/1)
    Cl_first = reactant2_slider.value * (1/70.9) * (2/3) * (55.85/1)

    if reactant2_slider.value > Fe_first:
        LR1 = "Fe"
        Excess1 = "Cl" + chr(0x2082)
        amount_excess1 = round(reactant2_slider.value - Fe_first,1)
        mass_product1 = round(reactant1_slider.value * (1/55.85) * (2/2) * (162.2/1),1)
    else:
        amount_excess1 = round(reactant1_slider.value - Cl_first,1)
        if amount_excess1 == 0:
            LR1 = "None"
            Excess1 = "None"
        else:
            LR1 = "Cl" + chr(0x2082)
            Excess1 = "Fe"
        
        mass_product1 = round(reactant2_slider.value * (1/32) * (2/1) * (18.016/1),1)
    
    with out_text:
        clear_output()
        text_answer1 = widgets.HTMLMath(value=r"LR: {}; Excess: {}, Mass of Excess: {} g; Mass of Product: {} g".format(LR1, Excess1, str(amount_excess1), str(mass_product1)))    
        display(text_answer1)

### Widget Interaction Function Calls ###
calc.on_click(on_submit_button_clicked)

display(out_text)

### Practice

Given the following reaction:

<br />
<center> 2H$_2$ + O$_2$ $\rightarrow$ 2H$_2$O</center>

Determine which reactant is in excess and which is limiting and calculate the mass of the excess and product. Round all answers to one decimal place. The mass of the reactants are given below.

#from IPython.display import Javascript, display
#from ipywidgets import widgets

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Randomize variables
H_amount = round(random.uniform(10.0, 100.0), 1)
O_amount = round(random.uniform(10.0, 200.0), 1)

amount_sentence = "Starting amount of hydrogen: {} g; Starting amount of oxygen: {} g".format(H_amount, O_amount)
print(amount_sentence)

#Answers
H_first = H_amount * (1/2.016) * (1/2) * (32/1)
O_first = O_amount * (1/32) * (2/1) * (2.016/1)

if O_amount > H_first:
    LR = "H" + chr(0x2082)
    Excess = "O" + chr(0x2082)
    amount_excess = round(O_amount - H_first,1)
    mass_product = round(H_amount * (1/32) * (2/2) * (18.016/1),1)
else:
    LR = "O" + chr(0x2082)
    Excess = "H" + chr(0x2082)
    amount_excess = round(H_amount - O_first,1)
    mass_product = round(O_amount * (1/32) * (2/1) * (18.016/1),1)

#Random Variations in Answer
wrong_answers = random.sample(range(1, 50), 6)

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "LR: {}; Excess: {}, Mass of Excess: {} g; Mass of Product: {} g".format(LR, Excess, str(amount_excess), str(mass_product))    
option_2 = "LR: {}; Excess: {}, Mass of Excess: {} g; Mass of Product: {} g".format(LR, Excess, str(amount_excess + wrong_answers[0]), str(mass_product + wrong_answers[1]))    
option_3 = "LR: {}; Excess: {}, Mass of Excess: {} g; Mass of Product: {} g".format(Excess, LR, str(amount_excess + wrong_answers[2]), str(mass_product + wrong_answers[3]))    
option_4 = "LR: {}; Excess: {}, Mass of Excess: {} g; Mass of Product: {} g".format(Excess, LR, str(amount_excess + wrong_answers[4]), str(mass_product + wrong_answers[5]))    

multiple_choice(option_1, option_2, option_3, option_4)

### Additional Resource

If you're still confused regarding the material above, this video should clear things up.

from IPython.display import YouTubeVideo
YouTubeVideo('pdoBH6Cg__o')

## Conclusion

- **Stoichiometry** is the calculation of relative quantities of reactants and products in chemical reactions. It allows us to:
    - Predict how much product will form in chemical reactions.
    - Determine which reactant is in excess and which is limiting.


- The coefficients in a balanced chemical equation indicate both the relative numbers of molecules in the reaction and the relative number of moles.


- A **limiting reactant** is the reactant that is completely consumed in a reaction. It will determine, or limit, the amount of product formed.


- **Excess reactants** are reactants that are added to a reaction in larger than necessary amounts.


- Use the **three step process** outlined above to determine which reactant is limiting, in excess, and to determine the mass of the products.

*Images and content in this notebook are by [DanPalmarin](https://palmarin.weebly.com)*

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