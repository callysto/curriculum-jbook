![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/StaticAndKineticFriction/StaticAndKineticFriction.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

(Click **Cell** > **Run All** before proceeding.)

%matplotlib inline

#----------
#Import modules and packages 
import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import random

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

# Static and Kinetic Friction

## Introduction

**Friction** is the name given to the force that resists the relative motion of one object as it slides against another. Most surfaces are rough and uneven. Even smooth surfaces, such as a polished mirror, can appear bumpy under a microscope. The bumps on these surfaces interlock as they rub against one another, which prevents them from sliding freely.

<img src="Images/rough_surfaces.svg" width="35%"/>

The more an object presses into a surface, the more the surface pushes back against the object. The force pushing back against the object is called the **normal force**, **$F_{n}$** and it is always perpendicular to the surface. From the image above, we can imagine that the more two objects are pressed together, the more difficult it is for the interlocking points to lift up and slide passed one another. As a consequence, the friction force increases. A relationship therefore exists between the magnitude of the friction force and that of the normal force. This relationship is expressed by the following equation: 

$$F_{f}=\mu F_{n}$$

where $F_{f}$ and $F_{n}$ are the magnitudes of the friction and normal forces respectively, and $\mu$ is the **coefficient of friction**. Here $\mu$ is the Greek letter $mu$.  The direction of the force of friction is parallel to the surface and opposite to the other forces acting on the object.

Use the slider below to observe the relationship between the normal force and the friction force. Pick any value for the coefficient of friction. Move the slider for the normal force back and forth to calculate the corresponding force of friction. 

#import ipywidgets as widgets

coeff = widgets.FloatSlider(description="Coefficient",min=0.1,max=0.9)
normal_force = widgets.IntSlider(description="Normal force",min=5,max=50)

#Boldface letters at the beginning of each option
start_bold = "\033[1m"; end_bold = "\033[0;0m"

def f(coeff, normal_force):
    friction_force = coeff * normal_force
    print(start_bold + "Friction force = (coefficient of friction) X (normal force)" + end_bold)
    print("Friction force = {} X {} = {} N".format(coeff, normal_force, round(friction_force,1)))

out = widgets.interactive_output(f,{'coeff': coeff, 'normal_force': normal_force})

widgets.HBox([widgets.VBox([coeff, normal_force]), out])

**Question:** *What happens to the friction force when the normal force increases?* 

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "The friction force increases." 
option_2 = "The friction force decreases."
option_3 = "The friction force remains constant."
option_4 = "The friction force equals zero."

multiple_choice(option_1, option_2, option_3, option_4)

The force of friction felt by an object depends on whether the objects are in motion with respect to each other.  In general the force of friction felt by an object which is not moving with respect to another is stronger than the force of friction felt once it begins moving.

**Static friction** describes the friction force that acts between an object and a surface to prevent it from sliding when a force is applied to it. Static friction applies to objects that are stationary with respect to one another.  

**Kinetic friction** describes the friction force that acts between an object and the surface it slides upon when a force is applied to it. Kinetic friction applies to objects that are in motion with respect to one another.

### Coefficients of Friction

Values for the coefficients of friction have been derived experimentally for various materials as they interact with one another. When we describe the friction acting on a stationary object, we must use the **coefficient of static friction, $\mu_{s}$**. When we describe the friction of a sliding object, we must use the **coefficient of kinetic friction, $\mu_{k}$**. Some values for the coefficients of static and kinetic friction are shown in the table below:  

 Materials          | Coefficients of static friction ($\mu_{s}$)| Coefficients of kinetic friction ($\mu_{k}$) 
 ---                | ---                                       | ---
 Steel on steel     | 0.7                                       | 0.6 
 Glass on glass     | 0.9                                       | 0.4
 Wood on wood       | 0.4                                       | 0.2 
 Rubber on concrete | 1.0                                       | 0.8

Use the slider again to observe the relationship between the coefficient of friction and the friction force. Pick any value for the normal force. Move the slider for the coefficient of friction back and forth to calculate the corresponding force of friction. 

#import ipywidgets as widgets

coeff = widgets.FloatSlider(description="Coefficient",min=0.1,max=0.9)
normal_force = widgets.IntSlider(description="Normal force",min=5,max=50)

#Boldface letters at the beginning of each option
start_bold = "\033[1m"; end_bold = "\033[0;0m"

def f(coeff, normal_force):
    friction_force = coeff * normal_force
    print(start_bold + "Friction force = (coefficient of friction) X (normal force)" + end_bold)
    print("Friction force = {} X {} = {} N".format(coeff, normal_force, round(friction_force,1)))

out = widgets.interactive_output(f,{'coeff': coeff, 'normal_force': normal_force})

widgets.HBox([widgets.VBox([coeff, normal_force]), out])

**Question:** *What happens to the friction force when the coefficient of friction increases?*

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "The friction force increases." 
option_2 = "The friction force decreases."
option_3 = "The friction force remains constant."
option_4 = "The friction force equals zero."

multiple_choice(option_1, option_2, option_3, option_4)

It is to be noted that the amount $\mu_s F_{n}$ is actually the **maximal value** for the magnitude of **static** friction $F_{f}$.  Assuming the forces acting on an object are insufficient to overcome this maximal value, the object will be stationary.  In this case, the actual magnitude of the force of static friction, $F_{f}$, will typically be less than maximal; it is exactly that amount required to have a net force of zero so that the object does not move.  

### Solving Friction Problems

When solving a friction problem, it is useful to construct a free-body diagram. A **free-body diagram** is a simple graphical representation of an object and all the relevant forces acting upon it. An example of a free-body diagram is shown below:

<img src="Images/free_body_diagram.svg" width="45%"/>

* $F_{a}$ represents the **applied force**: the force acting in the direction of motion of the object.
* $F_{f}$ represents the **friction force**: the force acting in the direction opposite to the motion of the object.
* $mg$ represents the weight: the force of gravity acting on the object. Here, $m$ is the mass of the object, and $g$ is the gravitational acceleration directed downwards and of magnitude $g=9.8\:m/s^2$.
* $F_{n}$ represents the normal force: the force perpendicular to the surface pressing up against the object.

### Example
A 10 kg object is pushed across a flat horizontal surface with an applied force of 25 N. The same object is later pushed again with an applied force of 50 N. The coefficients of static and kinetic frictions are 0.40 and 0.30, respectively. Calculate the friction force ($F_{f}$) at each of the applied forces. Use the formula: $F_{f}=\mu F_{n}$.

**Step 1:** *Construct a free-body diagram*. The free-body diagram shown above may be used for this example. 

**Step 2:** *Calculate the known forces*: **Recall:** The weight of the object, $mg$, is equal to the mass of the object multiplied by the acceleration due to gravity.

$$mg = (10 \times 9.8)\:N = 98\:N$$

Since there is no vertical acceleration on the object, the total vertical force must vanish so the magnitude of the normal force must be equal to that of the weight of the object ($F_{n} = mg$). Therefore, 

$$F_{n} = mg = (10 \times 9.8)\:N = 98\:N$$

**Step 3:** *Determine the maximum static friction force*: Now that the normal force is known, we can calculate the maximum static friction force using the following equation:

$$F_{s}=\mu_{s} F_{n} = (0.40 \times 98)\:N = 39\:N$$

This means that the object will resist up to 39 N of applied force before it begins to move. 

**Step 4:** *Determine the friction force at 25 N*: Since the applied force of 25 N is less than the maximum static friction force, the object will remain stationary. The friction will oppose the applied force up to 25 N. Therefore, 

$$F_{f} = 25\:N$$

The direction of $F_{f}$ will be opposite to the direction of the applied force.
    
**Step 5:** *Determine the friction force at 50 N*: Since the applied force of 50 N is greater than the maximum static friction force, the object will begin to move. When in motion, the object is no longer being opposed by the static friction force. Instead it is being opposed by the kinetic friction force. We can calculate the kinetic friction force using the following equation:

$$F_{k}=\mu_{k} F_{n} = (0.30 \times 98)\:N = 29\:N$$

Therefore, the magnitude of the friction force will be:

$$F_{f} = 29\:N$$

Once again, the direction of $F_{f}$ will be opposite to the direction of the applied force.

**Answer:** At an applied force of 25 N, the object is stationary and the magnitude of the friction force is 25 N. At an applied force of 50 N, the object is in motion and the magnitude of the friction force is 29 N. In both cases, the force of friction is directed parallel to the surface and opposite to the direction of the applied force.  

## Practice Problems
(Click **Cell** > **Run Cells** to generate new random values for each question. Refer to the previous table to get the coefficients of friction for specific materials.)

#import random
#import ipywidgets as widgets

#Randomize mass and friction coefficient
mass = random.randint(20,50)
coeff = (random.randint(10,100))/100

#Print question
question = "A " + str(mass) +" kg object is pushed across a flat horizontal surface. The coefficient of kinetic friction between the moving object and the surface is " + str(coeff) +". What is the magnitude of the friction force?"
print(question)

#Answer calculation
#Friction force = (friction coefficient) X (normal force)
answer = coeff*(mass*9.8)
answer = round(answer)

#Define range of values for random multiple choices
min = int(coeff*((mass-15)*9.8))  
max = int(coeff*((mass+15)*9.8))

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(min,max),3)
while choice_list.count(answer) >= 1:
    choice_list = random.sample(range(min,max),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(answer) + " N" 
option_2 = str(choice_list[0]) + " N"
option_3 = str(choice_list[1]) + " N"
option_4 = str(choice_list[2]) + " N"

multiple_choice(option_1, option_2, option_3, option_4)

#import random
#import ipywidgets as widgets

#Randomize mass and applied force
mass = random.randint(20,50)
applied_force = random.randint(150,300)

#Randomize material
material_options = ['steel', 'glass', 'wood']
material =random.choice(material_options)

#Define friction coefficients based on selected material 
if material == 'steel':
    us = 0.7; uk = 0.6
elif material == 'glass':
    us = 0.9; uk = 0.4 
elif material == 'wood':
    us = 0.4; uk = 0.2 

#Print question
question = "If a %d kg %s object is pushed across a flat horizontal %s surface with an applied force of %d N, what is the magnitude of the friction force?" %(mass, material, material, applied_force)
print(question)

#Answer calculation
#Friction force = (friction coefficient) X (normal force)
static_friction = us*(mass*9.8)
kinetic_friction = uk*(mass*9.8)

#If the applied force is less than or equal to the maximum static friction force, the object will remain stationary
#The friction force equals the applied force
if applied_force <= static_friction:
    answer = applied_force
else:
    answer = kinetic_friction

answer = round(answer)    
    
#Define range of values for random multiple choices
if applied_force <= static_friction:
    min = applied_force-15  
    max = applied_force+15
else:
    min = int(uk*((mass-15)*9.8))  
    max = int(uk*((mass+15)*9.8))

#Create three choices that are unique (and not equal to the answer) 
choice_list = random.sample(range(min,max),3)
while choice_list.count(answer) >= 1:
    choice_list = random.sample(range(min,max),3)

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(answer) + " N" 
option_2 = str(choice_list[0]) + " N"
option_3 = str(choice_list[1]) + " N"
option_4 = str(choice_list[2]) + " N"

multiple_choice(option_1, option_2, option_3, option_4)

#import random
#import ipywidgets as widgets

#Randomize applied and friction forces
applied_force = random.randint(51,75)
friction_force = random.randint(25,50)

#Randomize material
material_options = ['steel', 'glass', 'wood']
material =random.choice(material_options)

#Define friction coefficients based on selected material 
if material == 'steel':
    uk = 0.6; us = 0.7
elif material == 'glass':
    uk = 0.4; us = 0.9
elif material == 'wood':
    uk = 0.2; us = 0.4

#Print question
question = "If a %s object is pushed across a flat horizontal %s surface with an applied force of %d N, and a friction force of %d N occurs, what is the magnitude of the normal force?" %(material, material, applied_force, friction_force)
print(question)

#Answer calculation
#weight = normal force = (friction force)/(kinetic friction coefficient)
answer = friction_force/uk
answer = round(answer)

#Define range of values for random multiple choices
min = int((friction_force-15)/uk); max = int((friction_force+15)/uk)

#Create three choices that are unique (and not equal to the answer) 
choice_list = random.sample(range(min,max),3)
while choice_list.count(answer) >= 1:
    choice_list = random.sample(range(min,max),3)

#Assign each option to these four variables
#Option1 contains the answer
option_1 = str(answer) + " N" 
option_2 = str(random.randint(min,max)) + " N"
option_3 = str(random.randint(min,max)) + " N"
option_4 = str(random.randint(min,max)) + " N"

multiple_choice(option_1, option_2, option_3, option_4)

#import random
#import ipywidgets as widgets
#import numpy as np

#Randomize mass and applied force
mass = random.randint(5,10)
applied_force = random.randint(46,80)
friction_force = random.randint(10,45)

#Print question
question = "A %d kg object is pulled across a flat horizontal surface by a force of %d N. The friction force is %d N. What is the coefficient of kinetic friction?" %(mass, applied_force, friction_force)
print(question)

#Answer calculation
#friction coefficient = (friction force) / (normal force)
answer = friction_force/(mass*9.8)
answer = round(answer,2)

#Define range of values for random multiple choices
min = 0.1
max = 0.9
unique = 0

#Create three choices that are unique (and not equal to the answer) 
while unique < 4:
    choice_list = np.random.uniform(min, max, size=(3,))
    for i in range(3):
        choice_list[i] = round(choice_list[i],2)
        
    choice_list = np.append(choice_list, answer)
    list_unique = np.unique(choice_list)
    unique = list_unique.size

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(answer) 
option_2 = str(choice_list[0])
option_3 = str(choice_list[1])
option_4 = str(choice_list[2])

multiple_choice(option_1, option_2, option_3, option_4)

Use the diagram below to answer the following question:

<img src="Images/free_body_diagram_pulley.svg" width="45%"/>

#import random
#import ipywidgets as widgets

#Randomize mass and friction coefficient
mass = random.randint(20,50)
coeff = (random.randint(10,100))/100

#Print question
question = "A " + str(mass) +" kg object is suspended by a pulley and connected to an object resting on a flat surface. The friction coefficient between the object and the surface is " + str(coeff) +". What is the minimum mass required to keep this suspended object stationary?"
print(question)

#Answer calculation
#Friction force = applied force = (mass) X (9.8)
friction_force = mass*9.8

normal_force = friction_force/coeff
answer = normal_force/9.8
answer = round(answer)

#Define range of values for random multiple choices
min = int((normal_force-50)/9.8)  
max = int((normal_force+50)/9.8)

#Create three choices that are unique (and not equal to the answer)
choice_list = random.sample(range(min,max),3)
while choice_list.count(answer) >= 1:
    choice_list = random.sample(range(min,max),3)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(answer) + " N" 
option_2 = str(choice_list[0]) + " N"
option_3 = str(choice_list[1]) + " N"
option_4 = str(choice_list[2]) + " N"

multiple_choice(option_1, option_2, option_3, option_4)

## Experiment 

As mentioned above, the coefficients of static and kinetic friction are determined experimentally for different materials.

**Determination of Static Friction**

Try the following experiment to determine the coefficient of static friction.

**Step 1:** Find an object and a flat horizontal surface. Record the material type for the object and surface.

**Step 2:** Measure the mass of the object using a mass balance (kg). 

**Step 3:** Calculate the magnitude of the normal force using the following formula: $F_{n} = mg$

**Step 4:** Using a spring scale, gradually apply a force to the object. Record the value on the scale the moment the object begins to move. At this moment, the applied force is equal to the maximum static friction force.

<img src="Images/free_body_diagram_spring.svg" width="55%"/>

**Step 5:** Calculate the coefficient of static friction using the following formula: $\mu_{s} = F_{f} \div F_{n}$

**Determination of Kinetic Friction**

Continue the experiment to determine the coefficient of kinetic friction.

**Step 6:** Using a spring scale, apply enough force to drag the object across the surface at a constant velocity (acceleration = 0). Record the value on the scale while the object is moving. So long as the object moves at a constant velocity, the applied force is equal to the kinetic friction force. 

**Step 7:** Calculate the coefficient of kinetic friction using the following formula: $\mu_{k} = F_{f} \div F_{n}$

 (**Double click** this cell and update the table with your own data. Click **Cell** > **Run Cells** when done.)
 
Materials | Object mass (g) | Normal force (N) | Applied force (N) | Static friction coefficient | Kinetic friction coefficient 
 ---      | ---             | ---              | ---               | ---                         | ----   
 ?        | ?               | ?                | ?                 | ?                           | ?      
 ?        | ?               | ?                | ?                 | ?                           | ?      
 ?        | ?               | ?                | ?                 | ?                           | ?
 ?        | ?               | ?                | ?                 | ?                           | ?      
 ?        | ?               | ?                | ?                 | ?                           | ? 

## Force Diagrams

A useful way to visualize the friction forces is to construct a force diagram, as shown below. This diagram depicts the magnitudes of the forces acting on an object as it is pushed across a flat horizontal surface with increasing force. The y-axis depicts the friction force ($F_{f}$), and the x-axis depicts the applied force ($F_{a}$). The sliders can be manipulated to change the normal force ($F_{n}$), the coefficient of static friction ($\mu_{s}$), and the coefficient of kinetic friction ($\mu_{k}$). 

#import ipywidgets as widgets
#import matplotlib.pyplot as plt

def f(Fn=50,μs=0.75,μk=0.25):
    #Fn = normal force
    #μs = coefficient of static friction
    #μk = coefficient of kinetic friction
    
    plt.figure()
    xs = Fn*μs
    xk = Fn*μk
    plt.plot([0,xs,xs,100],[0,xs,xk,xk])
    plt.plot([xs,xs],[xk,0], linestyle="dotted")
    plt.ylim(0, 100)
    plt.xlim(0,100)
    plt.ylabel('Friction force (N)')
    plt.xlabel('Applied force (N)')
    plt.annotate(xy=[xs-15,xs+5],s="Static friction (max)")
    plt.annotate(xy=[(xs+(100-xs)/2)-10,xk+5],s="Kinetic friction")
    plt.show()

interactive_plot = widgets.interactive(f,Fn=(35,75,5),μs=(0.5, 1.0),μk=(0.1, 0.5))
output = interactive_plot.children[-1]
output.layout.height = '280px'
interactive_plot

**Interpreting the graph**

Read the graph from left to right. As the applied force gradually increases along the x-axis, the friction force also increases. Notice that the magnitude of the friction force is equal to the applied force ($F_{f} = F_{a}$) until it reaches the point of maximum static friction. This point is shown on the graph as a **peak**. The point of maximum static friction is determined by the following equation: $F_{f}=\mu_{s} F_{n}$. As the applied force continues to increase beyond the peak of maximum static friction, the object begins to move. The friction force is now described by the kinetic friction equation: $F_{f}=\mu_{k} F_{n}$.

Move the slider for the normal force back and forth. As the normal force increases, what happens to the static and kinetic friction forces?

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "The static and kinetic friction forces both increase." 
option_2 = "The static and kinetic friction forces both decrease."
option_3 = "The static friction force increases and the kinetic friction force decreases."
option_4 = "The static friction force decreases and the kinetic friction force increases."

multiple_choice(option_1, option_2, option_3, option_4)

Move the slider for the static friction coefficient back and forth. As the static friction coefficient increases, what happens to the static and kinetic friction forces?

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "The static friction force increases and the kinetic friction force remains constant." 
option_2 = "The static friction force decreases and the kinetic friction force remains constant."
option_3 = "The static friction force increases and the kinetic friction force decreases."
option_4 = "The static friction force decreases and the kinetic friction force increases."

multiple_choice(option_1, option_2, option_3, option_4)

Move the slider for the kinetic friction coefficient back and forth. As the kinetic friction coefficient increases, what happens to the static and kinetic friction forces?

#import ipywidgets as widgets

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "The kinetic friction force increases and the static friction force remains constant." 
option_2 = "The kinetic friction force decreases and the static friction force remains constant."
option_3 = "The kinetic friction force increases and the static friction force decreases."
option_4 = "The kinetic friction force decreases and the static friction force increases."

multiple_choice(option_1, option_2, option_3, option_4)

## Conclusions

In this notebook, the concepts of static and kinetic friction were examined. In summary:

* **Friction** describes the force that resists the relative motion of an object as it slides across a surface. Friction forces are proportional to the normal force:

$$F_{f} = \mu F_{n}$$

* **Static friction** describes the friction force that acts between an object and the surface to prevent it from sliding. Static friction must be overcome for an object to move.

* **Kinetic friction** describes the friction force that acts between an object and the surface it slides upon. Kinetic friction is used when describing objects in motion.

* **Coefficients of static and kinetic friction** are determined experimentally for different materials. Once determined, these values can be tabulated and used to solve friction problems. An experimental method for determining the coefficients of static and kinetic friction was presented. 

* **Friction problems** can be solved using free-body diagrams, the friction formula, and the tabulated values for the coefficients of friction.

* **Force diagrams** can be used to visualize the relationship between the friction force, the applied force, the normal force, and the coefficients of static and kinetic friction.

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