![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/PerimeterIrregularShapes/perimeter-irregular-shapes.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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


# Perimeter - Irregular Shapes

import matplotlib.pyplot as plt
import ipywidgets
from ipywidgets import widgets, interact, interact_manual, Button, Layout
from IPython.display import Javascript, display, Latex, clear_output, Markdown

Geometry is one of the most valuable topics of everyday life. It is important for driving, cooking, drawing, decorating, and many other tasks. It is also instinctive to human beings. Babies use geometry when deciding that circular pieces fit in circular holes. So, this notebook is describing the math behind natural activities.

In this notebook, you will learn how to measure the perimeter and area of irregular shapes. This topic will be taught through visual aids and interactive models.

## Irregular Shapes

## Irregular Shape Introduction

To better understand an *irregular shape*, we will first define what a *regular shape* is.

* A **Regular Shape** is *a shape that has sides and angles that are equal.*
* An **Irregular Shape** is *a shape that has sides and angles of any size.*

This idea is easier to see through visuals. So, the following shape would be a *regular shape*:

%%html
<svg height="400" width="1500">
<rect x="370" y="30" width="200" height="200" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "4cm" at the top of the shape
<text x="455" y="20" fill="black">4cm</text>

</svg>

But, the following shape is an *irregular shape*:

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

You may have noticed that you have already seen both of the examples above! This should help you feel more comfortable with the idea of irregular shapes.

To find the **perimeter** and **area** of these shapes, we **begin by dividing the shape into smaller pieces.** This will help us with our calculations greatly.  The continued example found below will help show this idea.

## A Continued Example
We will use the following *irregular shape* for the rest of our lesson:

%%html
<svg height="550" width="1500">

#### The following code is for the shape bellow.
#First point is at x = 200 and y = 300
#Second point at x = 450 and y = 300
#Third point at x = 450 and y = 200
#Fourth point at x = 650 and y = 300
#Fifth point is at x = 800 and y = 300
#Sixth point at x = 650 and y = 100
#Seventh point at x = 450 and y = 100
#Eight point at x = 450 and y = 50
#Ninth point is at x = 400 and y = 50
#Tenth point at x = 400 and y = 100
#Elleventh point at x = 100 and y = 100
#Twelfth point at x = 300 and y = 230
<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>

</svg>

Let's say you want to find the **perimeter** and **area** of this shape. To begin, you want to split the shape up into smaller shapes. These smaller shapes should be shapes you are more familiar with:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>

#The following text is for the "4cm" at the bottom of the shape
<text x="245" y="320" fill="black">4cm</text>
    
#The following text is for the "9cm" at the bottom of the shape
<text x="360" y="320" fill="black">9cm</text>

#The following text is for the "x" at the bottom of the shape
<text x="440" y="255" fill="black" transform="rotate(-90 440,255)"> x </text>

#The following text is for the "11cm" at the bottom side of the shape
<text x="540" y="235" fill="black" transform="rotate(32 540,235)">11cm</text>

#The following text is for the "10cm" at the right side of the shape
<text x="645" y="215" fill="black" transform="rotate(-90 645,215)">10cm</text>

#The following text is for the "y" at the top of the shape
<text x="535" y="90" fill="black"> y </text>

#The following text is for the "15cm" at the top of the shape
<text x="250" y="90" fill="black"> 15cm </text>

#The following text is for the "12cm" at the left side of the shape
<text x="190" y="180" fill="black" transform="rotate(35 190,180)">12cm</text>

#The following text is for the "5cm" at the left side of the shape
<text x="240" y="265" fill="black" transform="rotate(-40 240,265)">5cm</text>


### Dashed line at the bottom to make a triangle
<line x1="450" y1="300" x2="650" y2="300" stroke="black" stroke-width="2" stroke-dasharray=8/>    

#The following text is for the "10cm" at the bottom of the shape
<text x="525" y="295" fill="black">10cm</text>


#### Dashed line at the top of the shape to make a square
<line x1="400" y1="100" x2="450" y2="100" stroke="black" stroke-width="2" stroke-dasharray=8/>   

#The following text is for the "3cm" at the top of the shape
<text x="412" y="115" fill="black">3cm</text>


#### Dashed line at the left side of the shape to make two triangles
<line x1="305" y1="100" x2="305" y2="300" stroke="black" stroke-width="2" stroke-dasharray=8/>   

#Line at the left to separate two triangles
<line x1="305" y1="230" x2="320" y2="230" stroke="black" stroke-width="3"/> 

#The following text is for the "7cm" at the left side of the shape
<text x="310" y="150" fill="black" transform="rotate(90 310,150)">7cm</text>

#The following text is for the "z" at the left side of the shape
<text x="310" y="260" fill="black" transform="rotate(90 310,260)"> z </text> 


#### Line at the bottom side of the shape to give two numbers
<line x1="305" y1="300" x2="305" y2="315" stroke="black" stroke-width="3"/>   

</svg>

This may seem very intimidating at first. But don't be too worried, we will solve for the perimeter and area of this shape slowly!

We will begin by finding the variables that are missing. Let's begin by finding the $x$ value:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>

#The following text is for the "x" at the bottom of the shape
<text x="440" y="255" fill="black" transform="rotate(-90 440,255)"> x </text>

#The following text is for the "11cm" at the bottom side of the shape
<text x="540" y="235" fill="black" transform="rotate(32 540,235)">11cm</text>

### Dashed line at the bottom to make a triangle
<line x1="450" y1="300" x2="650" y2="300" stroke="black" stroke-width="2" stroke-dasharray=8/>    

#The following text is for the "10cm" at the bottom of the shape
<text x="525" y="295" fill="black">10cm</text>

</svg>

To find the length of $x$, we will use the Pythagorean theorem. Since $x$ can be seen as the "$A$" value, $10$ as the "$B$" value, and $11$ as the "$C$" value, we can do:

### $$
\begin{align*}
x &= \sqrt {(11\textrm{cm})^2 - (10\textrm{cm})^2} \\
&= \sqrt {121\textrm{cm}^2 - 100\textrm{cm}^2}\\
&= \sqrt {21\textrm{cm}^2}
\end{align*}
$$

So, we know that the length of $x \approx 5\textrm{cm}$

Now, we can add this value to our shape:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>

#The following text is for the "4cm" at the bottom of the shape
<text x="245" y="320" fill="black">4cm</text>
    
#The following text is for the "9cm" at the bottom of the shape
<text x="360" y="320" fill="black">9cm</text>

#The following text is for the "4cm" at the bottom of the shape
<text x="440" y="260" fill="black" transform="rotate(-90 440,260)">4cm</text>

#The following text is for the "11cm" at the bottom side of the shape
<text x="540" y="235" fill="black" transform="rotate(32 540,235)">11cm</text>

#The following text is for the "10cm" at the right side of the shape
<text x="645" y="215" fill="black" transform="rotate(-90 645,215)">10cm</text>

#The following text is for the "y" at the top of the shape
<text x="535" y="90" fill="black"> y </text>

#The following text is for the "15cm" at the top of the shape
<text x="250" y="90" fill="black"> 15cm </text>

#The following text is for the "12cm" at the left side of the shape
<text x="190" y="180" fill="black" transform="rotate(35 190,180)">12cm</text>

#The following text is for the "5cm" at the left side of the shape
<text x="240" y="265" fill="black" transform="rotate(-40 240,265)">5cm</text>


### Dashed line at the bottom to make a triangle
<line x1="450" y1="300" x2="650" y2="300" stroke="black" stroke-width="2" stroke-dasharray=8/>    

#The following text is for the "10cm" at the bottom of the shape
<text x="525" y="295" fill="black">10cm</text>


#### Dashed line at the top of the shape to make a square
<line x1="400" y1="100" x2="450" y2="100" stroke="black" stroke-width="2" stroke-dasharray=8/>   

#The following text is for the "3cm" at the top of the shape
<text x="412" y="115" fill="black">3cm</text>


#### Dashed line at the left side of the shape to make two triangles
<line x1="305" y1="100" x2="305" y2="300" stroke="black" stroke-width="2" stroke-dasharray=8/>   

#Line at the left to separate two triangles
<line x1="305" y1="230" x2="320" y2="230" stroke="black" stroke-width="3"/> 

#The following text is for the "7cm" at the left side of the shape
<text x="310" y="150" fill="black" transform="rotate(90 310,150)">7cm</text>

#The following text is for the "z" at the left side of the shape
<text x="310" y="260" fill="black" transform="rotate(90 310,260)"> z </text> 


#### Line at the bottom side of the shape to give two numbers
<line x1="305" y1="300" x2="305" y2="315" stroke="black" stroke-width="3"/>   

</svg>

Let's continue by finding the length of $y$. To do this, we have to look at the values we already have:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>

#The following text is for the "y" at the top of the shape
<text x="535" y="90" fill="black"> y </text>

### Dashed line at the bottom to make a triangle
<line x1="450" y1="300" x2="650" y2="300" stroke="black" stroke-width="2" stroke-dasharray=8/>    

#The following text is for the "10cm" at the bottom of the shape
<text x="525" y="295" fill="black">10cm</text>

</svg>

The bottom $10$cm is the same length as the length of $y$. So, we know that the length of $y = 10\textrm{cm}$

Now, we can add this value to our shape:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>

#The following text is for the "4cm" at the bottom of the shape
<text x="245" y="320" fill="black">4cm</text>
    
#The following text is for the "9cm" at the bottom of the shape
<text x="360" y="320" fill="black">9cm</text>

#The following text is for the "5cm" at the bottom of the shape
<text x="440" y="260" fill="black" transform="rotate(-90 440,260)">5cm</text>

#The following text is for the "11cm" at the bottom side of the shape
<text x="540" y="235" fill="black" transform="rotate(32 540,235)">11cm</text>

#The following text is for the "10cm" at the right side of the shape
<text x="645" y="215" fill="black" transform="rotate(-90 645,215)">10cm</text>

#The following text is for the "10cm" at the top of the shape
<text x="535" y="90" fill="black">10cm</text>

#The following text is for the "15cm" at the top of the shape
<text x="250" y="90" fill="black"> 15cm </text>

#The following text is for the "12cm" at the left side of the shape
<text x="190" y="180" fill="black" transform="rotate(35 190,180)">12cm</text>

#The following text is for the "5cm" at the left side of the shape
<text x="240" y="265" fill="black" transform="rotate(-40 240,265)">5cm</text>


### Dashed line at the bottom to make a triangle
<line x1="450" y1="300" x2="650" y2="300" stroke="black" stroke-width="2" stroke-dasharray=8/>    

#The following text is for the "10cm" at the bottom of the shape
<text x="525" y="295" fill="black">10cm</text>


#### Dashed line at the top of the shape to make a square
<line x1="400" y1="100" x2="450" y2="100" stroke="black" stroke-width="2" stroke-dasharray=8/>   

#The following text is for the "3cm" at the top of the shape
<text x="412" y="115" fill="black">3cm</text>


#### Dashed line at the left side of the shape to make two triangles
<line x1="305" y1="100" x2="305" y2="300" stroke="black" stroke-width="2" stroke-dasharray=8/>   

#Line at the left to separate two triangles
<line x1="305" y1="230" x2="320" y2="230" stroke="black" stroke-width="3"/> 

#The following text is for the "7cm" at the left side of the shape
<text x="310" y="150" fill="black" transform="rotate(90 310,150)">7cm</text>

#The following text is for the "z" at the left side of the shape
<text x="310" y="260" fill="black" transform="rotate(90 310,260)"> z </text> 


#### Line at the bottom side of the shape to give two numbers
<line x1="305" y1="300" x2="305" y2="315" stroke="black" stroke-width="3"/>   

</svg>

Finally, we have to find the length of $z$:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>

#The following text is for the "4cm" at the bottom of the shape
<text x="245" y="320" fill="black">4cm</text>

#The following text is for the "10cm" at the right side of the shape
<text x="645" y="215" fill="black" transform="rotate(-90 645,215)">10cm</text>

#The following text is for the "5cm" at the left side of the shape
<text x="240" y="265" fill="black" transform="rotate(-40 240,265)">5cm</text>


#### Dashed line at the left side of the shape to make two triangles
<line x1="305" y1="100" x2="305" y2="300" stroke="black" stroke-width="2" stroke-dasharray=8/>   

#Line at the left to separate two triangles
<line x1="305" y1="230" x2="320" y2="230" stroke="black" stroke-width="3"/> 

#The following text is for the "7cm" at the left side of the shape
<text x="310" y="150" fill="black" transform="rotate(90 310,150)">7cm</text>

#The following text is for the "z" at the left side of the shape
<text x="310" y="260" fill="black" transform="rotate(90 310,260)"> z </text> 

</svg>

There are actually two ways to find the length of $z$:

* ### The Pythagorean Method
Here, we start by using $z$ as the "$A$" value, $4$cm as the "$B$" value, and $5$cm as the "$C$" value. Now, we can calculate for $z$ by doing: <br>
### $$
\begin{align*}
z &= \sqrt {(5\textrm{cm})^2 - (4\textrm{cm})^2} \\
&= \sqrt {25\textrm{cm}^2 - 16\textrm{cm}^2}\\
&= \sqrt {9\textrm{cm}^2}
\end{align*}
$$
So, we know that the length of $z = 3$cm


* ### The Known Values Method
Here, we start by looking at the length on the far right side of the shape. We see that it is $10$cm long. This tells us that the length of the dotted line on the left must equal $10$cm. Then, we can do: <br>
### $$
\begin{align*}
z &= 10 - 7
\end{align*}
$$
So, we know that the length of $z = 3$cm

Now, we can add this value to our shape:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>

#The following text is for the "4cm" at the bottom of the shape
<text x="245" y="320" fill="black">4cm</text>
    
#The following text is for the "9cm" at the bottom of the shape
<text x="360" y="320" fill="black">9cm</text>

#The following text is for the "5cm" at the bottom of the shape
<text x="440" y="260" fill="black" transform="rotate(-90 440,260)">5cm</text>

#The following text is for the "11cm" at the bottom side of the shape
<text x="540" y="235" fill="black" transform="rotate(32 540,235)">11cm</text>

#The following text is for the "10cm" at the right side of the shape
<text x="645" y="215" fill="black" transform="rotate(-90 645,215)">10cm</text>

#The following text is for the "10cm" at the top of the shape
<text x="535" y="90" fill="black">10cm</text>

#The following text is for the "15cm" at the top of the shape
<text x="250" y="90" fill="black"> 15cm </text>

#The following text is for the "12cm" at the left side of the shape
<text x="190" y="180" fill="black" transform="rotate(35 190,180)">12cm</text>

#The following text is for the "5cm" at the left side of the shape
<text x="240" y="265" fill="black" transform="rotate(-40 240,265)">5cm</text>


#### Dashed line at the bottom to make a triangle
<line x1="450" y1="300" x2="650" y2="300" stroke="black" stroke-width="2" stroke-dasharray=8/>    

#The following text is for the "10cm" at the bottom of the shape
<text x="525" y="295" fill="black">10cm</text>


#### Dashed line at the top of the shape to make a square
<line x1="400" y1="100" x2="450" y2="100" stroke="black" stroke-width="2" stroke-dasharray=8/>   

#The following text is for the "3cm" at the top of the shape
<text x="412" y="115" fill="black">3cm</text>


#### Dashed line at the left side of the shape to make two triangles
<line x1="305" y1="100" x2="305" y2="300" stroke="black" stroke-width="2" stroke-dasharray=8/>   

#Line at the left to separate two triangles
<line x1="305" y1="230" x2="320" y2="230" stroke="black" stroke-width="3"/> 

#The following text is for the "7cm" at the left side of the shape
<text x="310" y="150" fill="black" transform="rotate(90 310,150)">7cm</text>

#The following text is for the "3cm" at the left side of the shape
<text x="310" y="250" fill="black" transform="rotate(90 310,250)">3cm</text> 


#### Line at the bottom side of the shape to give two numbers
<line x1="305" y1="300" x2="305" y2="315" stroke="black" stroke-width="3"/>   

</svg>

Let's use this as a chance for you to practice. Try finding the perimeter of this shape.

#Used to ensure the description text doesn't get cut off.
style = {'description_width': 'initial'}

#Create an input integer widget
question6 = widgets.IntText(
    value=None,
    description='Input your perimeter here: ',
    disabled=False,
    style = style
    )

#Create a button titled "Check Answer"
checkButton6 = widgets.Button(description = "Check Answer")

def checkAnswer(a):
    #questionAnswer will be the input given by the user.
    questionAnswer = question6.value
    
    #answers is a list of possible answers that can be inputted. 
    answers = [91]
    
    #Check if the input is in the list of answers. If this is the case:
    if (questionAnswer in answers):
        #Clear the output
        clear_output()
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give an explenation for the answer.
        display(Markdown("Well done! <br> \
                         We get this answer by adding together all lengths of the shape: <br> \
                         <h3 align='center'>$\ (4$cm$) + (9$cm$) + (5$cm$) + (11$cm$) + (10$cm$) \
                         + (10$cm$) + 3 × (3$cm$) + (15$cm$) + (12$cm$) + (6$cm$) = (91$cm$) $</h3> "))
        
    #Otherwise, if no answer has been given, do nothing.
    elif (questionAnswer == 0):
        None
    
    #Lastly, if the answer is wrong, give the user a hint.
    else:
        #Clear the output
        clear_output()
        
        #Display the input integer and check button widgets
        display(question6)
        display(checkButton6)
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give a hint for the question
        display(Markdown("Not quite. <br> \
                      Remember, to find the perimeter of an irregular shape *you must add the length of \
                      every edge together*."))

display(question6)
display(checkButton6)

checkButton6.on_click(checkAnswer)

Next, let's try finding the **area** of this shape. We will do this by taking the area of shapes we know. We will also assume that:

<h3 align='center'>$\rm CM = cm^2 $</h3>

Let's start by finding the area of the square on top:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>

#### The following rectangle is for the red square at the top
<rect x="400" y="50" width="50" height="50" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "3cm" at the top of the shape
<text x="412" y="115" fill="black">3cm</text>

</svg>

We should know that the **area of a square** is *the length of any side squared*:

<h3 align='center'>$\rm (Length)^2 = Area $</h3>

So, the area of the <span style="color:red">**red square**</span> above is:

### $$
\begin{align*}
(3\textrm{cm})^2 = 9\textrm{cm}^2
\end{align*}
$$

Next, we'll calculate the area of the triangle at the bottom:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>

#### The following rectangle is for the red square at the top
<rect x="400" y="50" width="50" height="50" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "9CM at the top of the shape
<text x="412" y="80" fill="black">9CM</text>

#### The following polygon is for the pink triangle at the bottom
<polygon points = "450 300 450 200 650 300"
 stroke="black" fill="lightpink" stroke-width="5"/>

#The following text is for the "5cm" at the bottom of the shape
<text x="440" y="260" fill="black" transform="rotate(-90 440,260)">5cm</text>

#The following text is for the "11cm" at the bottom side of the shape
<text x="540" y="235" fill="black" transform="rotate(32 540,235)">11cm</text>

#The following text is for the "10cm" at the bottom of the shape
<text x="525" y="295" fill="black">10cm</text>

</svg>

We should know that the **area of a triangle** is *the length times the height, divided by two*:

<h3 align='center'>$\rm \frac {(Length) \times (Height)}{2} = Area $</h3>

So, the area of the <span style="color:pink">**pink triangle**</span> above is:

### $$
\begin{align*}
\frac{(10\textrm{cm}) \times (5\textrm{cm})}{2} = 25\textrm{cm}^2
\end{align*}
$$

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>

#### The following rectangle is for the red square at the top
<rect x="400" y="50" width="50" height="50" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "9CM" at the top of the shape
<text x="412" y="80" fill="black">9CM</text>

#### The following polygon is for the pink triangle at the bottom
<polygon points = "450 300 450 200 650 300"
 stroke="black" fill="lightpink" stroke-width="5"/>

#The following text is for the "25CM" at the bottom of the shape
<text x="490" y="270" fill="black">25CM</text>

</svg>

Now, we'll calculate the triangle at the top left:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>   

#### The following rectangle is for the red square at the top
<rect x="400" y="50" width="50" height="50" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "9CM" at the top of the shape
<text x="412" y="80" fill="black">9CM</text>

#### The following polygon is for the pink triangle at the bottom
<polygon points = "450 300 450 200 650 300"
 stroke="black" fill="lightpink" stroke-width="5"/>

#The following text is for the "25CM" at the bottom of the shape
<text x="490" y="270" fill="black">25CM</text>

#### The following polygon is for the pink triangle in the left
<polygon points = "300 100 100 100 300 230"
 stroke="black" fill="hotpink" stroke-width="5"/>
    
#The following text is for the "x" at the top of the shape
<text x="210" y="93" fill="black" >x</text>    

#The following text is for the "12cm" at the left side of the shape
<text x="190" y="180" fill="black" transform="rotate(35 190,180)">12cm</text> 

#The following text is for the "7cm" at the left side of the shape
<text x="310" y="150" fill="black" transform="rotate(90 310,150)">7cm</text>

</svg>

To calculate the area of the <span style="color:hotpink">**pink triangle**</span> above, we have to find its length. This is denoted by a $x$. To do this, we have to use *the Pythagorean theorem*. We start by using $x$ as the "$A$" value, $7$cm as the "$B$" value, and $12$cm as the "$C$" value.

### $$
\begin{align*}
x &= \sqrt {(12\textrm{cm})^2 - (7\textrm{cm})^2} \\
&= \sqrt {144\textrm{cm}^2 - 49\textrm{cm}^2}\\
&= \sqrt {95\textrm{cm}^2}
\end{align*}
$$

So, we know that the length of $x \approx 10$cm

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>   

#### The following rectangle is for the red square at the top
<rect x="400" y="50" width="50" height="50" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "9CM" at the top of the shape
<text x="412" y="80" fill="black">9CM</text>

#### The following polygon is for the pink triangle at the bottom
<polygon points = "450 300 450 200 650 300"
 stroke="black" fill="lightpink" stroke-width="5"/>

#The following text is for the "25CM" at the bottom of the shape
<text x="490" y="270" fill="black">25CM</text>

#### The following polygon is for the pink triangle in the left
<polygon points = "300 100 100 100 300 230"
 stroke="black" fill="hotpink" stroke-width="5"/>
    
#The following text is for the "10cm" at the top of the shape
<text x="200" y="93" fill="black" >10cm</text>    

#The following text is for the "12cm" at the left side of the shape
<text x="190" y="180" fill="black" transform="rotate(35 190,180)">12cm</text> 

#The following text is for the "7cm" at the left side of the shape
<text x="310" y="150" fill="black" transform="rotate(90 310,150)">7cm</text>

</svg>

Now, we can calculate the area of the <span style="color:hotpink">**pink triangle**</span>:

### $$
\begin{align*}
\rm \frac{(7cm) \times (10cm)}{2} = 35cm^2
\end{align*}
$$

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>   

#### The following rectangle is for the red square at the top
<rect x="400" y="50" width="50" height="50" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "9CM" at the top of the shape
<text x="412" y="80" fill="black">9CM</text>

#### The following polygon is for the pink triangle at the bottom
<polygon points = "450 300 450 200 650 300"
 stroke="black" fill="lightpink" stroke-width="5"/>

#The following text is for the "25CM" at the bottom of the shape
<text x="490" y="270" fill="black">25CM</text>

#### The following polygon is for the pink triangle in the left
<polygon points = "300 100 100 100 300 230"
 stroke="black" fill="hotpink" stroke-width="5"/>
    
#The following text is for the "35CM" at the top of the shape
<text x="215" y="145" fill="black" >35CM</text>    

</svg>

Now, we'll calculate for the triangle at the bottom left:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>   

#### The following rectangle is for the red square at the top
<rect x="400" y="50" width="50" height="50" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "9CM" at the top of the shape
<text x="412" y="80" fill="black">9CM</text>

#### The following polygon is for the pink triangle at the bottom
<polygon points = "450 300 450 200 650 300"
 stroke="black" fill="lightpink" stroke-width="5"/>

#The following text is for the "25CM" at the bottom of the shape
<text x="490" y="270" fill="black">25CM</text>

#### The following polygon is for the pink triangle in the left
<polygon points = "300 100 100 100 300 230"
 stroke="black" fill="hotpink" stroke-width="5"/>
    
#The following text is for the "35CM" at the top of the shape
<text x="215" y="145" fill="black" >35CM</text>  

#### The following polygon is for the pink triangle in the left
<polygon points = "300 230 200 300 300 300"
 stroke="black" fill="deeppink" stroke-width="5"/>

#The following text is for the "4cm" at the bottom of the shape
<text x="245" y="320" fill="black">4cm</text>

#The following text is for the "3cm" at the left side of the shape
<text x="310" y="250" fill="black" transform="rotate(90 310,250)">3cm</text> 

#The following text is for the "5cm" at the left side of the shape
<text x="240" y="265" fill="black" transform="rotate(-40 240,265)">5cm</text>

</svg>

It's your turn to try some of what you've learned. Calculate the area of the <span style="color:deeppink">**pink triangle**</span>:

#Used to ensure the description text doesn't get cut off.
style = {'description_width': 'initial'}

#Create an input integer widget
question7 = widgets.IntText(
    value=None,
    description='Input your area here: ',
    disabled=False,
    style = style
    )

#Create a button titled "Check Answer"
checkButton7 = widgets.Button(description = "Check Answer")

def checkAnswer(a):
    #questionAnswer will be the input given by the user.
    questionAnswer = question7.value
    
    #answers is a list of possible answers that can be inputted. 
    answers = [6]
    
    #Check if the input is in the list of answers. If this is the case:
    if (questionAnswer in answers):
        #Clear the output
        clear_output()
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give an explenation for the answer.
        display(Markdown("Well done! <br> \
                         We get this answer by using the formula: <br> \
                         <h3 align='center'>$ ($Length$ × $Height$) ÷ 2 = $ Area </h3> <br> \
                         To get: <br> \
                         <h3 align='center'>$ (4$cm$ × 3$cm$) ÷ 2 = 6$cm$^2$</h3> <br> \
                         We will say that the value of $T$ is $6$cm."))
        
    #Otherwise, if no answer has been given, do nothing.
    elif (questionAnswer == 0):
        None
    
    #Lastly, if the answer is wrong, give the user a hint.
    else:
        #Clear the output
        clear_output()
        
        #Display the input integer and check button widgets
        display(question7)
        display(checkButton7)
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give a hint for the question
        display(Markdown("Not quite. <br> \
                      Remember, the formula for finding the area of a triangle is: <br> \
                      <h3 align='center'>$ ($Length$ × $Height$) ÷ 2 = $ Area </h3> "))

display(question7)
display(checkButton7)

checkButton7.on_click(checkAnswer)

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="salmon" stroke-width="5"/>   

#### The following rectangle is for the red square at the top
<rect x="400" y="50" width="50" height="50" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "9CM" at the top of the shape
<text x="412" y="80" fill="black">9CM</text>

#### The following polygon is for the pink triangle at the bottom
<polygon points = "450 300 450 200 650 300"
 stroke="black" fill="lightpink" stroke-width="5"/>

#The following text is for the "25CM" at the bottom of the shape
<text x="490" y="270" fill="black">25CM</text>

#### The following polygon is for the pink triangle in the left
<polygon points = "300 100 100 100 300 230"
 stroke="black" fill="hotpink" stroke-width="5"/>
    
#The following text is for the "35CM" at the top of the shape
<text x="215" y="145" fill="black" >35CM</text>  

#### The following polygon is for the pink triangle in the left
<polygon points = "300 230 200 300 300 300"
 stroke="black" fill="deeppink" stroke-width="5"/>

#The following text is for the "T" at the bottom of the shape
<text x="260" y="285" fill="black">T</text>

</svg>

Now, the last area you will have to find is that of a **rectangle**:

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="orange" stroke-width="5"/>   

#The following text is for the "10cm" at the right side of the shape
<text x="645" y="215" fill="black" transform="rotate(-90 645,215)">10cm</text>

#The following text is for the "19cm" at the bottom of the shape
<text x="450" y="320" fill="black">19cm</text>

#### The following rectangle is for the red square at the top
<rect x="400" y="50" width="50" height="50" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "9CM" at the top of the shape
<text x="412" y="80" fill="black">9CM</text>

#### The following polygon is for the pink triangle at the bottom
<polygon points = "450 300 450 200 650 300"
 stroke="black" fill="lightpink" stroke-width="5"/>

#The following text is for the "25CM" at the bottom of the shape
<text x="490" y="270" fill="black">25CM</text>

#### The following polygon is for the pink triangle in the left
<polygon points = "300 100 100 100 300 230"
 stroke="black" fill="hotpink" stroke-width="5"/>
    
#The following text is for the "35CM" at the top of the shape
<text x="215" y="145" fill="black" >35CM</text>   

#### The following polygon is for the pink triangle in the left
<polygon points = "300 230 200 300 300 300"
 stroke="black" fill="deeppink" stroke-width="5"/>

#The following text is for the "T" at the bottom of the shape
<text x="260" y="285" fill="black">T</text>
    

</svg>

To find the area of a rectangle, multiply *the height of the rectangle by the length*:

<h3 align='center'>$\rm (Length) \times (Height) = Area $</h3>

You must calculate the area of the <span style="color:orange">**orange rectangle**</span>:

#Used to ensure the description text doesn't get cut off.
style = {'description_width': 'initial'}

#Create an input integer widget
question8 = widgets.IntText(
    value=None,
    description='Input your area here: ',
    disabled=False,
    style = style
    )

#Create a button titled "Check Answer"
checkButton8 = widgets.Button(description = "Check Answer")

def checkAnswer(a):
    #questionAnswer will be the input given by the user.
    questionAnswer = question8.value
    
    #answers is a list of possible answers that can be inputted. 
    answers = [190]
    
    #Check if the input is in the list of answers. If this is the case:
    if (questionAnswer in answers):
        #Clear the output
        clear_output()
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give an explenation for the answer.
        display(Markdown("Well done! <br> \
                         We get this answer by using the formula: <br> \
                         <h3 align='center'>$\ ($Length$) × ($Height$) = $ Area</h3> <br> \
                         To get: <br> \
                         <h3 align='center'>$ (19$cm$) × (10$cm$) = 190$cm$^2 $</h3> <br> \
                         We will say that the value of $R$ is $190$cm$^2$."))
        
    #Otherwise, if no answer has been given, do nothing.
    elif (questionAnswer == 0):
        None
    
    #Lastly, if the answer is wrong, give the user a hint.
    else:
        #Clear the output
        clear_output()
        
        #Display the input integer and check button widgets
        display(question8)
        display(checkButton8)
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give a hint for the question
        display(Markdown("Not quite. <br> \
                      Remember, the formula for finding the area of a rectangle is: <br> \
                      <h3 align='center'>$\ ($Length$) × ($Height$) = $Area </h3>"))

display(question8)
display(checkButton8)

checkButton8.on_click(checkAnswer)

%%html
<svg height="550" width="1500">

<polygon points = "200 300 450 300 450 200 650 300 650 100 450 100 450 50 400 50 400 100 100 100 300 230"
 stroke="black" fill="orange" stroke-width="5"/>

#The following text is for the "R" at the center of the shape
<text x="465" y="200" fill="black">R</text>
    
#### The following rectangle is for the red square at the top
<rect x="400" y="50" width="50" height="50" stroke="black" fill="red" stroke-width="5"/>

#The following text is for the "9CM" at the top of the shape
<text x="412" y="80" fill="black">9CM</text>

#### The following polygon is for the pink triangle at the bottom
<polygon points = "450 300 450 200 650 300"
 stroke="black" fill="lightpink" stroke-width="5"/>

#The following text is for the "25CM" at the bottom of the shape
<text x="490" y="270" fill="black">25CM</text>

#### The following polygon is for the pink triangle in the left
<polygon points = "300 100 100 100 300 230"
 stroke="black" fill="hotpink" stroke-width="5"/>
    
#The following text is for the "35CM" at the top of the shape
<text x="215" y="145" fill="black" >35CM</text>    

#### The following polygon is for the pink triangle in the left
<polygon points = "300 230 200 300 300 300"
 stroke="black" fill="deeppink" stroke-width="5"/>

#The following text is for the "T" at the bottom of the shape
<text x="260" y="285" fill="black">T</text>

</svg>

Finally, it's up to you to *calculate the area of the whole shape*! To do this, you have to:

> **Add the Areas of the Shapes Inside** <br>
NOTE: We only add the areas of shapes that are inside our original shape. So, for this example, we would not add the <span style="color:pink">**pink triangle**</span> on the bottom right.

> **Subtract the Areas of the Shapes That are Holes** <br>
NOTE: We only subtract the areas of shapes that are not inside our original shape. So, for this example, we would subtract the <span style="color:pink">**pink triangle**</span> on the bottom right.

Calculate the area of the whole shape:

#Used to ensure the description text doesn't get cut off.
style = {'description_width': 'initial'}

#Create an input integer widget
question9 = widgets.IntText(
    value=None,
    description='Input your area here: ',
    disabled=False,
    style = style
    )

#Create a button titled "Check Answer"
checkButton9 = widgets.Button(description = "Check Answer")

def checkAnswer(a):
    #questionAnswer will be the input given by the user.
    questionAnswer = question9.value
    
    #answers is a list of possible answers that can be inputted. 
    answers = [215]
    
    #Check if the input is in the list of answers. If this is the case:
    if (questionAnswer in answers):
        #Clear the output
        clear_output()
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give an explenation for the answer.
        display(Markdown("Well done! <br> \
                         We get this answer by first *adding the areas of the shapes inside*: <br> \
                         <h3 align='center'>$\ (9$cm$^2) + (35$cm$^2) + (6$cm$^2) + (190$cm$^2) \
                         = 240$cm$^2 $</h3> <br> \
                         Then, we *subtract the areas of the shapes that are holes*: <br> \
                         <h3 align='center'>$ (240$cm$^2) - (25$cm$^2) = 215$cm$^2 $</h3> <br> \
                         So, the area of our original shape is $217$cm$^2$."))
        
    #Otherwise, if no answer has been given, do nothing.
    elif (questionAnswer == 0):
        None
    
    #Lastly, if the answer is wrong, give the user a hint.
    else:
        #Clear the output
        clear_output()
        
        #Display the input integer and check button widgets
        display(question9)
        display(checkButton9)
        
        #Let the user know what they inputed.
        display(Markdown("You answered: $" + str(questionAnswer) + "$"))
        
        #Give a hint for the question
        display(Markdown("Not quite. <br> \
                      Remember, to find the area of a shape like this we start by: <br> \
                      1) *Adding the areas of the shapes inside* and, <br> \
                      2) *Subtracting the areas of the shapes that are holes*."))

display(question9)
display(checkButton9)

checkButton9.on_click(checkAnswer)

## Conclusion:

In this notebook, you will have learned:

* How to find the **perimeter** of *quadrilaterals* and *triangles*.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)