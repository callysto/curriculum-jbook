![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/SpecificAndLatentHeat/specific-and-latent-heat.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

(Click **Cell** > **Run All** before proceeding.) 

%matplotlib inline

#----------

#Import modules and packages 
import ipywidgets as widgets
import random
import math
import matplotlib.pyplot as plt
from ipywidgets import Output, IntSlider, VBox, HBox, Layout
from IPython.display import clear_output, display, HTML, Javascript, SVG

#----------

#import ipywidgets as widgets
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
    
    #Print the letters (A) to (D) in sequence with randomly chosen options
    for i in range(4):
        option_text = option_list.pop()
        print(start_bold + letters[i] + end_bold + option_text)

        #Store the correct answer
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
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Moccasin'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Lightgray'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button2_clicked(b):
        if "(B) " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Moccasin'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Lightgray'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button3_clicked(b):
        if "(C) " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Moccasin'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Lightgray'; button4.style.button_color = 'Whitesmoke'

    def on_button4_clicked(b):
        if "(D) " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Lightgray'

    button1.on_click(on_button1_clicked); button2.on_click(on_button2_clicked)
    button3.on_click(on_button3_clicked); button4.on_click(on_button4_clicked)

# Specific and Latent Heat

## Introduction

**Heat** is defined as the *transfer of energy* from one object to another due to a difference in their relative temperatures. As heat flows from one object into another, the temperature of either one or both objects changes. 

<img src="Images/heat.svg" width="55%"/>

### Specific Heat Capacity

The amount of heat required to change the temperature of a given material is given by the following equation:

$$Q = m C \Delta T$$

where $Q$ represents heat in joules (J), $m$ represents mass kilograms (kg), and $\Delta T$ represents the change in temperature in Celsius (°C) or kelvin (K). The parameter $C$ is an experimentally determined value characteristic of a particular material. This parameter is called the **specific heat** or **specific heat capacity** (J/kg$\cdot$°C). The specific heat capacity of a material is determined by measuring the amount of heat required to raise the temperature of 1 kg of the material by 1°C. For ordinary temperatures and pressures, the value of $C$ is considered constant. Values for the specific heat capacity of common materials are shown in the table below:

 Material                  | Specific Heat Capacity (J/kg$\cdot$°C)
 ---                       | ---
 Aluminum                  | 903
 Brass                     | 376
 Carbon                    | 710
 Copper                    | 385
 Glass                     | 664
 Ice                       | 2060
 Iron                      | 450
 Lead                      | 130
 Methanol                  | 2450
 Silver                    | 235
 Stainless Steal           | 460
 Steam                     | 2020
 Tin                       | 217
 Water                     | 4180
 Zinc                      | 388

Use the slider below to observe the relationship between the specific heat capacity and the amount of heat required to raise the temperature of a 5 kg mass by 50 °C.

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, HBox 

mass_1 = 5
delta_temperature = 50
specific_heat_capacity = widgets.IntSlider(description="C (J/kg⋅°C)",min=100,max=1000)

#Boldface text between these strings
start_bold = "\033[1m"; end_bold = "\033[0;0m"

def f(specific_heat_capacity):
    heat_J = int((mass_1 * specific_heat_capacity * delta_temperature))
    heat_kJ = int(heat_J/1000)
    print(start_bold + "Heat = (mass) X (specific heat capacity) X (change in temperature)" + end_bold)
    print("Heat = ({} X {} X {}) J = {} J or {} kJ".format(mass_1, specific_heat_capacity, delta_temperature, heat_J, heat_kJ))

out1 = widgets.interactive_output(f,{'specific_heat_capacity': specific_heat_capacity,})

HBox([VBox([specific_heat_capacity]), out1])

**Question:** *As the specific heat increases, the amount of heat required to cause the temperature change:* 

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Increases" 
option_2 = "Decreases"
option_3 = "Remains constant"
option_4 = "Equals zero"

multiple_choice(option_1, option_2, option_3, option_4)

### Example
How many kilojoules (kJ) of heat are needed to raise the temperature of a 3.0 kg piece of aluminum from 10°C to 50°C? Round the answer to 2 significant figures.

#import ipywidgets as widgets
#from ipywidgets import Output, VBox 
#from IPython.display import clear_output, display, HTML

out2 = Output()
button_step1 = widgets.Button(description="Step One", layout=Layout(width='20%', height='100%'), button_style='primary')
count1 = 1

text1_1 = widgets.HTMLMath(value="The first step is to identify all known and unknown variables required to solve the problem. In this case, three variables are known ($m$, $C$, $\Delta T$), and one variable is unknown ($Q$):")
text1_2 = widgets.HTMLMath(value="$m$ = 3.0 kg")
text1_3 = widgets.HTMLMath(value="$\Delta T$ = 50°C $-$ 10°C = 40°C")
text1_4 = widgets.HTMLMath(value="$C$ = 903 J/kg$\cdot$°C (The specific heat capacity for aluminum may be found in the table above.)")
text1_5 = widgets.HTMLMath(value="$Q$ = ?")

def on_button_step1_clicked(b):
    global count1
    count1 += 1
    with out2:
        clear_output()
        if count1 % 2 == 0:
            display(text1_1, text1_2, text1_3, text1_4, text1_5)
            
display(VBox([button_step1, out2]))
button_step1.on_click(on_button_step1_clicked)

#import ipywidgets as widgets
#from ipywidgets import Output, VBox 
#from IPython.display import clear_output, display, HTML

out3 = Output()
button_step2 = widgets.Button(description="Step Two", layout=Layout(width='20%', height='100%'), button_style='primary')
count2 = 1

text2_1 = widgets.HTMLMath(value="Substitute each known variable into the formula to solve for the unknown variable:")
text2_2 = widgets.HTMLMath(value="$Q = mC\Delta T$")
text2_3 = widgets.HTMLMath(value="$Q$ = (3.0 kg) (903 J/kg$\cdot$°C) (40°C) = 108,360 J")
text2_4 = widgets.HTMLMath(value="$Q$ = 108,360 J")

def on_button_step2_clicked(b):
    global count2
    count2 += 1
    with out3:
        clear_output()
        if count2 % 2 == 0:
            display(text2_1, text2_2, text2_3, text2_4)
            
display(VBox([button_step2, out3]))
button_step2.on_click(on_button_step2_clicked)

#import ipywidgets as widgets
#from ipywidgets import Output, VBox 
#from IPython.display import clear_output, display, HTML

out4 = Output()
button_step3 = widgets.Button(description="Step Three", layout=Layout(width='20%', height='100%'), button_style='primary')
count3 = 1

text3_1 = widgets.HTMLMath(value="Round the answer to the correct number of significant figures and convert to the correct units (if needed):")
text3_2 = widgets.HTMLMath(value="$Q$ = 108,360 J = 110,000 J or 110 kJ")
text3_3 = widgets.HTMLMath(value="The amount of heat required to increase the temperature of a 3.0 kg piece of aluminum from 10°C to 50°C is 110,000 J or 110 kJ.")

def on_button_step3_clicked(b):
    global count3
    count3 += 1
    with out4:
        clear_output()
        if count3 % 2 == 0:
            display(text3_1, text3_2, text3_3)
            
display(VBox([button_step3, out4]))
button_step3.on_click(on_button_step3_clicked)

### Practice

The heat transfer equation shown above may be rearranged to solve for each variable in the equation. These rearrangements are shown below:

$$Q = mC\Delta T \qquad m = \dfrac{Q}{C \Delta T} \qquad C = \dfrac{Q}{m \Delta T} \qquad \Delta T = \dfrac{Q}{mC}$$

Try the four different practice problems below. Each question will require the use of one or more formula above. Use the *Generate New Question* button to generate additional practice problems.

#from IPython.display import Javascript, display
#from ipywidgets import widgets

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Randomize variables
mass = round(random.uniform(25.0, 50.0), 1)
temperature_initial = round(random.uniform(15.0, 25.0), 1)
temperature_final = round(random.uniform(55.0, 65.0), 1)

#Dictionary of materials
materials = {"aluminum": 903, "brass": 376, "carbon": 710, "copper": 385, "glass": 664, "iron": 450, "silver": 235, "stainless steal": 460, "tin": 217, "zinc": 388}
material = random.choice(list(materials.keys()))

#Print question
question = "How much heat is required to raise the temperature of a {} g sample of {} from {}°C to {}°C?".format(mass, material, temperature_initial, temperature_final)
print(question)

#Answer and option calculations
answer = (mass/1000) * materials[material] * (temperature_final - temperature_initial)

#Define range of values for random multiple choices
mini = 100
maxa = 2300

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)

#Round options to the specified number of significant figures
def round_sf(number, significant):
    return round(number, significant - len(str(number)))

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(round_sf(int(answer),3)) + " J"
option_2 = str(round_sf(int(choice_list[0]),3)) + " J"
option_3 = str(round_sf(int(choice_list[1]),3)) + " J"
option_4 = str(round_sf(int(choice_list[2]),3)) + " J"

multiple_choice(option_1, option_2, option_3, option_4)

#import math
#from IPython.display import Javascript, display
#from ipywidgets import widgets

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Randomize variables
heat = random.randint(10, 250)
temperature_initial = round(random.uniform(10.0, 35.0), 1)
temperature_final = round(random.uniform(45.0, 100.0), 1)

#Dictionary of materials
materials = {"aluminum": 903, "brass": 376, "carbon": 710, "copper": 385, "glass": 664, "iron": 450, "silver": 235, "stainless steal": 460, "tin": 217, "zinc": 388}
material = random.choice(list(materials.keys()))

#Print question
question = "Suppose some {} lost {} kJ of heat as it cooled from {}°C to {}°C. Find the mass. Note: you will need to make the sign of Q negative because heat is flowing out of the material as it cools.".format(material, heat, temperature_final, temperature_initial)
print(question)

#Answer calculation
answer = (-heat*1000) / (materials[material] * (temperature_initial - temperature_final))

#Define range of values for random multiple choices
mini = 100
maxa = 2000

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str('{:.2f}'.format(round(answer,2))) + " kg" 
option_2 = str(round(choice_list[0],2)/100) + " kg"
option_3 = str(round(choice_list[1],2)/100) + " kg"
option_4 = str(round(choice_list[2],2)/100) + " kg"

multiple_choice(option_1, option_2, option_3, option_4)

#from IPython.display import Javascript, display
#from ipywidgets import widgets

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Randomize variables
heat = round(random.uniform(23.00, 26.00),1)
mass = round(random.uniform(1.00, 3.00), 2)
temperature_initial = round(random.uniform(24.0, 25.0), 1)
temperature_final = round(random.uniform(35.0, 36.0), 1)

#Print question
question = "A newly made synthetic material weighing {} kg requires {} kJ to go from {}°C to {}°C (without changing state). What is the specific heat capacity of this new material?".format(mass, heat, temperature_initial, temperature_final)
print(question)

#Answer calculation
answer = (heat*1000) / (mass * (temperature_final - temperature_initial))

#Define range of values for random multiple choices
mini = 990
maxa = 2510

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)

#Round options to the specified number of significant figures
def round_sf(number, significant):
    return round(number, significant - len(str(number)))

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(round_sf(int(answer),3)) + " J/(kg°C)"
option_2 = str(round_sf(int(choice_list[0]),3)) + " J/(kg°C)"
option_3 = str(round_sf(int(choice_list[1]),3)) + " J/(kg°C)"
option_4 = str(round_sf(int(choice_list[2]),3)) + " J/(kg°C)"

multiple_choice(option_1, option_2, option_3, option_4)

#import math
#from IPython.display import Javascript, display
#from ipywidgets import widgets

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Dictionary of materials
materials = {"aluminum": 903, "brass": 376, "carbon": 710, "copper": 385, "glass": 664, "iron": 450, "silver": 235, "stainless steal": 460, "tin": 217, "zinc": 388}
material = random.choice(list(materials.keys()))

#Randomize Variables
heat = random.randint(100, 150)
mass = round(random.uniform(1.0, 5.0), 1)
temperature_initial = round(random.uniform(10.0, 30.0), 1)
temperature_final = round(random.uniform(40.0, 60.0), 1)

#Determine question type
question_type = random.randint(1,3)

if question_type == 1:
    #Type 1: Finding change in temperature
    question = "If {} kg of {} receives {} kJ of heat, determine its change in temperature to one decimal place.".format(mass, material, heat)
    print(question)
    answer = (heat*1000) / (materials[material] * mass)
elif question_type == 2:
    #Type 2: Finding final temperature
    question = "If {} kg of {} receives {} kJ of heat, and if the {}'s initial temperature is {}°C, determine its final temperature to one decimal place. Hint: ΔT = final temperature - initial temperature.".format(mass, material, heat, material, temperature_initial)
    print(question)
    answer = ((heat*1000) / (materials[material] * mass)) + temperature_initial
elif question_type == 3:
    #Type 3: Finding initial temperature
    question = "If {} kg of {} receives {} kJ of heat, and if the {}'s final temperature is {}°C, determine its initial temperature to one decimal place. Hint: ΔT = final temperature - initial temperature.".format(mass, material, heat, material, temperature_final)
    print(question)
    answer = temperature_final - ((heat*1000) / (materials[material] * mass))

#Define range of values for random multiple choices
mini = int(answer*100 - 1000)
maxa = int(answer*100 + 1000)

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str((round(answer,1))) + " °C" 
option_2 = str(round(choice_list[0]/100,1)) + " °C"
option_3 = str(round(choice_list[1]/100,1)) + " °C"
option_4 = str(round(choice_list[2]/100,1)) + " °C"

multiple_choice(option_1, option_2, option_3, option_4)

## Change of Phase

In the previous examples and exercises, the material remained in a constant state while heat was added or taken away. However, the addition or subtraction of heat is often accompanied by a **phase change**. The three most common phases are solid, liquid, and gas:

<img src="Images/phase_change.svg" width="75%"/>

**Problem:** *Determine the amount of heat required to raise the temperature of a 100 g block of ice from -20°C to steam at 200°C.*

**Attempt:** There are two phase changes in this problem: (1) the melting of ice into water, and (2) the boiling of water into steam. To determine $Q$, let's utilize the heat formula: 

$$Q=mC\Delta T$$ 

To solve this problem, we can split it up into steps that are simple to calculate. For example, we can start by calculating the heat required to warm ice from -20°C to 0°C. Then, we can calculate the heat required to warm water from 0°C to 100°C. Finally, we can calculate the heat required to warm steam from 100°C to 200°C:

$Q_{ice}$ = (0.100 kg) (2060 J/kg$\cdot$°C) (0°C - (-20°C)) = 4120 J

$Q_{water}$ = (0.100 kg) (4180 J/kg$\cdot$°C) (100°C - 0°C) = 41800 J

$Q_{steam}$ = (0.100 kg) (2020 J/kg$\cdot$°C) (200°C - 100°C) = 20200 J

Then, by adding up the heat calculated in each step, the original problem can be solved: 

$Q$ = (4120 + 41800 + 20200) J = 66120 J, or 66.1 kJ.

### Experiment

Let's conduct an experiment to check the above calculation. We will start with a 100 g sample of ice at -20°C, and then add a constant amount of heat until the entire sample is converted to steam at 200°C. Every minute, we will take the temperature of the sample.

The data from this experiment is shown in the interactive graphs below. The temperature of the material versus time is shown on left. The heat added to the material versus time is shown on the right.

#import ipywidgets as widgets
#import matplotlib.pyplot as plt
#from ipywidgets import HBox, Output, VBox
#from IPython.display import clear_output

out5 = Output()
play = widgets.Play(interval=500, value=0, min=0, max=25, step=1, description="Press play", disabled=False)
time_slider = widgets.IntSlider(description='Time (min)', value=0, min=0, max=25, continuous_update = False)
widgets.jslink((play, 'value'), (time_slider, 'value'))

#Make lists of x and y values
x_values = list(range(26))
y_values = [-20, -10, 0, 0, 10, 40, 80, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 120, 140, 160, 180, 200]

heat_y = []
increment = 0
for i in range(26):
    heat_y.append(increment)
    increment += 13.021

#Plot graphs
def plot_graphs(change):
    x = change['new']
    with out5:
        clear_output(wait=True)
        temp_x_values = []
        temp_y_values = []
        graph2y = []
        
        for i in range(x+1):
            temp_x_values.append(x_values[i])
            temp_y_values.append(y_values[i])
            graph2y.append(heat_y[i])    
        
        plt.figure(figsize=(15,5))
        plt.style.use('seaborn')
        plt.rcParams["axes.edgecolor"] = "black"
        plt.rcParams["axes.linewidth"] = 0.5
        
        plt.subplot(1,2,1)
        plt.ylim(-30, 210)
        plt.xlim(-0.5,26)
        plt.scatter(temp_x_values, temp_y_values)
        plt.ylabel('Temperature (°C)')
        plt.xlabel('Time (min)')
        
        plt.subplot(1,2,2)
        plt.ylim(-25, 350)
        plt.xlim(-2,26)
        plt.scatter(temp_x_values, graph2y, color='red')
        plt.ylabel('Heat (kJ)')
        plt.xlabel('Time (min)')
        
        plt.show()

#Get slider value
time_slider.observe(plot_graphs, 'value')
plot_graphs({'new': time_slider.value})

#Display widget
display(HBox([play, time_slider]))
display(out5)

**Question**: *Examine the graph on the left. It shows the temperature of the material at each minute. At what temperature(s) does the temperature remain constant for some time?*

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "0°C and 100°C. We have horizontal lines at those temperatures."
option_2 = "-20°C, 0°C, 100°C, and 200°C."
option_3 = "100°C."
option_4 = "The temperature is never constant."

multiple_choice(option_1, option_2, option_3, option_4)

**Question:** *Examine the graph on the right. It shows how much heat was required to turn a block of ice at -20°C into steam at 200°C. Does this agree with the value we arrived at from our above calculation (66.1 kJ)?*

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Based on the graph, the amount of heat required is around 325 kJ. It does not agree with our calculation."
option_2 = "Based on the graph, the amount of heat required is close enough to our calculation; hence, it does agree."
option_3 = "Both values match perfectly."
option_4 = "The values are close and it is impossible to say if they match perfectly or not."

multiple_choice(option_1, option_2, option_3, option_4)

**Question**: *Examine the graph on the right. Observe that the slope of the line is constant. What does this imply?*

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "The amount of heat added to the system is constant for the entire 25 min period."
option_2 = "The amount of heat added to the system is not constant, the rate increases throughout the 25 min period."
option_3 = "No heat is added at the start, but around 325 kJ of heat is added at the very end."
option_4 = "As time increases, the amount of heat required decreases."

multiple_choice(option_1, option_2, option_3, option_4)

### Experimental Results

Our experimental data indicates that our calculation of 66.1 kJ is incorrect and that it in fact takes around 325 kJ to heat ice from -20°C to steam at 200°C. *So what did we miss?*

**Answer:** The *phase changes*.

The graph on the right shows us that the rate heat was added to the system over the 25 minute period was constant, yet the temperature remained constant at two points for some time (0°C and 100°C). How is this possible? That is, *how can we add heat to a material while its temperature remains constant?*

**Answer:** Every material has two common "critical temperature points". These are the points at which the *state* of the material *changes*. For water, these points are at 0°C and 100°C. If heat is coming into a material *during a phase change*, then this energy is used to overcome the intermolecular forces between the molecules of the material.

Let's consider when ice melts into water at 0°C. Immediately after the molecular bonds in the ice are broken, the molecules are moving (vibrating) at the same average speed as before, and so their average kinetic energy remains the same. *Temperature* is precisely a measure of the average kinetic energy of the particles in a material. Hence, during a phase change, the temperature remains constant.

### Latent Heat of Fusion and Vaporization

The **latent heat of fusion ($H_f$)** is the quantity of heat needed to melt 1 kg of a solid to a liquid without a change in temperature.

<img src="Images/latent_heat_fusion.svg" width="65%"/>

The **latent heat of vaporization ($H_v$)** is the quantity of heat needed to vaporise 1 kg of a liquid to a gas without a change in temperature.

<img src="Images/latent_heat_vaporization.svg" width="65%"/>

The latent heats of fusion and vaporization are empirical characteristics of a particular material. As such, they must be experimentally determined. Values for the latent heats of fusion and vaporization of common materials are shown in the table below:

Materials                  | Heat of Fusion (J/kg) |Heat of Vaporization (J/kg)
 ---                       | ---                         | ---
 Copper                    | $2.05 \times 10^5$          | $5.07 \times 10^6$
 Gold                      | $6.03 \times 10^4$          | $1.64 \times 10^6$
 Iron                      | $2.66 \times 10^5$          | $6.29 \times 10^6$
 Lead                      | $2.04 \times 10^4$          | $8.64 \times 10^5$
 Mercury                   | $1.15 \times 10^4$          | $2.72 \times 10^5$
 Methanol                  | $1.09 \times 10^5$          | $8.78 \times 10^5$
 Silver                    | $1.04 \times 10^4$          | $2.36 \times 10^6$
 Water (ice)               | $3.34 \times 10^5$          | $2.26 \times 10^6$

The following formulae are used to calculate the amount of heat needed to change a material from a solid to a liquid (fusion), or from a liquid to a gas (vaporization):

$$Q_f = mH_f \qquad Q_v = mH_v$$


### Example (revisited)

Recall our previous problem:

**Problem:** *Determine the amount of heat required to raise the temperature of a 100 g block of ice from -20°C to steam at 200°C.*

**Solution:** Previously, we split the problem into three steps. It turns out that those steps correctly calculated the heat required to warm ice from -20°C to 0°C, water from 0°C to 100°C. and steam from 100°C to 200°C. What was absent was the latent heat required to complete the phase changes at 0°C and 100°C. Therefore, we need to **add two more steps**, which incorporate the above formulae. 

For completion, the previous steps are restated and the entire calculation is shown in **five steps** below (plus a final step to sum up the heats calculated in the previous steps):

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, HBox
#from IPython.display import clear_output, SVG, HTML, display

out6 = Output()
frame_1 = 1

#Toggle images
def show_steps_1():
    global frame_1

    I11 = widgets.HTMLMath(value="Step 1: Calculate the heat required to change ice from -20°C to 0°C. Since the temperature changes, we use $Q = mCΔT$.")
    Q11 = widgets.HTMLMath(value="$Q_{1}$ = (0.1 kg) (2060 J/kg°C) (0°C - (-20°C)) = 4120 J")
    I12 = widgets.HTMLMath(value="Step 2: Calculate the heat required to change ice at 0°C to water at 0°C. Since the temperature does not change as we are at the melting point of water, we use $Q = mH_{f}$.")
    Q12 = widgets.HTMLMath(value="$Q_{2}$ = (0.1 kg) (334000 J/kg) = 33400 J")
    I13 = widgets.HTMLMath(value="Step 3: Calculate the heat required to change water from 0°C to 100°C. Since the temperature changes, we use $Q = mCΔT$.")
    Q13 = widgets.HTMLMath(value="$Q_{3}$ = (0.1 kg) (4180 J/kg°C) (100°C - 0°C) = 41800 J")
    I14 = widgets.HTMLMath(value="Step 4: Calculate the heat required to change water at 100°C to steam at 100°C. Since the temperature does not change at we are at the boiling point of water, we use $Q = mH_{v}$.")
    Q14 = widgets.HTMLMath(value="$Q_{4}$ = (0.1 kg) (2260000 J/kg) = 226000 J")
    I15 = widgets.HTMLMath(value="Step 5: Calculate the heat required to change steam from 100°C to 200°C. Since the temperature changes, we use $Q = mCΔT$.")
    Q15 = widgets.HTMLMath(value="$Q_{5}$ = (0.1 kg) (2020 J/kg°C) (200°C - 100°C) = 20200 J")
    I16 = widgets.HTMLMath(value="Summary: Calculate total heat by adding up the values calculated in the previous steps. $Q$ = $Q_1$ + $Q_2$ + $Q_3$ + $Q_4$ + $Q_5$")
    Q16 = widgets.HTMLMath(value="$Q$ = (4120 + 33400 + 41800 + 226000 + 20200) J = 325520 J or 326 kJ")
    
    if frame_1 == 0:
        display(SVG("Images/phase_diagram_1_0.svg"))
        frame_1 = 1
    elif frame_1 == 1:
        display(SVG("Images/phase_diagram_1_1.svg"))
        display(I11, Q11)
        frame_1 = 2
    elif frame_1 == 2:
        display(SVG("Images/phase_diagram_1_2.svg"))
        display(I11, Q11, I12, Q12)
        frame_1 = 3
    elif frame_1 == 3:
        display(SVG("Images/phase_diagram_1_3.svg"))
        display(I11, Q11, I12, Q12, I13, Q13)
        frame_1 = 4
    elif frame_1 == 4:
        display(SVG("Images/phase_diagram_1_4.svg"))
        display(I11, Q11, I12, Q12, I13, Q13, I14, Q14)
        frame_1 = 5
    elif frame_1 == 5:
        display(SVG("Images/phase_diagram_1_5.svg"))
        display(I11, Q11, I12, Q12, I13, Q13, I14, Q14, I15, Q15)
        frame_1 = 6
    elif frame_1 == 6:
        display(SVG("Images/phase_diagram_1_6.svg"))
        display(I11, Q11, I12, Q12, I13, Q13, I14, Q14, I15, Q15, I16, Q16)
        frame_1 = 0

button_phase_diagram_1 = widgets.Button(description="Show Next Step", button_style = 'primary')
display(button_phase_diagram_1)

def on_submit_button_phase_diagram_1_clicked(b):
    with out6:
        clear_output(wait=True)
        show_steps_1()

with out6:
    display(SVG("Images/phase_diagram_1_0.svg"))
    
button_phase_diagram_1.on_click(on_submit_button_phase_diagram_1_clicked)
display(out6)

**Note:** that the *state* of a material can include more than one *phase*. For example, at 0°C, the state of water includes both solid (ice) and liquid (water) phases. At 100°C, the state of water includes both liquid (water) and gas (steam) phases.

It is common to cool down a material (as opposed to heating it up). In this scenario, heat must be taken away. By convention, a negative $Q$ is used to represent heat being taken away from a material (cooling), while a positive $Q$ is used to represent heat being added to a material (warming). Be aware of the sign of $Q$ as it indicates the direction the heat is flowing. For $Q=mH_f$ and $Q=mH_v$, you must be aware of whether heat is being added to or taken away from the material. If heat is being taken away, then a negative sign must be placed in front of $H_f$ and $H_v$. 

It is not necessary for each problem to be five steps. A problem could have 1-5 steps depending on the situation. Let's do another example together. An interactive graph is provided to help determine the number of steps required.

### Example

How much heat must be removed to change 10.0 g of steam at 120.0°C to water at 50°C? Round to two significant figures.

#import ipywidgets as widgets
#import matplotlib.pyplot as plt
#from ipywidgets import HBox, Output, VBox
#from IPython.display import clear_output

out7 = Output()
play2 = widgets.Play(interval=500, value=0, min=0, max=25, step=1, description="Press play", disabled=False)
time_slider2 = widgets.IntSlider(description='Time', value=0, min=0, max=20, continuous_update = False)
widgets.jslink((play2, 'value'), (time_slider2, 'value'))

#Make lists of x and y values
x_values2 = list(range(21))
y_values2 = [120, 110, 100, 100, 100, 100, 100, 100, 100, 100, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50]

heat_y2 = []
increment2 = 0
for i in range(26):
    heat_y2.append(increment2)
    increment2 += 13021

#Plot graph
def time_temp(change):
    x = change['new']
    with out7:
        clear_output(wait=True)
        temp_x_values2 = []
        temp_y_values2 = []
        graph2y2 = []
        
        for i in range(x+1):
            temp_x_values2.append(x_values2[i])
            temp_y_values2.append(y_values2[i])
            graph2y2.append(heat_y2[i])    
        
        plt.figure(figsize=(7,5))
        plt.style.use('seaborn')
        plt.rcParams["axes.edgecolor"] = "black"
        plt.rcParams["axes.linewidth"] = 0.5
        plt.ylim(0, 150)
        plt.xlim(-0.5,26)
        plt.xticks([])
        plt.scatter(temp_x_values2, temp_y_values2)
        plt.ylabel('Temperature (°C)')
        plt.xlabel('Time')
        plt.figtext(0.5, 0.01, "This graph consists of three line-segments. This indicates that we require three steps.", wrap=True, horizontalalignment='center', fontsize=12)
        plt.show()

#Get slider value
time_temp({'new': time_slider2.value})
time_slider2.observe(time_temp, 'value')

#Display widget
display(HBox([play2, time_slider2]))
display(out7)

#import ipywidgets as widgets
#from IPython.display import clear_output, SVG

out8 = widgets.Output()
frame_2 = 1

#Toggle images
def show_steps_2():
    global frame_2

    I21 = widgets.HTMLMath(value="Step 1: Calculate the heat loss required to change steam from 120°C to 100°C. Since there is no phase change taking place, we use $Q = mCΔT$.")
    Q21 = widgets.HTMLMath(value="$Q_{1}$ = (0.01 kg) (2020 J/kg°C) (100°C - 120°C) = -404 J")
    I22 = widgets.HTMLMath(value="Step 2: Calculate the heat loss required to change steam at 100°C to water at 100°C. Since a phase change is taking place (condensation), we use $Q = -mH_{v}$.")
    Q22 = widgets.HTMLMath(value="$Q_{2}$ = - (0.01 kg) (2260000 J/kg) = -22600 J")
    I23 = widgets.HTMLMath(value="Step 3: Calculate the heat loss required to change water from 100°C to 50°C. Since there is no phase change taking place, we use $Q = mCΔT$.")
    Q23 = widgets.HTMLMath(value="$Q_{3}$ = (0.01 kg) (4180 J/kg°C) (50°C - 100°C) = -2090 J")
    I24 = widgets.HTMLMath(value="Summary: Calculate the total heat loss by adding up the values calculated in the previous steps. $Q$ = $Q_1$ + $Q_2$ + $Q_3$")
    Q24 = widgets.HTMLMath(value="$Q$ = (-404 + -22600 + -2090) J = -25000 J or -25 kJ")
    
    if frame_2 == 0:
        display(SVG("Images/phase_diagram_2_0.svg"))
        frame_2 = 1
    elif frame_2 == 1:
        display(SVG("Images/phase_diagram_2_1.svg"))
        display(I21, Q21)
        frame_2 = 2
    elif frame_2 == 2:
        display(SVG("Images/phase_diagram_2_2.svg"))
        display(I21, Q21, I22, Q22)
        frame_2 = 3
    elif frame_2 == 3:
        display(SVG("Images/phase_diagram_2_3.svg"))
        display(I21, Q21, I22, Q22, I23, Q23)
        frame_2 = 4
    elif frame_2 == 4:
        display(SVG("Images/phase_diagram_2_4.svg"))
        display(I21, Q21, I22, Q22, I23, Q23, I24, Q24)
        frame_2 = 0
        
button_phase_diagram_2 = widgets.Button(description="Show Next Step", button_style = 'primary')
display(button_phase_diagram_2)

def on_submit_button_phase_diagram_2_clicked(b):
    with out8:
        clear_output(wait=True)
        show_steps_2()

with out8:
    display(SVG("Images/phase_diagram_2_0.svg"))
    
button_phase_diagram_2.on_click(on_submit_button_phase_diagram_2_clicked)
display(out8)

### Practice

There are many variations that are possible with specific heat and latent heat questions. Use the *Generate New Question* button to generate additional practice problems. These practice problems will vary from one to five steps.

**One Step Problem**

#import math
#import random
#from IPython.display import Javascript, display
#from ipywidgets import widgets, Layout

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Dictionary of materials
materials = {"aluminum": 903, "brass": 376, "carbon": 710, "copper": 385, "glass": 664, "iron": 450, "lead": 130, "silver": 235, "stainless Steal": 460, "tin": 217, "water": 4180, "zinc": 388}
material = random.choice(list(materials.keys()))

#Randomize variables
mass = round(random.uniform(100.0, 1000.0), 1)
temperature_initial, temperature_final = 0,0

variety1 = random.randint(1,5)
    
if variety1 == 1:
    #Makes certain that initial and final temps are different
    while temperature_initial == temperature_final:
        temperature_initial = round(random.uniform(-50.0, 0.0), 1)
        temperature_final = round(random.uniform(-50.0, 0.0), 1)

    question = "How much heat is needed for a {} g block of ice at {}°C to change temperature to {}°C?".format(mass, temperature_initial, temperature_final)
    print(question)
    answer = (mass/1000) * 2060 * (temperature_final - temperature_initial)
elif variety1 == 2:
    while temperature_initial == temperature_final:
        temperature_initial = round(random.uniform(0.0, 100.0), 1)
        temperature_final = round(random.uniform(0.0, 100.0), 1)

    question = "How much heat is needed for {} g of water at {}°C to change temperature to {}°C?".format(mass, temperature_initial, temperature_final)
    print(question)
    answer = (mass/1000) * 4180 * (temperature_final - temperature_initial)
elif variety1 == 3:
    while temperature_initial == temperature_final:
        temperature_initial = round(random.uniform(100.0, 150.0), 1)
        temperature_final = round(random.uniform(100.0, 150.0), 1)

    question = "How much heat is needed for {} g of steam at {}°C to change temperature to {}°C?".format(mass, temperature_initial, temperature_final)
    print(question)
    answer = (mass/1000) * 2020 * (temperature_final - temperature_initial)
elif variety1 == 4:
    temperature_initial = 0
    temperature_final = 0
    direction_variety = random.randint(1,2)
    if direction_variety == 1:
        question = "How much heat is needed to change {} g of ice at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = (mass/1000) * 334000
    elif direction_variety == 2:
        question = "How much heat is needed to change {} g of water at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = (mass/1000) * -334000
elif variety1 == 5:
    temperature_initial = 100
    temperature_final = 100
    direction_variety = random.randint(1,2)
    if direction_variety == 1:
        question = "How much heat is needed to change {} g of water at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = (mass/1000) * 2260000
    elif direction_variety == 2:
        question = "How much heat is needed to change {} g of steam at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = (mass/1000) * -2260000
            
#Define range of values for random multiple choices
mini = -1000
maxa = 1000

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(int(round(answer/1000))) + " kJ" 
option_2 = str(round(choice_list[0],1)) + " kJ"
option_3 = str(round(choice_list[1],1)) + " kJ"
option_4 = str(round(-1*choice_list[2],1)) + " kJ"

multiple_choice(option_1, option_2, option_3, option_4)

**Two Step Problem**

#import math
#import random
#from IPython.display import Javascript, display
#from ipywidgets import widgets, Layout

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Dictionary of materials
materials = {"aluminum": 903, "brass": 376, "carbon": 710, "copper": 385, "glass": 664, "iron": 450, "lead": 130, "silver": 235, "stainless Steal": 460, "tin": 217, "water": 4180, "zinc": 388}
material = random.choice(list(materials.keys()))

#Randomize variables
mass = round(random.uniform(100.0, 1000.0), 1)
temperature_initial, temperature_final = 0,0

variety2 = random.randint(1,4)
    
if variety2 == 1:
    direction_variety = random.randint(1,2)
    if direction_variety == 1:
        temperature_initial = round(random.uniform(-50.0, -1.0), 1)
        temperature_final = 0
        question = "How much heat is needed to change {} g of ice at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2060*(temperature_final - temperature_initial)) + ((mass/1000) * 334000)
    elif direction_variety == 2:
        temperature_initial = 0
        temperature_final = round(random.uniform(-50.0, -1.0), 1)
        question = "How much heat is needed to change {} g of water at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2060*(temperature_final - temperature_initial)) + ((mass/1000) * -334000)
elif variety2 == 2:
    direction_variety = random.randint(1,2)
    if direction_variety == 1:
        temperature_initial = 0
        temperature_final = round(random.uniform(1.0, 99.0), 1)
        question = "How much heat is needed to change {} g of ice at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*4180*(temperature_final - temperature_initial)) + ((mass/1000) * 334000)
    elif direction_variety == 2:
        temperature_initial = round(random.uniform(1.0, 99.0), 1)
        temperature_final = 0
        question = "How much heat is needed to change {} g of water at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*4180*(temperature_final - temperature_initial)) + ((mass/1000) * -334000)
elif variety2 == 3:
    direction_variety = random.randint(1,2)
    if direction_variety == 1:
        temperature_initial = round(random.uniform(1.0, 99.0), 1)
        temperature_final = 100
        question = "How much heat is needed to change {} g of water at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*4180*(temperature_final - temperature_initial)) + ((mass/1000) * 2260000)
    elif direction_variety == 2:
        temperature_initial = 100
        temperature_final = round(random.uniform(1.0, 99.0), 1)
        question = "How much heat is needed to change {} g of steam at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*4180*(temperature_final - temperature_initial)) + ((mass/1000) * -2260000)
elif variety2 == 4:
    direction_variety = random.randint(1,2)
    if direction_variety == 1:
        temperature_initial = 100
        temperature_final = round(random.uniform(101.0, 150.0), 1)
        question = "How much heat is needed to change {} g of water at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2020*(temperature_final - temperature_initial)) + ((mass/1000) * 2260000)
    elif direction_variety == 2:
        temperature_initial = round(random.uniform(101.0, 150.0), 1)
        temperature_final = 100
        question = "How much heat is needed to change {} g of steam at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2020*(temperature_final - temperature_initial)) + ((mass/1000) * -2260000)

#Define range of values for random multiple choices
mini = -1000
maxa = 1000

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(int(round(answer/1000))) + " kJ" 
option_2 = str(round(choice_list[0],1)) + " kJ"
option_3 = str(round(choice_list[1],1)) + " kJ"
option_4 = str(round(-1*choice_list[2],1)) + " kJ"

multiple_choice(option_1, option_2, option_3, option_4)

**Three Step Problem**

#import math
#import random
#from IPython.display import Javascript, display
#from ipywidgets import widgets, Layout

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Dictionary of materials
materials = {"aluminum": 903, "brass": 376, "carbon": 710, "copper": 385, "glass": 664, "iron": 450, "lead": 130, "silver": 235, "stainless Steal": 460, "tin": 217, "water": 4180, "zinc": 388}
material = random.choice(list(materials.keys()))

#Randomize variables
mass = round(random.uniform(100.0, 1000.0), 1)
temperature_initial, temperature_final = 0,0

variety3 = random.randint(1,2)

if variety3 == 1:
    direction_variety = random.randint(1,2)
    if direction_variety == 1:
        temperature_initial = round(random.uniform(-50.0, -1.0), 1)
        temperature_final = round(random.uniform(1.0, 99.0), 1)
        question = "How much heat is needed to change {} g of ice at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2060*(0 - temperature_initial)) + ((mass/1000)*4180*(temperature_final - 0)) + ((mass/1000) * 334000)
    elif direction_variety == 2:
        temperature_initial = round(random.uniform(1.0, 99.0), 1)
        temperature_final = round(random.uniform(-50.0, -1.0), 1)
        question = "How much heat is needed to change {} g of water at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2060*(temperature_final-0)) + ((mass/1000)*4180*(0 - temperature_initial)) + ((mass/1000) * -334000)
elif variety3 == 2:
    direction_variety = random.randint(1,2)
    if direction_variety == 1:
        temperature_initial = round(random.uniform(1.0, 99.0), 1)
        temperature_final = round(random.uniform(101.0, 150.0), 1)
        question = "How much heat is needed to change {} g of water at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*4180*(100 - temperature_initial)) + ((mass/1000)*2020*(temperature_final - 100)) + ((mass/1000) * 2260000)
    elif direction_variety == 2:
        temperature_initial = round(random.uniform(101.0, 150.0), 1)
        temperature_final = round(random.uniform(1.0, 99.0), 1)
        question = "How much heat is needed to change {} g of steam at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*4180*(temperature_final-100)) + ((mass/1000)*2020*(100 - temperature_initial)) + ((mass/1000) * -2260000)

#Define range of values for random multiple choices
mini = -1000
maxa = 1000

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(int(round(answer/1000))) + " kJ" 
option_2 = str(round(choice_list[0],1)) + " kJ"
option_3 = str(round(choice_list[1],1)) + " kJ"
option_4 = str(round(-1*choice_list[2],1)) + " kJ"

multiple_choice(option_1, option_2, option_3, option_4)

**Four Step Problem**

#import math
#import random
#from IPython.display import Javascript, display
#from ipywidgets import widgets, Layout

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Dictionary of materials
materials = {"aluminum": 903, "brass": 376, "carbon": 710, "copper": 385, "glass": 664, "iron": 450, "lead": 130, "silver": 235, "stainless Steal": 460, "tin": 217, "water": 4180, "zinc": 388}
material = random.choice(list(materials.keys()))

#Randomize variables
mass = round(random.uniform(100.0, 1000.0), 1)
temperature_initial, temperature_final = 0,0

variety4 = random.randint(1,2)

if variety4 == 1:
    direction_variety = random.randint(1,2)
    if direction_variety == 1:
        temperature_initial = round(random.uniform(-50.0, -1.0), 1)
        temperature_final = 100
        question = "How much heat is needed to change {} g of ice at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2060*(0 - temperature_initial)) + ((mass/1000)*4180*(temperature_final - 0)) + ((mass/1000) * 334000) + ((mass/1000) * 2260000)
    elif direction_variety == 2:
        temperature_initial = 100
        temperature_final = round(random.uniform(-50.0, -1.0), 1)
        question = "How much heat is needed to change {} g of steam at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2060*(temperature_final-0)) + ((mass/1000)*4180*(0 - temperature_initial)) + ((mass/1000) * -334000) + ((mass/1000) * -2260000)
elif variety4 == 2:
    direction_variety = random.randint(1,2)
    if direction_variety == 1:
        temperature_initial = 0
        temperature_final = round(random.uniform(100.0, 150.0), 1)
        question = "How much heat is needed to change {} g of ice at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2020*(temperature_final - 100)) + ((mass/1000)*4180*(100 - temperature_initial)) + ((mass/1000) * 334000) + ((mass/1000) * 2260000)
    elif direction_variety == 2:
        temperature_initial = round(random.uniform(100.0, 150.0), 1)
        temperature_final = 0
        question = "How much heat is needed to change {} g of steam at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2020*(100-temperature_initial)) + ((mass/1000)*4180*(temperature_final-100)) + ((mass/1000) * -334000) + ((mass/1000) * -2260000)

#Define range of values for random multiple choices
mini = -1000
maxa = 1000

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(int(round(answer/1000))) + " kJ" 
option_2 = str(round(choice_list[0],1)) + " kJ"
option_3 = str(round(choice_list[1],1)) + " kJ"
option_4 = str(round(-1*choice_list[2],1)) + " kJ"

multiple_choice(option_1, option_2, option_3, option_4)

**Five Step Problem**

#import math
#import random
#from IPython.display import Javascript, display
#from ipywidgets import widgets, Layout

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Dictionary of materials
materials = {"aluminum": 903, "brass": 376, "carbon": 710, "copper": 385, "glass": 664, "iron": 450, "lead": 130, "silver": 235, "stainless Steal": 460, "tin": 217, "water": 4180, "zinc": 388}
chosen_material = random.choice(list(materials.keys()))

#Randomize variables
mass = round(random.uniform(100.0, 1000.0), 1)
temperature_initial, temperature_final = 0,0

direction_variety = random.randint(1,2)

if direction_variety == 1:
    temperature_initial = round(random.uniform(-50.0, -1.0), 1)
    temperature_final = round(random.uniform(101.0, 150.0), 1)
    question = "How much heat is needed to change {} g of ice at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
    print(question)
    answer = ((mass/1000)*2060*(0 - temperature_initial)) + ((mass/1000)*4180*(100 - 0)) + ((mass/1000)*2020*(temperature_final - 100)) + ((mass/1000) * 334000) + ((mass/1000) * 2260000)
elif direction_variety == 2:
    temperature_initial = round(random.uniform(101.0, 150.0), 1)
    temperature_final = round(random.uniform(-50.0, -1.0), 1)
    question = "How much heat is needed to change {} g of steam at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
    print(question)
    answer = ((mass/1000)*2020*(100 - temperature_initial)) + ((mass/1000)*4180*(0 - 100)) + ((mass/1000)*2060*(temperature_final - 0)) + ((mass/1000) * -334000) + ((mass/1000) * -2260000)

#Define range of values for random multiple choices
mini = -1000
maxa = 1000

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(int(round(answer/1000))) + " kJ" 
option_2 = str(round(choice_list[0],1)) + " kJ"
option_3 = str(round(choice_list[1],1)) + " kJ"
option_4 = str(round(-1*choice_list[2],1)) + " kJ"

multiple_choice(option_1, option_2, option_3, option_4)

**Mixed Step Problems**

In the dropdown menus below, select how many steps are required and select the correct amount of heat required for each question.

**Hint:** Have some scrap-paper nearby for the calculations and be sure to sketch a diagram of each scenario to determine how many steps are required.

#import math
#import random
#from IPython.display import Javascript, display
#from ipywidgets import widgets, Layout

def generate_new_question(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

button_generate_question = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'), button_style='success')
button_generate_question.on_click(generate_new_question)
display(button_generate_question)

#Randomize variables
mass = round(random.uniform(100.0, 1000.0), 1)
temperature_initial, temperature_final = 0,0

#Determine question type
question_type = random.randint(1,5)

if question_type == 1:
    #Type 1: One Step
    steps = "One Step"
    type1_variety = random.randint(1,5)
    
    if type1_variety == 1:
        #Makes certain that initial and final temps are different
        while temperature_initial == temperature_final:
            temperature_initial = round(random.uniform(-50.0, 0.0), 1)
            temperature_final = round(random.uniform(-50.0, 0.0), 1)
        
        question = "How much heat is needed for a {} g block of ice at {}°C to change temperature to {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = (mass/1000) * 2060 * (temperature_final - temperature_initial)
    elif type1_variety == 2:
        while temperature_initial == temperature_final:
            temperature_initial = round(random.uniform(0.0, 100.0), 1)
            temperature_final = round(random.uniform(0.0, 100.0), 1)
        
        question = "How much heat is needed for {} g of water at {}°C to change temperature to {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = (mass/1000) * 4180 * (temperature_final - temperature_initial)
    elif type1_variety == 3:
        while temperature_initial == temperature_final:
            temperature_initial = round(random.uniform(100.0, 150.0), 1)
            temperature_final = round(random.uniform(100.0, 150.0), 1)
        
        question = "How much heat is needed for {} g of steam at {}°C to change temperature to {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = (mass/1000) * 2020 * (temperature_final - temperature_initial)
    elif type1_variety == 4:
        temperature_initial = 0
        temperature_final = 0
        direction_variety = random.randint(1,2)
        if direction_variety == 1:
            question = "How much heat is needed to change {} g of ice at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = (mass/1000) * 334000
        elif direction_variety == 2:
            question = "How much heat is needed to change {} g of water at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = (mass/1000) * -334000
    elif type1_variety == 5:
        temperature_initial = 100
        temperature_final = 100
        direction_variety = random.randint(1,2)
        if direction_variety == 1:
            question = "How much heat is needed to change {} g of water at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = (mass/1000) * 2260000
        elif direction_variety == 2:
            question = "How much heat is needed to change {} g of steam at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = (mass/1000) * -2260000
elif question_type == 2:
    #Type 2: Two Steps
    steps = "Two Steps"
    type2_variety = random.randint(1,4)
    
    if type2_variety == 1:
        direction_variety = random.randint(1,2)
        if direction_variety == 1:
            temperature_initial = round(random.uniform(-50.0, -1.0), 1)
            temperature_final = 0
            question = "How much heat is needed to change {} g of ice at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*2060*(temperature_final - temperature_initial)) + ((mass/1000) * 334000)
        elif direction_variety == 2:
            temperature_initial = 0
            temperature_final = round(random.uniform(-50.0, -1.0), 1)
            question = "How much heat is needed to change {} g of water at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*2060*(temperature_final - temperature_initial)) + ((mass/1000) * -334000)
    elif type2_variety == 2:
        direction_variety = random.randint(1,2)
        if direction_variety == 1:
            temperature_initial = 0
            temperature_final = round(random.uniform(1.0, 99.0), 1)
            question = "How much heat is needed to change {} g of ice at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*4180*(temperature_final - temperature_initial)) + ((mass/1000) * 334000)
        elif direction_variety == 2:
            temperature_initial = round(random.uniform(1.0, 99.0), 1)
            temperature_final = 0
            question = "How much heat is needed to change {} g of water at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*4180*(temperature_final - temperature_initial)) + ((mass/1000) * -334000)
    elif type2_variety == 3:
        direction_variety = random.randint(1,2)
        if direction_variety == 1:
            temperature_initial = round(random.uniform(1.0, 99.0), 1)
            temperature_final = 100
            question = "How much heat is needed to change {} g of water at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*4180*(temperature_final - temperature_initial)) + ((mass/1000) * 2260000)
        elif direction_variety == 2:
            temperature_initial = 100
            temperature_final = round(random.uniform(1.0, 99.0), 1)
            question = "How much heat is needed to change {} g of steam at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*4180*(temperature_final - temperature_initial)) + ((mass/1000) * -2260000)
    elif type2_variety == 4:
        direction_variety = random.randint(1,2)
        if direction_variety == 1:
            temperature_initial = 100
            temperature_final = round(random.uniform(101.0, 150.0), 1)
            question = "How much heat is needed to change {} g of water at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*2020*(temperature_final - temperature_initial)) + ((mass/1000) * 2260000)
        elif direction_variety == 2:
            temperature_initial = round(random.uniform(101.0, 150.0), 1)
            temperature_final = 100
            question = "How much heat is needed to change {} g of steam at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*2020*(temperature_final - temperature_initial)) + ((mass/1000) * -2260000)
elif question_type == 3:
    #Type 3: Three Steps
    steps = "Three Steps"
    type3_variety = random.randint(1,2)
    
    if type3_variety == 1:
        direction_variety = random.randint(1,2)
        if direction_variety == 1:
            temperature_initial = round(random.uniform(-50.0, -1.0), 1)
            temperature_final = round(random.uniform(1.0, 99.0), 1)
            question = "How much heat is needed to change {} g of ice at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*2060*(0 - temperature_initial)) + ((mass/1000)*4180*(temperature_final - 0)) + ((mass/1000) * 334000)
        elif direction_variety == 2:
            temperature_initial = round(random.uniform(1.0, 99.0), 1)
            temperature_final = round(random.uniform(-50.0, -1.0), 1)
            question = "How much heat is needed to change {} g of water at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*2060*(temperature_final-0)) + ((mass/1000)*4180*(0 - temperature_initial)) + ((mass/1000) * -334000)
    elif type3_variety == 2:
        direction_variety = random.randint(1,2)
        if direction_variety == 1:
            temperature_initial = round(random.uniform(1.0, 99.0), 1)
            temperature_final = round(random.uniform(101.0, 150.0), 1)
            question = "How much heat is needed to change {} g of water at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*4180*(100 - temperature_initial)) + ((mass/1000)*2020*(temperature_final - 100)) + ((mass/1000) * 2260000)
        elif direction_variety == 2:
            temperature_initial = round(random.uniform(101.0, 150.0), 1)
            temperature_final = round(random.uniform(1.0, 99.0), 1)
            question = "How much heat is needed to change {} g of steam at {}°C to water at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*4180*(temperature_final-100)) + ((mass/1000)*2020*(100 - temperature_initial)) + ((mass/1000) * -2260000)
elif question_type == 4:
    #Type 4: Four Steps
    steps = "Four Steps"
    type4_variety = random.randint(1,2)
    
    if type4_variety == 1:
        direction_variety = random.randint(1,2)
        if direction_variety == 1:
            temperature_initial = round(random.uniform(-50.0, -1.0), 1)
            temperature_final = 100
            question = "How much heat is needed to change {} g of ice at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*2060*(0 - temperature_initial)) + ((mass/1000)*4180*(temperature_final - 0)) + ((mass/1000) * 334000) + ((mass/1000) * 2260000)
        elif direction_variety == 2:
            temperature_initial = 100
            temperature_final = round(random.uniform(-50.0, -1.0), 1)
            question = "How much heat is needed to change {} g of steam at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*2060*(temperature_final-0)) + ((mass/1000)*4180*(0 - temperature_initial)) + ((mass/1000) * -334000) + ((mass/1000) * -2260000)
    elif type4_variety == 2:
        direction_variety = random.randint(1,2)
        if direction_variety == 1:
            temperature_initial = 0
            temperature_final = round(random.uniform(100.0, 150.0), 1)
            question = "How much heat is needed to change {} g of ice at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*2020*(temperature_final - 100)) + ((mass/1000)*4180*(100 - temperature_initial)) + ((mass/1000) * 334000) + ((mass/1000) * 2260000)
        elif direction_variety == 2:
            temperature_initial = round(random.uniform(100.0, 150.0), 1)
            temperature_final = 0
            question = "How much heat is needed to change {} g of steam at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
            print(question)
            answer = ((mass/1000)*2020*(100-temperature_initial)) + ((mass/1000)*4180*(temperature_final-100)) + ((mass/1000) * -334000) + ((mass/1000) * -2260000)
elif question_type == 5:
    #Type 5: Five Steps
    steps = "Five Steps"
    direction_variety = random.randint(1,2)

    if direction_variety == 1:
        temperature_initial = round(random.uniform(-50.0, -1.0), 1)
        temperature_final = round(random.uniform(101.0, 150.0), 1)
        question = "How much heat is needed to change {} g of ice at {}°C to steam at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2060*(0 - temperature_initial)) + ((mass/1000)*4180*(100 - 0)) + ((mass/1000)*2020*(temperature_final - 100)) + ((mass/1000) * 334000) + ((mass/1000) * 2260000)
    elif direction_variety == 2:
        temperature_initial = round(random.uniform(101.0, 150.0), 1)
        temperature_final = round(random.uniform(-50.0, -1.0), 1)
        question = "How much heat is needed to change {} g of steam at {}°C to ice at {}°C?".format(mass, temperature_initial, temperature_final)
        print(question)
        answer = ((mass/1000)*2020*(100 - temperature_initial)) + ((mass/1000)*4180*(0 - 100)) + ((mass/1000)*2060*(temperature_final - 0)) + ((mass/1000) * -334000) + ((mass/1000) * -2260000)

#Define range of values for random multiple choices
mini = -1000
maxa = 1000

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(int(round(answer/1000))) + " kJ" 
option_2 = str(round(choice_list[0],1)) + " kJ"
option_3 = str(round(choice_list[1],1)) + " kJ"
option_4 = str(round(-1*choice_list[2],1)) + " kJ"

option_list = [option_1, option_2, option_3, option_4]
correct_answer = option_list[0]

#Randomly shuffle the options
random.shuffle(option_list)

#Create dropdown menus
dropdown1_1 = widgets.Dropdown(options={' ':0,'One Step': 1, 'Two Steps': 2, 'Three Steps': 3, 'Four Steps': 4, 'Five Steps': 5}, value=0, description='Steps',)
dropdown1_2 = widgets.Dropdown(options={' ':0,option_list[0]: 1, option_list[1]: 2, option_list[2]: 3, option_list[3]: 4}, value=0, description='Answer',)

#Display menus as 1x2 table
container1_1 = widgets.HBox(children=[dropdown1_1, dropdown1_2])
display(container1_1), print(" ", end='\r')

#Evaluate input
def check_answer_dropdown(b):
    answer1_1 = dropdown1_1.label
    answer1_2 = dropdown1_2.label
    
    if answer1_1 == steps and answer1_2 == correct_answer:
        print("Correct!    ", end='\r')
    elif answer1_1 != ' ' and answer1_2 != ' ':
        print("Try again.", end='\r')
    else:
        print("            ", end='\r')

dropdown1_1.observe(check_answer_dropdown, names='value')
dropdown1_2.observe(check_answer_dropdown, names='value')

## Conclusions

* The **specific heat capacity** of a material is an empirically determined value characteristic of a particular material. It is defined as the amount of heat needed to raise the temperature of 1 kg of the material by 1°C.
* We use the formula $Q=mc\Delta T$ to calculate the amount of heat required to change the temperature of a material in which there is no change of phase.
* The **latent heat of fusion** ($H_f$) is defined as the amount of heat needed to melt 1 kg of a solid without a change in temperature.
* The **latent heat of vaporization** ($H_v$) is define as the amount of heat needed to vaporise 1 kg of a liquid without a change in temperature.
* We use the formula $Q=mH_f$ to calculate the heat required to change a material from a solid to a liquid, or from a liquid to a solid.
* We use the formula $Q=mH_v$ to calculate the heat required to change a material from a liquid to a gas, or from a gas to a liquid.
* If heat is being taken away, then a negative sign must be placed in front of $H_f$ and $H_v$.
* We use a combination of the above formulae to compute the heat required to change a material from an initial temperature to a final temperature when one (or more) phase changes occur across a range of temperatures.

Images in this notebook represent original artwork.

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