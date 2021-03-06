![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/ReflectionsOfLightByPlaneAndSphericalMirrors/reflections-of-light-by-plane-and-spherical-mirrors.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

from IPython.display import display, Math, Latex, HTML
HTML('''<script>
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
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>''')

from helper import *
%matplotlib inline

# Reflection of Light 

## by Plane and Spherical Mirrors

## Introduction

When light shines onto the surface of an object, some of the light is reflected, while the rest is either absorbed or transmitted. We can imagine the light consisting of many narrow beams that travel in straight-line paths called **rays**. The light rays that strike the surface are called the **incident rays**. The light rays that reflect off the surface are called the **reflected rays**. This model of light is called the **ray model**, and it can be used to describe many aspects of light, including the reflection and formation of images by plane and spherical mirrors.

## Law of Reflection

<img src="Images/law_of_reflection.svg" width="50%"/>

To measure the angles of the incident and reflected rays, we first draw the **normal**, which is the line perpendicular to the surface. The **angle of incidence, $\theta_{i}$,** is the angle between the incident ray and the normal. Likewise, the **angle of reflection, $\theta_{r}$,** is the angle between the reflected ray and the normal. The incident ray, the reflected ray, and the normal to the reflecting surface all lie within the same plane. This is shown in the figure above. Notice that the angle of reflection is equal to the angle of incidence. This is known as the **law of reflection**, and it can be expressed by the following equation:

$$\theta_{r} = \theta_{i}$$

Use the slider below to change the angle of incidence. This changes the angle between the incident ray and the normal. Notice how the angle of reflection also changes when the slider is moved.

interactive_plot = widgets.interactive(f, Angle=widgets.IntSlider(value=45,min=0,max=90,step=15,continuous_update=False))
output = interactive_plot.children[-1]
output.layout.height = '280px'
interactive_plot

**Question:** *When the angle of incidence increases, what happens to the angle of reflection?* 

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "The angle of reflection increases." 
option_2 = "The angle of reflection decreases."
option_3 = "The angle of reflection remains constant."
option_4 = "The angle of reflection equals zero."

multiple_choice(option_1, option_2, option_3, option_4)

## Specular and Diffuse Reflections

 For a very smooth surface, such as a mirror, almost all of the light is reflected to produce a **specular reflection**. In a specular reflection, the reflected light rays are parallel to one another and point in the same direction. This allows specular reflections to form images. If the surface is not very smooth, then the light may bounce off of the surface in various directions. This produces a **diffuse reflection**. Diffuse reflections cannot form images. 

<img src="Images/specular_diffuse_reflections.svg" width="70%"/>

**Note:** The law of reflection still applies to diffuse reflections, even though the reflected rays are pointing in various directions. We can imagine that each small section of the rough surface is like a flat plane orientated differently than the sections around it. Since each of these sections is orientated differently, the angle of incidence is different at each section. This causes the reflected rays to scatter.


**Question:** *Which of the following is an example of a specular reflection?* 

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "The reflection off a clean window." 
option_2 = "The reflection off a wooden deck."
option_3 = "The reflection off a carpet floor."
option_4 = "The reflection off a table cloth."

multiple_choice(option_1, option_2, option_3, option_4)

**Question:** *Which of the following is an example of a diffuse reflection?* 

#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = "The reflection off a concrete sidewalk." 
option_2 = "The reflection off a mirror."
option_3 = "The reflection off the surface of a still lake."
option_4 = "The reflection off a polished sheet of metal."

multiple_choice(option_1, option_2, option_3, option_4)

## Image Formation by Plane Mirrors

A **plane mirror** is simply a mirror made from a flat (or planar) surface. These types of mirrors are commonly found in bedroom or bathroom fixtures. When an object is reflected in a plane mirror, the image of the object appears to be located behind the mirror. This is because our brains interpret the reflected light rays entering our eyes as having travelled in straight-line paths. The light rays entering our eyes simply do not contain enough information for our brains to differentiate between a straight-line path and a path that changed direction due to a reflection.  

<img src="Images/plane_mirror_reflection.svg" width="60%"/>

Notice in the figure above that the light rays do not actually converge at the location where the image appears to be formed (behind the mirror). Since the light rays do not actually go behind the mirror, they are represented as projections using dashed lines. If a film were placed at the image location behind the mirror, it would not be able to capture the image. As a result, this type of image is called a **virtual image**. 

For objects reflected in a plane mirror, the distance of the image from the mirror, $d_{i}$, is always equal to the distance of the object from the mirror, $d_{o}$. If the object is moved toward the mirror, the image of the object will also move toward the mirror such that the object and the image are always equidistant from the surface of the mirror.

Use the slider below to change the object distance. Notice how the image distance also changes when the slider is moved.

interactive_plot = widgets.interactive(f,Distance=widgets.IntSlider(value=30,min=10,max=50,step=10,continuous_update=False))
output = interactive_plot.children[-1]
output.layout.height = '280px'
interactive_plot

#Print question
distance = round(random.uniform(5,10),1)
print("If you stand " + str(distance) + " m in front of a plane mirror, how many metres behind the mirror is your virtual image?")

#Answer calculation
answer = distance
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(round((answer),1)) + " m" 
option_2 = str(round((answer * 2),1)) + " m"
option_3 = str(round((answer / 2),1)) + " m"
option_4 = str(round((answer / 4),1)) + " m"

multiple_choice(option_1, option_2, option_3, option_4)

#Print question
distance = round(random.uniform(5,10),1)
print("If you stand " + str(distance) + " m in front of a plane mirror, how many metres will separate you from your virtual image?")

#Answer calculation
answer = (distance * 2)
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(round((answer),1)) + " m" 
option_2 = str(round((answer * 2),1)) + " m"
option_3 = str(round((answer / 2),1)) + " m"
option_4 = str(round((answer / 4),1)) + " m"

multiple_choice(option_1, option_2, option_3, option_4)

## Spherical Mirrors

Two common types of curved mirror are formed from a section of a sphere. If the reflection takes place on the inside of the spherical section, then the mirror is called a **concave mirror**. The reflecting surface of a concave mirror curves inward and away from the viewer. If the reflection takes place on the outside of the spherical section, then the mirror is called a **convex mirror**. The reflecting surface of a convex mirror curves outward and toward the viewer.

<img src="Images/concave_convex_mirrors.svg" width="75%"/>

 The **centre of curvature, $C$,** is the point located at the centre of the sphere used to create the mirror. The **vertex, $V$,** is the point located at the geometric centre of the mirror itself. The **focus, $F$,** is the point located midway between the centre of curvature and the vertex. The line passing through the centre of curvature and the vertex is called the **principal axis**. Notice that the focus also lies on the principal axis.

When an incident ray parallel to the principle axis strikes the mirror, the reflected ray always passes through the focus. When an incident ray passes through the focus and strikes the mirror, the reflected ray is always parallel to the principle axis. (In the above diagrams, reverse the arrow directions to see this case). These properties make the focus particularly useful when examining spherical mirrors. 

**Note:** The distance from the centre of curvature to the vertex is equal to the **radius, $R$,** of the sphere used to create the mirror. Any straight line drawn from the centre to any point on the surface of a spherical mirror will have a length equal to the radius. The distance from the vertex to the focus is called the **focal length, $f$**. This distance is equal to half the distance of the radius.

$$f = \frac{R}{2}$$

#Print question
radius = round(random.uniform(10,30),1)
print("If the radius of a curved mirror is " + str(radius) + " cm, how many centimetres is the focal length?")

#Answer calculation
answer = radius/2
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(round((answer),1)) + " cm" 
option_2 = str(round((answer * 2),1)) + " cm"
option_3 = str(round((answer / 2),1)) + " cm"
option_4 = str(round((answer * 4),1)) + " cm"

multiple_choice(option_1, option_2, option_3, option_4)

#Print question
focal_length = round(random.uniform(5,15),1)
print("If the focal length of a curved mirror is " + str(focal_length) + " cm, how many centimetres is the radius of curvature?")

#Answer calculation
answer = focal_length*2
    
#Assign each multiple choice to these four variables
#Option_1 contains the answer
option_1 = str(round((answer),1)) + " cm" 
option_2 = str(round((answer * 2),1)) + " cm"
option_3 = str(round((answer / 2),1)) + " cm"
option_4 = str(round((answer / 4),1)) + " cm"

multiple_choice(option_1, option_2, option_3, option_4)

## Image Formation by Spherical Mirrors

A simple way to determine the position and characteristics of an image formed by the rays reflected from a spherical mirror is to construct a **ray diagram**. A ray diagram is used to shown the path taken by light rays as they reflect from an object or mirror. This was used to find the image created by a plane mirror in the previous section. When constructing a ray diagram, we need only consider ourselves with finding the location of a single point on the reflected image. To do this, any point on the object may be chosen, but for consistency, we will choose the topmost point for the diagrams shown below. Any rays may be chosen, but there are three particular rays that are easy to draw:

* **Ray 1:** This ray is drawn parallel to the principle axis from a point on the object to the surface of the mirror. Since the incident ray is parallel to the principle axis, the reflected ray must pass through the focus. 


* **Ray 2:** This ray is drawn from a point on the object and through the focus. Since the incident ray passes through the focus, the reflected ray must be parallel to the principle axis. 


* **Ray 3:** This ray is drawn from a point on the object and through the centre of curvature. This ray is therefore perpendicular to the mirror's surface (incident angle = 0). As such, the reflected ray must return along the same path and pass through the centre of curvature. 

The point at which any two of these three rays converge can be used to find the location and characteristics of the reflected image.

### Concave Mirrors

The characteristics of an image formed in a concave mirror depend on the position of the object. There are essentially five cases. Each of these five cases are demonstrated below:

### Case 1: Object Located at a Distance Greater than $C$

In the first case, the distance of the object from the mirror is greater than the radius used to define the centre of curvature. In other words, the object is further away from the mirror than the centre of curvature. In this example, we can draw any two of the three rays mentioned above to find the image of the reflected object. 

**Note:** You only need to draw two of the three rays to find the image of the reflected object.

output_case_1 = widgets.Output()
frame_case_1 = 1

#Toggle images
def show_svg_case_1():
    global frame_case_1
    if frame_case_1 == 0:
        display(SVG("Images/case_1_0.svg"))
        frame_case_1 = 1
    elif frame_case_1 == 1:
        display(SVG("Images/case_1_1.svg"))
        frame_case_1 = 2
    elif frame_case_1 == 2:
        display(SVG("Images/case_1_2.svg"))
        frame_case_1 = 3
    elif frame_case_1 == 3:
        display(SVG("Images/case_1_3.svg"))
        frame_case_1 = 0
        
button_case_1 = widgets.Button(description="Toggle rays", button_style = 'success')
display(button_case_1)

def on_submit_button_case_1_clicked(b):
    with output_case_1:
        clear_output(wait=True)
        show_svg_case_1()

with output_case_1:
    display(SVG("Images/case_1_0.svg"))
    
button_case_1.on_click(on_submit_button_case_1_clicked)
display(output_case_1)

**Question:** *Which options from the dropdown menus best describe the image formed by the reflected rays shown above?* 

#Create dropdown menus
dropdown1_1 = widgets.Dropdown(options={' ':0,'Beyond C': 1, 'At C': 2, 'Between C and F': 3, 'At F': 4, 'Between F and V': 5, 'Beyond V': 6, 'Not applicable (no image)': 7}, value=0, description='Position',)
dropdown1_2 = widgets.Dropdown(options={' ':0,'Larger than the object': 1, 'Same size as the object': 2, 'Smaller than the object': 3, 'Not applicable (no image)': 4}, value=0, description='Relative size',)
dropdown1_3 = widgets.Dropdown(options={' ':0,'Upright': 1, 'Inverted': 2, 'Not applicable (no image)': 3}, value=0, description='Orientation',)
dropdown1_4 = widgets.Dropdown(options={' ':0,'Real': 1, 'Virtual': 2, 'Not applicable (no image)': 3}, value=0, description='Type',)

#Display menus as 2x2 table
container1_1 = widgets.VBox(children=[dropdown1_1,dropdown1_2])
container1_2 = widgets.VBox(children=[dropdown1_3,dropdown1_4])
display(widgets.HBox(children=[container1_1, container1_2])), print(" ", end='\r')

#Evaluate input
def check_answer1(b):
    answer1_1 = dropdown1_1.label 
    answer1_2 = dropdown1_2.label
    answer1_3 = dropdown1_3.label 
    answer1_4 = dropdown1_4.label
    
    if answer1_1 == "Between C and F" and answer1_2 == "Smaller than the object" and answer1_3 == "Inverted" and answer1_4 == "Real":
        print("Correct!    ", end='\r')
    elif answer1_1 != ' ' and answer1_2 != ' ' and answer1_3 != ' ' and answer1_4 != ' ':
        print("Try again.", end='\r')
    else:
        print("            ", end='\r')

dropdown1_1.observe(check_answer1, names='value')
dropdown1_2.observe(check_answer1, names='value')
dropdown1_3.observe(check_answer1, names='value')
dropdown1_4.observe(check_answer1, names='value')

### Case 2: Object Located at $C$

In the second case, the distance of the object from the mirror is equal to the radius used to define the centre of curvature.
In other words, the object is located at the centre of curvature. In this case, we can draw only two rays to find the image of the reflected object. We cannot draw a ray passing through the centre of curvature because the object is located at $C$. 

output_case_2 = widgets.Output()
frame_case_2 = 1

#Toggle images
def show_svg_case_2():
    global frame_case_2
    if frame_case_2 == 0:
        display(SVG("Images/case_2_0.svg"))
        frame_case_2 = 1
    elif frame_case_2 == 1:
        display(SVG("Images/case_2_1.svg"))
        frame_case_2 = 2
    elif frame_case_2 == 2:
        display(SVG("Images/case_2_2.svg"))
        frame_case_2 = 0
        
button_case_2 = widgets.Button(description="Toggle rays", button_style = 'success')
display(button_case_2)

def on_submit_button_case_2_clicked(b):
    with output_case_2:
        clear_output(wait=True)
        show_svg_case_2()

with output_case_2:
    display(SVG("Images/case_2_0.svg"))
    
button_case_2.on_click(on_submit_button_case_2_clicked)
display(output_case_2)

**Question:** *Which options from the dropdown menus best describe the image formed by the reflected rays shown above?*

#Create dropdown menus
dropdown2_1 = widgets.Dropdown(options={' ':0,'Beyond C': 1, 'At C': 2, 'Between C and F': 3, 'At F': 4, 'Between F and V': 5, 'Beyond V': 6, 'Not applicable (no image)': 7}, value=0, description='Position',)
dropdown2_2 = widgets.Dropdown(options={' ':0,'Larger than the object': 1, 'Same size as the object': 2, 'Smaller than the object': 3, 'Not applicable (no image)': 4}, value=0, description='Relative size',)
dropdown2_3 = widgets.Dropdown(options={' ':0,'Upright': 1, 'Inverted': 2, 'Not applicable (no image)': 3}, value=0, description='Orientation',)
dropdown2_4 = widgets.Dropdown(options={' ':0,'Real': 1, 'Virtual': 2, 'Not applicable (no image)': 3}, value=0, description='Type',)

#Display menus as 2x2 table
container2_1 = widgets.VBox(children=[dropdown2_1,dropdown2_2])
container2_2 = widgets.VBox(children=[dropdown2_3,dropdown2_4])
display(widgets.HBox(children=[container2_1, container2_2])), print(" ", end='\r')

#Evaluate input
def check_answer2(b):
    answer2_1 = dropdown2_1.label 
    answer2_2 = dropdown2_2.label
    answer2_3 = dropdown2_3.label 
    answer2_4 = dropdown2_4.label
    
    if answer2_1 == "At C" and answer2_2 == "Same size as the object" and answer2_3 == "Inverted" and answer2_4 == "Real":
        print("Correct!    ", end='\r')
    elif answer2_1 != ' ' and answer2_2 != ' ' and answer2_3 != ' ' and answer2_4 != ' ':
        print("Try again.", end='\r')
    else:
        print("            ", end='\r')

dropdown2_1.observe(check_answer2, names='value')
dropdown2_2.observe(check_answer2, names='value')
dropdown2_3.observe(check_answer2, names='value')
dropdown2_4.observe(check_answer2, names='value')

### Case 3: Object Located between $C$ and $F$

In the third case, the distance of the object from the mirror is less than the radius used to define the centre of curvature, but greater than the focal length. In other words, the object is located between $F$ and $C$. In this case, we can find the image of the reflected object using two rays as shown below. If the mirror is large enough, a third ray that passes through $C$ can also be drawn. 

output_case_3 = widgets.Output()
frame_case_3 = 1

#Toggle images
def show_svg_case_3():
    global frame_case_3
    if frame_case_3 == 0:
        display(SVG("Images/case_3_0.svg"))
        frame_case_3 = 1
    elif frame_case_3 == 1:
        display(SVG("Images/case_3_1.svg"))
        frame_case_3 = 2
    elif frame_case_3 == 2:
        display(SVG("Images/case_3_2.svg"))
        frame_case_3 = 0
        
button_case_3 = widgets.Button(description="Toggle rays", button_style = 'success')
display(button_case_3)

def on_submit_button_case_3_clicked(b):
    with output_case_3:
        clear_output(wait=True)
        show_svg_case_3()

with output_case_3:
    display(SVG("Images/case_3_0.svg"))
    
button_case_3.on_click(on_submit_button_case_3_clicked)
display(output_case_3)

**Question:** *Which options from the dropdown menus best describe the image formed by the reflected rays shown above?*

#Create dropdown menus
dropdown3_1 = widgets.Dropdown(options={' ':0,'Beyond C': 1, 'At C': 2, 'Between C and F': 3, 'At F': 4, 'Between F and V': 5, 'Beyond V': 6, 'Not applicable (no image)': 7}, value=0, description='Position',)
dropdown3_2 = widgets.Dropdown(options={' ':0,'Larger than the object': 1, 'Same size as the object': 2, 'Smaller than the object': 3, 'Not applicable (no image)': 4}, value=0, description='Relative size',)
dropdown3_3 = widgets.Dropdown(options={' ':0,'Upright': 1, 'Inverted': 2, 'Not applicable (no image)': 3}, value=0, description='Orientation',)
dropdown3_4 = widgets.Dropdown(options={' ':0,'Real': 1, 'Virtual': 2, 'Not applicable (no image)': 3}, value=0, description='Type',)

#Display menus as 2x2 table
container3_1 = widgets.VBox(children=[dropdown3_1,dropdown3_2])
container3_2 = widgets.VBox(children=[dropdown3_3,dropdown3_4])
display(widgets.HBox(children=[container3_1, container3_2])), print(" ", end='\r')

#Evaluate input
def check_answer3(b):
    answer3_1 = dropdown3_1.label 
    answer3_2 = dropdown3_2.label
    answer3_3 = dropdown3_3.label 
    answer3_4 = dropdown3_4.label
    
    if answer3_1 == "Beyond C" and answer3_2 == "Larger than the object" and answer3_3 == "Inverted" and answer3_4 == "Real":
        print("Correct!    ", end='\r')
    elif answer3_1 != ' ' and answer3_2 != ' ' and answer3_3 != ' ' and answer3_4 != ' ':
        print("Try again.", end='\r')
    else:
        print("            ", end='\r')

dropdown3_1.observe(check_answer3, names='value')
dropdown3_2.observe(check_answer3, names='value')
dropdown3_3.observe(check_answer3, names='value')
dropdown3_4.observe(check_answer3, names='value')

### Case 4: Object Located at $F$

In the fourth case, the distance of the object from the mirror is equal to the focal length. In other words, the object is located at the focus. In this case, we can draw only two rays to find the image of the reflected object. We cannot draw a ray passing through the focus because the object is located at $F$. Notice that the reflected rays are parallel and therefore do not intersect. As a consequence, no image is formed.

output_case_4 = widgets.Output()
frame_case_4 = 1

#Toggle images
def show_svg_case_4():
    global frame_case_4
    if frame_case_4 == 0:
        display(SVG("Images/case_4_0.svg"))
        frame_case_4 = 1
    elif frame_case_4 == 1:
        display(SVG("Images/case_4_1.svg"))
        frame_case_4 = 2
    elif frame_case_4 == 2:
        display(SVG("Images/case_4_2.svg"))
        frame_case_4 = 0
        
button_case_4 = widgets.Button(description="Toggle rays", button_style = 'success')
display(button_case_4)

def on_submit_button_case_4_clicked(b):
    with output_case_4:
        clear_output(wait=True)
        show_svg_case_4()

with output_case_4:
    display(SVG("Images/case_4_0.svg"))
    
button_case_4.on_click(on_submit_button_case_4_clicked)
display(output_case_4)

**Question:** *Which options from the dropdown menus best describe the image formed by the reflected rays shown above?*

#import ipywidgets as widgets

#Create dropdown menus
dropdown4_1 = widgets.Dropdown(options={' ':0,'Beyond C': 1, 'At C': 2, 'Between C and F': 3, 'At F': 4, 'Between F and V': 5, 'Beyond V': 6, 'Not applicable (no image)': 7}, value=0, description='Position',)
dropdown4_2 = widgets.Dropdown(options={' ':0,'Larger than the object': 1, 'Same size as the object': 2, 'Smaller than the object': 3, 'Not applicable (no image)': 4}, value=0, description='Relative size',)
dropdown4_3 = widgets.Dropdown(options={' ':0,'Upright': 1, 'Inverted': 2, 'Not applicable (no image)': 3}, value=0, description='Orientation',)
dropdown4_4 = widgets.Dropdown(options={' ':0,'Real': 1, 'Virtual': 2, 'Not applicable (no image)': 3}, value=0, description='Type',)

#Display menus as 2x2 table
container4_1 = widgets.VBox(children=[dropdown4_1,dropdown4_2])
container4_2 = widgets.VBox(children=[dropdown4_3,dropdown4_4])
display(widgets.HBox(children=[container4_1, container4_2])), print(" ", end='\r')

#Evaluate input
def check_answer4(b):
    answer4_1 = dropdown4_1.label 
    answer4_2 = dropdown4_2.label
    answer4_3 = dropdown4_3.label 
    answer4_4 = dropdown4_4.label
    
    if answer4_1 == "Not applicable (no image)" and answer4_2 == "Not applicable (no image)" and answer4_3 == "Not applicable (no image)" and answer4_4 == "Not applicable (no image)":
        print("Correct!    ", end='\r')
    elif answer4_1 != ' ' and answer4_2 != ' ' and answer4_3 != ' ' and answer4_4 != ' ':
        print("Try again.", end='\r')
    else:
        print("            ", end='\r')

dropdown4_1.observe(check_answer4, names='value')
dropdown4_2.observe(check_answer4, names='value')
dropdown4_3.observe(check_answer4, names='value')
dropdown4_4.observe(check_answer4, names='value')

### Case 5: Object Located between $F$ and $V$

In the fifth case, the distance of the object from the mirror is less than the focal length. In other words, the object is located between $F$ and $V$. In this case, we can find the image of the reflected object using two rays as shown below. Notice that the reflected rays do not actually converge. However, the projections of the reflected rays *do* converge behind the mirror. Therefore, a virtual image is formed.

output_case_5 = widgets.Output()
frame_case_5 = 1

#Toggle images
def show_svg_case_5():
    global frame_case_5
    if frame_case_5 == 0:
        display(SVG("Images/case_5_0.svg"))
        frame_case_5 = 1
    elif frame_case_5 == 1:
        display(SVG("Images/case_5_1.svg"))
        frame_case_5 = 2
    elif frame_case_5 == 2:
        display(SVG("Images/case_5_2.svg"))
        frame_case_5 = 0
        
button_case_5 = widgets.Button(description="Toggle rays", button_style = 'success')
display(button_case_5)

def on_submit_button_case_5_clicked(b):
    with output_case_5:
        clear_output(wait=True)
        show_svg_case_5()

with output_case_5:
    display(SVG("Images/case_5_0.svg"))
    
button_case_5.on_click(on_submit_button_case_5_clicked)
display(output_case_5)

**Question:** *Which options from the dropdown menus best describe the image formed by the reflected rays shown above?*

#Create dropdown menus
dropdown5_1 = widgets.Dropdown(options={' ':0,'Beyond C': 1, 'At C': 2, 'Between C and F': 3, 'At F': 4, 'Between F and V': 5, 'Beyond V': 6, 'Not applicable (no image)': 7}, value=0, description='Position',)
dropdown5_2 = widgets.Dropdown(options={' ':0,'Larger than the object': 1, 'Same size as the object': 2, 'Smaller than the object': 3, 'Not applicable (no image)': 4}, value=0, description='Relative size',)
dropdown5_3 = widgets.Dropdown(options={' ':0,'Upright': 1, 'Inverted': 2, 'Not applicable (no image)': 3}, value=0, description='Orientation',)
dropdown5_4 = widgets.Dropdown(options={' ':0,'Real': 1, 'Virtual': 2, 'Not applicable (no image)': 3}, value=0, description='Type',)

#Display menus as 2x2 table
container5_1 = widgets.VBox(children=[dropdown5_1,dropdown5_2])
container5_2 = widgets.VBox(children=[dropdown5_3,dropdown5_4])
display(widgets.HBox(children=[container5_1, container5_2])), print(" ", end='\r')

#Evaluate input
def check_answer5(b):
    answer5_1 = dropdown5_1.label 
    answer5_2 = dropdown5_2.label
    answer5_3 = dropdown5_3.label 
    answer5_4 = dropdown5_4.label
    
    if answer5_1 == "Beyond V" and answer5_2 == "Larger than the object" and answer5_3 == "Upright" and answer5_4 == "Virtual":
        print("Correct!    ", end='\r')
    elif answer5_1 != ' ' and answer5_2 != ' ' and answer5_3 != ' ' and answer5_4 != ' ':
        print("Try again.", end='\r')
    else:
        print("            ", end='\r')

dropdown5_1.observe(check_answer5, names='value')
dropdown5_2.observe(check_answer5, names='value')
dropdown5_3.observe(check_answer5, names='value')
dropdown5_4.observe(check_answer5, names='value')

### Convex Mirrors

For reflections in convex mirrors, the location of the object does not change the general characteristics of the image. The image will always be between F and V, smaller than the object, upright, and virtual.

output_convex = widgets.Output()
frame_convex = 1

#Toggle images
def show_svg_convex():
    global frame_convex
    if frame_convex == 0:
        display(SVG("Images/convex_mirror_reflection_0.svg"))
        frame_convex = 1
    elif frame_convex == 1:
        display(SVG("Images/convex_mirror_reflection_1.svg"))
        frame_convex = 2
    elif frame_convex == 2:
        display(SVG("Images/convex_mirror_reflection_2.svg"))
        frame_convex = 0
        
button_convex = widgets.Button(description="Toggle rays", button_style = 'success')
display(button_convex)

def on_submit_button_convex_clicked(b):
    with output_convex:
        clear_output(wait=True)
        show_svg_convex()

with output_convex:
    display(SVG("Images/convex_mirror_reflection_0.svg"))
    
button_convex.on_click(on_submit_button_convex_clicked)
display(output_convex)

**Question:** *Which options from the dropdown menus best describe the image formed by the reflected rays shown above?*

#Create dropdown menus
dropdown6_1 = widgets.Dropdown(options={' ':0,'Beyond C': 1, 'At C': 2, 'Between C and F': 3, 'At F': 4, 'Between F and V': 5, 'Beyond V': 6, 'Not applicable (no image)': 7}, value=0, description='Position',)
dropdown6_2 = widgets.Dropdown(options={' ':0,'Larger than the object': 1, 'Same size as the object': 2, 'Smaller than the object': 3, 'Not applicable (no image)': 4}, value=0, description='Relative size',)
dropdown6_3 = widgets.Dropdown(options={' ':0,'Upright': 1, 'Inverted': 2, 'Not applicable (no image)': 3}, value=0, description='Orientation',)
dropdown6_4 = widgets.Dropdown(options={' ':0,'Real': 1, 'Virtual': 2, 'Not applicable (no image)': 3}, value=0, description='Type',)

#Display menus as 2x2 table
container6_1 = widgets.VBox(children=[dropdown6_1,dropdown6_2])
container6_2 = widgets.VBox(children=[dropdown6_3,dropdown6_4])
display(widgets.HBox(children=[container6_1, container6_2])), print(" ", end='\r')

#Evaluate input
def check_answer6(b):
    answer6_1 = dropdown6_1.label 
    answer6_2 = dropdown6_2.label
    answer6_3 = dropdown6_3.label 
    answer6_4 = dropdown6_4.label
    
    if answer6_1 == "Between F and V" and answer6_2 == "Smaller than the object" and answer6_3 == "Upright" and answer6_4 == "Virtual":
        print("Correct!    ", end='\r')
    elif answer6_1 != ' ' and answer6_2 != ' ' and answer6_3 != ' ' and answer6_4 != ' ':
        print("Try again.", end='\r')
    else:
        print("            ", end='\r')

dropdown6_1.observe(check_answer6, names='value')
dropdown6_2.observe(check_answer6, names='value')
dropdown6_3.observe(check_answer6, names='value')
dropdown6_4.observe(check_answer6, names='value')

## Conclusions

In this notebook, the reflection of light off of plane and spherical mirrors was examined. In summary:

* Light can be thought of as a collection of narrow beams called **rays** which travel in straight-line paths. This conceptualization of light is called the **ray model**.

* The **law of reflection** states that the angle of reflection is equal to the angle of incidence. 

$$\theta_{r} = \theta_{i}$$

* A **specular reflection** is characterized by having reflected rays that are parallel and pointing in the same direction. 

* A **diffuse reflection** is characterized by having reflected rays pointing in various directions.

* **Plane mirrors** always produce a virtual image behind the mirror. This image has the same size and orientation of the object, and the image and object are always equidistant from the mirror.

* **A spherical mirror** is formed from a section of a sphere. If the reflecting surface is on the inside of the spherical section, the mirror is **concave**. If it is on the outside, the mirror is **convex**.

* A **ray diagram** can be used to find the location and characteristics of a reflection in concave and convex mirrors. For concave mirrors, the characteristics of the possible images are summarized as follows: 

Object position | Image position  | Relative size           | Orientation | Type 
---             | ---             | ---                     | ---         | ---
Beyond C        | Between C and F | Smaller than the object | Inverted    | Real
At C            | At C            | Same size as the object | Inverted    | Real
Between C and F | Beyond C        | Larger than the object  | Inverted    | Real
At F            | (No image)      | (No image)              | (No image)  | (No image)
Between F and V | Beyond V        | Larger than the object  | Upright     | Virtual

* The images formed by a convex mirror are always between F and V, smaller than the object, upright, and virtual.

Images in this notebook represent original artwork.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)