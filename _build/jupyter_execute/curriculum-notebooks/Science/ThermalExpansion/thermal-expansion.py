![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/ThermalExpansion/thermal-expansion.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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

from ipywidgets import Output, IntSlider, VBox, Layout
from IPython.display import Javascript,clear_output, display, HTML
import ipywidgets as widgets
import random
from plotly.offline import init_notebook_mode, iplot
from ipywidgets import HBox
import plotly.graph_objs as go
import numpy as np
import random

init_notebook_mode(connected=True)

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

def run_all(ev):
    display(Javascript('IPython.notebook.execute_cell()'))

# Thermal Linear Expansion

## Introduction

The goal of this notebook is to discuss the following:
- Review **Kinetic Molecular Theory** and how it relates to thermal expansion.
- Derive a **formula** to compute thermal expansion.
- **Apply** this formula to real-world scenarios.

## Kinetic Molecular Theory

**Summary:**

- Matter is made up of particles that are constantly moving.
- The temperature of a substance is a measure of the average kinetic energy of the particles.
- There are spaces between particles of matter. The average amount of empty space between molecules gets progressively larger as a sample of matter moves from solid to the liquid and gas phases.

<img style="float: center;" src="images/particles.svg" width="400">

start_bold = "\033[1m"; end_bold = "\033[0;0m"
question = start_bold + "Key Question: " + end_bold + \
"Most solids " + start_bold + "expand" + end_bold + " when heated. Based on the points above, " + start_bold + "why is this the case?" + end_bold
print(question)
print("")
option_1 = "When heat is added to a substance, the molecules vibrate faster causing the space between molecules to increase."
option_2 = "An increase in temperature causes the molecules to loosen up and move freely but slowly around."
option_3 = "As objects become hotter, they contract and the molecules increase their speed."
option_4 = "An increase in temperature causes the molecules to tighten up and move in a constricted manner."

multiple_choice(option_1, option_2, option_3, option_4)

## Thermal Linear Expansion

**Definition:** The increase in length of a solid in one direction (due to an increase in temperature) is called *thermal linear expansion*. 

**Goal:** Given any solid, we wish to **predict** how much the solid will expand with a change in temperature; i.e. how do we predict the *change in length* ($\Delta L$) of a solid due to an increase in temperature?

<img style="float: center;" src="images/RodExpanding.svg"  width="400">

start_bold = "\033[1m"; end_bold = "\033[0;0m"
question = start_bold + "Key Question: " + end_bold + "What " + start_bold + "variable(s)" + end_bold + " would you need know to predict how much a substance will expand when heat is added?"
print(question)
print("")
option_1 = "Type of material, Initial length/size, Amount of heat added"
option_2 = "Type of material, Amount of heat added"
option_3 = "Pressure acting material, Amount of heat added"
option_4 = "Roughness of the material, Type of material"

multiple_choice(option_1, option_2, option_3, option_4)

**Fact:** The change of length $(\Delta L)$ of a solid depends on **three** factors:
1. *Initial length* of the solid $(L)$
2. *Temperature change* $(\Delta T)$
3. Type of material, distinguished by a constant value named the *coefficient of linear expansion* $(\alpha)$

Some values for the coefficient of linear expansion are shown in the table below:

 Materials                 | Coefficient of linear expansion, $\alpha$ $\:$ ($1/°\rm{C}$)
 ---                       | ---
 Aluminum                  | 25 $\times$ 10$^{-6}$
 Concrete, iron, steel     | 12 $\times$ 10$^{-6}$
 Copper                    | 16 $\times$ 10$^{-6}$
 Glass (soft), Platinum    | 9 $\times$ 10$^{-6}$
 Glass (Pyrex)             | 3 $\times$ 10$^{-6}$

The following formula relates these **four quantities variables** together: 

$$\Delta L = \alpha L \Delta T$$

We will derive this formula later on in the notebook. Before that, let's get accustomed to using this formula in practical situations.

### Example

The longest continuous bridge in Saskatchewan is a 380 m long steel bridge in North Battleford. The temperature in the area varies from -40.0 $^\circ$C to 30.0 $^\circ$C. What is the *change in length of the bridge*? Round to two significant figures.

out1 = Output()
Step1B = widgets.Button(description="STEP 1", layout=Layout(width='20%', height='100%'))
count1 = 1

info1 = widgets.HTMLMath(value="Identify the variables that we know and what we're looking for:")
math_text1 = widgets.HTMLMath(value="Initial length: $L=380\:m$")
math_text2 = widgets.HTMLMath(value="Change in temperature: $\Delta T = T_{final} - T_{initial}$ = 30°C $-$ ($-$40°C) = 70°C")
math_text3 = widgets.HTMLMath(value="Coefficient of linear expansion (specific to steel): " + chr(0x3B1) + " = $12 × 10^{-6}$ °C$^{-1}$ (reference from table)")
math_text4 = widgets.HTMLMath(value="Change in length of the bridge:  $\Delta L$ = ?")



def on_Step1B_clicked(b):
    global count1
    count1 += 1
    with out1:
        clear_output()
        if count1 % 2 == 0:
            display(info1, math_text1, math_text2, math_text3, math_text4)
            
display(VBox([Step1B, out1]))
Step1B.on_click(on_Step1B_clicked)

out2 = Output()
Step2B = widgets.Button(description="STEP 2", layout=Layout(width='20%', height='100%'))
count2 = 1

info2 = widgets.HTMLMath(value="Substitute each known value into the formula and solve for the missing variable:")
math_text5 = widgets.HTMLMath(value="$\Delta L$ = " + chr(0x3B1) + " L $\Delta T$ = ($12 × 10^{-6}$ °C$^{-1}$)(380 m)(70 °C) = 0.3192 m")

def on_Step2B_clicked(b):
    global count2
    count2 += 1
    with out2:
        clear_output()
        if count2 % 2 == 0:
            display(info2, math_text5)
            
display(VBox([Step2B, out2]))
Step2B.on_click(on_Step2B_clicked)

out3 = Output()
Step3B = widgets.Button(description="STEP 3", layout=Layout(width='20%', height='100%'))
count3 = 1

info3 = widgets.HTMLMath(value="Round to the correct number of significant figures and convert to the correct units (if needed):")
math_text6 = widgets.HTMLMath(value="0.3192 m = 0.32 m or 32 cm")

def on_Step3B_clicked(b):
    global count3
    count3 += 1
    with out3:
        clear_output()
        if count3 % 2 == 0:
            display(info3, math_text6)
            
display(VBox([Step3B, out3]))
Step3B.on_click(on_Step3B_clicked)

### Practice
Try multiple practice problems by clicking the 'Generate New Question' button upon completing a problem.

button = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'))
button.on_click(run_all)
display(button)

#Variables to randomize
initial_length = round(random.uniform(2.0, 6.0), 2)
initial_temp = round(random.uniform(-50.0, -20.0), 1)
final_temp = round(random.uniform(30.0, 45.0), 1)

#Dictionary of different materials
materials = {"aluminum": 0.000025, "iron": 0.000012, "steel": 0.000012, "glass (soft)": 0.000009, "glass (pyrex)": 0.000003, "concrete": 0.000012, "platinum": 0.000009, "copper": 0.000016}
chosen_material = random.choice(list(materials.keys()))

#Print question
question = "A piece of {} is {} m on a cold winter day ({} °C). How much longer is it on a very hot summer day ({} °C)? Round to two decimal places.".format(chosen_material, initial_length, initial_temp, final_temp)
print(question)

#Answer calculation
answer = round((initial_length * materials[chosen_material] * (final_temp - initial_temp))*100, 2)

#Define range of values for random multiple choices
mini = 1
maxa = 100

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer*100)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = '{:.2f}'.format(answer) + " cm" 
option_2 = '{:.2f}'.format(choice_list[0]/100) + " cm"
option_3 = '{:.2f}'.format(choice_list[1]/100) + " cm"
option_4 = '{:.2f}'.format(choice_list[2]/100) + " cm"

multiple_choice(option_1, option_2, option_3, option_4)

## Deriving the Formula

Now that you are comfortable using the thermal expansion formula, we now discuss how it is derived experimentally. Of the four quantities in the equation, $\Delta L = \alpha L \Delta T$, it is the coefficient of linear expansion ($\alpha$) that may be still be mysterious in how it is measured. Previously, we have referenced a table of values to determine $\alpha$, but *where do these values come from?*

We demonstrate how to calculate $\alpha$ experimentally below. We will require two different materials so we can compare each expansion (which you can select in the dropdown menus below). We then apply *the exact same amount of heat to both materials* (which you can adjust using the slider). When you are ready, click the "Calculate Linear Expansion" button below. 

coefficients = {"Aluminum": 0.000025, "Iron": 0.000012, "Steel": 0.000012, "Glass (soft)": 0.000009, "Glass (Pyrex)": 0.000003, "Concrete": 0.000012, "Platinum": 0.000009, "Copper": 0.000016}

graph_out = Output()

selection1 = widgets.Dropdown(
    options={'Aluminum', 'Steel', 'Copper'},
    value='Aluminum',
    description='Material 1:',
)

selection2 = widgets.Dropdown(
    options={'Iron', 'Platinum', 'Glass (Pyrex)'},
    value='Iron',
    description='Material 2:',
)

temp_slider = IntSlider(continuous_update=False, wait=True, value=500, min=50, max=1000, step=50, description=chr(0x0394) + 'T (°C)')
initial_length_slider = IntSlider(continuous_update=False, wait=True, value=5, min=1, max=10, step=1, description='L (m)')

submit_button = widgets.Button(description="Calculate Linear Expansion", layout=Layout(width='20%', height='88%'),button_style='success')

################ Functions ##################

def initial_graph(material1, material2):
################# Parametric Equations #################
    s3 = np.linspace(0, 2 * np.pi, 30)
    t3 = np.linspace(0, 5, 30)
    tGrid3, sGrid3 = np.meshgrid(s3, t3)

    x3 = np.cos(tGrid3) + 1.5
    y3 = np.sin(tGrid3) + 1.5
    z3 = sGrid3

    s4 = np.linspace(0, 2 * np.pi, 30)
    t4 = np.linspace(0, 5, 30)
    tGrid4, sGrid4 = np.meshgrid(s4, t4)

    x4 = np.cos(tGrid4) + 3.5
    y4 = np.sin(tGrid4) + 3.5
    z4 = sGrid4

    ######################################################

    trace1 = go.Surface(x=x3, y=y3, z=z3, colorscale='Greens', showscale=False, text = material1, hoverinfo='text')
    trace2 = go.Surface(x=x4, y=y4, z=z4, colorscale='Blues', showscale=False, text = material2, hoverinfo='text')
    data = [trace1, trace2]
    layout = go.Layout(title = material1 + " and " + material2 + " (before heat is applied)",
    scene = dict(xaxis = dict(title='', range = [0,5],
                     backgroundcolor="rgb(200, 200, 230)",
                     gridcolor="rgb(255, 255, 255)",
                     showbackground=True,
                     zerolinecolor="rgb(255, 255, 255)",
                     showticklabels=False,),
                yaxis = dict(title='', range = [0,5],
                    backgroundcolor="rgb(230, 200,230)",
                    gridcolor="rgb(255, 255, 255)",
                    showbackground=True,
                    zerolinecolor="rgb(255, 255, 255)",
                    showticklabels=False),
                zaxis = dict(title='', range = [0,4],
                    backgroundcolor="rgb(230, 230,200)",
                    gridcolor="rgb(255, 255, 255)",
                    showbackground=True,
                    zerolinecolor="rgb(255, 255, 255)",
                    showticklabels=False,),),
              )
    config={'showLink': False, 'editable': False}
    fig = go.Figure(data=data, layout=layout)
    iplot(fig, config=config)


def graph(h, h2, material1, material2, initial_length):
    with graph_out:
        clear_output(wait=True)
        
        ################# Parametric Equations #################
        s = np.linspace(0, 2 * np.pi, 30)
        t = np.linspace(0, h, 30)
        tGrid, sGrid = np.meshgrid(s, t)
        
        x = np.cos(tGrid) + 1.5
        y = np.sin(tGrid) + 1.5
        z = sGrid + initial_length
        
        s2 = np.linspace(0, 2 * np.pi, 30)
        t2 = np.linspace(0, h2, 30)
        tGrid2, sGrid2 = np.meshgrid(s2, t2)
        
        x2 = np.cos(tGrid2) + 3.5
        y2 = np.sin(tGrid2) + 3.5
        z2 = sGrid2 + initial_length
        
        s3 = np.linspace(0, 2 * np.pi, 30)
        t3 = np.linspace(0, initial_length, 30)
        tGrid3, sGrid3 = np.meshgrid(s3, t3)
        
        x3 = np.cos(tGrid3) + 1.5
        y3 = np.sin(tGrid3) + 1.5
        z3 = sGrid3
        
        s4 = np.linspace(0, 2 * np.pi, 30)
        t4 = np.linspace(0, initial_length, 30)
        tGrid4, sGrid4 = np.meshgrid(s4, t4)
        
        x4 = np.cos(tGrid4) + 3.5
        y4 = np.sin(tGrid4) + 3.5
        z4 = sGrid4
        ######################################################
        
        trace1 = go.Surface(x=x, y=y, z=z, colorscale='Reds', showscale=False, text = chr(0x0394) + 'L (' + material1 + ') = ' + str(round(h/5 * 100 ,5)) + ' cm', hoverinfo='text')
        trace2 = go.Surface(x=x2, y=y2, z=z2, colorscale='Reds', showscale=False, text = chr(0x0394) + 'L (' + material2 + ') = ' + str(round(h2/5 * 100,5)) + ' cm', hoverinfo='text')
        trace3 = go.Surface(x=x3, y=y3, z=z3, colorscale='Greens', showscale=False, text = material1, hoverinfo='text')
        trace4 = go.Surface(x=x4, y=y4, z=z4, colorscale='Blues', showscale=False, text = material2, hoverinfo='text')
        
        data = [trace1, trace2, trace3, trace4]
        layout = go.Layout(title = chr(0x0394) + 'L (' + material1 + ') = ' + str(round(h/5 * 100 ,5)) + ' cm;  ' + chr(0x0394) + 'L (' + material2 + ') = ' + str(round(h2/5 * 100,5)) + ' cm',
                    scene = dict(
                    xaxis = dict(title='', range = [0,5],
                         backgroundcolor="rgb(200, 200, 230)",
                         gridcolor="rgb(255, 255, 255)",
                         showbackground=True,
                         zerolinecolor="rgb(255, 255, 255)",
                         showticklabels=False,),
                    yaxis = dict(title='', range = [0,5],
                        backgroundcolor="rgb(230, 200,230)",
                        gridcolor="rgb(255, 255, 255)",
                        showbackground=True,
                        zerolinecolor="rgb(255, 255, 255)",
                        showticklabels=False),
                    zaxis = dict(title='', range = [0,initial_length + max(h,h2)],
                        backgroundcolor="rgb(230, 230,200)",
                        gridcolor="rgb(255, 255, 255)",
                        showbackground=True,
                        zerolinecolor="rgb(255, 255, 255)",
                        showticklabels=False,),),
                  )
        config={'showLink': False, 'editable': False}
        fig = go.Figure(data=data, layout=layout)
        note = widgets.HTMLMath(value=r"$\textbf{Note: } \text{The thermal expansion shown below (coloured red) is magnified (5x) for easier viewing.}$")
        display(note)
        iplot(fig, config=config)

def on_submit_button_clicked(b):
    height = (initial_length_slider.value*temp_slider.value*coefficients[selection1.value]) * 5
    height2 = (initial_length_slider.value*temp_slider.value*coefficients[selection2.value]) *  5
    graph(height, height2, selection1.value, selection2.value, initial_length_slider.value)
    

display(HBox([VBox([selection1, selection2]), VBox([temp_slider, initial_length_slider])]))
display(submit_button)
display(graph_out)

with graph_out:
    initial_graph(selection1.value, selection2.value)
    
submit_button.on_click(on_submit_button_clicked)

*Use the interactive simulation above to answer the following two questions.*

start_bold = "\033[1m"; end_bold = "\033[0;0m"
question = "Keep ΔT fixed and only adjust L. Run the simulation many times, each with a different value for L (but the same value for ΔT). What happens to ΔL?"
print(question)
print("")
option_1 = "ΔL increases as L increases and ΔL decreases as L decreases."
option_2 = "ΔL increases as L decreases and ΔL decreases as L increases."
option_3 = "There is no relationship between ΔL and L."
option_4 = "When L decreases or increases, ΔL remains constant."

multiple_choice(option_1, option_2, option_3, option_4)

start_bold = "\033[1m"; end_bold = "\033[0;0m"
question = "Now, keep L fixed and only adjust ΔT. Again, run the simulation many times, each with a different value for ΔT (but the same value for L). What happens to ΔL?"
print(question)
print("")
option_1 = "ΔL increases as ΔT increases and ΔL decreases as ΔT decreases."
option_2 = "ΔL increases as ΔT decreases and ΔL decreases as ΔT increases."
option_3 = "There is no relationship between ΔL and ΔT."
option_4 = "When ΔT decreases or increases, ΔL remains constant."

multiple_choice(option_1, option_2, option_3, option_4)

**Goal:** To establish a thermal expansion formula capable of accurately predicting how much a material will expand linearly when heat is applied.

Observe how $\Delta L$ is different for some materials (aluminum versus platinum), but the same for others (steel versus iron). This is due to similarities and differences between the chemical composition of each material. For example, steel is comprised of around 90-95% iron, which accounts for both materials' identical rate of thermal expansion. 

Simply knowing the initial length ($L$) and change in temperature ($\Delta T$) is clearly not enough to predict change in length ($\Delta L$). We can see this above: when both materials share the same values of $L$ and $\Delta T$, their $\Delta L$ is often different. We somehow must assign a *constant* value (which we call $\alpha$) for each material that we can use alongside $L$ and $\Delta T$ to compute $\Delta L$. Since we experimentally measured $\Delta L$ above, we in fact have all the information we need to establish such a constant.

The above simulation and questions indicates that the relationship between $L$, $\Delta T$, and $\Delta L$ is direct rather than inverse ($1/\Delta T$ or $1/L$). Since $\Delta L$ becomes larger as both $L$ and $\Delta T$ become larger, we guess that their relationship is multiplicative. Hence, we begin by writing down the following formula that we want:

$$\Delta L = \alpha L \Delta T$$

The $\alpha$ is the constant that we need, but do not know. However, we measured $\Delta L$ and we know both $L$ and $\Delta T$, so computing $\alpha$ is easy:

$$\alpha  = \dfrac{\Delta L}{L \Delta T}$$
    
Using the sliders below, input the change in length ($\Delta L$) for both materials 1 and 2 from the above experimental simulation to compute $\alpha$ for each material. **Hint:** Use your *arrow keys* on your keyboard to use the sliders with precision.

out_text = Output()

################ Widgets #################
style = {'description_width': 'initial'}
temp1_slider = IntSlider(continuous_update=False, wait=True, value=500, min=10, max=1000, step=1, description=chr(0x0394) + 'T (°C)')
change1_slider = widgets.FloatSlider(continuous_update=False, wait=True, value=0, min=0, max=10, step=0.001, readout_format='.3f', description=chr(0x0394) + 'L'+ chr(0x2081) + ' (cm)', style=style)
change2_slider = widgets.FloatSlider(continuous_update=False, wait=True, value=0, min=0, max=10, step=0.001, readout_format='.3f', description=chr(0x0394) + 'L'+ chr(0x2082) + ' (cm)', style=style)
coeff_calc = widgets.Button(description="Calculate " + chr(0x03b1) + chr(0x2081) + " and " + chr(0x03b1) + chr(0x2082), layout=Layout(width='20%', height='88%'),button_style='success')
###########################################

display(VBox([temp1_slider, change1_slider, change2_slider, coeff_calc]))

def on_submit_button_clicked(b):
    ans1 = round(change1_slider.value / (300.0 * temp1_slider.value), 8)
    ans2 = round(change2_slider.value / (300.0 * temp1_slider.value), 8)
    with out_text:
        clear_output()
        text_answer = widgets.HTMLMath(value=r"$\alpha_1 = $ " + str(ans1) + " °C$^{-1}$" + "$\qquad$" + r"$\alpha_2 = $ " + str(ans2) + " °C$^{-1}$")
        text_answer2 = widgets.HTMLMath(value=r"Compare each $\alpha_1$ and $\alpha_2$ to those found in the table of coefficients of linear expansion above. See if they match.")
        display(text_answer)
        display(text_answer2)

### Widget Interaction Function Calls ###
coeff_calc.on_click(on_submit_button_clicked)

display(out_text)

## Variations on the Thermal Expansion Formula

As we've just seen, the formula $\Delta L = \alpha L \Delta T$ is not always used to find $\Delta L$. Often, we can experimentally measure $\Delta L$. Depending on the application, we can then theoretically compute one of the other quantities (assuming we know the value of two of the other quantities). It is worth noting the three variations of the thermal expansion formula:

$$\alpha = \dfrac{\Delta L}{L \Delta T} \qquad L = \dfrac{\Delta L}{\alpha \Delta T} \qquad \Delta T = \dfrac{\Delta L}{\alpha L}$$

**Note:** This is **one** formula being displayed in **three** different ways. It is convenient to make use of the variation that corresponds to the unknown value that you wish to determine.

### Practice 

Try the three different types of questions using the above variations of the thermal expansion formula. Use the 'Generate New Question' button to complete additional practice problems.

button1 = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'))
button1.on_click(run_all)
display(button1)

#Variables to randomize
change_length = round(random.uniform(0.2, 0.9), 2)
initial_length = round(random.uniform(1.0, 3.0), 2)
initial_temp = round(random.uniform(10.0, 25.0), 1)
final_temp = round(random.uniform(100.0, 150.0), 1)

#Print question
question = "An newly made synthetic material {} m long expands {} mm when heated from {}°C to {}°C. What is the coefficient of linear expansion of this new material?".format(initial_length, change_length, initial_temp, final_temp)
print(question)

#Answer calculation
answer = round((change_length/1000) / (initial_length * (final_temp - initial_temp)), 8)

#Define range of values for random multiple choices
mini = 100
maxa = 900

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer*100000000)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(answer) + " °C" + chr(0x207B) + chr(0x00B9) 
option_2 = str(choice_list[0]/100000000) + " °C" + chr(0x207B) + chr(0x00B9)
option_3 = str(choice_list[1]/100000000) + " °C" + chr(0x207B) + chr(0x00B9)
option_4 = str(choice_list[2]/100000000) + " °C" + chr(0x207B) + chr(0x00B9)

multiple_choice(option_1, option_2, option_3, option_4)

button2 = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'))
button2.on_click(run_all)
display(button2)

#Variables to randomize
change_length = round(random.uniform(0.5, 2.0), 2)
initial_temp = round(random.uniform(20.0, 30.0), 1)
final_temp = round(random.uniform(100.0, 250.0), 1)

#Dictionary of different materials
materials = {"aluminum": 0.000025, "iron": 0.000012, "steel": 0.000012, "glass (soft)": 0.000009, "glass (pyrex)": 0.000003, "concrete": 0.000012, "platinum": 0.000009, "copper": 0.000016}
chosen_material = random.choice(list(materials.keys()))

#Print question
question = "A piece of {} changes in length by {} m. The initial temperature was {}°C and the final temperature was {}°C. Determine the original length of the material. Leave your answer unrounded.".format(chosen_material, change_length, initial_temp, final_temp)
print(question)

#Answer calculation
answer = round(change_length / (materials[chosen_material] * (final_temp - initial_temp)), 2)

#Define range of values for random multiple choices
mini = 500
maxa = 1500

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(int(answer)) >= 1:
    choice_list = random.sample(range(mini,maxa),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = '{:.2f}'.format(answer) + " m" 
option_2 = '{:.2f}'.format(choice_list[0]) + " m"
option_3 = '{:.2f}'.format(choice_list[1]) + " m"
option_4 = '{:.2f}'.format(choice_list[2]) + " m"

multiple_choice(option_1, option_2, option_3, option_4)

button3 = widgets.Button(description="Generate New Question", layout=Layout(width='20%', height='100%'))
button3.on_click(run_all)
display(button3)


#Variables to randomize
change_length = round(random.uniform(1.0, 4.0), 2)
initial_length = round(random.uniform(100.0, 150.0), 1)

#Dictionary of different materials
materials = {"aluminum": 0.000025, "iron": 0.000012, "steel": 0.000012, "glass (soft)": 0.000009, "glass (pyrex)": 0.000003, "concrete": 0.000012, "platinum": 0.000009, "copper": 0.000016}
chosen_material = random.choice(list(materials.keys()))

#Print question
question = "By how much would you need to heat a {} inch {} sample to make it expand by {} inches? Round to the nearest degree Celsius.".format(initial_length, chosen_material, change_length)
print(question)

#Answer calculation
answer = int(change_length / (materials[chosen_material] * initial_length))

#Define range of values for random multiple choices
mini = 600
maxa = 3000

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(mini,maxa),3)
while choice_list.count(answer) >= 1:
    choice_list = random.sample(range(mini,maxa),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(answer) + " °C" 
option_2 = str(choice_list[0]) + " °C"
option_3 = str(choice_list[1]) + " °C"
option_4 = str(choice_list[2]) + " °C"

multiple_choice(option_1, option_2, option_3, option_4)

## Application: Aircraft Components

Aircraft materials often require *specialized properties* in order to operate in the most desirable manner. The specialized property of the material may be the most important consideration in materials selection. Listed below are several key specialized properties considered in aircraft materials selection:

- Electrical conductivity (important for the outer skin of the aircraft)
- Stealth (materials that can absorb radar waves and/or reduce the infrared visibility are used in the external surface of covert military aircraft)
- Thermal conductivity (used in high-temperature applications, such as heat shields and engine components)
- <span style="color: maroon">Thermal expansion (used in high-temperature range applications, such as wing and engine components)</span>

### Problem

An unknown metal alloy is being tested to discover its thermal properties to see if it suitable for use as a *spar*, which is a component of an airplane wing (shown in red below). The alloy is formed into a bar measuring 1.00 metre in length and it is then heated from its starting temperature of 30 °C to a final temperature of 100.0 °C. The length of the heated bar is measured to be exactly 1.002 metres in length. **What is the coefficient of thermal expansion of the alloy? Round your answer to two significant figures.**

<img style="float: center;" src="images/WingSpar.svg" width="600">

option_1 = str(0.000029) + " °C" + chr(0x207B) + chr(0x00B9)
option_2 = str(0.014) + " °C" + chr(0x207B) + chr(0x00B9)
option_3 = str(0.000032) + " °C" + chr(0x207B) + chr(0x00B9)
option_4 = str(0.0140) + " °C" + chr(0x207B) + chr(0x00B9)

multiple_choice(option_1, option_2, option_3, option_4)

The aircraft wing (from above) experiences temperature extremes that span 210 ℃. The spar for the wing will have a length of 18.0 metres. Testing indicates that the aircraft wing will remain stable only if the spar never expands to a length larger than 18.103 metres. **If the component is made from the metal alloy in question, will it meet this requirement?**

**Hint:** Use the sliders below to calculate the linear expansion of the spar.

################ Widgets #################
app_out = Output()
style = {'description_width': 'initial'}
temp_span = IntSlider(continuous_update=False, wait=True, value=0, min=0, max=500, step=1, description=chr(0x0394) + 'T (°C)')
initialL_alloy = widgets.FloatSlider(continuous_update=False, wait=True, value=0, min=0, max=30, step=1, readout_format='.1f', description= 'L (m)', style=style)
linear_constant = widgets.FloatSlider(continuous_update=False, wait=True, value=0, min=0, max=10, step=0.1, readout_format='.1f', description= chr(0x03b1) + " (1" + chr(0x2A09) + "10" + chr(0x207B) + chr(0x2075) + " , " + chr(0x2103) + chr(0x207B) + chr(0x00B9) + ")", style=style)
calc_change = widgets.Button(description="Calculate Linear Expansion", layout=Layout(width='20%', height='88%'),button_style='success')

############## Functions ################
def initial_spar():
    layout = go.Layout(title = "Unknown Alloy (before heat is applied)", scene = dict(
                    xaxis = dict(title='', range = [0,5],
                         backgroundcolor="rgb(200, 200, 230)",
                         gridcolor="rgb(255, 255, 255)",
                         showbackground=True,
                         zerolinecolor="rgb(255, 255, 255)",
                         showticklabels=False,),
                    yaxis = dict(title='', range = [0,5],
                        backgroundcolor="rgb(230, 200,230)",
                        gridcolor="rgb(255, 255, 255)",
                        showbackground=True,
                        zerolinecolor="rgb(255, 255, 255)",
                        showticklabels=False),
                    zaxis = dict(title='', range = [0,18],
                        backgroundcolor="rgb(230, 230,200)",
                        gridcolor="rgb(255, 255, 255)",
                        showbackground=True,
                        zerolinecolor="rgb(255, 255, 255)",
                        showticklabels=False,),),
                  )
    data = [go.Mesh3d(
            x = [2, 2, 4, 4, 2, 2, 4, 4],
            y = [2, 3, 3, 2, 2, 3, 3, 2],
            z = [0, 0, 0, 0, 18, 18, 18, 18],
            i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
            j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
            name='Unknown Alloy',
            color='#000066',
            text = "Spar (wing component; unknown alloy)", hoverinfo='text',
        )]
    config={'showLink': False, 'editable': False}
    fig = go.Figure(data=data, layout=layout)
    iplot(fig, config=config)


def draw_spar(new, i_height):
    clear_output(wait=True)
    layout = go.Layout(title = chr(0x0394) + 'L (Unknown Alloy) = ' + str(round(new * 100 ,5)) + ' cm', scene = dict(
                    xaxis = dict(title='', range = [0,5],
                         backgroundcolor="rgb(200, 200, 230)",
                         gridcolor="rgb(255, 255, 255)",
                         showbackground=True,
                         zerolinecolor="rgb(255, 255, 255)",
                         showticklabels=False,),
                    yaxis = dict(title='', range = [0,5],
                        backgroundcolor="rgb(230, 200,230)",
                        gridcolor="rgb(255, 255, 255)",
                        showbackground=True,
                        zerolinecolor="rgb(255, 255, 255)",
                        showticklabels=False),
                    zaxis = dict(title='', range = [0,18],
                        backgroundcolor="rgb(230, 230,200)",
                        gridcolor="rgb(255, 255, 255)",
                        showbackground=True,
                        zerolinecolor="rgb(255, 255, 255)",
                        showticklabels=False,),),
                  )
    data = [go.Mesh3d(
            x = [2, 2, 4, 4, 2, 2, 4, 4],
            y = [2, 3, 3, 2, 2, 3, 3, 2],
            z = [0, 0, 0, 0, 18, 18, 18, 18],
            i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
            j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
            name='Unknown Alloy',
            color='#000066',
            text = "Initial length (L) = " + str(i_height) + ' m', hoverinfo='text',
        ), go.Mesh3d(
            x = [2, 2, 4, 4, 2, 2, 4, 4],
            y = [2, 3, 3, 2, 2, 3, 3, 2],
            z = [18, 18, 18, 18, 18+new, 18+new, 18+new, 18+new],
            i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
            j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
            name='Thermal Expansion',
            color = "#CC0000",
            text = "Thermal Expansion ("+chr(0x0394)+"L) = " + str(round(new,5)) + ' m', hoverinfo='text',
        )]
    config={'showLink': False, 'editable': False}
    fig = go.Figure(data=data, layout=layout)
    iplot(fig, config=config)


def on_submit_button_clicked(b):
    alloy_change = temp_span.value * initialL_alloy.value * (linear_constant.value * 0.00001)
    with app_out:
        draw_spar(alloy_change, initialL_alloy.value)


######### Display #########
display(VBox([temp_span, initialL_alloy, linear_constant]))
display(calc_change)
display(app_out)

with app_out:
    initial_spar()
    
calc_change.on_click(on_submit_button_clicked)

option_1 = "The final length of the spar is 18.10962 m; therefore, it fails the requirement."
option_2 = "The final length of the spar is 10.962 cm; therefore, it passes the requirement."
option_3 = "The final length of the spar is 18.103 m; therefore, it passes the requirement."
option_4 = "The final length of the spar is 28.962 m; therefore, it fails the requirement."

multiple_choice(option_1, option_2, option_3, option_4)

## Conclusion

- Thermal Linear Expansion is calculated using the formula: $\Delta L = \alpha L \Delta T$.
- The coefficient of linear expansion ($\alpha$) is experimentally calculated. The experiment involves measuring $\Delta L$ and solving for $\alpha$ using the above formula.
- If the material is known (such as steel, concrete, iron, etc.) you can reference the material's coefficient of linear expansion using a Table of Coefficient of Linear Expansion.
- There are many applications to being able to predict thermal expansion, such as the building of bridges, skyscrapers, airplanes, cars, and piping (to name a few).
- This notebook covered *linear* thermal expansion. If you are interested in applying what you have learned or gaining further knowledge of material science, you're next step is to study *area expansion* and *volume expansion*, which will explore the 2-dimensional and 3-dimensional expansion of materials.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)