![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/ParallelogramArea/parallelogram-area.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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

!pip install --upgrade --force-reinstall --user git+git://github.com/callysto/nbplus.git#egg=geogebra\&subdirectory=geogebra

from importlib import reload
import site
reload(site)

from geogebra.ggb import *
ggb = GGB()

from IPython.display import Image

import ipywidgets as widgets
import IPython

# Parallelogram: Area

#### Grade 7 Curriculum

This is a notebook on how to calculate the area of a parallelogram. In this notebook, we will focus on how to calculate the area of any parallelogram. We will also learn how to find out the length of one variable, either base or height, when given the other variable and the area. 

This notebook will help you understand how to find the area of a parallelogram, and give a few practice questions. This one notebook won’t be enough practice to master this skill, so you'll need to do lots of practice. A parallelogram is a special type of *quadrilateral* -- a shape with four sides. There are many different types of quadrilateral, as shown below:

![pic](http://www.mathwords.com/q/q_assets/q12.gif) www.mathwords.com

### Recall what a Parallelogram is

A parallelogram is a four-sided shape where both pair of sides are parallel, like this:

![picture](https://www.mathsisfun.com/images/quadrilateral-parallelogram.gif) www.mathisfun.com

**It's also important to note that a rectangle and a square are also types of parallelograms.**

### How to find the area

Since we know a rectangle is a type of parallelogram, let's recall the area of a rectangle: $$\text{base} \times \text{height}$$
Can we use this formula for all parallelograms? Actually, yes we can! This is because of the fact that parallelograms have parallel sides.

![animation](https://upload.wikimedia.org/wikipedia/commons/2/27/Parallelogram_area_animated.gif) wikimedia.org

### What about skewed parallelograms?

Certain parallelograms are so skewed that they do not resemble a rectangle with a triangle on either end like the one above. However, the same area formula applies.

The applet below automatically calculates the area of the parallelogram shown. You can move the sliders to change the length and height, and you can also move the point $P$ to change how skewed the parallelogram is. Notice how the area changes when you change the base or height, but not when you move the point $P$.

ggb.material('YFS3rJVz').draw()

It turns out all parallelograms have the same formula for area, no matter what angle their sides are at. 

### Example

Let's go through an example. Here is a parallelogram. What is its area?

Image('images/ParaStep1.png',width=400,height=500)

Let's dissect this parallelogram using two vertical lines. Then let's move the triangles inwards to create a rectangle.

Image('images/ParaStep2.png',width=400,height=500)

Image('images/ParaStep3.png',width=400,height=500)

Now we can see that the area of this parallelogram can be calculated like the area of a rectangle:
$$\begin{align*}
\text{Area of parallelogram} & = \text{Area of rectangle}\\
\text{Area of parallelogram} & = \text{base} \times \text{height}\\
\text{Area of parallelogram} & = 2 \text{ cm} \times 3 \text{ cm}\\
\text{Area of parallelogram} & = 6 \text{ cm}^2
\end{align*}$$

For one last check, slide point $P$ forward and back, perhaps lining up with the height line, to confirm that the parallelogram can be turned into a rectangle without changing how much area is there.

ggb.file('ParaEx.ggb').draw()

### Calculate Area

Let's try a few examples. Don't forget the formula:

$$\text{Area of parallelogram} = \text{base} \times \text{height}$$

**Note:** if units are given for the lengths of the two sides, then you should include units in your answer for area! Remember that area is given in square units, like $\text{cm}^2$ or $\text{m}^2$. You can include units in your answer by typing `cm^2` or `m^2`. Round to 2 decimal places.

### Question 1

Image('images/ParaQ1.png',width=400,height=500)

ans = widgets.Text(value='',placeholder='0',description='Area=',continuous_update=False)

def display():
    print("What is the area of this parallelogram?")
    IPython.display.display(ans)

def check(a):
    IPython.display.clear_output(wait=True)
    display()
    if ans.value == '8.84m^2' or ans.value == '8.84 m^2':
        print("Great job!")
    else:
        if ans.value == '':
            pass
        if ans.value == '8.84':
            print("Don't forget units! Remember that area is given in square units.")
            print("You can include units in your answer by typing cm^2, m^2, or mm^2.")
        else:
            print("Not quite, don't forget the formula. Area = base x height")

display()
ans.observe(check, 'value')

Image('images/ParaQ2.png',width=300,height=300)

ans2 = widgets.Text(value='',placeholder='0',description='Area=',continuous_update=False)

def display2():
    print("What is the area of this parallelogram?")
    IPython.display.display(ans2)

def check2(a):
    IPython.display.clear_output(wait=True)
    display2()
    if ans2.value == '1.61mm^2' or ans2.value == '1.61 mm^2':
        print("Great job!")
    else:
        if ans2.value == '':
            pass
        if ans2.value == '1.61':
            print("Don't forget units! Remember that area is given in square units.")
            print("You can include units in your answer by typing cm^2, m^2, or mm^2.")
        else:
            print("Not quite, don't forget the formula.")

display2()
ans2.observe(check2, 'value')

### How does changing the base change the area?

Let's take the first parallelogram from the example we went through where the base is 2 cm and the height is 3 cm which we figured out the area is $6 cm^2$. What do you think would happen to the area if we doubled the base to 4 cm? 
Let's calculate it:
$$\begin{align*}
\text{Area of parallelogram} & = \text{base} \times \text{height}\\
\text{Area of parallelogram} & = 4 \text{ cm} \times 3 \text{ cm}\\
\text{Area of parallelogram} & = 12 \text{ cm}^2
\end{align*}$$

Interesting. The new area, $12 \text{ cm}^2$ is double the amount of the old area, $6.8 \text{ cm}^2$. Perhaps that was just a coincidence? There's a slider over the next parallelogram labelled base, slide it to double the current base length and look at what happens to the area. Can we generalize that when the base is doubled then the area is doubled?

### How does changing the height change the area?

Now instead of changing the base, let's double the height of the parallelogram in the first example to 6 cm and keep the base at 2 cm. How will this new area compare to the old area? How will it compare to the area when we changed the base?
Let's calculate it:
$$\begin{align*}
\text{Area of parallelogram} & = \text{base} \times \text{height}\\
\text{Area of parallelogram} & = 6 \text{ cm} \times 2 \text{ cm}\\
\text{Area of parallelogram} & = 12 \text{ cm}^2
\end{align*}$$

Look at that! This new area is the same as when we doubled the base! Let's confirm that doubling the height doubles the area by using the slider labelled height over the parallelogram below to double the height and watch what happens to the area.

**Note:** you can slide P back and forth to create differently skewed parallelograms, including a rectangle, or even a square if you choose the same base length and height.

ggb.material('YFS3rJVz').draw()

### What conclusion can we draw?

By trying different values for base and height of the parallelogram above, we can safely conclude that doubling the base or doubling the height will double the area. 

Let's extend this conclusion: 
>What would happen to the area if the base or the height were halved?

Go back to the parallelogram above and try it!

## Practice

Lets use what you've learned to answer these questions:

#### Question 1

What is the area of a parallelogram with a base length of 3.2 m and a height of 4 m?

#### Question 2

What is the area of the parallelogram in question 1 if the height is halved?

#### Question 3

What is the area of the parallelogram in question 1 if the base is halved and the height is doubled?

### What if you know the area, but not one of the variables?

Let's say you know the area and the base, but are asked for the height, or you know the area and the height, but are asked for the base. How can we find these missing variables? Look at this example below. What is the height of the parallelogram?

Image('images/ParaQ3.png',width=300)

Let's look at the formula: $$ \text{Area of parallelogram} = \text{base} \times \text{height}$$

Now let's plug in all the values we know into the formula: $$10 \text{ mm}^2 = 2.5 \text{ mm} \times \text{height}$$

This looks a lot different than when all the numbers we know are on one side of the equals sign, so let's solve this equation for $height$ which will put all the numbers on one side of the equals sign and $height$ will be the only thing on the other side of the equals sign. 

*Don't forget, to keep the meaning of the equation the same, any operation you do on one side, you must do it to the other.*

$$ \begin{align*}
10 \text{ mm}^2 & = 2.5 \text{ mm} \times \text{height}\\
10 \text{ mm}^2 \div 2.5 \!\!\!\!\diagup \text{ mm} & = 2.5 \!\!\!\!\diagup \text{ mm} \times \text{height} \tag{divide by 2.5 mm to cancel multiplication}\\[4pt]
10 \text{ mm}^2 \div 2.5 \text{ mm} & = \text{height} \tag{Solve}\\[4pt]
10 \text{ mm}^2\!\!\!\!\!\diagup \div 2.5 \text{ mm}\!\!\!\!\!\diagup & = \text{height} \tag{cancel units}\\
4 \text{ mm} & = \text{height}
\end{align*}$$

At the step with the comment "Solve" on it, that step actually shows us the formula for height when you know the base and area. Let's remove the values from that step to see what the formula is in general: $$\frac{\text{Area of parallelogram}}{\text{base}} = \text{height}$$

This can also be written with height on the left and the formula on the right: $$\text{height} = \frac{\text{Area of parallelogram}}{\text{base}}$$

### What about the other way?

We can do the same thing if we know the height and not the base! What is the base length of this parallelogram?

Image('images/ParaQ4.png',width=200)

Let's use the same steps as the last example to solve this one.

*Don't forget, to keep the meaning of the equation the same, any operation you do on one side, you must do it to the other.*

$$\begin{align*}
\text{Area of parallelogram} & = \text{base} \times \text{height}\\
35 \text{ cm}^2 & = \text{base} \times 4 \text{ cm} \tag{plug in values}\\[4pt]
35 \text{ cm}^2 \div 4 \text{ cm} & = \text{base} \times 4 \!\!\!\!\diagup \text{ cm} \div 4 \!\!\!\!\diagup \text{ cm} \tag{divide by 4 to cancel out the multiplication}\\[4pt]
35 \text{ cm}^2 \div 4 \text{ cm} & = \text{base} \tag{Solve}\\[4pt]
35 \text{ cm}^2\!\!\!\!\diagup \div 4 \text{ cm}\!\!\!\!\diagup & = \text{base} \tag{cancel units}\\
8.75 \text{ cm} & = \text{base}
\end{align*}$$

Now let's get the general formula from the "Solve" step: $$\frac{\text{Area of parallelogram}}{\text{height}} = \text{base}$$

we can also write this with base on the left and the formula on the right: $$\text{base} = \frac{\text{Area of parallelogram}}{\text{height}}$$

### Practice Questions

Try to figure out the values of the missing base or height. 

##### Question 1
What is the base length of this parallelogram?

Image('images/ParaQ5.png',width=300)

ans3 = widgets.Text(value='',placeholder='0',description='Base=',continuous_update=False)

def display3():
    print("What is the base length of this parallelogram?")
    IPython.display.display(ans3)

def check3(a):
    IPython.display.clear_output(wait=True)
    display3()
    if ans3.value == '2.5 m' or ans3.value == '2.5m':
        print("Great job!")
    else:
        if ans3.value == '':
            pass
        if ans3.value == '2.5':
            print("Don't forget units! Remember that area is given in square units.")
            print("You can include units in your answer by typing cm^2, m^2, or mm^2.")
        else:
            print("Not quite, don't forget the formula.")

display3()
ans3.observe(check3, 'value')

##### Question 2
What is the height of this parallelogram?

Image('images/ParaQ6.png',width=700)

ans4 = widgets.Text(value='',placeholder='0',description='Height=',continuous_update=False)

def display4():
    print("What is the height of this parallelogram?")
    IPython.display.display(ans4)

def check4(a):
    IPython.display.clear_output(wait=True)
    display4()
    if ans4.value == '0.5 cm' or ans4.value == '0.5cm':
        print("Great job!")
    else:
        if ans4.value == '':
            pass
        if ans4.value == '0.5':
            print("Don't forget units! Remember that area is given in square units.")
            print("You can include units in your answer by typing cm^2, m^2, or mm^2.")
        else:
            print("Not quite, don't forget the formula.")

display4()
ans4.observe(check4, 'value')

## Conclusion

Let's review what we've learned in this notebook.

- The area of a parallelogram is the same as the area of a rectangle with the same base and height.
- The formula is $\text{Area} = \text{base} \times \text{height}$
- The formula works for all types of parallelograms as long as you know base and height.
- The formula works for finding any variable that is missing by rearranging values on either side of the equals sign.

Take the time to learn this formula and how to fill it in. You may not always have the formula to read, but filling in and manipulating equations like this formula will be essential for many math skills in the future. As always in mathematics, the more you practice, the easier it gets!

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)