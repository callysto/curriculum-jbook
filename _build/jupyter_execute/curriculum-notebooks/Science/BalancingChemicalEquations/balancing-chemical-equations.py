![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/BalancingChemicalEquations/balancing-chemical-equations.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

(Click **Cell** > **Run All** before proceeding.) 

%matplotlib inline

#----------

#Import modules and packages 
import ipywidgets as widgets
import random

from ipywidgets import Output, IntSlider, VBox, HBox, Layout
from IPython.display import clear_output, display, HTML

#----------

#import ipywidgets as widgets
#import random

#This function produces a multiple choice form with four options
def multiple_choice_4(option_1, option_2, option_3, option_4):
    option_list = [option_1, option_2, option_3, option_4]
    answer = option_list[0]
    letters = ["<b>(A)</b> ", "<b>(B)</b> ", "<b>(C)</b> ", "<b>(D)</b> "]

    #Randomly shuffle the options
    random.shuffle(option_list)
    
    #Print the letters (A) to (D) in sequence with randomly chosen options
    for i in range(4):
        option_text = option_list.pop()
        option_text_2 = letters[i] + option_text
        option_output = widgets.HTMLMath(value=option_text_2)
        display(option_output)
                
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
        if "<b>(A)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Moccasin'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Lightgray'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button2_clicked(b):
        if "<b>(B)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Moccasin'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Lightgray'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button3_clicked(b):
        if "<b>(C)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Moccasin'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Lightgray'; button4.style.button_color = 'Whitesmoke'

    def on_button4_clicked(b):
        if "<b>(D)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Lightgray'

    button1.on_click(on_button1_clicked); button2.on_click(on_button2_clicked)
    button3.on_click(on_button3_clicked); button4.on_click(on_button4_clicked)

#----------

#This function produces a multiple choice form with three options
def multiple_choice_3(option_1, option_2, option_3):
    option_list = [option_1, option_2, option_3]
    answer = option_list[0]
    letters = ["<b>(A)</b> ", "<b>(B)</b> ", "<b>(C)</b> "]

    #Randomly shuffle the options
    random.shuffle(option_list)
    
    #Print the letters (A) to (D) in sequence with randomly chosen options
    for i in range(3):
        option_text = option_list.pop()
        option_text_2 = letters[i] + option_text
        option_output = widgets.HTMLMath(value=option_text_2)
        display(option_output)
                
        #Stores the correct answer
        if option_text == answer:
            letter_answer = letters[i]

    button1 = widgets.Button(description="(A)"); button2 = widgets.Button(description="(B)"); button3 = widgets.Button(description="(C)")
    
    button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'; button3.style.button_color = 'Whitesmoke'
    
    container = widgets.HBox(children=[button1,button2,button3])
    display(container)
    print(" ", end='\r')

    def on_button1_clicked(b):
        if "<b>(A)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Moccasin'; button2.style.button_color = 'Whitesmoke'; button3.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Lightgray'; button2.style.button_color = 'Whitesmoke'; button3.style.button_color = 'Whitesmoke'

    def on_button2_clicked(b):
        if "<b>(B)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Moccasin'; button3.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Lightgray'; button3.style.button_color = 'Whitesmoke'

    def on_button3_clicked(b):
        if "<b>(C)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'; button3.style.button_color = 'Moccasin';
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'; button3.style.button_color = 'Lightgray'

    button1.on_click(on_button1_clicked); button2.on_click(on_button2_clicked); button3.on_click(on_button3_clicked)

#----------

#This function produces a true or false choice form with four options
def true_false(option_1, bool_1, option_2, bool_2, option_3, bool_3, option_4, bool_4, button_text_1, button_text_2):
 
    #Convert string to HTMLMath so equations can be displayed
    TF_question_1 = widgets.HTMLMath(value=option_1)
    TF_question_2 = widgets.HTMLMath(value=option_2)
    TF_question_3 = widgets.HTMLMath(value=option_3)
    TF_question_4 = widgets.HTMLMath(value=option_4)
    
    #Create true and false bottons
    button1_1 = widgets.Button(description=button_text_1); button1_2 = widgets.Button(description=button_text_2)
    button2_1 = widgets.Button(description=button_text_1); button2_2 = widgets.Button(description=button_text_2)
    button3_1 = widgets.Button(description=button_text_1); button3_2 = widgets.Button(description=button_text_2)
    button4_1 = widgets.Button(description=button_text_1); button4_2 = widgets.Button(description=button_text_2)
    
    button1_1.style.button_color = 'Whitesmoke'; button1_2.style.button_color = 'Whitesmoke'
    button2_1.style.button_color = 'Whitesmoke'; button2_2.style.button_color = 'Whitesmoke'
    button3_1.style.button_color = 'Whitesmoke'; button3_2.style.button_color = 'Whitesmoke'
    button4_1.style.button_color = 'Whitesmoke'; button4_2.style.button_color = 'Whitesmoke'

    #Display buttons in front of each question 
    container1 = widgets.HBox(children=[button1_1,button1_2,TF_question_1])
    container2 = widgets.HBox(children=[button2_1,button2_2,TF_question_2]) 
    container3 = widgets.HBox(children=[button3_1,button3_2,TF_question_3])
    container4 = widgets.HBox(children=[button4_1,button4_2,TF_question_4])
    
    #Place true or false questions in an array so they can be shuffled
    containers = [container1, container2, container3, container4]
    random.shuffle(containers)
    
    #Reassign containers and display
    container1 = containers[0]; container2 = containers[1]
    container3 = containers[2]; container4 = containers[3]
    display(container1, container2, container3, container4)
    print(" ", end='\r')

    def on_button1_1_clicked(b):
        if bool_1 == True:
            print("Correct!    ", end='\r')
            button1_1.style.button_color = 'Moccasin'; button1_2.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1_1.style.button_color = 'Lightgray'; button1_2.style.button_color = 'Whitesmoke'

    def on_button1_2_clicked(b):
        if bool_1 == False:
            print("Correct!    ", end='\r')
            button1_1.style.button_color = 'Whitesmoke'; button1_2.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button1_1.style.button_color = 'Whitesmoke'; button1_2.style.button_color = 'Lightgray'

            
    def on_button2_1_clicked(b):
        if bool_2 == True:
            print("Correct!    ", end='\r')
            button2_1.style.button_color = 'Moccasin'; button2_2.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button2_1.style.button_color = 'Lightgray'; button2_2.style.button_color = 'Whitesmoke'

    def on_button2_2_clicked(b):
        if bool_2 == False:
            print("Correct!    ", end='\r')
            button2_1.style.button_color = 'Whitesmoke'; button2_2.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button2_1.style.button_color = 'Whitesmoke'; button2_2.style.button_color = 'Lightgray'        
            
    
    def on_button3_1_clicked(b):
        if bool_3 == True:
            print("Correct!    ", end='\r')
            button3_1.style.button_color = 'Moccasin'; button3_2.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button3_1.style.button_color = 'Lightgray'; button3_2.style.button_color = 'Whitesmoke'

    def on_button3_2_clicked(b):
        if bool_3 == False:
            print("Correct!    ", end='\r')
            button3_1.style.button_color = 'Whitesmoke'; button3_2.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button3_1.style.button_color = 'Whitesmoke'; button3_2.style.button_color = 'Lightgray'
    
    def on_button4_1_clicked(b):
        if bool_4 == True:
            print("Correct!    ", end='\r')
            button4_1.style.button_color = 'Moccasin'; button4_2.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button4_1.style.button_color = 'Lightgray'; button4_2.style.button_color = 'Whitesmoke'

    def on_button4_2_clicked(b):
        if bool_4 == False:
            print("Correct!    ", end='\r')
            button4_1.style.button_color = 'Whitesmoke'; button4_2.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button4_1.style.button_color = 'Whitesmoke'; button4_2.style.button_color = 'Lightgray'
    
    button1_1.on_click(on_button1_1_clicked); button1_2.on_click(on_button1_2_clicked)
    button2_1.on_click(on_button2_1_clicked); button2_2.on_click(on_button2_2_clicked)
    button3_1.on_click(on_button3_1_clicked); button3_2.on_click(on_button3_2_clicked)
    button4_1.on_click(on_button4_1_clicked); button4_2.on_click(on_button4_2_clicked)

# Chemical Equations: Writing and Balancing

## Introduction

A **chemical equation** is a symbolic representation of a chemical reaction. The general form of a chemical equation is:

<img src="images/general_equation_3.1.svg" width="90%"/>

The chemicals represented in a chemical equation are organized into two groups: the reactants and the products. The **reactants** are the chemicals undergoing the reaction, and the **products** are the chemicals generated by the reaction. In the equation above, the reactants and products are represented by "*R<sub>1</sub>, R<sub>2</sub>, ...*", and "*P<sub>1</sub>, P<sub>2</sub>, ...*", respectively. The reactants and products are separated from each other by an arrow symbol (&rarr;). The chemicals on each side of the arrow are separated from each other by a plus sign (+). The symbols "*c<sub>1</sub>, c<sub>2</sub>, ...*" represent the **stoichiometric coefficients**. These coefficients indicate the relative amount of each chemical involved in the reaction. An example of a chemical equation is shown below:

&nbsp; &nbsp; &nbsp; &nbsp; 2H<sub>2</sub> + O<sub>2</sub> &rarr; 2H<sub>2</sub>O

In this example, the reactants are hydrogen (H<sub>2</sub>) and oxygen (O<sub>2</sub>), and the product is water (</span>H<sub>2</sub>O). The stoichiometric coefficients are 2,1, and 2 for hydrogen, oxygen, and water, respectively. These coefficients indicate that two hydrogen molecules and one oxygen molecule are required to produced two water molecules.    

**Practice:** *Select 'reactant' or 'product' for each chemical highlighted in <span style='color:blue'>blue</span> in the following chemical equations.* 

randomize1_1 = random.randint(1, 4)

if randomize1_1 == 1:
    option1_1 = "4<span style='color:blue'>Fe</span> + 3O<sub>2</sub> &rarr; 2Fe<sub>2</sub>O<sub>3</sub>"; bool1_1 = True    
elif randomize1_1 == 2:
    option1_1 = "4Fe + 3<span style='color:blue'>O<sub>2</sub></span> &rarr; 2Fe<sub>2</sub>O<sub>3</sub>"; bool1_1 = True     
elif randomize1_1 == 3:
    option1_1 = "4Fe + 3O<sub>2</sub> &rarr; 2<span style='color:blue'>Fe<sub>2</sub>O<sub>3</sub></span>"; bool1_1 = False
elif randomize1_1 == 4:
    option1_1 = "4Fe + 3O<sub>2</sub> &rarr; 2<span style='color:blue'>Fe<sub>2</sub>O<sub>3</sub></span>"; bool1_1 = False

randomize1_2 = random.randint(1, 4)

if randomize1_2 == 1:
    option1_2 = "<span style='color:blue'>CH<sub>4</sub></span> + 2O<sub>2</sub> &rarr; CO<sub>2</sub> + 2H<sub>2</sub>O"; bool1_2 = True 
elif randomize1_2 == 2:
    option1_2 = "CH<sub>4</sub> + 2<span style='color:blue'>O<sub>2</sub></span> &rarr; CO<sub>2</sub> + 2H<sub>2</sub>O"; bool1_2 = True 
elif randomize1_2 == 3:
    option1_2 = "CH<sub>4</sub> + 2O<sub>2</sub> &rarr; <span style='color:blue'>CO<sub>2</sub></span> + 2H<sub>2</sub>O"; bool1_2 = False
elif randomize1_2 == 4:
    option1_2 = "CH<sub>4</sub> + 2O<sub>2</sub> &rarr; CO<sub>2</sub> + 2<span style='color:blue'>H<sub>2</sub>O</span>"; bool1_2 = False

randomize1_3 = random.randint(1, 4)

if randomize1_3 == 1:
    option1_3 = "2<span style='color:blue'>H<sub>2</sub>O<sub>2</sub></span> &rarr; 2H<sub>2</sub>O + O<sub>2</sub>"; bool1_3 = True
elif randomize1_3 == 2:
    option1_3 = "2<span style='color:blue'>H<sub>2</sub>O<sub>2</sub></span> &rarr; 2H<sub>2</sub>O + O<sub>2</sub>"; bool1_3 = True
elif randomize1_3 == 3:
    option1_3 = "2H<sub>2</sub>O<sub>2</sub> &rarr; 2<span style='color:blue'>H<sub>2</sub>O</span> + O<sub>2</sub>"; bool1_3 = False
elif randomize1_3 == 4:
    option1_3 = "2H<sub>2</sub>O<sub>2</sub> &rarr; 2H<sub>2</sub>O + <span style='color:blue'>O<sub>2</sub></span>"; bool1_3 = False

randomize1_4 = random.randint(1, 4)

if randomize1_4 == 1:
    option1_4 = "<span style='color:blue'>CaCl<sub>2</sub></span> + Na<sub>2</sub>CO<sub>3</sub> &rarr; CaCO<sub>3</sub> + 2NaCl"; bool1_4 = True
elif randomize1_4 == 2:
    option1_4 = "CaCl<sub>2</sub> + <span style='color:blue'>Na<sub>2</sub>CO<sub>3</sub></span> &rarr; CaCO<sub>3</sub> + 2NaCl"; bool1_4 = True
elif randomize1_4 == 3:
    option1_4 = "CaCl<sub>2</sub> + Na<sub>2</sub>CO<sub>3</sub> &rarr; <span style='color:blue'>CaCO<sub>3</sub></span> + 2NaCl"; bool1_4 = False
elif randomize1_4 == 4:
    option1_4 = "CaCl<sub>2</sub> + Na<sub>2</sub>CO<sub>3</sub> &rarr; CaCO<sub>3</sub> + 2<span style='color:blue'>NaCl</span>"; bool1_4 = False
   
true_false(option1_1, bool1_1, option1_2, bool1_2, option1_3, bool1_3, option1_4, bool1_4, "Reactant", "Product")

**Practice:** *Select the correct stoichiometric coefficient for each chemical represented in the chemical equation.* 

#import ipywidgets as widgets

#Create dropdown menus

randomize2_1 = random.randint(1, 4)

if randomize2_1 == 1:
    equation1 = widgets.HTMLMath(value="2Al + 3Cu(NO<sub>3</sub>)<sub>2</sub> &rarr; 3Cu + 2Al(NO<sub>3</sub>)<sub>3</sub>")
    chem1_1 = "Al"; chem1_2 = "Cu(NO<sub>3</sub>)<sub>2</sub>"
    chem1_3 = "Cu"; chem1_4 = "Al(NO<sub>3</sub>)<sub>3</sub>"
    ans1_1 = "2"; ans1_2 = "3"; ans1_3 = "3"; ans1_4 = "2"
    display(equation1)
elif randomize2_1 == 2:
    equation2 = widgets.HTMLMath(value="2Pb(NO<sub>3</sub>)<sub>2</sub> &rarr; 2PbO + 4NO<sub>2</sub> + O<sub>2</sub>")
    chem1_1 = "Pb(NO<sub>3</sub>)<sub>2</sub>"; chem1_2 = "PbO"
    chem1_3 = "NO<sub>2</sub>"; chem1_4 = "O<sub>2</sub>"
    ans1_1 = "2"; ans1_2 = "2"; ans1_3 = "4"; ans1_4 = "1"
    display(equation2)
elif randomize2_1 == 3:
    equation3 = widgets.HTMLMath(value="3NaOH + H<sub>3</sub>PO<sub>4</sub> &rarr; Na<sub>3</sub>PO<sub>4</sub> + 3H<sub>2</sub>O")
    chem1_1 = "NaOH"; chem1_2 = "H<sub>3</sub>PO<sub>4</sub>"
    chem1_3 = "Na<sub>3</sub>PO<sub>4</sub>"; chem1_4 = "H<sub>2</sub>O"
    ans1_1 = "3"; ans1_2 = "1"; ans1_3 = "1"; ans1_4 = "3"
    display(equation3)
elif randomize2_1 == 4:
    equation4 = widgets.HTMLMath(value="Na<sub>2</sub>S + 2HCl &rarr; 2NaCl + H<sub>2</sub>S")
    chem1_1 = "Na<sub>2</sub>S"; chem1_2 = "HCl"
    chem1_3 = "NaCl"; chem1_4 = "H<sub>2</sub>S"
    ans1_1 = "1"; ans1_2 = "2"; ans1_3 = "2"; ans1_4 = "1"
    display(equation4)

dropdown1_1 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5}, value=0, description=chem1_1,)
dropdown1_2 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5}, value=0, description=chem1_2,)
dropdown1_3 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5}, value=0, description=chem1_3,)
dropdown1_4 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5}, value=0, description=chem1_4,)

#Display menus as 2x2 table
container1_1 = widgets.VBox(children=[dropdown1_1,dropdown1_2])
container1_2 = widgets.VBox(children=[dropdown1_3,dropdown1_4])
display(widgets.HBox(children=[container1_1, container1_2])), print(" ", end='\r')

#Evaluate input
def check_answer1_1(b):
    answer1_1 = dropdown1_1.label 
    answer1_2 = dropdown1_2.label
    answer1_3 = dropdown1_3.label 
    answer1_4 = dropdown1_4.label

    if answer1_1 == ans1_1 and answer1_2 == ans1_2 and answer1_3 == ans1_3 and answer1_4 == ans1_4:
        print("Correct!    ", end='\r')
    elif answer1_1 != ' ' and answer1_2 != ' ' and answer1_3 != ' ' and answer1_4 != ' ':
        print("Try again.", end='\r')
    else:
        print("            ", end='\r')

dropdown1_1.observe(check_answer1_1, names='value')
dropdown1_2.observe(check_answer1_1, names='value')
dropdown1_3.observe(check_answer1_1, names='value')
dropdown1_4.observe(check_answer1_1, names='value')

## Writing Chemical Equations

A chemical equation may be written by following a few simple steps.

&nbsp; &nbsp; &nbsp; &nbsp; **Step 1:** Identify the reactants and products. <br>
&nbsp; &nbsp; &nbsp; &nbsp; **Step 2:** Organize the reactants and products into a chemical equation, by placing the reactants on the left of the arrow and the products on the right. <br>
&nbsp; &nbsp; &nbsp; &nbsp; **Step 3:** Balance the equation using stoichiometric coefficients. (The process of balancing will be examined in more detail in the following section.) <br>

A **balanced chemical equation** means that there are an equal number of atoms for each element on both sides of the equation.  

**Example:** *A sample of solid copper was placed into a solution of silver nitrate. The copper reacted with the silver nitrate to form aqueous copper(II) nitrate and metallic silver. Write a chemical equation to describe this reaction.*

#import ipywidgets as widgets
#from ipywidgets import Output, VBox 
#from IPython.display import clear_output, display, HTML

out1_1 = Output()
button_step1_1 = widgets.Button(description="Step One", layout=Layout(width='20%', height='100%'), button_style='primary')
count1_1 = 1

text1_11 = widgets.HTMLMath(value="<b>Step 1:</b> <i>Identify the reactants and products.</i>")
text1_12 = widgets.HTMLMath(value="In this example we are told that copper and silver nitrate were reacted to produce copper(II) nitrate and silver. Therefore, the reactants were <b>copper</b> and <b>silver nitrate</b>, and the products were <b>copper(II) nitrate</b> and <b>silver</b>.")
text1_13 = widgets.HTMLMath(value="<b>Reactants: copper (Cu), silver nitrate (AgNO<sub>3</sub>).")
text1_14 = widgets.HTMLMath(value="<b>Products: silver (Ag), copper(II) nitrate (Cu(NO<sub>3</sub>)<sub>2</sub>).")

def on_button_step1_1_clicked(b):
    global count1_1
    count1_1 += 1
    with out1_1:
        clear_output()
        if count1_1 % 2 == 0:
            display(text1_11, text1_12, text1_13, text1_14)
            
display(VBox([button_step1_1, out1_1]))
button_step1_1.on_click(on_button_step1_1_clicked)

#import ipywidgets as widgets
#from ipywidgets import Output, VBox 
#from IPython.display import clear_output, display, HTML

out1_2 = Output()
button_step1_2 = widgets.Button(description="Step Two", layout=Layout(width='20%', height='100%'), button_style='primary')
count1_2 = 1

text1_21 = widgets.HTMLMath(value="<b>Step 2:</b> <i>Organize the reactants and products into a chemical equation.</i>")
text1_22 = widgets.HTMLMath(value="Using the general form for a chemical equation, the reactants are placed on the left side of the arrow, while the products are placed on the right. Each chemical is separated by a plus sign: <b>copper + silver nitrate &rarr; silver + copper(II) nitrate</b>.")
text1_23 = widgets.HTMLMath(value="<b>Unbalanced chemical equation: Cu + AgNO<sub>3</sub> &rarr; Ag + Cu(NO<sub>3</sub>)<sub>2</sub></b>")

def on_button_step1_2_clicked(b):
    global count1_2
    count1_2 += 1
    with out1_2:
        clear_output()
        if count1_2 % 2 == 0:
            display(text1_21, text1_22, text1_23)
            
display(VBox([button_step1_2, out1_2]))
button_step1_2.on_click(on_button_step1_2_clicked)

#import ipywidgets as widgets
#from ipywidgets import Output, VBox 
#from IPython.display import clear_output, display, HTML

out1_3 = Output()
button_step1_3 = widgets.Button(description="Step Three", layout=Layout(width='20%', height='100%'), button_style='primary')
count1_3 = 1

text1_31 = widgets.HTMLMath(value="<b>Step 3:</b> <i>Balance the equation using stoichiometric coefficients.</i>")
text1_32 = widgets.HTMLMath(value="To balance the chemical equation, each side must contain an equal number of atoms for each element. This can be accomplished by placing a 2 in front of <b>AgNO<sub>3</sub></b> and <b>Ag</b>.")
text1_33 = widgets.HTMLMath(value="<b>Balanced chemical equation: Cu + 2AgNO<sub>3</sub> &rarr; 2Ag + Cu(NO<sub>3</sub>)<sub>2</sub></b>")

def on_button_step1_3_clicked(b):
    global count1_3
    count1_3 += 1
    with out1_3:
        clear_output()
        if count1_3 % 2 == 0:
            display(text1_31, text1_32, text1_33)
            
display(VBox([button_step1_3, out1_3]))
button_step1_3.on_click(on_button_step1_3_clicked)

**Practice:** *Select the unbalanced chemical equation that represents each of the following reactions.* 

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

display(widgets.HTMLMath(value="<b>Chemical reaction:</b> A sample of potassium sulfate was reacted with barium nitrate to form potassium nitrate and barium sulfate."))

option_1 = "K<sub>2</sub>SO<sub>4</sub> + Ba(NO<sub>3</sub>)<sub>2</sub> &rarr; KNO<sub>3</sub> + BaSO<sub>4</sub>" 
option_2 = "KNO<sub>3</sub> + BaSO<sub>4</sub> &rarr; K<sub>2</sub>SO<sub>4</sub> + Ba(NO<sub>3</sub>)<sub>2</sub>"
option_3 = "K<sub>2</sub>SO<sub>4</sub> &rarr; Ba(NO<sub>3</sub>)<sub>2</sub> + KNO<sub>3</sub> + BaSO<sub>4</sub>"
option_4 = "K<sub>2</sub>SO<sub>4</sub> + KNO<sub>3</sub> &rarr; Ba(NO<sub>3</sub>)<sub>2</sub> + BaSO<sub>4</sub>"

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

display(widgets.HTMLMath(value="<b>Chemical reaction:</b> Silver chloride and sodium nitrate were produced by combining sodium chloride (table salt) with silver nitrate."))

option_1 = "NaCl + AgNO<sub>3</sub> &rarr; AgCl + NaNO<sub>3</sub>" 
option_2 = "AgCl + NaNO<sub>3</sub> &rarr; NaCl + AgNO<sub>3</sub>"
option_3 = "AgCl + AgNO<sub>3</sub> &rarr; NaCl + NaNO<sub>3</sub>"
option_4 = "NaCl + NaNO<sub>3</sub> &rarr; AgCl + AgNO<sub>3</sub>"

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

display(widgets.HTMLMath(value="<b>Chemical reaction:</b> The combustion of octane resulted in the formation of carbon dioxide, carbon monoxide, and steam."))

option_1 = "C<sub>8</sub>H<sub>18</sub> + O<sub>2</sub> &rarr; CO<sub>2</sub> + CO + H<sub>2</sub>O" 
option_2 = "C<sub>8</sub>H<sub>18</sub> + O<sub>2</sub> &rarr; CO<sub>2</sub> + H<sub>2</sub>O"
option_3 = "C<sub>8</sub>H<sub>18</sub> + O<sub>2</sub> &rarr; CO<sub>2</sub> + CH<sub>4</sub> + H<sub>2</sub>O"
option_4 = "C<sub>8</sub>H<sub>18</sub> + O<sub>2</sub> &rarr; C<sub>8</sub>H<sub>18</sub> + CO<sub>2</sub> + CO + H<sub>2</sub>O"

multiple_choice_4(option_1, option_2, option_3, option_4)

## States of Matter

Chemical equations may provide additional information, such as the **state of matter** of the chemicals at the time of the reaction. The symbols for each state are: solid (s), liquid (l), gas (g), and aqueous (aq). Recall that an *aqueous* state means that the chemical is dissolved in water. These symbols are placed as a subscript at the end of each chemical in the equation. For example:

H<sub>2(g)</sub> + O<sub>2(g)</sub> &rarr; H<sub>2</sub>O<sub>(l)</sub>

**Example (revisited):** *A sample of solid copper was placed into a solution of silver nitrate. The copper reacted with the silver nitrate to form aqueous copper(II) nitrate and metallic silver. Select the unbalanced chemical equation that properly represents each state of the reactants and products.*

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "Cu<sub>(s)</sub> + 2AgNO<sub>3(aq)</sub> &rarr; 2Ag<sub>(s)</sub> + Cu(NO<sub>3</sub>)<sub>2(aq)</sub>" 
option_2 = "Cu<sub>(s)</sub> + 2AgNO<sub>3(l)</sub> &rarr; 2Ag<sub>(s)</sub> + Cu(NO<sub>3</sub>)<sub>2(l)</sub>"
option_3 = "Cu<sub>(s)</sub> + 2AgNO<sub>3(l)</sub> &rarr; 2Ag<sub>(s)</sub> + Cu(NO<sub>3</sub>)<sub>2(aq)</sub>"
option_4 = "Cu<sub>(s)</sub> + 2AgNO<sub>3(aq)</sub> &rarr; 2Ag<sub>(aq)</sub> + Cu(NO<sub>3</sub>)<sub>2(aq)</sub>"

multiple_choice_4(option_1, option_2, option_3, option_4)

## Conservation of Mass

The reactions represented by a chemical equation usually occur in a **closed system**: this means that the reactants and products cannot escape. A representation of a closed system is shown below:

<img src="images/conservation_of_mass.svg" width="75%"/>

In this figure, the box surrounding each side of the equation represents the system in which the reactants and products cannot escape. As a consequence, the total mass within the system, before and after the reaction, remains the same. This is a demonstration of the **law of conservation of mass**, which states that *for any closed system, the mass of the system remains constant over time*. In order for this to occur, the number of atoms of each element in the reactants must be equal to the number of atoms of those same elements in the products. This is the basis for balancing chemical equations. 

## Balancing Chemical Equations

A **balanced chemical equation** is one in which there are an equal number of atoms for each element on both sides of the equation. For example, suppose we wish to balance the following chemical equation:

<img src="images/balancing_example_1.0.svg" width="50%"/>

There are two Cl atoms on the reactant side, and three Cl atoms on the product side. The equation is unbalanced because there are more Cl atoms on the product side than on the reactant side. To balance the equation, we change the coefficients in front of the reactants and products until both sides have an equal number of atoms for each element. The goal when balancing an equation is to find an appropriate number for <span style='color:blue'>c<sub>1</sub></span>, <span style='color:blue'>c<sub>2</sub></span>, and <span style='color:blue'>c<sub>3</sub></span> that will make the equation: <span style='color:blue'>c<sub>1</sub></span>Fe + <span style='color:blue'>c<sub>2</sub></span>Cl<sub>2</sub> &rarr; <span style='color:blue'>c<sub>3</sub></span>FeCl<sub>3</sub> balanced. 

<img src="images/balancing_example_1.1.svg" width="50%"/>

In this example, there are two Cl atoms on the reactant side, and three Cl atoms on the product side. To add Cl atoms to the reactant side, we can only increase the number of Cl<sub>2</sub> molecules (we cannot change the composition of the molecules themselves). Therefore, we can only add Cl atoms in multiples of two to the reactant side.

1Cl<sub>2</sub> = 2 Cl atoms <br>
2Cl<sub>2</sub> = 4 Cl atoms <br>
3Cl<sub>2</sub> = 6 Cl atoms <br>

Likewise, to add Cl atoms to the product side, we can only increase the number of FeCl<sub>3</sub> molecules. Therefore, we can only add Cl atoms in multiples of three to the product side.

1FeCl<sub>3</sub> = 3 Cl atoms <br>
2FeCl<sub>3</sub> = 6 Cl atoms <br>
3FeCl<sub>3</sub> = 9 Cl atoms <br>

Notice from above that the lowest common multiple of two and three is six. Therefore, we will need to change the coefficient of Cl<sub>2</sub> to 3Cl<sub>2</sub>, and FeCl<sub>3</sub> to 2FeCl<sub>3</sub>. This results in six Cl atoms on both sides of the equation. After this change, there is one additional Fe atom on the product side. Therefore, the coefficient of Fe must be changed to 2Fe. This results in two Fe atoms on both sides of the equation. The chemical equation is now balanced. 

The guideline below is a common approach to balancing most common chemical equations:

&nbsp; &nbsp; &nbsp; &nbsp; **Step 1:** Balance the metallic elements. <br>
&nbsp; &nbsp; &nbsp; &nbsp; **Step 2:** Balance the non-metallic elements, *excluding* hydrogen and oxygen. <br>
&nbsp; &nbsp; &nbsp; &nbsp; **Step 3:** Balance the hydrogen. <br>
&nbsp; &nbsp; &nbsp; &nbsp; **Step 4:** Balance the oxygen. <br>
&nbsp; &nbsp; &nbsp; &nbsp; **Step 5:** Recheck to ensure each element is balanced. Reduce the coefficients if possible. <br>

Tip: If any *polyatomic ions* are present (e.g. SO<sub>4</sub>, NH<sub>4</sub>, NO<sub>3</sub>, CO<sub>3</sub>, OH, etc.), then they may be balanced as one unit. This only works if they occur on both sides of the equation.

**Example:** *Balance the following reaction:* <b>Al(OH)<sub>3</sub> + H<sub>2</sub>SO<sub>4</sub> &rarr; Al<sub>2</sub>(SO<sub>4</sub>)<sub>3</sub> + H<sub>2</sub>O</b>

#import ipywidgets as widgets
#from ipywidgets import Output, VBox 
#from IPython.display import clear_output, display, HTML

out2_1 = Output()
button_step2_1 = widgets.Button(description="Step One", layout=Layout(width='20%', height='100%'), button_style='primary')
count2_1 = 1

text2_11 = widgets.HTMLMath(value="<b>Step 1:</b> <i>Balance the metallic elements.</i>")
text2_12 = widgets.HTMLMath(value="There is one metallic element present: aluminium (Al). There is one Al atom on the reactant side, and two Al atoms on the product side. Therefore, a two must be placed in front of the molecule bearing the Al atom on the reactant side.")
text2_13 = widgets.HTMLMath(value="<span style='color:blue'>2Al</span>(OH)<sub>3</sub> + H<sub>2</sub>SO<sub>4</sub> &rarr; <span style='color:blue'>Al<sub>2</span></sub>(SO<sub>4</sub>)<sub>3</sub> + H<sub>2</sub>O")
text2_14 = widgets.HTMLMath(value="There are now two Al atoms on both the reactant and product sides. The Al is now balanced.")

def on_button_step2_1_clicked(b):
    global count2_1
    count2_1 += 1
    with out2_1:
        clear_output()
        if count2_1 % 2 == 0:
            display(text2_11, text2_12, text2_13, text2_14)
            
display(VBox([button_step2_1, out2_1]))
button_step2_1.on_click(on_button_step2_1_clicked)

#import ipywidgets as widgets
#from ipywidgets import Output, VBox 
#from IPython.display import clear_output, display, HTML

out2_2 = Output()
button_step2_2 = widgets.Button(description="Step Two", layout=Layout(width='20%', height='100%'), button_style='primary')
count2_2 = 1

text2_21 = widgets.HTMLMath(value="<b>Step 2:</b> <i>Balance the non-metallic elements, excluding hydrogen and oxygen.</i>")
text2_22 = widgets.HTMLMath(value="There is one non-metallic element present (excluding the hydrogen and oxygen): sulfur (S). There is one S atom on the reactant side, and three S atoms on the product side. Therefore, a three must be placed in front of the molecule bearing the sulfur on the reactant side.")
text2_23 = widgets.HTMLMath(value="2Al(OH)<sub>3</sub> + <span style='color:blue'>3</span>H<sub>2</sub><span style='color:blue'>S</span>O<sub>4</sub> &rarr; Al<sub>2</sub>(<span style='color:blue'>S</span>O<sub>4</sub>)<span style='color:blue'><sub>3</sub></span> + H<sub>2</sub>O")
text2_24 = widgets.HTMLMath(value="There are now three S atoms on both the reactant and product sides. The S is now balanced.")

def on_button_step2_2_clicked(b):
    global count2_2
    count2_2 += 1
    with out2_2:
        clear_output()
        if count2_2 % 2 == 0:
            display(text2_21, text2_22, text2_23, text2_24)
            
display(VBox([button_step2_2, out2_2]))
button_step2_2.on_click(on_button_step2_2_clicked)

#import ipywidgets as widgets
#from ipywidgets import Output, VBox 
#from IPython.display import clear_output, display, HTML

out2_3 = Output()
button_step2_3 = widgets.Button(description="Step Three", layout=Layout(width='20%', height='100%'), button_style='primary')
count2_3 = 1

text2_31 = widgets.HTMLMath(value="<b>Step 3:</b> <i>Balance the hydrogen.</i>")
text2_32 = widgets.HTMLMath(value="There are twelve H atoms on the reactant side, and two H atoms on the product side. Therefore, a six must be placed in front of the molecule bearing the hydrogen on the product side.")
text2_33 = widgets.HTMLMath(value="<span style='color:blue'>2</span>Al(O<span style='color:blue'>H</span>)<span style='color:blue'><sub>3</sub></span> + <span style='color:blue'>3H<sub>2</sub></span>SO<sub>4</sub> &rarr; Al<sub>2</sub>(SO<sub>4</sub>)<sub>3</sub> + <span style='color:blue'>6H<sub>2</sub></span>O")
text2_34 = widgets.HTMLMath(value="There are now twelve H atoms on both the reactant and product sides. The H is now balanced.")

def on_button_step2_3_clicked(b):
    global count2_3
    count2_3 += 1
    with out2_3:
        clear_output()
        if count2_3 % 2 == 0:
            display(text2_31, text2_32, text2_33, text2_34)
            
display(VBox([button_step2_3, out2_3]))
button_step2_3.on_click(on_button_step2_3_clicked)

#import ipywidgets as widgets
#from ipywidgets import Output, VBox 
#from IPython.display import clear_output, display, HTML

out2_4 = Output()
button_step2_4 = widgets.Button(description="Step Four", layout=Layout(width='20%', height='100%'), button_style='primary')
count2_4 = 1

text2_41 = widgets.HTMLMath(value="<b>Step 4:</b> <i>Balance the oxygen.</i>")
text2_42 = widgets.HTMLMath(value="There are eighteen O atoms on the reactant side, and eighteen O atoms on the product side. Therefore, the oxygen atoms are balanced.")
text2_43 = widgets.HTMLMath(value="<span style='color:blue'>2</span>Al(<span style='color:blue'>O</span>H)<span style='color:blue'><sub>3</sub></span> + <span style='color:blue'>3</span>H<sub>2</sub>S<span style='color:blue'>O<sub>4</sub></span> &rarr; Al<sub>2</sub>(S<span style='color:blue'>O<sub>4</sub></span>)<span style='color:blue'><sub>3</sub></span> + <span style='color:blue'>6</span>H<sub>2</sub><span style='color:blue'>O</span>")

def on_button_step2_4_clicked(b):
    global count2_4
    count2_4 += 1
    with out2_4:
        clear_output()
        if count2_4 % 2 == 0:
            display(text2_41, text2_42, text2_43)
            
display(VBox([button_step2_4, out2_4]))
button_step2_4.on_click(on_button_step2_4_clicked)

#import ipywidgets as widgets
#from ipywidgets import Output, VBox 
#from IPython.display import clear_output, display, HTML

out2_5 = Output()
button_step2_5 = widgets.Button(description="Step Five", layout=Layout(width='20%', height='100%'), button_style='primary')
count2_5 = 1

text2_51 = widgets.HTMLMath(value="<b>Step 5:</b> <i>Recheck to ensure each element is balanced. Reduce the coefficients if possible.</i>")
text2_52 = widgets.HTMLMath(value="There are two Al atoms, three S atoms, twelve H atoms and eighteen O atoms on each side of the equation. The equation is therefore balanced. The stoichiometric coefficients are 2, 3, 1, and 6. The greatest common divisor among these integers is 1. Therefore, the coefficients are already reduced to their lowest terms. If the coefficients were not in their lowest terms, then they could be reduced by factoring each coefficient into primes, and then cancelling all of the primes common to every term.")
text2_53 = widgets.HTMLMath(value="The final balanced chemical equation is: <span style='color:blue'>2Al(OH)<sub>3</sub> + 3H<sub>2</sub>SO<sub>4</sub> &rarr; Al<sub>2</sub>(SO<sub>4</sub>)<sub>3</sub> + 6H<sub>2</sub>O</span>")

def on_button_step2_5_clicked(b):
    global count2_5
    count2_5 += 1
    with out2_5:
        clear_output()
        if count2_5 % 2 == 0:
            display(text2_51, text2_52, text2_53)
            
display(VBox([button_step2_5, out2_5]))
button_step2_5.on_click(on_button_step2_5_clicked)

**Practice:** *Select the properly balanced equation for each reaction.* 

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

display(widgets.HTMLMath(value="<b>Chemical reaction:</b> Al + O<sub>2</sub> &rarr; Al<sub>2</sub>O<sub>3</sub>."))

option_1 = "4Al + 3O<sub>2</sub> &rarr; 2Al<sub>2</sub>O<sub>3</sub>" 
option_2 = "2Al + 3O<sub>2</sub> &rarr; 2Al<sub>2</sub>O<sub>3</sub>"
option_3 = "Al + 3O<sub>2</sub> &rarr; 2Al<sub>2</sub>O<sub>3</sub>"
option_4 = "2Al + O<sub>2</sub> &rarr; Al<sub>2</sub>O<sub>3</sub>"

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

display(widgets.HTMLMath(value="<b>Chemical reaction:</b> N<sub>2</sub> + H<sub>2</sub> &rarr; NH<sub>3</sub>."))

option_1 = "N<sub>2</sub> + 3H<sub>2</sub> &rarr; 2NH<sub>3</sub>" 
option_2 = "N<sub>2</sub> + 6H<sub>2</sub> &rarr; 2NH<sub>3</sub>"
option_3 = "N<sub>2</sub> + 3H<sub>2</sub> &rarr; NH<sub>3</sub>"
option_4 = "N<sub>2</sub> + H<sub>2</sub> &rarr; NH<sub>3</sub>"

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

display(widgets.HTMLMath(value="<b>Chemical reaction:</b> Al + Br<sub>2</sub> &rarr; AlBr<sub>3</sub>."))

option_1 = "2Al + 3Br<sub>2</sub> &rarr; 2AlBr<sub>3</sub>" 
option_2 = "Al + Br<sub>2</sub> &rarr; AlBr<sub>3</sub>"
option_3 = "Al + 3Br<sub>2</sub> &rarr; 2AlBr<sub>3</sub>"
option_4 = "Al + 3Br<sub>2</sub> &rarr; AlBr<sub>3</sub>"

multiple_choice_4(option_1, option_2, option_3, option_4)

**Practice:** *Assign the correct stoichiometric coefficients to each chemical to balance the chemical equation.* 

#import ipywidgets as widgets

#Create dropdown menus

equation2_1 = widgets.HTMLMath(value="N<sub>2</sub>H<sub>4</sub> + O<sub>2</sub> &rarr; H<sub>2</sub>O + N<sub>2</sub>")
chem2_1 = "N<sub>2</sub>H<sub>4</sub>"; chem2_2 = "O<sub>2</sub>"; chem2_3 = "H<sub>2</sub>O"; chem2_4 = "N<sub>2</sub>"
ans2_1 = "1"; ans2_2 = "1"; ans2_3 = "2"; ans2_4 = "1"

display(equation2_1)

dropdown2_1 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem2_1,)
dropdown2_2 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem2_2,)
dropdown2_3 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem2_3,)
dropdown2_4 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem2_4,)

#Display menus as 2x2 table
container2_1 = widgets.VBox(children=[dropdown2_1,dropdown2_2])
container2_2 = widgets.VBox(children=[dropdown2_3,dropdown2_4])
display(widgets.HBox(children=[container2_1, container2_2])), print(" ", end='\r')

#Evaluate input
def check_answer2_1(b):
    answer2_1 = dropdown2_1.label 
    answer2_2 = dropdown2_2.label
    answer2_3 = dropdown2_3.label 
    answer2_4 = dropdown2_4.label

    if answer2_1 == ans2_1 and answer2_2 == ans2_2 and answer2_3 == ans2_3 and answer2_4 == ans2_4:
        print("Correct! The balanced equation is: N\u2082H\u2084 + O\u2082 \u2192 2H\u2082O + N\u2082", end='\r')
    elif answer2_1 != ' ' and answer2_2 != ' ' and answer2_3 != ' ' and answer2_4 != ' ':
        print("Try again.                                                                            ", end='\r')
    else:
        print("                                                                                      ", end='\r')

dropdown2_1.observe(check_answer2_1, names='value')
dropdown2_2.observe(check_answer2_1, names='value')
dropdown2_3.observe(check_answer2_1, names='value')
dropdown2_4.observe(check_answer2_1, names='value')

#import ipywidgets as widgets

#Create dropdown menus

equation3_1 = widgets.HTMLMath(value="Na + H<sub>2</sub>O &rarr; NaOH + H<sub>2</sub>")
chem3_1 = "Na"; chem3_2 = "H<sub>2</sub>O"; chem3_3 = "NaOH"; chem3_4 = "H<sub>2</sub>"
ans3_1 = "2"; ans3_2 = "2"; ans3_3 = "2"; ans3_4 = "1"

display(equation3_1)

dropdown3_1 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem3_1,)
dropdown3_2 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem3_2,)
dropdown3_3 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem3_3,)
dropdown3_4 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem3_4,)

#Display menus as 2x2 table
container3_1 = widgets.VBox(children=[dropdown3_1,dropdown3_2])
container3_2 = widgets.VBox(children=[dropdown3_3,dropdown3_4])
display(widgets.HBox(children=[container3_1, container3_2])), print(" ", end='\r')

#Evaluate input
def check_answer3_1(b):
    answer3_1 = dropdown3_1.label 
    answer3_2 = dropdown3_2.label
    answer3_3 = dropdown3_3.label 
    answer3_4 = dropdown3_4.label

    if answer3_1 == ans3_1 and answer3_2 == ans3_2 and answer3_3 == ans3_3 and answer3_4 == ans3_4:
        print("Correct! The balanced equation is: 2Na + 2H\u2082O \u2192 2NaOH + H\u2082", end='\r')
    elif answer3_1 != ' ' and answer3_2 != ' ' and answer3_3 != ' ' and answer3_4 != ' ':
        print("Try again.                                                                            ", end='\r')
    else:
        print("                                                                                      ", end='\r')

dropdown3_1.observe(check_answer3_1, names='value')
dropdown3_2.observe(check_answer3_1, names='value')
dropdown3_3.observe(check_answer3_1, names='value')
dropdown3_4.observe(check_answer3_1, names='value')

#import ipywidgets as widgets

#Create dropdown menus

equation4_1 = widgets.HTMLMath(value="Ca + HNO<sub>3</sub> &rarr; H<sub>2</sub> + Ca(NO<sub>3</sub>)<sub>2</sub>")
chem4_1 = "Ca"; chem4_2 = "HNO<sub>3</sub>"; chem4_3 = "H<sub>2</sub>"; chem4_4 = "Ca(NO<sub>3</sub>)<sub>2</sub>"
ans4_1 = "1"; ans4_2 = "2"; ans4_3 = "1"; ans4_4 = "1"

display(equation4_1)

dropdown4_1 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem4_1,)
dropdown4_2 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem4_2,)
dropdown4_3 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem4_3,)
dropdown4_4 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem4_4,)

#Display menus as 2x2 table
container4_1 = widgets.VBox(children=[dropdown4_1,dropdown4_2])
container4_2 = widgets.VBox(children=[dropdown4_3,dropdown4_4])
display(widgets.HBox(children=[container4_1, container4_2])), print(" ", end='\r')

#Evaluate input
def check_answer4_1(b):
    answer4_1 = dropdown4_1.label 
    answer4_2 = dropdown4_2.label
    answer4_3 = dropdown4_3.label 
    answer4_4 = dropdown4_4.label

    if answer4_1 == ans4_1 and answer4_2 == ans4_2 and answer4_3 == ans4_3 and answer4_4 == ans4_4:
        print("Correct! The balanced equation is: Ca + 2HNO\u2083 \u2192 H\u2082 + Ca(NO\u2083)\u2082", end='\r')
    elif answer4_1 != ' ' and answer4_2 != ' ' and answer4_3 != ' ' and answer4_4 != ' ':
        print("Try again.                                                                            ", end='\r')
    else:
        print("                                                                                      ", end='\r')

dropdown4_1.observe(check_answer4_1, names='value')
dropdown4_2.observe(check_answer4_1, names='value')
dropdown4_3.observe(check_answer4_1, names='value')
dropdown4_4.observe(check_answer4_1, names='value')

#import ipywidgets as widgets

#Create dropdown menus

equation5_1 = widgets.HTMLMath(value="Fe(NO<sub>3</sub>)<sub>3</sub> + (NH<sub>4</sub>)<sub>2</sub>CO<sub>3</sub> &rarr; Fe<sub>2</sub>(CO<sub>3</sub>)<sub>3</sub> + NH<sub>4</sub>NO<sub>3</sub>")
chem5_1 = "Fe(NO<sub>3</sub>)<sub>3</sub>"; chem5_2 = "(NH<sub>4</sub>)<sub>2</sub>CO<sub>3</sub>"; chem5_3 = "Fe<sub>2</sub>(CO<sub>3</sub>)<sub>3</sub>"; chem5_4 = "NH<sub>4</sub>NO<sub>3</sub>"
ans5_1 = "2"; ans5_2 = "3"; ans5_3 = "1"; ans5_4 = "6"

display(equation5_1)

dropdown5_1 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem5_1,)
dropdown5_2 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem5_2,)
dropdown5_3 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem5_3,)
dropdown5_4 = widgets.Dropdown(options={' ':0,'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7}, value=0, description=chem5_4,)

#Display menus as 2x2 table
container5_1 = widgets.VBox(children=[dropdown5_1,dropdown5_2])
container5_2 = widgets.VBox(children=[dropdown5_3,dropdown5_4])
display(widgets.HBox(children=[container5_1, container5_2])), print(" ", end='\r')

#Evaluate input
def check_answer5_1(b):
    answer5_1 = dropdown5_1.label 
    answer5_2 = dropdown5_2.label
    answer5_3 = dropdown5_3.label 
    answer5_4 = dropdown5_4.label

    if answer5_1 == ans5_1 and answer5_2 == ans5_2 and answer5_3 == ans5_3 and answer5_4 == ans5_4:
        print("Correct! The balanced equation is: 2Fe(NO\u2083)\u2083 + 3(NH\u2084)\u2082CO\u2083 \u2192 Fe\u2082(CO\u2083)\u2083 + 6NH\u2084NO\u2083", end='\r')
    elif answer5_1 != ' ' and answer5_2 != ' ' and answer5_3 != ' ' and answer5_4 != ' ':
        print("Try again.                                                                            ", end='\r')
    else:
        print("                                                                                      ", end='\r')

dropdown5_1.observe(check_answer5_1, names='value')
dropdown5_2.observe(check_answer5_1, names='value')
dropdown5_3.observe(check_answer5_1, names='value')
dropdown5_4.observe(check_answer5_1, names='value')

## Conclusion

* A **chemical equation** is a symbolic representation of a chemical reaction.

* The reactions represented by a chemical equation usually occur in a **closed system**: this means that the reactants and products cannot escape.

* This is a demonstration of the **law of conservation of mass**, which states that *for any closed system, the mass of the system remains constant over time*.

* A **balanced chemical equation** means that there are an equal number of atoms for each element on both sides of the equation.

* The following steps are a common approach to balancing most chemical equations: <br>
&nbsp; &nbsp; &nbsp; &nbsp; **Step 1:** Balance the metallic elements. <br>
&nbsp; &nbsp; &nbsp; &nbsp; **Step 2:** Balance the non-metallic elements, *excluding* hydrogen and oxygen. <br>
&nbsp; &nbsp; &nbsp; &nbsp; **Step 3:** Balance the hydrogen. <br>
&nbsp; &nbsp; &nbsp; &nbsp; **Step 4:** Balance the oxygen. <br>
&nbsp; &nbsp; &nbsp; &nbsp; **Step 5:** Recheck to ensure each element is balanced. Reduce the coefficients if possible. <br>

* If any *polyatomic ions* are present, they may be balanced as one unit. This only works if they occur on both sides of the equation.

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