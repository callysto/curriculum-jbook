![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)
 
<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fonline-courses&branch=master&subPath=Mathematics/ProbabilityExperiment/probability-experiment.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"></a>

To run this notebook press the >> Button and confirm "Restart and Run all".

![](./images/RunB.png)

from IPython.display import HTML

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
The raw code for this IPython notebook is by default hidden for easier reading.
To toggle on/off the raw code, click <a href="javascript:code_toggle()">here</a>.''')


%%html
<style>
.output_wrapper button.btn.btn-default,
.output_wrapper .ui-dialog-titlebar {
  display: none;
}
</style>

# Modules

import string
import numpy as np
import pandas as pd
import qgrid as q
import matplotlib.pyplot as plt

# Widgets & Display modules, etc..

from ipywidgets import widgets as w
from ipywidgets import Button, Layout
from IPython.display import display, Javascript, Markdown

# grid features for interactive grids 

grid_features = { 'fullWidthRows': True,
                  'syncColumnCellResize': True,
                  'forceFitColumns': True,
                  'rowHeight': 40,
                  'enableColumnReorder': True,
                  'enableTextSelectionOnCells': True,
                  'editable': True,
                  'filterable': False,
                  'sortable': False,
                  'highlightSelectedRow': True}

from ipywidgets import Button , Layout , interact,widgets
from IPython.display import Javascript, display

# Function: executes previous cell on button widget click event and hides achievement indicators message

def run_current(ev):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+0,IPython.notebook.get_selected_index()+1)'))    
    
# Counter for toggling achievement indicator on/off

button_ctr = 0

# Achievement Indicators

line_1 = "#### Achievement Indicators"
line_2 = "**General Outcome:**"
line_3 = "* The general outcome of this notebook is to use experimental or theoretical probabilities to represent and solve problems involving uncertainty."
line_4 = "**Specific Outcome 4:**"
line_5 = "* Express probabilities as ratios, fractions and percents."
line_6 = "**Specific Outcome 5:**"
line_7 = "* Identify the sample space (where the combined sample space has 36 or fewer elements) for a probability experiment involving two independent events.*"
line_8 = "**Specific Outcome 6:**"
line_9 = "* Conduct a probability experiment to compare the theoretical probability (determined using a tree diagram, table or other graphic organizer) and experimental probability of two independent events*"

# Use to print lines, then save in lines_list

def print_lines(n):
    
    lines_str = ""
    
    for i in range(1,n+1):
        lines_str = lines_str + "line_"+str(i)+","
        
    lines_str = lines_str[:-1]

    print(lines_str)
    
lines_list = [line_1,line_2,line_3,line_4,line_5,line_6,line_7,line_8,line_9]
    
# Show/Hide buttons

ai_button_show = widgets.Button(button_style='info',description="Show Achievement Indicators", layout=Layout(width='25%', height='30px') )
ai_button_hide = widgets.Button(button_style='info',description="Hide Achievement Indicators", layout=Layout(width='25%', height='30px') )

display(Markdown("For instructors:"))

button_ctr += 1

if(button_ctr % 2 == 0):

    for line in lines_list:
        display(Markdown(line))
    
    display(ai_button_hide)
    ai_button_hide.on_click( run_current )
    
else:

    display(ai_button_show)
    ai_button_show.on_click( run_current )

# Statistics and Probability 

## Chance and Uncertainty

#### Grade 11  Math 

<h2 align='center'>Overview</h2>

In this notebook we will explore basic notions and properties about expressing and manipulating probabilities. 
The general outcome of this notebook is to use experimental or theoretical probabilities to represent and solve problems involving uncertainty.

<h2 align='center'>Probabilities as ratios, fractions and percents</h2>

A natural question to ask is: how do we measure the probability associated to an event of a given probability experiment, i.e. for a given event, what is the probability it occurs?  We define this now, illustrate with a simple example involving dice, and we will then provide an interactive exercise. 


<div class="alert alert-warning">
<font color="black"><b>Definition.</b> The probability of an event is the ratio between the size of the event (as a collection of outcomes) and the size of the sample space. </font>
</div>

The sample space of rolling a single dice is given by $\lbrace$1,2,3,4,5,6 $\rbrace$ and had sample size 6.  If we assume each face is equally likely to occur (i.e. the dice is unbiased), then the probability of getting each face is the ratio or fraction $\dfrac{1}{6}$. 

We will denote the probability of getting each number as $P(i)$, where $i$ can either be 1,2,3,4,5,6. 
Then, the probability of getting event 1, denoted $P(1)$ is equal to $\dfrac{1}{6}$; more precisely: $P(1)=P(2)=P(3)=P(4)=P(5)=P(6)=\dfrac{1}{6}$.

This is equivalent to stating that the probability of getting any given face is 1 in 6, or $1:6$. Using ratios we have $P(i) = 1:6$, where $i = 1,2,3,4,5,6$. We can also express probabilities using percents. The total number of outcomes is considered 100%. Since there are 6 possible outcomes and assuming equal probability, $P(i) = 100 / 6  = 16.67 \%$. 

We summarize in the table below.

|Event  $i$                  |1 |2 |3 |4 |5 |6 |
|----------------------------|--|--|--|--|--|--|
|Probability $P(i)$ as a fraction|$\dfrac{1}{6}$|$\dfrac{1}{6}$|$\dfrac{1}{6}$|$\dfrac{1}{6}$|$\dfrac{1}{6}$|$\dfrac{1}{6}$|
|Probability $P(i)$ as a ratio            |1:6|1:6|1:6|1:6|1:6|1:6|
|Probability $P(i)$ as a percent|16.67%|16.67%|16.67%|16.67%|16.67%|16.67%|

import numpy as np
import matplotlib 
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
import matplotlib.gridspec as gridspec
import ipywidgets
from ipywidgets import interact,interact_manual,widgets
%matplotlib inline

### Interactive Example: Probabilities as Fractions, Ratios and Percents

The widget below illustrates a probability experiment using roulettes of various sizes. The basic experiment consists in spinning  a roulette, divided in a given number of compartments, each of the same size and associated with a unique number that identifies it. The outcome of the experiment is the compartment of the roulette whose number shows in red. Basically, this is an experiment similar to rolling a dice, but where we control the number of faces (number of compartments in the roulette). We assume the roulette is unbiased: each compartment has the same chance to appear in red whenspinning the roulette.

On the upper side of the widget you find a drop down menu indicating the size of the sample space, which is the number of compartments of the roulette. In this case, we are considering roulettes whose outcomes are integers from 1 to the size of the sample space. We consider roulettes with sample spaces of size 2, 4, 6 and 8.

Below the drop down menu you will find find a red button. Click it to play. 

On the left hand side of the widget you will see a roulette with numbers in black and one number in red. The number in red corresponds to the outcome of the experiment. 

On the right hand side you will find a printed message explaining what the probability of the event associated to the obtained outcome is. 

Play multiple times to simulate what would happen if you spun the roulette. Change the size of the sample space to learn what the different probabilities associated to each event in the roulette are. 

### 
def roulette(number_parititions,value):
    if value==True or value==False:
        lucky_number_one = random.choice(np.arange(1,2*number_parititions+1))

        
        axalpha = 0.05
        figcolor = 'white'
        dpi = 80
        fig = plt.figure(figsize=(15,10), dpi=dpi,facecolor='black')
        plt.subplot(211)

        plt.subplot(212)

        fig.patch.set_edgecolor(figcolor)
        fig.patch.set_facecolor(figcolor)
        ax = plt.subplot(121,projection='polar',facecolor="red")
        

        ax.patch.set_alpha(axalpha)
        ax.set_axisbelow(True)
        
        ax1 = plt.subplot(122)
        ax1.grid(False)
        ax1.set_xlim(0.1,0.9)
        ax1.set_ylim(0.4,0.8)
        
        ax1.set_xticklabels([])
        ax1.set_yticklabels([])
        ax1.axis("off")
    
        arc = 2. * np.pi
        N = number_parititions
        theta = np.arange(0.0, arc, arc/N)
        
        if number_parititions == 4:
            radii_ar = [1.0 for i in range(number_parititions)]
            width_ar = [1.0 for i in range(number_parititions)]
    
            radii = 10 * np.array(radii_ar)
            width = np.pi/4  * np.array(width_ar)
    
            bars = ax.bar(theta, radii, width=width, bottom=0.0)
            for r, bar in zip(radii, bars):
                bar.set_facecolor("pink")
                bar.set_alpha(0.6)
            
            ax.text(0, 7, "1", fontsize=20,transform=ax.transData._b,)
            ax.text(5, 5, "2", fontsize=20,transform=ax.transData._b)
            ax.text(7, 0, "3", fontsize=20,transform=ax.transData._b)
            ax.text(4, -5.5, "4", fontsize=20,transform=ax.transData._b)
            ax.text(0, -7, "5", fontsize=20,transform=ax.transData._b)
            ax.text(-5, -5, "6", fontsize=20,transform=ax.transData._b)
            ax.text(-5, 5, "8", fontsize=20,transform=ax.transData._b)
            ax.text(-7, 0, "7", fontsize=20,transform=ax.transData._b)
            
            if lucky_number_one==1:
                ax.text(0, 7, "1", fontsize=20,transform=ax.transData._b,color="red")
            elif lucky_number_one==2:
                ax.text(5, 5, "2", fontsize=20,transform=ax.transData._b,color="red")
            elif lucky_number_one==3:
                ax.text(7, 0, "3", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==4:
                ax.text(4, -5.5, "4", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==5:
                ax.text(0, -7, "5", fontsize=20,transform=ax.transData._b,color="red")
            elif lucky_number_one==6:
                ax.text(-5, -5, "6", fontsize=20,transform=ax.transData._b,color="red")
            elif lucky_number_one==7:
                ax.text(-7, 0, "7", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==8:
                ax.text(-5, 5, "8", fontsize=20,transform=ax.transData._b,color='red')
            ax1.text(0.1,0.77,"Probability of each event",fontsize=25)
            ax1.text(0.1,0.5,"P(1) = 1/8 = 1:8 = 12.5%\n\nP(2) = 1/8 = 1:8 = 12.5%\n\nP(3) = 1/8 = 1:8 = 12.5%\n\nP(4) = 1/8 = 1:8 = 12.5%\n\nP(5) = 1/8 = 1:8 = 12.5%\n\nP(6) = 1/8 = 1:8 = 12.5%\n\nP(7) = 1/8 = 1:8 = 12.5%\n\nP(8) = 1/8 = 1:8 = 12.5%"\
                      ,fontsize=20)
            ax1.text(0.1,0.45,"Probability Outcome",fontsize=25)
            ax1.text(0.1,0.42,"The result after spinning is " + str(lucky_number_one),fontsize=20)

        elif number_parititions == 3:
    
            radii_ar = [1.0 for i in range(number_parititions)]
            width_ar = [1.3 for i in range(number_parititions)]
    
            radii = 10 * np.array(radii_ar)
            width = np.pi/4  * np.array(width_ar)
    
            bars = ax.bar(theta, radii, width=width, bottom=0.0)
            for r, bar in zip(radii, bars):
                bar.set_facecolor("pink")
                bar.set_alpha(0.6)
            ax.text(-4, 7, "1", fontsize=20,transform=ax.transData._b)
            ax.text(3, 6.5, "2", fontsize=20,transform=ax.transData._b)
            ax.text(7, 0, "3", fontsize=20,transform=ax.transData._b)
            ax.text(3, -6.5, "4", fontsize=20,transform=ax.transData._b)
            ax.text(-4, -7, "5", fontsize=20,transform=ax.transData._b)
            ax.text(-8, 0, "6", fontsize=20,transform=ax.transData._b)
            
            if lucky_number_one==1:
                ax.text(-4, 7, "1", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==2:
                ax.text(3, 6.5, "2", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==3:
                ax.text(7, 0, "3", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==4:
                ax.text(3, -6.5, "4", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==5:
                ax.text(-4, -7, "5", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==6:
                ax.text(-8, 0, "6", fontsize=20,transform=ax.transData._b,color='red')
            
            ax1.text(0.1,0.74,"Probability of each event",fontsize=25)
            ax1.text(0.1,0.55,"P(1) = 1/6 = 1:6 = 16.67%\n\nP(2) = 1/6 = 1:6 = 16.67%\n\nP(3) = 1/6 = 1:6 = 16.67\n\nP(4) = 1/6 = 1:6 = 16.67%\n\nP(5) = 1/6 = 1:6 = 16.67%\n\nP(6) = 1/6 = 1:6 = 16.67%"\
                      ,fontsize=20)
            ax1.text(0.1,0.5,"Probability Outcome",fontsize=25)
            ax1.text(0.1,0.48,"The result after spinning is " + str(lucky_number_one),fontsize=20)

            
        elif number_parititions == 2:
            radii_ar = [1.0 for i in range(number_parititions)]
            width_ar = [1.7 for i in range(number_parititions)]
    
            radii = 10 * np.array(radii_ar)
            width = np.pi/4  * np.array(width_ar)
    
            bars = ax.bar(theta, radii, width=width, bottom=0.0)
            for r, bar in zip(radii, bars):
                bar.set_facecolor("pink")
                bar.set_alpha(0.6)
            ax.text(0, 8, "1", fontsize=20,transform=ax.transData._b)
            ax.text(7, 0, "2", fontsize=20,transform=ax.transData._b)
            ax.text(0, -8, "3", fontsize=20,transform=ax.transData._b)
            ax.text(-8, 0, "4", fontsize=20,transform=ax.transData._b)
            
            if lucky_number_one==1:
                ax.text(0, 8, "1", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==2:
                ax.text(7, 0, "2", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==3:
                ax.text(0, -8, "3", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==4:
                ax.text(-8, 0, "4", fontsize=20,transform=ax.transData._b,color='red')
            
            ax1.text(0.1,0.74,"Probability of each event",fontsize=25)
            ax1.text(0.1,0.6,"P(1) = 1/4 = 1:4 = 25%\n\nP(2) = 1/4 = 1:4 =25%\n\nP(3) = 1/4 = 1:4 =25%\n\nP(4) = 1/4 = 1:4 =25%",fontsize=20)
            #ax1.text(0.1,0.5,"This is equivalent to 50%.",fontsize=20)
            ax1.text(0.1,0.54,"Probability Outcome",fontsize=25)
            ax1.text(0.1,0.52,"The result after spinning is " + str(lucky_number_one),fontsize=20)


        elif number_parititions == 1:
            radii_ar = [1.0 for i in range(number_parititions)]
            width_ar = [4 for i in range(number_parititions)]
    
            radii = 10 * np.array(radii_ar)
            width = np.pi/4  * np.array(width_ar)
    
            bars = ax.bar(theta, radii, width=width, bottom=0.0)
            for r, bar in zip(radii, bars):
                bar.set_facecolor("pink")
                bar.set_alpha(0.6)
            ax.text(8, 0, "1", fontsize=20,transform=ax.transData._b)
            ax.text(-8, 0, "2", fontsize=20,transform=ax.transData._b)
            
            if lucky_number_one==1:
                ax.text(8, 0, "1", fontsize=20,transform=ax.transData._b,color='red')
            elif lucky_number_one==2:
                ax.text(-8, 0, "2", fontsize=20,transform=ax.transData._b,color='red')
            
            ax1.text(0.1,0.7,"Probability of each event",fontsize=25)
            ax1.text(0.1,0.6,"P(1) = 1/2 = 1:2 = 50%\n\nP(2) = 1/2 = 1:2 =50%",fontsize=20)
            ax1.text(0.1,0.54,"Probability Outcome",fontsize=25)
            ax1.text(0.1,0.52,"The result after spinning is " + str(lucky_number_one),fontsize=20)

        ax.tick_params(labelbottom=False, labeltop=False,
                   labelleft=False, labelright=False)

        ax.grid(False)
        ax.set_yticks(np.arange(1, 9, 2))
        ax1.set_yticks([])
        ax1.set_xticks([])
    
        ax1.set_title("Probabilities as fractions, ratios and percents",fontsize=30)
        plt.show()
    
style = {'description_width': 'initial'}    
lucky = interact(roulette,number_parititions = widgets.Dropdown(
    options={'Two': 1, 'Four': 2, 'Six': 3,'Eight':4},
    value=4,
    description='Size of sample space:',
    style=style
),
    value = widgets.ToggleButton(
        value=True,
        description='Click to Play!',
        disabled=False,
        button_style='danger', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Description',
        icon='check'
    ))


### Question 1

Using fractions, what is the probability of the event 1, denoted $P(1)$, if the sample size of the roulette is 4?

from ipywidgets import interact_manual,widgets


s = {'description_width': 'initial'}        
@interact(answer =widgets.Select(
                    options=["Select option","1/2",\
                            "4","1/3",\
                             "1/4"],
                    value='Select option',
                    description="Probability as fraction",
                    disabled=False,
                    style=s
))

def reflective_angle_question(answer):
    if answer=="Select option":
        print("Click on the correct probability expressed as a fraction.")
    
    elif answer=="1/4":
        print("Correct!\nWith a sample space of size 4, each with equal likelihood, P(1)=1/4.")
    elif answer != "1/4" or answer != "Select Option":
        print("Hint: What is P(1) if P(i) = 1/4 for all i = 1,2,3,4?")

### Question 2

What is P(1) if the size of the sample space is 4, but this time expressed as percent?

from ipywidgets import interact_manual,widgets


s = {'description_width': 'initial'}        
@interact(answer =widgets.Select(
                    options=["Select option","25%",\
                            "100%","40%",\
                             "10%"],
                    value='Select option',
                    description="Probability as percent",
                    disabled=False,
                    style=s
))

def reflective_angle_question(answer):
    if answer=="Select option":
        print("Click on the correct probability expressed in percent.")
    
    elif answer=="25%":
        print("Correct!\nWith four probability events, each with equal likelihood, P(1) = 25%.")
    elif answer != "25%" or answer != "Select Option":
        print("Hint: The total number of outcomes is 4, which corresponds to 100%. What is 100/4?")

### Question 3

Using the widget created above, change the Size of sample space to 8. What is $P(7)$ as a ratio? 

from ipywidgets import interact_manual,widgets


s = {'description_width': 'initial'}        
@interact(answer =widgets.Select(
                    options=["Select option","1:6",\
                            "1:4","1:8",\
                             "1:7"],
                    value='Select option',
                    description="Probability as ratio",
                    disabled=False,
                    style=s
))

def reflective_angle_question(answer):
    if answer=="Select option":
        print("Click on the correct probability expressed as a percentage.")
    
    elif answer=="1:8":
        print("Correct!\nWith eight probability events, each with equal likelihood, \nP(7) =  1:8.")
    elif answer != "1:8" or answer != "Select Option":
        print("Hint: 1 in every 8 corresponds to the event 7. What is P(7) in ratio?")

<h2 align='center'>Independent Events & Sample Space</h2>
<!-- Specific Outcome 5 Identify the sample space (where the combined sample space has 36 or fewer elements) for a probability experiment involving two independent events.-->

In this section, we define the concept of **independent probability experiments** as well as the corresponding sample space, and provide a game where we can experiment with the two concepts. 

<div class="alert alert-warning">
<font color="black"><b>Definition.</b> We say that two probability experiments are <i>independent</i> if the outcome of one does not affect the outcome of the other. </font>
</div>

For example, if we spin two roulettes at the same time, then the two experiments are independent since the outcome of each does not affect the other.

Try spinning the two roulettes below via using the red button. As before, in each the number in red denotes the outcome of the experiment. These two roulettes are not linked and as you can see from a few spins, their outcomes are not related at all: spinning them are independent experiments.

def spin(value):
    if value==True or value==False:
        
        lucky_number_one = random.choice([1,2,3,4,5,6])
        
        lucky_number_one_c = random.choice([1,2,3,4,5,6])
        
        x_t,y_t = [i/10 for i in range(10)],[i/10 for i in range(10)]

        axalpha = 0.05
        figcolor = 'white'
        dpi = 80
        
        gs = gridspec.GridSpec(2, 3)
        fig = plt.figure(figsize=(15,8), dpi=dpi,facecolor='black')      

        fig.patch.set_edgecolor(figcolor)
        fig.patch.set_facecolor(figcolor)
        
        ax1 = plt.subplot(gs[0, 0]) 
        ax1.grid(False)
        ax1.axis("Off")
        ax2 = plt.subplot(gs[1, 0]) 
        ax2.grid(False)
        ax2.axis("Off")
        ax5 = plt.subplot(gs[0, 2]) 
        ax5.grid(False)
        ax5.axis("Off")
        ax6 = plt.subplot(gs[1, 2]) 
        ax6.grid(False)
        ax6.axis("Off")
        #ax.axis("Off")
        
        ax = plt.subplot(gs[0,0],projection='polar',facecolor="red") # row 0, col 0
        plt.plot([0,1])
    
        ax.plot(x_t,y_t,transform=ax.transData._b,color="#FEE9FF",linewidth=5)
            
        ax.patch.set_alpha(axalpha)
        ax.set_axisbelow(True)
    
        number_parititions = 3
        arc = 2. * np.pi
        N = number_parititions
        theta = np.arange(0.0, arc, arc/N)
    
        radii_ar = [1.0 for i in range(number_parititions)]
        width_ar = [1.3 for i in range(number_parititions)]
    
        radii = 10 * np.array(radii_ar)
        width = np.pi/4  * np.array(width_ar)
    
        bars = ax.bar(theta, radii, width=width, bottom=0.0)
        for r, bar in zip(radii, bars):
            bar.set_facecolor("pink")
            bar.set_alpha(0.6)
        ax.text(-4, 7, "1", fontsize=20,transform=ax.transData._b)
        ax.text(3, 6.5, "2", fontsize=20,transform=ax.transData._b)
        ax.text(7, 0, "3", fontsize=20,transform=ax.transData._b)
        ax.text(3, -6.5, "4", fontsize=20,transform=ax.transData._b)
        ax.text(-4, -7, "5", fontsize=20,transform=ax.transData._b)
        ax.text(-8, 0, "6", fontsize=20,transform=ax.transData._b)
        
        if lucky_number_one==1:
            #bar3.set_facecolor("#000000")
            ax.text(-4, 7, "1", fontsize=20,transform=ax.transData._b,color='red')
        elif lucky_number_one==2:
            #bar2.set_facecolor("#000000")
            ax.text(3, 6.5, "2", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==3:
            #bar1.set_facecolor("#000000")
            ax.text(7, 0, "3", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==4:
            #bar6.set_facecolor("#000000")
            ax.text(3, -6.5, "4", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==5:
            #bar5.set_facecolor("#000000")
            ax.text(-4, -7, "5", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==6:
            #bar4.set_facecolor("#000000")
            ax.text(-8, 0, "6", fontsize=20,transform=ax.transData._b,color='red')
        
        ax.tick_params(labelbottom=False, labeltop=False,
                   labelleft=False, labelright=False)

        ax.grid(False)
        ax.axis("On")
        ax.set_title("Top Roulette",fontsize=20)
        
        ax4 = plt.subplot(gs[1, 0],projection='polar',facecolor="red") # row 0, col 0
        plt.plot([0,1])

        ax4.plot(x_t,y_t,transform=ax4.transData._b,color="#FEE9FF",linewidth=5)
        ax4.patch.set_alpha(axalpha)
        ax4.set_axisbelow(True)
    
        bars = ax4.bar(theta, radii, width=width, bottom=0.0)
        for r, bar in zip(radii, bars):
            bar.set_facecolor("pink")
            bar.set_alpha(0.6)
        ax4.text(-4, 7, "1", fontsize=20,transform=ax4.transData._b)
        ax4.text(3, 6.5, "2", fontsize=20,transform=ax4.transData._b)
        ax4.text(7, 0, "3", fontsize=20,transform=ax4.transData._b)
        ax4.text(3, -6.5, "4", fontsize=20,transform=ax4.transData._b)
        ax4.text(-4, -7, "5", fontsize=20,transform=ax4.transData._b)
        ax4.text(-8, 0, "6", fontsize=20,transform=ax4.transData._b)
        
        if lucky_number_one_c==1:
            #bar3.set_facecolor("#000000")
            ax4.text(-4, 7, "1", fontsize=20,transform=ax4.transData._b,color='red')
        elif lucky_number_one_c==2:
            #bar2.set_facecolor("#000000")
            ax4.text(3, 6.5, "2", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==3:
            #bar1.set_facecolor("#000000")
            ax4.text(7, 0, "3", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==4:
            #bar6.set_facecolor("#000000")
            ax4.text(3, -6.5, "4", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==5:
            #bar5.set_facecolor("#000000")
            ax4.text(-4, -7, "5", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==6:
            #bar4.set_facecolor("#000000")
            ax4.text(-8, 0, "6", fontsize=20,transform=ax4.transData._b,color='red')
        
        ax4.tick_params(labelbottom=False, labeltop=False,
                   labelleft=False, labelright=False)

        ax4.grid(False)
        ax4.axis("On")
        ax4.set_title("Bottom Roulette",fontsize=20)
        
        x,y = np.array([i/10 for i in range(11)]),np.array([i/10 for i in range(11)])
        
        ax2 = plt.subplot(gs[0,1:]) # row 0, col 0
        plt.plot([0,1])
        
        ax2.grid(False)
        ax2.axis("Off")
        #ax2.set_title("Top Roulette Outcome",fontsize=20)
        ax2.plot(x,y,color='white',linewidth=4)
        ax2.text(0.1,0.5,"Top Roulette Outcome: " +str(lucky_number_one),fontsize=20)
        
        ax5 = plt.subplot(gs[1,1:]) # row 0, col 0
        plt.plot([0,1])
        
        ax5.grid(False)
        ax5.axis("Off")
        #ax5.set_title("Bottom Roulette Outcome",fontsize=20)
        ax5.plot(x,y,color='white',linewidth=4)
        ax5.text(0.1,0.5,"Bottom Roulette Outcome: " + str(lucky_number_one_c),fontsize=20)
        
lucky = interact(spin,value = widgets.ToggleButton(
        value=True,
        description="Spin",
        disabled=False,
        button_style='danger', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Description',
        icon='check'
    ))

Recall that 

<div class="alert alert-warning">
    <font color="black"><b>Definition.</b> The <i>sample space</i> of an experiment is the set of all possible outcomes of that experiment.</font>
</div>

If, for example, we take the two roulettes above, we can define the sample space of spinning both of then at the same time as the set of all ordered pairs $(n_t,n_b)$, where $n_t$ denotes the outcome of spinning the top roulette and $n_b$ denotes the outcome of spinning the bottom roulette. This sample space is given by the table below, which is a 6 by 6 table where each entry is a pair $(n_t,n_b)$.

def spin_sample_space(value):
    if value==True or value==False:
        
        lucky_number_one = random.choice([1,2,3,4,5,6])
        
        lucky_number_one_c = random.choice([1,2,3,4,5,6])
        
        x_t,y_t = [i/10 for i in range(10)],[i/10 for i in range(10)]
    
        axalpha = 0.05
        figcolor = 'white'
        dpi = 80
        
        gs = gridspec.GridSpec(2, 2)
        fig = plt.figure(figsize=(15,8), dpi=dpi,facecolor='black')      

        fig.patch.set_edgecolor(figcolor)
        fig.patch.set_facecolor(figcolor)
        ax = plt.subplot(gs[0, 0],projection='polar',facecolor="red") 
        plt.plot([0,1])

        ax.patch.set_alpha(axalpha)
        ax.set_axisbelow(True)
        
        ax.plot(x_t,y_t,transform=ax.transData._b,color="#FEE9FF",linewidth=5)
    
        number_parititions = 3
        arc = 2. * np.pi
        N = number_parititions
        theta = np.arange(0.0, arc, arc/N)
    
        radii_ar = [1.0 for i in range(number_parititions)]
        width_ar = [1.3 for i in range(number_parititions)]
    
        radii = 10 * np.array(radii_ar)
        width = np.pi/4  * np.array(width_ar)
    
        bars = ax.bar(theta, radii, width=width, bottom=0.0)
        for r, bar in zip(radii, bars):
            bar.set_facecolor("pink")
            bar.set_alpha(0.6)
        ax.text(-4, 7, "1", fontsize=20,transform=ax.transData._b)
        ax.text(3, 6.5, "2", fontsize=20,transform=ax.transData._b)
        ax.text(7, 0, "3", fontsize=20,transform=ax.transData._b)
        ax.text(3, -6.5, "4", fontsize=20,transform=ax.transData._b)
        ax.text(-4, -7, "5", fontsize=20,transform=ax.transData._b)
        ax.text(-8, 0, "6", fontsize=20,transform=ax.transData._b)
        
        if lucky_number_one==1:
            #bar3.set_facecolor("#000000")
            ax.text(-4, 7, "1", fontsize=20,transform=ax.transData._b,color='red')
        elif lucky_number_one==2:
            #bar2.set_facecolor("#000000")
            ax.text(3, 6.5, "2", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==3:
            #bar1.set_facecolor("#000000")
            ax.text(7, 0, "3", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==4:
            #bar6.set_facecolor("#000000")
            ax.text(3, -6.5, "4", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==5:
            #bar5.set_facecolor("#000000")
            ax.text(-4, -7, "5", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==6:
            #bar4.set_facecolor("#000000")
            ax.text(-8, 0, "6", fontsize=20,transform=ax.transData._b,color='red')
        
        ax.tick_params(labelbottom=False, labeltop=False,
                   labelleft=False, labelright=False)

        ax.grid(False)
        ax.axis("On")
        ax.set_title("Top Roulette",fontsize=20)
        
        ax4 = plt.subplot(gs[1, 0],projection='polar',facecolor="red") # row 0, col 0
        plt.plot([0,1])

        ax4.patch.set_alpha(axalpha)
        ax4.set_axisbelow(True)
        
        ax4.plot(x_t,y_t,transform=ax4.transData._b,color="#FEE9FF",linewidth=5)
        bars = ax4.bar(theta, radii, width=width, bottom=0.0)
        for r, bar in zip(radii, bars):
            bar.set_facecolor("pink")
            bar.set_alpha(0.6)
        ax4.text(-4, 7, "1", fontsize=20,transform=ax4.transData._b)
        ax4.text(3, 6.5, "2", fontsize=20,transform=ax4.transData._b)
        ax4.text(7, 0, "3", fontsize=20,transform=ax4.transData._b)
        ax4.text(3, -6.5, "4", fontsize=20,transform=ax4.transData._b)
        ax4.text(-4, -7, "5", fontsize=20,transform=ax4.transData._b)
        ax4.text(-8, 0, "6", fontsize=20,transform=ax4.transData._b)
        
        if lucky_number_one_c==1:
            #bar3.set_facecolor("#000000")
            ax4.text(-4, 7, "1", fontsize=20,transform=ax4.transData._b,color='red')
        elif lucky_number_one_c==2:
            #bar2.set_facecolor("#000000")
            ax4.text(3, 6.5, "2", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==3:
            #bar1.set_facecolor("#000000")
            ax4.text(7, 0, "3", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==4:
            #bar6.set_facecolor("#000000")
            ax4.text(3, -6.5, "4", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==5:
            #bar5.set_facecolor("#000000")
            ax4.text(-4, -7, "5", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==6:
            #bar4.set_facecolor("#000000")
            ax4.text(-8, 0, "6", fontsize=20,transform=ax4.transData._b,color='red')
        
        ax4.tick_params(labelbottom=False, labeltop=False,
                   labelleft=False, labelright=False)

        ax4.grid(False)
        ax4.axis("On")
        ax4.set_title("Bottom Roulette",fontsize=20)
        
        ax1 = plt.subplot(gs[:, 1:],facecolor='#0475A8') # row 1, span all columns
        plt.plot([0,1])
        ax1.set_axisbelow(True)
        ax1.grid(color='black', linestyle='-', linewidth=2)
        
        ax1.set_xlim(0.1,0.7)
        ax1.set_ylim(0.1,0.7)

        rec = Rectangle([lucky_number_one/10,lucky_number_one_c/10],0.1,0.1,facecolor="black")
        ax1.add_patch(rec)
        x,y = [lucky_number_one/10,lucky_number_one/10+ 0.1], [lucky_number_one_c/10,lucky_number_one_c/10 + 0.1]
        ax1.plot(x,y,color='black',linewidth=4)
        for i in range(1,7):
            for j in range(1,7):
                ax1.text(i/10 + 0.02,j/10 + 0.055,"(" + str(i)+","+ str(j)+")",fontsize = 15,color='white') 
        ax1.set_xticklabels([" ",1,2,3,4,5,6])
        ax1.set_yticklabels([" ",1,2,3,4,5,6])
        ax1.set_xlabel("Top Roulette Outcome",fontsize = 20)
        ax1.set_ylabel("Bottom Roulette Outcome",fontsize = 20)
        ax1.xaxis.tick_top()
        ax1.invert_yaxis()

        plt.show()
        
lucky = interact(spin_sample_space,value = widgets.ToggleButton(
        value=True,
        description="Spin",
        disabled=False,
        button_style='danger', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Description',
        icon='check'
    ))

In this case, since the events are independent and each event has six possible outcomes, the sample space contains

$$6 \times 6 = 36$$

possible outcomes, where each outcome is a pair of the form $(n_t,n_b)$. 

The probability of obtaining any given pair $(n_t,n_b)$, is given by the probability of obtaining $n_t$ with the top roulette (first experiment) multiplied by the probability of obtaining $n_b$ with the bottom roulette (second experiment). If we assume that each event is equally likely to occur

$$P(n_t,n_b) = \dfrac{1}{6} \times \dfrac{1}{6} = \dfrac{1}{36}$$

Note that we can multiply 
* the sizes of the two sample spaces (for each roulette) to obtain the sample space size of the combined experiments
* the probabilities of obtaining $n_t$ and $n_b$ to obtain the probability of the event $(n_t,n_b)$
**because** the two experiments are **independent**. This is an important property of joint probability experiments.

<div class="alert alert-warning">
<font color="black"><b>Property.</b> Consider two independent probability experiments $E_1$ and $E_2$ of respective sample space sizes $N_1$ and $N_2$. The size of the sample space of the joint experiment $(E_1,E_2)$ is $N_1\times N_2$. The probability of the event $(n_1,n_2)$ is $P(n_1)\times P(n_2)$.</font>
</div>

## Question 4

What is the probability assigned to the event (1,1)?

from ipywidgets import interact_manual,widgets

s = {'description_width': 'initial'}        
@interact(answer =widgets.Select(
                    options=["Select option","2/36",\
                            "1/6","36",\
                             "1/36"],
                    value='Select option',
                    description="Probability as fraction",
                    disabled=False,
                    style=s
))

def reflective_angle_question(answer):
    if answer=="Select option":
        print("Click on the correct probability expressed as a fraction.")
    
    elif answer=="1/36":
        print("Correct!")
    elif answer != "1/36" or answer != "Select Option":
        print("Hint: There are 36 events, each with equal likelihood of occurrence. \nYou also know that each pair is unique.")

<h3 align='left'>A second example of a sample space</h3>

Let's take the two roulettes as before but this time let's define the sample space of spinning both of them at the same time as the as the **parity** of the sum $$n_t + n_b$$ where as before $n_t$ denotes the outcome of the Top Roulette and $n_b$ denotes the outcome of the Bottom Roulette.

Then the sample space is given by the set $\lbrace \text{even},\text{odd} \rbrace$

This sample space is given by the table below, which is a 6 by 6 table where each entry is a pair contains the **parity** of the sum $$n_t + n_b$$

def fair(value):
    if value==True or value==False:
        
        lucky_number_one = random.choice([1,2,3,4,5,6])
        lucky_number_one_c = random.choice([1,2,3,4,5,6])
        
        x_t,y_t = [i/10 for i in range(10)],[i/10 for i in range(10)]

        axalpha = 0.05
        figcolor = 'white'
        dpi = 80
        
        gs = gridspec.GridSpec(2, 2)
        fig = plt.figure(figsize=(15,8), dpi=dpi,facecolor='black')      

        fig.patch.set_edgecolor(figcolor)
        fig.patch.set_facecolor(figcolor)
        ax = plt.subplot(gs[0, 0],projection='polar',facecolor="red") # row 0, col 0
        plt.plot([0,1])

        ax.patch.set_alpha(axalpha)
        ax.set_axisbelow(True)
        ax.plot(x_t,y_t,transform=ax.transData._b,color="#FEE9FF",linewidth=5)
        number_parititions = 3
        arc = 2. * np.pi
        N = number_parititions
        theta = np.arange(0.0, arc, arc/N)
    
        radii_ar = [1.0 for i in range(number_parititions)]
        width_ar = [1.3 for i in range(number_parititions)]
    
        radii = 10 * np.array(radii_ar)
        width = np.pi/4  * np.array(width_ar)
    
        bars = ax.bar(theta, radii, width=width, bottom=0.0)
        for r, bar in zip(radii, bars):
            bar.set_facecolor("pink")
            bar.set_alpha(0.6)
        ax.text(-4, 7, "1", fontsize=20,transform=ax.transData._b)
        ax.text(3, 6.5, "2", fontsize=20,transform=ax.transData._b)
        ax.text(7, 0, "3", fontsize=20,transform=ax.transData._b)
        ax.text(3, -6.5, "4", fontsize=20,transform=ax.transData._b)
        ax.text(-4, -7, "5", fontsize=20,transform=ax.transData._b)
        ax.text(-8, 0, "6", fontsize=20,transform=ax.transData._b)
        
        if lucky_number_one==1:
            #bar3.set_facecolor("#000000")
            ax.text(-4, 7, "1", fontsize=20,transform=ax.transData._b,color='red')
        elif lucky_number_one==2:
            #bar2.set_facecolor("#000000")
            ax.text(3, 6.5, "2", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==3:
            #bar1.set_facecolor("#000000")
            ax.text(7, 0, "3", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==4:
            #bar6.set_facecolor("#000000")
            ax.text(3, -6.5, "4", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==5:
            #bar5.set_facecolor("#000000")
            ax.text(-4, -7, "5", fontsize=20,transform=ax.transData._b,color='red')
            
        elif lucky_number_one==6:
            #bar4.set_facecolor("#000000")
            ax.text(-8, 0, "6", fontsize=20,transform=ax.transData._b,color='red')
        
        ax.tick_params(labelbottom=False, labeltop=False,
                   labelleft=False, labelright=False)

        ax.grid(False)
        ax.axis("On")
        ax.set_title("Top Roulette",fontsize=20)
        
        ax1 = plt.subplot(gs[:, 1:],facecolor='#0475A8') # row 1, span all columns
        plt.plot([0,1])
        ax1.set_axisbelow(True)
        ax1.grid(color='black', linestyle='-', linewidth=2)

        ax1.set_xlim(0.1,0.7)
        ax1.set_ylim(0.1,0.7)
        ax1.set_xlabel("Top Roulette Outcome",fontsize=18)
        ax1.set_ylabel("Bottom Roulette Outcome",fontsize=18)
        ax1.xaxis.tick_top()
        ax1.invert_yaxis()
        #
        for i in range(1,7):
            for j in range(1,7):
                if (i+j)%2==0:
                    ax1.text(i/10 + 0.02,j/10 + 0.055,"even" ,fontsize = 15,color='white') 
                else:
                    ax1.text(i/10 + 0.02,j/10 + 0.055,"odd" ,fontsize = 15,color='white') 
        
        rec = Rectangle([lucky_number_one/10,lucky_number_one_c/10],0.1,0.1,facecolor="black")
        x,y = [lucky_number_one/10,lucky_number_one/10+ 0.1], [lucky_number_one_c/10,lucky_number_one_c/10 + 0.1]
        ax1.plot(x,y,color='black',linewidth=4)
        #rec_c = Rectangle([lucky_number_one_c/10,lucky_number_two_c/10],0.1,0.1,facecolor="#6b6e72")
        ax1.add_patch(rec)
        #ax1.add_patch(rec_c)
        ax1.set_xticklabels([" ",1,2,3,4,5,6])
        ax1.set_yticklabels([" ",1,2,3,4,5,6])
        
        ax4 = plt.subplot(gs[1, 0],projection='polar',facecolor="red") # row 0, col 0
        plt.plot([0,1])

        ax4.patch.set_alpha(axalpha)
        ax4.set_axisbelow(True)
        
        ax4.plot(x_t,y_t,transform=ax4.transData._b,color="#FEE9FF",linewidth=5)
        
        bars = ax4.bar(theta, radii, width=width, bottom=0.0)
        for r, bar in zip(radii, bars):
            bar.set_facecolor("pink")
            bar.set_alpha(0.6)
        ax4.text(-4, 7, "1", fontsize=20,transform=ax4.transData._b)
        ax4.text(3, 6.5, "2", fontsize=20,transform=ax4.transData._b)
        ax4.text(7, 0, "3", fontsize=20,transform=ax4.transData._b)
        ax4.text(3, -6.5, "4", fontsize=20,transform=ax4.transData._b)
        ax4.text(-4, -7, "5", fontsize=20,transform=ax4.transData._b)
        ax4.text(-8, 0, "6", fontsize=20,transform=ax4.transData._b)
        
        if lucky_number_one_c==1:
            #bar3.set_facecolor("#000000")
            ax4.text(-4, 7, "1", fontsize=20,transform=ax4.transData._b,color='red')
        elif lucky_number_one_c==2:
            #bar2.set_facecolor("#000000")
            ax4.text(3, 6.5, "2", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==3:
            #bar1.set_facecolor("#000000")
            ax4.text(7, 0, "3", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==4:
            #bar6.set_facecolor("#000000")
            ax4.text(3, -6.5, "4", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==5:
            #bar5.set_facecolor("#000000")
            ax4.text(-4, -7, "5", fontsize=20,transform=ax4.transData._b,color='red')
            
        elif lucky_number_one_c==6:
            #bar4.set_facecolor("#000000")
            ax4.text(-8, 0, "6", fontsize=20,transform=ax4.transData._b,color='red')
        
        ax4.tick_params(labelbottom=False, labeltop=False,
                   labelleft=False, labelright=False)

        ax4.grid(False)
        ax4.axis("On")
        ax4.set_title("Bottom Roulette",fontsize=20)

        sum_n = lucky_number_one + lucky_number_one_c
        
        #print("Top Roulette Outcome + Bottom Roulette Outcome")
        print(str(lucky_number_one) + " + " + str(lucky_number_one_c) + " = " + str(sum_n))
        if sum_n %2==0:
            print("OUTCOME: even" )
        else:
            print("OUTCOME: odd" )

        plt.show()

lucky = interact(fair,value = widgets.ToggleButton(
        value=True,
        description="Let's Play",
        disabled=False,
        button_style='danger', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Description',
        icon='check'
    ))

### Question 5

We claim that this game is fair, but how can we verify it? 

Recall that a probability experiment is fair if every outcome is equally likely to occur. In order for this experiment to be fair, the probability of the event **even**  *must* be equal to the probability of event **odd**. 

What is the probability that the sum of the numbers in the top and bottom roulettes is even?

from ipywidgets import interact_manual,widgets

s = {'description_width': 'initial'}        
@interact(answer =widgets.Select(
                    options=["Select option","1/2",\
                            "4/36","1/3",\
                             "18/36"],
                    value='Select option',
                    description="Probability sum is even",
                    disabled=False,
                    style=s
))

def fair_game(answer):
    if answer=="Select option":
        print("Click on the correct probability expressed as a fraction.")
    
    elif answer=="1/2" or answer=="18/36":
        print("Correct!\nThere are a total of 36 possible outcomes. 18 out of 36 are even numbers.\nThus the probability P(even) = 18/36 or 1/2. ")
    elif answer != "1/2" or answer != "Select Option" or answer!="18/36":
        print("Hint: There are 36 entries in our sample space, each with equal likelihood of occurrence.\nHow many of the 36 correspond to even numbers")

### Question 6
What is the probability that the sum of the numbers in the top and bottom roulettes is odd? In other words, what is the probability that Bob will win?

from ipywidgets import interact_manual,widgets

s = {'description_width': 'initial'}        
@interact(answer =widgets.Select(
                    options=["Select option","19/36",\
                            "17/36","18/36",\
                             "1/2"],
                    value='Select option',
                    description="Probability sum is odd",
                    disabled=False,
                    style=s
))

def fair_game(answer):
    if answer=="Select option":
        print("Click on the correct probability expressed as a fraction.")
    
    elif answer=="1/2" or answer=="18/36":
        print("Correct!\nThere are a total of 36 possible outcomes. 18 out of 36 are odd numbers.\nThus the P(odd) = 18/36 or 1/2. ")
    elif answer != "1/2" or answer != "Select Option" or answer!="18/36":
        print("Hint: There are 36 entries in our sample space, each with equal likelihood of occurrence.\nHow many of the 36 correspond to odd numbers?")

In the section above we learned that the there are 18 out of 36 possible outcomes where the sum 

$$n_t + n_b$$

is an even number. Thus

$$P(even) = \dfrac{18}{36} = \dfrac{1}{2}$$

Similarly, there are 18 out of 36 possible outcomes where the sum

$$n_t + n_b$$

is an odd number. Thus

$$P(odd) = \dfrac{18}{36} = \dfrac{1}{2}$$

Then $P(odd) = P(even)$. With this we verify that indeed the experiment is fair. 

<h2 align='center'>Theoretical vs Experimental Probability</h2>



We begin by stating a few definitions. 

<div class="alert alert-warning">
    <font color="black"><b>Definition.</b> The <i>Theoretical Probability</i> of an event $A$, denoted $P_T(A)$, is the ratio of the number of outcomes corresponding to this event to the number of possible outcomes. </font>
</div>

$$P_T(A) = \dfrac{\text{Total Number of Instances of event A in the Sample Space}}{\text{Total Number of Possible Outcomes}}$$

If we take our fair experiment with two roulettes and sample space parity of outcome sum $\lbrace \text{even}, \text{odd} \rbrace$, the theoretical probability of an even event is

$$P_T(\text{even}) = \dfrac{18}{36}$$

<div class="alert alert-warning">
<font color="black"><b>Definition.</b> The <i>Experimental Probability</i> of an event $A$, denoted $P_E(A)$, is computed over running the probability experiment a number of times and computing the observed ratio between the number of time the event occured  and the number of trials of the experiment. </font>
</div>

$$P_E(A) = \dfrac{\text{Number of Times Event A Actually Occurred}}{\text{Number of trials}}$$

In order to determine $P_E(\text{even})$, we first need to spin the roulettes a few times and compare.

Use the widget below to simulate spinning the two roulettes. Use the slider to set a number of trials. In this interactive exercise, you can set number of trials as an integer between 1 and 100. Press `Run Interact` to run an experiment for the given number of trials.

On the right hand side you will find a printed message outlining the experimental probability of each event: Sum is Even and Sum is Odd from the number of trial specified using the widget. 

On the left hand side you can find a graph comparing both. 

Press the `Run Interact` button several times. 

%matplotlib inline

def die(number):
    count_A,count_C = 0,0
    
    for i in range(number):
        lucky_number_one = random.choice([1,2,3,4,5,6])
        lucky_number_two = random.choice([1,2,3,4,5,6])
        if lucky_number_one - lucky_number_two >=0:
            count_A +=1
        else:
            count_C +=1
            
    return [count_A,count_C]

def even_sum(number):
    count_A,count_C = 0,0
    
    for i in range(number):
        lucky_number_one = random.choice([1,2,3,4,5,6])
        lucky_number_two = random.choice([1,2,3,4,5,6])
        
        sum_n = lucky_number_one + lucky_number_two
        if  sum_n%2 == 0:
            count_A +=1
        else:
            count_C +=1
            
    return [count_A,count_C]

def experimental_prob(number):
    [varoi_1,varoi_2] = even_sum(number)
    fig,(ax1,ax2,ax3) = plt.subplots(1,3,sharey=True,figsize=(15,4))

    ax2.axis("Off")
    ax3.axis("Off")
    axalpha = 0.05
    
    even = varoi_1/number
    odd = varoi_2/number
    
    labels = ['', '',  'Even Sum', '','Odd Sum']

    ax1 = plt.subplot(131,facecolor="white")
    ax1.set_title("Experimental Probability",fontsize=20)
    ax1.set_ylabel("Probability",fontsize=15)
    ax1.set_xlabel("Outcomes",fontsize=15)
    ax1.set_xlim([0,3])

    ax1.set_xticklabels(labels)

    x = np.arange(1,3)
    f1,f2= ax1.bar(x,[even,odd])
    f1.set_facecolor("#8642f4")
    f2.set_facecolor("#518900")

    ax1.grid(which='both')
    ax1.grid(b=True,which='minor',alpha=0.2,linestyle='--',color='black')
    ax1.grid(which='major', alpha=0.2,linestyle='--',color='black')
    
    ax3 = plt.subplot(132)
    ax3.axis("Off")
    
    #ax3.set_title( "Positive vs Negative\nLuck Roulette: Outcome",fontsize=20)
    rec1 = Rectangle((0.1,0.8),0.3,0.1,facecolor="#8642f4")
    ax3.add_patch(rec1)
    ax3.text(0.5,0.83,"Experimental Probability: Sum is Even",fontsize=20)
    rec2 = Rectangle((0.1,0.7),0.3,0.1,facecolor="#518900")
    ax3.add_patch(rec2)
    ax3.text(0.5,0.73,"Experimental Probability: Sum is Odd",fontsize=20)

    ax2 = plt.subplot(133,facecolor="white")
    ax2.axis("Off")

    ax2.text(0.9,0.83,str(varoi_1) + "/" + str(number),fontsize=20)
    ax2.text(0.9,0.73,str(varoi_2) + "/" + str(number),fontsize=20)
    
    ax3.set_title("                   Even or Odd Sum Experiment:\n",fontsize=20)
    
    plt.show()
    
def run_fair_exp(number):
    experimental_prob(number)
    #experimental_prob(number,"Negative")
interact_manual(experimental_prob,number=widgets.IntSlider(
            value=10,
            min=1,
            max=100,
            step=1,
            description='Total Number of Trials',
            disabled=False,
            continuous_update=False,
            orientation='horizontal',
            readout=True,
            readout_format='d',
            style =style
));

### Question 7

Use the box below to enter your observations. 

How do the experimental probabilities of each event change as you increase the number of trials?

from ipywidgets import widgets as w
from ipywidgets import Button, Layout
from IPython.display import display, Javascript, Markdown

def rerun_cell( b ):    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,IPython.notebook.get_selected_index()+2)'))   

style = {'description_width': 'initial'}

question7_text = w.Textarea( value='', placeholder='Write your answer here. Press Record Answer when you finish.', description='', disabled=False , layout=Layout(width='100%', height='75px') )
question7_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))

display(question7_text)
display(question7_button)

question7_button.on_click( rerun_cell ) 

question7_input = question7_text.value

if(question7_input != ''):
    question7_text.close()
    question7_button.close()
    display(Markdown("### Your answer for Question 7: Conclusions"))
    display(Markdown(question7_input))

**Remarks**

We observe that every time we press the `Run Interact` button on the interactive above, the experimental probability of each event varies. However, it seems like as we increase the number of trials, the experimental probabilities of each event approach $1/2$. 

Let us explore what happens if we increase the number of trials to, say 10,000. 

In the widget below you can find a slider that allows you to control the number of trials. In this interactive exercise, you can set number of trials as an integer between 1 and 10,000. 

On the left hand side you can find a plot like the one we explored above. On the right hand side you can find the theoretical probability of events Sum is Even and Sum is Odd. 

Press the `Run Interact` button. Increase the Total Number of Trials and press the `Run Interact` button multiple times. 

def toss(number):
    store_head = []
    store_tail = []
    other = []
    for i in range(number):
        toss_coin= random.choice(np.arange(2))
        
        if toss_coin==0:
            store_head.append(toss_coin)
        elif toss_coin==1:
            store_tail.append(toss_coin)
        
    return [store_head,store_tail]

def plot_coin_experiment(number):
    varoi = toss(number)
    fig,ax = plt.subplots(figsize=(5,5))

    ax.set_title("Distribution of Experimental Coin Flipping",fontsize=35)
    plt.ylabel("Frequency",fontsize=25)
    plt.xlabel("Heads or Tails",fontsize=25)
    plt.xticks(np.arange(2), ('Total Number of Heads', 'Total Number of Tails'))
    plt.hist(varoi[0])
    plt.hist(varoi[1])
    plt.grid(which='both')
    plt.grid(b=True,which='minor',alpha=0.2,linestyle='--',color='black')
    plt.grid(which='major', alpha=0.2,linestyle='--',color='black')

def plot_die_experiment(number):
    varoi = die(number)
    theor_A = 21/36
    theor_C = 15/36
    #print(theor)
    fig,(ax1,ax2) = plt.subplots(1,2,sharey=True,figsize=(15,8))
    
    # Experimental Probability
    ax1.set_title("Experimental Distribution",fontsize=25)
    ax1.set_ylabel("Frequency",fontsize=25)
    ax1.set_xlabel("Outcomes",fontsize=25)
    ax1.set_xlim([0,3])

    ax1.set_xticks([])

    x = np.arange(1,3)
    dice = [varoi[0]/number,varoi[1]/number]
    f1,f2 = ax1.bar(x,dice)
    f1.set_facecolor("#8642f4")
    f2.set_facecolor("#518900")
    ax1.grid(which='both')
    ax1.grid(b=True,which='minor',alpha=0.2,linestyle='--',color='black')
    ax1.grid(which='major', alpha=0.2,linestyle='--',color='black')
    
    # Theoretical Probability
    ax2.set_title("Theoretical Distribution",fontsize=25)
    ax2.set_ylabel("Frequency",fontsize=25)
    ax2.set_xlabel("Outcomes",fontsize=25)
    x = np.arange(1,3)
    dice_exp = [theor_A,theor_C]
    f11,f21 = ax2.bar(x,dice_exp)
    f11.set_facecolor("#8642f4")
    f21.set_facecolor("#518900")

    ax2.set_xlim([0,3])
    
    ax2.set_xticks(["Even","Odd"])
    
    ax2.grid(which='both')
    ax2.grid(b=True,which='minor',alpha=0.2,linestyle='--',color='black')
    ax2.grid(b=True,which='major', alpha=0.2,linestyle='--',color='black')

    plt.ylim(0,number)
    
    plt.show()
    
def plot_fair_experiment(number):
    [varoi_1,varoi_2] = even_sum(number)
    theor_A = 18/36
    theor_C = 18/36
    
    even = varoi_1/number
    odd= varoi_2/number
    x = np.arange(1,3)
    
    labels = ['', '',  'Even Sum', '','Odd Sum']
    
    fig,(ax1,ax2) = plt.subplots(1,2,sharey=True,figsize=(15,8))
    
    # Experimental Probability
    ax1.set_title("Even or Odd Sum Probability Experiment:\nExperimental Probability",fontsize=20)
    ax1.set_ylabel("Probability",fontsize=25)
    ax1.set_xlabel("Events",fontsize=25)
    ax1.set_xlim([0,3])
    ax1.set_xticklabels(labels)
    ax1.grid(which='major', alpha=0.2,linestyle='--',color='black')
    
    f1,f2 = ax1.bar(x,[even,odd])
    f1.set_facecolor("#8642f4")
    f2.set_facecolor("#518900")
    
    # Theoretical Probability
    ax2.set_title("Even or Odd Sum Probability Experiment:\nTheoretical Probability",fontsize=20)
    ax2.set_ylabel("Probability",fontsize=25)
    ax2.set_xlabel("Events",fontsize=25)
    ax2.set_xlim([0,3])
    ax2.set_xticklabels(labels)
    ax2.grid(b=True,which='major', alpha=0.2,linestyle='--',color='black')
    
    dice_exp = [theor_A,theor_C]
    f11,f21 = ax2.bar(x,dice_exp)
    f11.set_facecolor("#8642f4")
    f21.set_facecolor("#518900")
    
    plt.ylim(0,1)
    plt.show()

interact_manual(plot_fair_experiment,number=widgets.IntSlider(
            value=5,
            min=1,
            max=10000,
            step=1,
            description='Total Number of Trials',
            disabled=False,
            continuous_update=False,
            orientation='horizontal',
            readout=True,
            readout_format='d',
            style =style
));

### Question 8

How does the experimental probability of each event change as we increase the number of trials? Use the textbox below to record your answers. 

from ipywidgets import widgets as w
from ipywidgets import Button, Layout
from IPython.display import display, Javascript, Markdown

def rerun_cell( b ):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,IPython.notebook.get_selected_index()+2)'))   
style = {'description_width': 'initial'}


question8_text = w.Textarea( value='', placeholder='Write your answer here. Press Record Answer when you finish.', description='', disabled=False , layout=Layout(width='100%', height='75px') )
question8_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))

display(question8_text)
display(question8_button)

question8_button.on_click( rerun_cell ) 

question8_input = question8_text.value

if(question8_input != ''):
    
    question8_text.close()
    question8_button.close()
    display(Markdown("### Your answer for Question 8: Conclusions"))
    display(Markdown(question8_input))

As the number of trials increases, we observe that the experimental probability of each event approaches the corresponding theoretical probability. This is known as the "Law of Large Numbers".

<h2 align='center'>Conclusion</h2>

In this notebook we learned what a probability experiment is, what the sample space, events and outcome associated to a given probability experiment are. We learned how to express probabilities as ratios, fractions and percents. 

We learned what independent probability events are and introduced the concept of a fair game. 

We learned what theoretical and experimental probability are and with the help of an interactive exercise, we learned that as the number of trials increases, experimental probability approaches theoretical probability. 

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)