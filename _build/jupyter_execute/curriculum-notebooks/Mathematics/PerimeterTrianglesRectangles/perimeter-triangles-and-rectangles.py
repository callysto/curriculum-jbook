![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/PerimeterTrianglesRectangles/perimeter-triangles-and-rectangles.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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


# Perimeter - Triangles and Rectangles

import matplotlib.pyplot as plt
import ipywidgets
from ipywidgets import widgets, interact, interact_manual, Button, Layout
from IPython.display import Javascript, display, Latex, clear_output, Markdown

Geometry is one of the most valuable topics of everyday life. It is important for driving, cooking, drawing, decorating, and many other tasks. It is also instinctive to human beings. Babies use geometry when deciding that circular pieces fit in circular holes. So, this notebook is describing the math behind natural activities.

In this notebook, you will learn how to find the perimeter of quadrilaterals and triangles. These topics will be taught through visual aids and interactive models.

## Perimeter Background

## Squares

A **perimeter** is: "The continuous line that forms a boundary around a shape." This means that a perimeter is the *length of every edge of a shape added together*. So, let's say we want to find the **perimeter of a square**:

%%html
<svg height="400" width="1500">
<rect x="370" y="30" width="200" height="200" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "4cm" at the top of the shape
<text x="455" y="20" fill="black">4cm</text>

</svg>

To calculate the perimeter of a square, add the length of all the edges together:

$$
\rm (Length) + (Length) + (Length) + (Length) = Perimeter 
$$

But, we know that the length of every edge on a square is the same. So, we can do:

$$
 \rm 4 \times (Length) = Perimeter 
$$

So, the perimeter of the square above is:

$$
\rm 4 \times (4cm) = 16cm 
$$

### Calculator for Perimeter of a Square

The following is an interactive calculator for getting the perimeter of any square:

%matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt

#Used to ensure the description text doesn't get cut off.
stl = {'description_width': 'initial'}

def f(sqrLength):
    #Draw a square using the sqrLength input
    plt.plot([0, sqrLength, sqrLength, 0, 0], [0, 0, sqrLength, sqrLength, 0])
    
    #Scale the plot to look like a square at all times
    plt.axis('scaled')
    plt.show()
    
    #Calculate the perimeter of the square by multiplying the length of the square by 4
    sqrPerimeter = 4 * sqrLength
    
    display(Latex("Given a length of $" + str(sqrLength) + "$, the perimeter is $" + str(sqrPerimeter) + "$"))

#Create an interactive plot with the f function and an IntSlider as input. The IntSlider
# will determine the length of a square.
interactive_plot = interactive(f, sqrLength = widgets.IntSlider(min = 1, max = 100, \
                               description = 'Square length:', style = stl))

interactive_plot

## Rectangles

Now, let's say we have to find the **perimeter of a rectangle**:

%%html
<svg height="400" width="1500">
<rect x="300" y="30" width="370" height="170" stroke="black" fill="orange" stroke-width="5"/>

#The following text is for the "9cm" at the top of the shape
<text x="470" y="20" fill="black">9cm</text>

#The following text is for the "4cm" at the bottom of the shape
<text x="290" y="130" fill="black" transform="rotate(-90 290,130)">4cm</text>
</svg>

To calculate the perimeter of a rectangle, add the length of all the edges together:

$$
\rm (Length) + (Length) + (Height) + (Height) = Perimeter 
$$

But, we know that a rectangle has 4 edges, and every edge is equal to another. 

This means that *the length of the edge on the bottom is equal to the length of the edge on the top*. This also means that *the length of the edge on the right side is equal to the length of the edge on the left*. 

So, we can do:

$$
\rm 2 \times (Length) + 2 \times (Height) = Perimeter $
$$

So, the perimeter of the rectangle above is:

$$
\begin{align*}
\rm 2 \times (9cm) + 2 \times (4cm) = 26cm
\end{align*}
$$

### Calculator for Perimeter of a Rectangle

The following is an interactive calculator for getting the perimeter of any rectangle:

%matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt

#Used to ensure the description text doesn't get cut off.
stl = {'description_width': 'initial'}

def f(rectLength, rectHeight):
    #Draw a rectangle using the rectLength as the length and the rectHeight as the height
    rect = plt.plot([0, rectLength, rectLength, 0, 0], [0, 0, rectHeight, rectHeight, 0])
    
    #Scale the plot to look like a rectangle at all times
    plt.axis('scaled')
    plt.show()
    
    #Calculate the perimeter of the rectangle by adding the product of 2 times the length 
    # and 2 times the height together
    rectPerimeter = (rectLength * 2) + (rectHeight * 2)

    display(Latex("Given a length of $" + str(rectLength) + "$, and a height of $" + str(rectHeight) + \
          "$, the perimeter of a rectangle is $" + str(rectPerimeter) + "$"))

#Create an interactive plot with the f function and two IntSliders as input. One for the 
# rectangle's length, (rectLength) and the other for the rectangle's height, (rectHeight)
interactive_plot = interactive(f, rectLength = widgets.IntSlider(min = 1, max = 100, \
                               description = 'Rectangle Length:', style = stl), \
                               rectHeight = widgets.IntSlider(min = 1, max = 100, \
                               description = 'Rectangle Height:', style = stl))

interactive_plot

## Quadrilaterals

Now, let's say we have to find the **perimeter of some quadrilateral shape** that isn't a square or rectangle. For example, how do you find the perimeter of the following quadrilateral?

%%html
<svg height="400" width="1500">

#First point is at x = 300 and y = 80
#Second point at x = 500 and y = 40
#Third point at x = 650 and y = 200
#Fourth point at x = 260 and y = 200
<polygon points="300 80 500 40 650 200 260 200" 
 stroke="black" fill="midnightblue" stroke-width="5"/>

#The following text is for the "4cm" at the left side of the shape
<text x="265" y="150" fill="black" transform="rotate(-70 265,150)">4cm</text>

#The following text is for the "6cm" at the top of the shape
<text x="380" y="55" fill="black" transform="rotate(-10 380,55)">6cm</text>

#The following text is for the "7cm" at the right side of the shape
<text x="570" y="100" fill="black" transform="rotate(50 570,100)">7cm</text>

#The following text is for the "9cm" at the bottom of the shape
<text x="430" y="220" fill="black">9cm</text>

</svg>

In this situation, we can't simplify the original formula. This is because the shape is neither a square or rectangle. So, the only way we can find the perimeter is by adding the length of each side together.

<$$
\rm (Length) + (Length) + (Length) + (Length) = (Perimeter) 
$$

So, the perimeter of the quadrilateral above is:

$$
\begin{align*}
\rm (4cm) + (6cm) + (7cm) + (9cm) = 26cm
\end{align*}
$$

### Practice Problem 1

What is the perimeter of the following quadrilateral?

%%html
<svg height="400" width="1500">

#First point at x = 350 and y = 100
#Second point at x = 500 and y = 60
#Third point at x = 650 and y = 220
#Fourth point at x = 350 and y = 150
<polygon points="350 100 500 60 650 220 350 150" 
 stroke="black" fill="mediumblue" stroke-width="5"/>

#The following text is for the "7cm" at the left side of the shape
<text x="340" y="140" fill="black" transform="rotate(-90 340,140)">7cm</text>

#The following text is for the "17cm" at the top of the shape
<text x="410" y="75" fill="black" transform="rotate(-15 410,75)">17cm</text>

#The following text is for the "10cm" at the right side of the shape
<text x="570" y="120" fill="black" transform="rotate(50 570,120)">25cm</text>

#The following text is for the "34cm" at the bottom of the shape
<text x="460" y="195" fill="black" transform="rotate(12 460,195)">34cm</text>

</svg>

#Used to ensure the description text doesn't get cut off.
style = {'description_width': 'initial'}

#Create an input integer widget
question1 = widgets.IntText(
    value=None,
    description='Input your perimeter here: ',
    disabled=False,
    style = style
    )

#Create a button titled "Check Answer"
checkButton1 = widgets.Button(description = "Check Answer")

def checkAnswer(a):
    #questionAnswer will be the input given by the user.
    questionAnswer = question1.value
    
    #answers is a list of possible answers that can be inputted. 
    answers = [83]
    
    #Check if the input is in the list of answers. If this is the case:
    if (questionAnswer in answers):
        #Clear the output
        clear_output()
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give an explenation for the answer.
        display(Markdown("Well done! <br> \
                         We get this answer by doing: <br> \
                         <h3 align='center'>$\ ($Length$) + ($Length$) + ($Length$) + ($Length$) \
                         = ($Perimeter$) $</h3> <br> \
                         So: <br> \
                         <h3 align='center'>$\ (7$cm$) + (17$cm$) + (25$cm$) + (34$cm$) = 83$cm </h3>"))
        
    #Otherwise, if no answer has been given, do nothing.
    elif (questionAnswer == 0):
        None
    
    #Lastly, if the answer is wrong, give the user a hint.
    else:
        #Clear the output
        clear_output()
        
        #Display the input integer and check button widgets
        display(question1)
        display(checkButton1)
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give a hint for the question
        display(Markdown("Not quite. <br> \
                      Remember, to find the perimeter of a quadrilateral you must add all the \
                      lengths together: <br> \
                      <h3 align='center'>$\ ($Length$) + ($Length$) + ($Length$) + ($Length$) \
                      = ($Perimeter$) $</h3>"))

display(question1)
display(checkButton1)

checkButton1.on_click(checkAnswer)

### Practice Problem 2

If the perimeter is $34$cm for the following quadrilateral, then what is the length of side **A**?

%%html
<svg height="400" width="1500">

#First point at x = 340 and y = 30
#Second point at x = 600 and y = 60
#Third point at x = 450 and y = 220
#Fourth point at x = 360 and y = 150
<polygon points="340 30 600 60 450 220 360 150" 
 stroke="black" fill="cornflowerblue" stroke-width="5"/>

#The following text is for the "A" at the left side of the shape
<text x="332" y="95" fill="black">A</text>

#The following text is for the "9cm" at the top of the shape
<text x="440" y="35" fill="black" transform="rotate(5 440,35)">14cm</text>

#The following text is for the "10cm" at the right side of the shape
<text x="525" y="170" fill="black" transform="rotate(-50 525,170)">10cm</text>

#The following text is for the "5cm" at the bottom left side of the shape
<text x="380" y="190" fill="black" transform="rotate(38 380,190)">5cm</text>

</svg>

#Used to ensure the description text doesn't get cut off.
style = {'description_width': 'initial'}

#Create an input integer widget
question2 = widgets.IntText(
    value=None,
    description='Input your length here: ',
    disabled=False,
    style = style
    )

#Create a button titled "Check Answer"
checkButton2 = widgets.Button(description = "Check Answer")

def checkAnswer(a):
    #questionAnswer will be the input given by the user.
    questionAnswer = question2.value
    
    #answers is a list of possible answers that can be inputted. 
    answers = [5]
    
    #Check if the input is in the list of answers. If this is the case:
    if (questionAnswer in answers):
        #Clear the output
        clear_output()
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give an explenation for the answer.
        display(Markdown("Well done! <br> \
                         We get this answer by doing: <br> \
                         <h3 align='center'>$\ ($Perimeter$) - ($Length$) - ($Length$) - ($Length$) \
                         = A $</h3> <br> \
                         So: <br> \
                         <h3 align='center'>$\ (34$cm$) - (14$cm$) - (10$cm$) - (5$cm$) = 5$cm$ $</h3>"))
        
    #Otherwise, if no answer has been given, do nothing.
    elif (questionAnswer == 0):
        None
    
    #Lastly, if the answer is wrong, give the user a hint.
    else:
        #Clear the output
        clear_output()
        
        #Display the input integer and check button widgets
        display(question2)
        display(checkButton2)
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give a hint for the question
        display(Markdown("Not quite. <br> \
                      Remember, the formula for finding the perimeter of a quadrilateral is: <br> \
                      <h3 align='center'>$\ ($Length$) + ($Length$) + ($Length$) + ($Length$) = \
                      ($Perimeter$) $</h3> <br> \
                      We can rearrange this formula to find length $A$ by doing: <br> \
                      <h3 align='center'>$\ A = ($Perimeter$) - ($Length$) - ($Length$) - ($Length$) $</h3>"))

display(question2)
display(checkButton2)

checkButton2.on_click(checkAnswer)

### Practice Problem 3

What is the perimeter of the following quadrilateral?

%%html
<svg height="400" width="1500">

#First point at x = 230 and y = 30
#Second point at x = 580 and y = 30
#Third point at x = 730 and y = 200
#Fourth point at x = 380 and y = 200
<polygon points="230 30 580 30 730 200 380 200" 
 stroke="black" fill="deepskyblue" stroke-width="5"/>
    
#The following text is for the "9cm" at the top of the shape
<text x="400" y="20" fill="black">9cm</text>

#The following text is for the "7cm" at the right side of the shape
<text x="655" y="100" fill="black" transform="rotate(50 655,100)">7cm</text>

</svg>

#Used to ensure the description text doesn't get cut off.
style = {'description_width': 'initial'}

#Create an input integer widget
question3 = widgets.IntText(
    value=None,
    description='Input your perimeter here: ',
    disabled=False,
    style = style
    )

#Create a button titled "Check Answer"
checkButton3 = widgets.Button(description = "Check Answer")

def checkAnswer(a):
    #questionAnswer will be the input given by the user.
    questionAnswer = question3.value
    
    #answers is a list of possible answers that can be inputted. 
    answers = [32]
    
    #Check if the input is in the list of answers. If this is the case:
    if (questionAnswer in answers):
        #Clear the output
        clear_output()
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give an explenation for the answer.
        display(Markdown("Well done! <br> \
                         We get this answer by doing: <br> \
                         <h3 align='center'>$\ 2 × ($Length$) + 2 × ($Length$) = ($Perimeter$) $</h3> <br> \
                         So: <br> \
                         <h3 align='center'>$\ 2 × (9$cm$) + 2 × (7$cm$) = 32$cm</h3>"))
        
    #Otherwise, if no answer has been given, do nothing.
    elif (questionAnswer == 0):
        None
    
    #Lastly, if the answer is wrong, give the user a hint.
    else:
        #Clear the output
        clear_output()
        
        #Display the input integer and check button widgets
        display(question3)
        display(checkButton3)
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give a hint for the question
        display(Markdown("Not quite. <br> \
                      Remember, the formula for finding the perimeter of a quadrilateral is: <br> \
                      <h3 align='center'>$\ ($Length$) + ($Length$) + ($Length$) + ($Length$) = \
                      ($Perimeter$) $</h3> <br> \
                      But, the shape we were given *has two sides that are equal*. This means that the top edge \
                      of the shape is the same length as the bottom edge. This also means that the left side \
                      of the shape is the same length as the right side. So, we can use the formula: <br> \
                      <h3 align='center'>$\  2 × ($Length$) + 2 × ($Length$) = ($Perimeter$) $</h3>"))

display(question3)
display(checkButton3)

checkButton3.on_click(checkAnswer)

## Triangles

For our next topic, we will cover how to find the **perimeter of a triangle**. If we are given the length of every edge on a triangle:

%%html
<svg height="400" width="1500">

#First point at x = 480 and y = 30
#Second point at x = 630 and y = 200
#Third point at x = 280 and y = 200
<polygon points="480 30 630 200 280 200" 
 stroke="black" fill="darkmagenta" stroke-width="5"/>
    
#The following text is for the "15cm" at the top of the shape
<text x="365" y="120" fill="black" transform="rotate(-45 365,120)">15cm</text>

#The following text is for the "12cm" at the right side of the shape
<text x="555" y="100" fill="black" transform="rotate(50 555,100)">12cm</text>

#The following text is for the "17cm" at the bottom of the shape
<text x="440" y="218" fill="black">17cm</text>

</svg>

Then the process for finding the perimeter is simple. We must add the length of all the edges together:

$$
\rm (Length) + (Length) + (Length) = (Perimeter) 
$$

So, the perimeter of the above triangle is:

$$
\begin{align*}
\rm (15cm) + (12cm) + (17cm) = 44cm
\end{align*}
$$

But, if we are not given the length of all the edges, we must add another step. If we are missing the edge of a right angle triangle, we can use the **Pythagorean theorem** to help us.

## Pythagorean Theorem

The Pythagorean theorem is one of the most important theorems you will learn. [This notebook](pythagorean-theorem.ipynb) provides an in-depth lesson on the Pythagorean theorem. The following will be a review of this material.

The theorem begins with a *right angle triangle*:

%%html
<svg height="400" width="1500">

### The following code is for the triangle gray triangle
#First point at x = 400 and y = 50
#Second point at x = 570 and y = 200
#Third point at x = 400 and y = 200
<polygon points="400 50 570 200 400 200" 
 stroke="black" fill="Gray" stroke-width="5"/>
    
#The following text is for the "A" at the top of the shape
<text x="390" y="130" fill="black" transform="rotate(-90 390,130)">A</text>

#The following text is for the "C" at the right side of the shape
<text x="490" y="120" fill="black" transform="rotate(40 490,120)">C</text>

#The following text is for the "B" at the bottom of the shape
<text x="475" y="218" fill="black">B</text>

###The following code is for the right angle mark inside the gray triangle.
<rect x="400" y="180" width="20" height="20"
 stroke="black" fill=None stroke-width="2"/>


</svg>

This is a crucial step when using the Pythagorean theorem. *If the triangle you are using does not have a right angle, then the theorem will not work*. 

Next, we will create squares using the $A$ and $B$ sides of the triangle:

%%html
<svg height="700" width="1500">

### The following code is for the triangle gray triangle
#First point at x = 400 and y = 50
#Second point at x = 570 and y = 200
#Third point at x = 400 and y = 200
<polygon points="400 50 570 200 400 200" 
 stroke="black" fill="Gray" stroke-width="5"/>

#The following text is for the "A" at the left side of the shape
<text x="390" y="155" fill="black" transform="rotate(-90 390,130)">A</text>

#The following text is for the "C" at the right side of the shape
<text x="490" y="120" fill="black" transform="rotate(40 490,120)">C</text>

#The following text is for the "B" at the bottom of the shape
<text x="475" y="195" fill="black">B</text>

###The following code is for the right angle mark inside the gray triangle.
<rect x="400" y="180" width="20" height="20"
 stroke="black" fill=None stroke-width="2"/>

###The following code is for the square created by the A edge.
<rect x="243" y="47" width="153" height="153"
 stroke="black" fill="deeppink" stroke-width="5"/>

###The following code is for the square created by the B edge.
<rect x="400" y="205" width="173" height="173"
 stroke="black" fill="hotpink" stroke-width="5"/>

</svg>

Finally, we will create a square using the $C$ side of the triangle:

%%html
<svg height="850" width="1500">

### The following code is for the triangle gray triangle
#First point at x = 400 and y = 50
#Second point at x = 570 and y = 200
#Third point at x = 400 and y = 200
<polygon points="400 190 570 340 400 340" 
 stroke="black" fill="Gray" stroke-width="5"/>

###The following code is for the square created by the A edge.
<rect x="243" y="187" width="153" height="153"
 stroke="black" fill="deeppink" stroke-width="5"/>

###The following code is for the square created by the B edge.
<rect x="400" y="344" width="173" height="173"
 stroke="black" fill="hotpink" stroke-width="5"/>
    
###The following code is for the square created by the C edge.
<rect x="552" y="10" width="234" height="234"
 stroke="black" fill="lightpink" stroke-width="5" transform="rotate(41.5 555,10)"/>    

#The following text is for the "A" at the left side of the shape
<text x="385" y="295" fill="black" transform="rotate(-90 390,270)">A</text>

#The following text is for the "B" at the bottom of the shape
<text x="475" y="335" fill="black">B</text>

#The following text is for the "C" at the right side of the shape
<text x="470" y="275" fill="black" transform="rotate(40 470,275)">C</text>

###The following code is for the right angle mark inside the gray triangle.
<rect x="400" y="320" width="20" height="20"
 stroke="black" fill=None stroke-width="2"/>
    
</svg>

The Pythagorean theorem states that the area of the square made by $C$ is equal to the areas of the squares $A$ and $B$:

$$
C^2 = A^2 + B^2 
$$

So, we can get the length of $C$ by doing:

$$ 
C = \sqrt {A^2 + B^2} 
$$

Let's give the triangle above numbers so we can try our formula on it:

%%html
<svg height="400" width="1500">

### The following code is for the triangle gray triangle
#First point at x = 400 and y = 50
#Second point at x = 570 and y = 200
#Third point at x = 400 and y = 200
<polygon points="400 50 570 200 400 200" 
 stroke="black" fill="Gray" stroke-width="5"/>
    
#The following text is for the "10cm" at the left side of the shape
<text x="390" y="140" fill="black" transform="rotate(-90 390,140)">10cm</text>

#The following text is for the "C" at the right side of the shape
<text x="490" y="120" fill="black" transform="rotate(40 490,120)">C</text>

#The following text is for the "10cm" at the bottom of the shape
<text x="465" y="218" fill="black">10cm</text>

###The following code is for the right angle mark inside the gray triangle.
<rect x="400" y="180" width="20" height="20"
 stroke="black" fill=None stroke-width="2"/>


</svg>

Now, we can calculate the length of $C$ by doing:

$$
\begin{align*}
C &= \sqrt {(10\textrm{cm})^2 + (10\textrm{cm})^2} \\
&= \sqrt {100\textrm{cm}^2 + 100\textrm{cm}^2}\\
&= \sqrt {200\textrm{cm}^2}
\end{align*}
$$

Finally, we know that the length of $C \approx 14\textrm{cm}$

But, let's say you didn't have the length of side $A$ instead:

%%html
<svg height="400" width="1500">

### The following code is for the triangle gray triangle
#First point at x = 400 and y = 50
#Second point at x = 570 and y = 200
#Third point at x = 400 and y = 200
<polygon points="400 50 570 200 400 200" 
 stroke="black" fill="Gray" stroke-width="5"/>
    
#The following text is for the "A" at the top of the shape
<text x="390" y="130" fill="black" transform="rotate(-90 390,130)">A</text>

#The following text is for the "14cm" at the right side of the shape
<text x="470" y="120" fill="black" transform="rotate(40 490,120)"> 14cm</text>

#The following text is for the "10cm" at the bottom of the shape
<text x="465" y="218" fill="black">10cm</text>

###The following code is for the right angle mark inside the gray triangle.
<rect x="400" y="180" width="20" height="20"
 stroke="black" fill=None stroke-width="2"/>


</svg>

Then, we can rearrange our original formula of:

$$
C^2 = A^2 + B^2 
$$

To the formula:

$$ 
A^2 = C^2 - B^2 
$$

So that:

$$ 
A = \sqrt{C^2 - B^2} 
$$

So, we can calculate the length of $A$ by doing:

$$
\begin{align*}
A &= \sqrt {(14\textrm{cm})^2 - (10\textrm{cm})^2} \\
&= \sqrt {196\textrm{cm}^2 - 100\textrm{cm}^2}\\
&= \sqrt {96\textrm{cm}^2}
\end{align*}
$$

Finally, we know that the length of $A \approx 10\textrm{cm}$

### Practice Problem 4

Daniel's school has an uneven baseball diamond:

%%html
<svg height="400" width="1500">

#First point at x = 480 and y = 30
#Second point at x = 600 and y = 200
#Third point at x = 350 and y = 200
<polygon points="480 30 600 200 350 200" 
 stroke="black" fill="orchid" stroke-width="5"/>
    
#The following text is for the "70m" at the top of the shape
<text x="395" y="120" fill="black" transform="rotate(-50 395,120)">70m</text>

#The following text is for the "60m" at the right side of the shape
<text x="540" y="100" fill="black" transform="rotate(52 540,100)">60m</text>

#The following text is for the "90m" at the bottom of the shape
<text x="460" y="218" fill="black">90m</text>

</svg>

How many meters would Daniel have to run to score a home run?

#Used to ensure the description text doesn't get cut off.
style = {'description_width': 'initial'}

#Create an input integer widget
question4 = widgets.IntText(
    value=None,
    description='Input your answer here: ',
    disabled=False,
    style = style
    )

#Create a button titled "Check Answer"
checkButton4 = widgets.Button(description = "Check Answer")

def checkAnswer(a):
    #questionAnswer will be the input given by the user.
    questionAnswer = question4.value
    
    #answers is a list of possible answers that can be inputted. 
    answers = [220]
    
    #Check if the input is in the list of answers. If this is the case:
    if (questionAnswer in answers):
        #Clear the output
        clear_output()
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give an explenation for the answer.
        display(Markdown("Well done! <br> \
                         We get this answer by doing: <br> \
                         <h3 align='center'>$\ ($Length$) + ($Length$) + ($Length$) = ($Perimeter$) $</h3> <br> \
                         So, Daniel would have to run: <br> \
                         <h3 align='center'>$\ (90$m$) + (60$m$) + (70$m$) = 220$m</h3>"))
        
    #Otherwise, if no answer has been given, do nothing.
    elif (questionAnswer == 0):
        None
    
    #Lastly, if the answer is wrong, give the user a hint.
    else:
        #Clear the output
        clear_output()
        
        #Display the input integer and check button widgets
        display(question4)
        display(checkButton4)
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give a hint for the question
        display(Markdown("Not quite. <br> \
                      Remember, the formula for finding the perimeter of a triangle is: <br> \
                      <h3 align='center'>$\ ($Length$) + ($Length$) + ($Length$) = ($Perimeter$) $</h3>"))

display(question4)
display(checkButton4)

checkButton4.on_click(checkAnswer)

### Practice Problem 5

What is the length of side $B$ in the following triangle?

%%html
<svg height="400" width="1500">

### The following code is for the triangle gray triangle
#First point at x = 400 and y = 50
#Second point at x = 480 and y = 200
#Third point at x = 400 and y = 200
<polygon points="400 50 480 200 400 200" 
 stroke="black" fill="pink" stroke-width="5"/>
    
#The following text is for the "12cm" at the top of the shape
<text x="390" y="150" fill="black" transform="rotate(-90 390,150)">12cm</text>

#The following text is for the "13cm" at the right side of the shape
<text x="445" y="115" fill="black" transform="rotate(60 445,115)">13cm</text>

#The following text is for the "B" at the bottom of the shape
<text x="435" y="218" fill="black">B</text>

###The following code is for the right angle mark inside the gray triangle.
<rect x="400" y="180" width="20" height="20"
 stroke="black" fill=None stroke-width="2"/>


</svg>

#Used to ensure the description text doesn't get cut off.
style = {'description_width': 'initial'}

#Create an input integer widget
question5 = widgets.IntText(
    value=None,
    description='Input your B value here: ',
    disabled=False,
    style = style
    )

#Create a button titled "Check Answer"
checkButton5 = widgets.Button(description = "Check Answer")

def checkAnswer(a):
    #questionAnswer will be the input given by the user.
    questionAnswer = question5.value
    
    #answers is a list of possible answers that can be inputted. 
    answers = [5]
    
    #Check if the input is in the list of answers. If this is the case:
    if (questionAnswer in answers):
        #Clear the output
        clear_output()
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give an explenation for the answer.
        display(Markdown("Well done! <br> \
                         We get this answer by using the formula: <br> \
                         <h3 align='center'>$\ (C)^2 - (A)^2 = (B)^2 $</h3> <br> \
                         Then, we fill in the values: <br> \
                         <h3 align='center'>$\ (13$cm$)^2 - (12$cm$)^2 = 25$cm$^2 = (B)^2 $</h3> <br> \
                         And after taking the square root, we get that: <br> \
                         <h3 align='center'>$ B = 5$cm$ $</h3> <br>"))
        
    #Otherwise, if no answer has been given, do nothing.
    elif (questionAnswer == 0):
        None
    
    #Lastly, if the answer is wrong, give the user a hint.
    else:
        #Clear the output
        clear_output()
        
        #Display the input integer and check button widgets
        display(question5)
        display(checkButton5)
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give a hint for the question
        display(Markdown("Not quite. <br> \
                      Remember, the formula for finding a missing length of a 90 degree triangle is: <br> \
                      <h3 align='center'>$\ (C)^2 - (A)^2 = (B)^2 $</h3>"))

display(question5)
display(checkButton5)

checkButton5.on_click(checkAnswer)

## Conclusion:

In this notebook, you will have learned:

* How to find the **perimeter** of *quadrilaterals* and *triangles*.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)