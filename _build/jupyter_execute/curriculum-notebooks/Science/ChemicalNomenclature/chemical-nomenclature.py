![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/ChemicalNomenclature/chemical-nomenclature.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

(Click **Cell** > **Run All** before proceeding.) 

<a id='Top'></a>

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

# Chemical Nomenclature

This notebook will outline and explain the following concepts:

- [Section 1](#Section_1): Review (Periodic Table, ions, and atomic structure)
- [Section 2](#Section_2): How Elements Form Compounds (ionic bonds versus covalent bonds)
- [Section 3](#Section_3): Naming Binary Ionic Compounds
- [Section 4](#Section_4): Naming Ionic Compounds with Polyatomic Ions
- [Section 5](#Section_5): Writing Formulas for Ionic Compounds
- [Section 6](#Section_6): Writing Formulas for Molecular Compounds
- [Section 7](#Section_7): Naming Molecular Compounds

<a id='Section_1'></a>

## Section 1: Review

[Back to Top](#Top)

Make reference to the following periodic table throughout this notebook:

<img src="Images/PeriodicTableFinal.svg" width="100%">


Note: The content covered in the following multiple choice is review material (concepts that you should already be familiar with).

**Question 1:** The elements on the Periodic Table are

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "In electronically neutral form." 
option_2 = "All metals or metal alloys."
option_3 = "All charged with either a positive or negative charge."
option_4 = "Unorganized and cannot be grouped together in any way."

multiple_choice(option_1, option_2, option_3, option_4)

**Question 2:** The subatomic particle that is involved in the bonding of atoms is called the

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Electron" 
option_2 = "Proton"
option_3 = "Neutron"
option_4 = "Nucleus"

multiple_choice(option_1, option_2, option_3, option_4)

**Question 3:** What is the name of the atomic model below?

<img src="Images/Bohr.svg" width="25%"/>

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Bohr Model" 
option_2 = "Quantum Mechanical Model"
option_3 = "Plum Pudding Model"
option_4 = "Solar System Model"

multiple_choice(option_1, option_2, option_3, option_4)

**Question 4:** What is the symbol and charge for each subatomic particle?

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Protons (p{}), electrons (e{}), neutrons (n{}).".format(chr(0x207A), chr(0x207B), chr(0x2070)) 
option_2 = "Protons (p{}), electrons (e{}), neutrons (n{}).".format(chr(0x207B), chr(0x207A), chr(0x2070))
option_3 = "Protons (p{}), electrons (e{}), neutrons (n{}).".format(chr(0x207A), chr(0x2070), chr(0x207B))
option_4 = "None of the options are correct."

multiple_choice(option_1, option_2, option_3, option_4)

**Question 5:** A *cation* is a _______ charged ion. An *anion* is a _______ charged ion.

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "positively; negatively" 
option_2 = "negatively; positively"
option_3 = "neutral; negatively"
option_4 = "positively; neutral"

multiple_choice(option_1, option_2, option_3, option_4)

<a id='Section_2'></a>

## Section 2: How Elements Form Compounds

[Back to Top](#Top)

Much of chemical activity involves the transfer or sharing of electrons. 

**Ionic compounds** are combinations of *cations* and *anions*, which are generally (but not always) metals and non-metals. Their compounds are held together by electrostatic attractions between oppositely charged ions (similar to a magnetic attraction). This is called an **ionic bond**.

**Covalent (or molecular) compounds** are generally composed of non-metals only. Electrons are shared between atoms. This is called a **covalent bond**.

<img src="Images/Bonding.svg" width="55%"/>

## Section 3: Naming Binary Ionic Compounds

[Back to Top](#Top)

Steps for naming **binary** ionic compounds:

1. Name the cation (often a metal) first.
2. Name the anion (often a non-metal) second. For the anion, **drop the ending and add "ide"**.
3. Use Roman numerals in parentheses to indicate which charge of cation is used. This is **only** used for metals that make more than one charge. Below is a table of the Roman numerals from 1 to 10:

Number | Roman Numeral
 ---  | ---
 1 | I
 2 | II
 3 | III
 4 | IV
 5 | V
 6 | VI
 7 | VII
 8 | VIII
 9 | IX
 10 | X

### Examples

Name the following ionic compounds:
1. Ca$_3$N$_2$
2. Mg$_3$P$_2$
3. Al$_2$O$_3$
4. CuCl$_2$
5. FeBr$_3$
6. CoN

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out1 = Output()
button1_step1 = widgets.Button(description="Answers 1-3", layout=Layout(width='20%', height='100%'), button_style='primary')
count1 = 1

text1_1 = widgets.HTMLMath(value=r"1. Calcium nitride")
text1_2 = widgets.HTMLMath(value=r"2. Magnesium phosphide")
text1_3 = widgets.HTMLMath(value=r"3. Aluminum oxide")

def on_button1_step1_clicked(b):
    global count1
    count1 += 1
    with out1:
        clear_output()
        if count1 % 2 == 0:
            display(text1_1, text1_2, text1_3)
            
display(VBox([button1_step1, out1]))
button1_step1.on_click(on_button1_step1_clicked)

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out2 = Output()
button1_step2 = widgets.Button(description="Answers 4-6", layout=Layout(width='20%', height='100%'), button_style='primary')
count2 = 1

text1_4 = widgets.HTMLMath(value=r"4. Reference the periodic table. Notice how copper makes more than one charge (+2 or +1). Recall how compounds are electronically neutral. Since chlorine always makes a -1 charge (and there are two chlorine atoms), this implies that copper must be taking a +2 charge in this situation.")
text1_4_2 = widgets.HTMLMath(value=r" Answer: Copper (II) chloride")
text1_5 = widgets.HTMLMath(value=r"5. Iron (III) bromide (similar to #4)")
text1_6 = widgets.HTMLMath(value=r"6. N takes a -3 charge and we have one nitrogen and one cobalt atom. Cobalt must be taking a +3 charge to make the compound neutral.")
text1_6_2 = widgets.HTMLMath(value=r"Answer: Cobalt (III) nitride")
def on_button1_step2_clicked(b):
    global count2
    count2 += 1
    with out2:
        clear_output()
        if count2 % 2 == 0:
            display(text1_4, text1_4_2, text1_5, text1_6, text1_6_2)
            
display(VBox([button1_step2, out2]))
button1_step2.on_click(on_button1_step2_clicked)

### Practice (Multiple Choice)

Choose the option with the correct name for the following ionic compounds.

**Question 1:** CaCl$_2$

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Calcium chloride" 
option_2 = "Calcium chlorine"
option_3 = "Chlorine Calcium"
option_4 = "Calcium (II) chloride"

multiple_choice(option_1, option_2, option_3, option_4)

**Question 2:** MgBr$_2$

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Magnesium bromide" 
option_2 = "Magnesium bromine"
option_3 = "Magnesium (II) bromide"
option_4 = "Magnesium (II) bromine"

multiple_choice(option_1, option_2, option_3, option_4)

**Question 3:** FeI$_3$

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Iron (III) iodide" 
option_2 = "Iron iodine"
option_3 = "Iron iodide"
option_4 = "Iron (III) iodinide"

multiple_choice(option_1, option_2, option_3, option_4)

**Question 4:** CuCl

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Copper (I) chloride" 
option_2 = "Copper chloride"
option_3 = "Copper chlorine"
option_4 = "Calcium (I) chlorine"

multiple_choice(option_1, option_2, option_3, option_4)

**Question 5:** Cr$_3$N$_2$

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Chromium (II) nitride" 
option_2 = "Chromium (VI) nitride"
option_3 = "Chromium (III) nitride"
option_4 = "Chromium nitride"

multiple_choice(option_1, option_2, option_3, option_4)

### Practice (Fill-in-the-blank)

Write the names for the following ionic compounds. Spelling, capitalization, and spacing matters! (Match the format of the examples above). Note that the first letter of each name is capitalized and roman numerals are capitalized.

blank1 = widgets.Text(
    value='',
    placeholder='Type name here & press ENTER',
    description="LiCl",
    disabled=False
)


display(blank1)

           
def callback1(wdgt):
    if (wdgt.value == "Lithium chloride") or (wdgt.value == "lithium chloride"):
        print("Correct! 👏                                                                                      ", end='\r')
        blank1.on_submit(callback1)
    else:
        print("Hint: Name the metal 1st and the non-metal 2nd. Remember to change the non-metal's ending to 'ide'!", end='\r')
        blank1.on_submit(callback1)

blank1.on_submit(callback1)



blank2 = widgets.Text(
    value='',
    placeholder='Type name here & press ENTER',
    description="Sr{}P{}".format(chr(0x2083), chr(0x2082)),
    disabled=False
)


display(blank2)

           
def callback2(wdgt):
    if (wdgt.value == "Strontium phosphide") or (wdgt.value == "strontium phosphide"):
        print("Correct! 👏                                                                                      ", end='\r')
        blank2.on_submit(callback2)
    else:
        print("Hint: Name the metal 1st and the non-metal 2nd. Remember to change the non-metal's ending to 'ide'!", end='\r')
        blank2.on_submit(callback2)

blank2.on_submit(callback2)



blank3 = widgets.Text(
    value='',
    placeholder='Type name here & press ENTER',
    description="Ag{}S".format(chr(0x2082)),
    disabled=False
)


display(blank3)

           
def callback3(wdgt):
    if (wdgt.value == "Silver sulfide") or (wdgt.value == "silver sulfide"):
        print("Correct! 👏                                                                                      ", end='\r')
        blank3.on_submit(callback3)
    else:
        print("Hint: Name the metal 1st and the non-metal 2nd. Remember to change the non-metal's ending to 'ide'!", end='\r')
        blank3.on_submit(callback3)

blank3.on_submit(callback3)



blank4 = widgets.Text(
    value='',
    placeholder='Type name here & press ENTER',
    description="SnI{}".format(chr(0x2084)),
    disabled=False
)


display(blank4)

           
def callback4(wdgt):
    if (wdgt.value == "Tin (IV) iodide") or (wdgt.value == "tin (iv) iodide"):
        print("Correct! 👏                                                         ", end='\r')
        blank4.on_submit(callback4)
    else:
        print("Hint: Remember to reference if the metal makes more than one charge!", end='\r')
        blank4.on_submit(callback4)

blank4.on_submit(callback4)


blank5 = widgets.Text(
    value='',
    placeholder='Type name here & press ENTER',
    description="PdS{}".format(chr(0x2082)),
    disabled=False
)


display(blank5)

           
def callback5(wdgt):
    if (wdgt.value == "Palladium (IV) sulfide") or (wdgt.value == "palladium (iv) sulfide"):
        print("Correct! 👏                                                         ", end='\r')
        blank5.on_submit(callback5)
    else:
        print("Hint: Remember to reference if the metal makes more than one charge!", end='\r')
        blank5.on_submit(callback5)

blank5.on_submit(callback5)


<a id='Section_3'></a>

## Section 4: Naming Ionic Compounds with Polyatomic Ions

[Back to Top](#Top)

**Polyatomic ions** are groups of atoms that tend to stay together and carry an overall ionic charge. Reference the following table of polyatomic ions throughout the rest of this notebook:

 Name | Formula
 ---  | ---
 Ammonium | NH$_4$   $^{+1}$
 Bicarbonate | HCO$_3$   $^{-1}$
 Carbonate | CO$_3$    $^{-2}$
 Carbonite | CO$_2$   $^{-2}$
 Chlorate | ClO$_3$   $^{-1}$
 Chlorite | ClO$_2$   $^{-1}$
 Chromate | CrO$_4$   $^{-2}$
 Cyanide | CN   $^{-1}$
 Hydroxide | OH $^{-1}$
 Iodate | IO$_3$   $^{-1}$
 Iodite | IO$_2$   $^{-1}$
 Nitrate | NO$_3$   $^{-1}$
 Nitrite | NO$_2$   $^{-1}$
 Phosphate | PO$_4$   $^{-3}$
 Phosphite | PO$_3$   $^{-3}$
 Sulfate | SO$_4$   $^{-2}$
 Sulfite | SO$_3$   $^{-2}$
 

**Section 2:** Steps for naming ionic compounds with *polyatomic ions*.

1. For polyatomic compounds, name the cation (metal) first followed by the name of the polyatomic ion. The endings **do not** change. 
2. Like before, use Roman numerals in parentheses to indicate which charge of cation is used. This is **only** used for metals that make more than one charge.

### Examples

Name the following ionic compounds:

1. Al(OH)$_3$
2. NaHCO$_3$
3. Sn(NO$_3$)$_4$

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out3 = Output()
button2_step1 = widgets.Button(description="Answers", layout=Layout(width='20%', height='100%'), button_style='primary')
count3 = 1

text2_1 = widgets.HTMLMath(value=r"1. Answer: Aluminum hydroxide. OH is a compound called 'hydroxide' (see the table of polyatomic ions above). Also, aluminum makes only one charge.")
text2_2 = widgets.HTMLMath(value=r"2. Answer: Sodium bicarbonate. NaHCO$_3$ is a compound called 'bicarbonate'. Also, sodium makes only one charge.")
text2_3 = widgets.HTMLMath(value=r"3. Answer: Tin (IV) nitrite. Sn(NO$_3$)$_4$ is a compound called 'nitrite'. Notice that Sn (tin) takes two charges (+2 or +4); therefore, we need to use Roman numerals. Nitrite takes a -1 charge, so tin is taking a +4 charge in this situation.")

def on_button2_step1_clicked(b):
    global count3
    count3 += 1
    with out3:
        clear_output()
        if count3 % 2 == 0:
            display(text2_1, text2_2, text2_3)
            
display(VBox([button2_step1, out3]))
button2_step1.on_click(on_button2_step1_clicked)

### Practice (Multiple Choice)

Choose the option with the correct name for the following ionic compounds involving polyatomic ions.

**Question 1:** KNO$_3$

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Potassium nitrate" 
option_2 = "Potassium nitride"
option_3 = "Potassium (II) nitrate"
option_4 = "Potassium (II) nitride"

multiple_choice(option_1, option_2, option_3, option_4)

**Question 2:** Mg$_3$(PO$_4$)$_2$

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Magnesium phosphate" 
option_2 = "Magnesium (II) phosphate"
option_3 = "Magnesium phosphide"
option_4 = "Magnesium (II) phosphide"

multiple_choice(option_1, option_2, option_3, option_4)

### Practice (Fill-in-the-blank)

Write the names for the following ionic compounds involving polyatomic ions. As before, spelling, capitalization, and spacing matters! Note that the first letter of each name is capitalized and Roman numerals are capitalized.

blank6 = widgets.Text(
    value='',
    placeholder='Type name here & press ENTER',
    description="NaOH",
    disabled=False
)


display(blank6)

           
def callback6(wdgt):
    if (wdgt.value == "Sodium hydroxide") or (wdgt.value == "sodium hydroxide"):
        print("Correct! 👏                                                    ", end='\r')
        blank6.on_submit(callback6)
    else:
        print("Hint: Remember to reference the table of polyatomic ions above!", end='\r')
        blank6.on_submit(callback6)

blank6.on_submit(callback6)


blank7 = widgets.Text(
    value='',
    placeholder='Type name here & press ENTER',
    description="Pb(NO{}){}".format(chr(0x2082), chr(0x2084)),
    disabled=False
)


display(blank7)

           
def callback7(wdgt):
    if (wdgt.value == "Lead (IV) nitrite") or (wdgt.value == "lead (iv) nitrite"):
        print("Correct! 👏                                                    ", end='\r')
        blank7.on_submit(callback7)
    else:
        print("Hint: Remember to reference the table of polyatomic ions above!", end='\r')
        blank7.on_submit(callback7)

blank7.on_submit(callback7)


<a id='Section_5'></a>

## Section 5: Writing Formulas for Ionic Compounds

[Back to Top](#Top)

We now consider how to convert a compound name to a formula. Since each ionic compound is electronically neutral, we have the following steps:

1. Note the **ionic** charges and the **symbols** for both the cation and anion.
2. Determine the lowest number of each element that would make the entire compound **electronically neutral**.

**Note:** 
- Some metals can make more than one kind of ion. Roman numerals in brackets indicate the **charge** of the ion.
- If you require more than one polyatomic ion, remember to put the *entire* polyatomic ion in brackets along with a subscript indicating the number required.

### Examples

Write the formulas for the following ionic compounds:

1. Calcium iodide
2. Sodium phosphide
3. Iron (III) oxide
4. Iron (II) oxide
5. Sodium carbonite
6. Aluminum sulfate

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out4 = Output()
button3_step1 = widgets.Button(description="Answers", layout=Layout(width='20%', height='100%'), button_style='primary')
count4 = 1

text3_1 = widgets.HTMLMath(value=r"1. Answer: CaI$_2$. The charges involved are Ca$^{+2}$ and I$^{-1}$. We need exactly 2 iodine atoms to cancel calcium's +2 charge.")
text3_2 = widgets.HTMLMath(value=r"2. Answer: Na$_3$P. We have Na$^+$ and P$^{-3}$, so we need 3 sodium atoms to cancel phosphorus' -3 charge.")
text3_3 = widgets.HTMLMath(value=r"3. Answer: Fe$_2$O$_3$. The Roman numeral III tells us that we have Fe$^{+3}$. Since oxygen takes a -2 charge, we need exactly 2 Fe atoms and 3 O atoms to arrive at an electronically neutral compound.")
text3_4 = widgets.HTMLMath(value=r"4. Answer: FeO. We have Fe$^{+2}$ and O$^{-2}$, so we need exactly 1 Fe atom and 1 O atom to arrive at an electronically neutral compound.")
text3_5 = widgets.HTMLMath(value=r"5. Answer: Na$_2$CO$_2$. We have Na$^+$ and CO$_2^{-2}$, so we need 2 Na atoms and 1 CO$_2$ molecule.")
text3_6 = widgets.HTMLMath(value=r"6. Al$^{+3}$ and SO$_4^{-2}$ $\implies$ Al$_2$(SO$_4$)$_3$.")

def on_button3_step1_clicked(b):
    global count4
    count4 += 1
    with out4:
        clear_output()
        if count4 % 2 == 0:
            display(text3_1, text3_2, text3_3, text3_4, text3_5, text3_6)
            
display(VBox([button3_step1, out4]))
button3_step1.on_click(on_button3_step1_clicked)

### Practice (Multiple Choice)

Choose the option with the correct formula for the following ionic compounds.

**Question 1:** Sodium bromide

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "NaBr" 
option_2 = "BrNa"
option_3 = "SBr{}".format(chr(0x2082))
option_4 = "SBr"

multiple_choice(option_1, option_2, option_3, option_4)

**Question 2:** Zinc iodide

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "ZnI{}".format(chr(0x2082)) 
option_2 = "ZnI"
option_3 = "Zn{}I{}".format(chr(0x2082), chr(0x2082))
option_4 = "ZnIO{}".format(chr(0x2083))

multiple_choice(option_1, option_2, option_3, option_4)

**Question 3:** Cobalt (II) chloride

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "CoCl{}".format(chr(0x2082))
option_2 = "CoClO{}".format(chr(0x2083))
option_3 = "CoCl"
option_4 = "Co{}Cl".format(chr(0x2082))

multiple_choice(option_1, option_2, option_3, option_4)

**Question 4:** Lead (IV) selenide

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "PbSe{}".format(chr(0x2082))
option_2 = "Pb{}Se{}".format(chr(0x2082), chr(0x2084))
option_3 = "PbSe"
option_4 = "PbSe".format(chr(0x2084))

multiple_choice(option_1, option_2, option_3, option_4)

**Question 5:** Silver nitrate

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "AgNO{}".format(chr(0x2083))
option_2 = "Ag(NO){}".format(chr(0x2083))
option_3 = "Ag{}N".format(chr(0x2083))
option_4 = "AgNO{}".format(chr(0x2082))

multiple_choice(option_1, option_2, option_3, option_4)

**Question 6:** Iron (II) phosphate

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "Fe{}(PO{}){}".format(chr(0x2083), chr(0x2084), chr(0x2082))
option_2 = "FePO{}".format(chr(0x2084))
option_3 = "Fe{}PO{}".format(chr(0x2083), chr(0x2084))
option_4 = "Fe{}(PO{}){}".format(chr(0x2082), chr(0x2084), chr(0x2083))

multiple_choice(option_1, option_2, option_3, option_4)

<a id='Section_6'></a>

## Section 6: Writing Formulas for Molecular Compounds

[Back to Top](#Top)

Recall that a binary molecular compound is composed of two non-metals and that they are share electrons via covalent bonds (ex. CO$_2$). There are two main steps to writing formulas for molecular compounds:

1. Write the symbols of each non-metal.
2. Write the appropriate subscripts for each non-metal that correspond to the prefixes used.

Note: The prefix *mono* is **never** used on the first non-metal.

Here is a list of prefixes used for molecular compounds:

 Number | Prefix
 ---  | ---
 1 | mono
 2 | di
 3 | tri
 4 | tetra
 5 | penta
 6 | hexa
 7 | hepta
 8 | octa
 9 | nona
 10 | deca

### Examples

Write the formulas for the following molecular compounds.

1. Carbon dioxide
2. Dinitrogen trioxide
3. Carbon tetrafluoride

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out5 = Output()
button4_step1 = widgets.Button(description="Answers", layout=Layout(width='20%', height='100%'), button_style='primary')
count5 = 1

text4_1 = widgets.HTMLMath(value=r"1. Answer: CO$_2$. No prefix in front of carbon implies that there is one carbon. The prefix 'di' implies that there are two oxygen atoms.")
text4_2 = widgets.HTMLMath(value=r"2. Answer: N$_2$O$_3$")
text4_3 = widgets.HTMLMath(value=r"3. Answer: CF$_4$")

def on_button4_step1_clicked(b):
    global count5
    count5 += 1
    with out5:
        clear_output()
        if count5 % 2 == 0:
            display(text4_1, text4_2, text4_3)
            
display(VBox([button4_step1, out5]))
button4_step1.on_click(on_button4_step1_clicked)

### Practice (Multiple Choice)

Choose the option with the correct formula for the following molecular compounds.

**Question 1:** Sulfur trioxide

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "SO{}".format(chr(0x2083))
option_2 = "S{}O".format(chr(0x2083))
option_3 = "S{}O{}".format(chr(0x2083), chr(0x2083))
option_4 = "Not possible"

multiple_choice(option_1, option_2, option_3, option_4)

**Question 2:** Diboron trioxide

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "B{}O{}".format(chr(0x2082), chr(0x2083))
option_2 = "B{}O{}".format(chr(0x2083), chr(0x2082))
option_3 = "2B3O"
option_4 = "3B2O"

multiple_choice(option_1, option_2, option_3, option_4)

**Question 3:** Phosphorus trihydride

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "PH{}".format(chr(0x2083))
option_2 = "P{}H".format(chr(0x2083))
option_3 = "P(OH){}".format(chr(0x2083))
option_4 = "P{}(OH)".format(chr(0x2083))

multiple_choice(option_1, option_2, option_3, option_4)

<a id='Section_7'></a>

## Section 7: Naming Molecular Compounds

[Back to Top](#Top)

Steps:

1. Write the name of the first non-metal and then the second.
2. Place the appropriate **prefixes** in front of each of the names. The prefixes correspond to the subscripts of each element.
3. Drop the ending of the last element named and add **ide**.

Note: Sometimes the prefixes are shortened when the ending vowel of the prefix "conflicts" with a starting vowel in the compound. This makes the name easier to pronounce. For example, "tetraoxide" is written as "tetroxide" and "monooxide" is shortened to "monoxide".

Recall the following list of prefixes:

 Number | Prefix
 ---  | ---
 1 | mono
 2 | di
 3 | tri
 4 | tetra
 5 | penta
 6 | hexa
 7 | hepta
 8 | octa
 9 | nona
 10 | deca

### Examples

Name the following molecular compounds.

1. CS$_2$
2. N$_2$O$_4$
3. P$_4$S$_{10}$

#----------

#import ipywidgets as widgets
#from ipywidgets import Output, VBox, Layout
#from IPython.display import clear_output, display, HTML

#----------

out6 = Output()
button5_step1 = widgets.Button(description="Answers", layout=Layout(width='20%', height='100%'), button_style='primary')
count6 = 1

text5_1 = widgets.HTMLMath(value=r"1. Answer: Carbon disulfide. The prefix 'mono' is never used for the first element.")
text5_2 = widgets.HTMLMath(value=r"2. Answer: Dinitrogen tetroxide. Recall that 'tetraoxide' is shortened to 'tetroxide'. This avoids two vowels being next to each other.")
text5_3 = widgets.HTMLMath(value=r"3. Answer: Tetraphosphorus decasulfide")

def on_button5_step1_clicked(b):
    global count6
    count6 += 1
    with out6:
        clear_output()
        if count6 % 2 == 0:
            display(text5_1, text5_2, text5_3)
            
display(VBox([button5_step1, out6]))
button5_step1.on_click(on_button5_step1_clicked)

### Practice (Fill-in-the-blank)

Write the names for the following molecular compounds. Remember that spelling and spacing matters.

blank8 = widgets.Text(
    value='',
    placeholder='Type name here & press ENTER',
    description="CO",
    disabled=False
)


display(blank8)

           
def callback8(wdgt):
    if (wdgt.value == "Carbon monoxide") or (wdgt.value == "carbon monoxide"):
        print("Correct! 👏                                    ", end='\r')
        blank8.on_submit(callback8)
    else:
        print("Hint: Remember to drop the vowel in the prefix!", end='\r')
        blank8.on_submit(callback8)

blank8.on_submit(callback8)


blank9 = widgets.Text(
    value='',
    placeholder='Type name here & press ENTER',
    description="CF{}".format(chr(0x2084)),
    disabled=False
)


display(blank9)

           
def callback9(wdgt):
    if (wdgt.value == "Carbon tetrafluoride") or (wdgt.value == "carbon tetrafluoride"):
        print("Correct! 👏                                                                  ", end='\r')
        blank9.on_submit(callback9)
    else:
        print("Hint: Remember that the prefix 'mono' is never used for the first element!", end='\r')
        blank9.on_submit(callback9)

blank9.on_submit(callback9)


blank10 = widgets.Text(
    value='',
    placeholder='Type name here & press ENTER',
    description="N{}O{}".format(chr(0x2082), chr(0x2085)),
    disabled=False
)


display(blank10)

           
def callback10(wdgt):
    if (wdgt.value == "Dinitrogen pentoxide") or (wdgt.value == "dinitrogen pentoxide"):
        print("Correct! 👏                                    ", end='\r')
        blank10.on_submit(callback10)
    else:
        print("Hint: Remember to drop the vowel in the prefix!", end='\r')
        blank10.on_submit(callback10)

blank10.on_submit(callback10)


## Summary

 - There are generally two types of compounds: ionic and covalent.
 - Ionic compounds are composed of a cation (usually a metal) and an anion (usually a non-metal).
 - Covalent compounds are usually composed of non-metals only.
 - There are two separate naming systems for both ionic and covalent compounds.
 - It is critical to become fluent in both naming systems in order to achieve success and understanding in chemistry.

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