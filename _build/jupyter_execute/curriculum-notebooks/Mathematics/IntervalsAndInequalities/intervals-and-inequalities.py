![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/IntervalsAndInequalities/intervals-and-inequalities.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

from IPython.display import display, Math, Latex, Markdown, HTML, clear_output, Javascript
HTML('''<script>
  function code_toggle() {
    if (code_shown){
      $('div.input').hide();
      $('#toggleButton').val('Show Code')
    } else {
      $('div.input').show();
      $('#toggleButton').val('Hide Code')
    }
    code_shown = !code_shown
  }

  $( document ).ready(function(){
    code_shown=false;
    $('div.input').hide()
  });
</script>
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form''')

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, Math, Latex, Markdown, HTML, clear_output, Javascript
import matplotlib as mpl
import ipywidgets as widgets
from ipywidgets import interact, interactive, Layout, Label,interact_manual,Text, HBox
from ipywidgets import IntSlider as slid
import time
import matplotlib.image as mpimg
from ipywidgets import IntSlider

# Intervals and inequalities

In this notebook, we will review some basics about polynomial functions such as
- the general form of a polynomial
- what terms make up a polynomial
- what defines the degree or order of a polynomial

We will then examine solving inequalities involving polynomials of degree 3 or less, both analytically and graphically, and briefly look over how to display the solutions on a number line, and how to represent solutions in interval notation. 

Finally, we will visualize how changing certain parameters of polynomials can change the shape of its graph, which results in a different interval, satisfying a given inequality.

At the end of this notebook, there will be a small section covering some basics of  `python` syntax and coding. This optional section will show the user how to create simple plots of polynomials in `python`, which can be used to help solve some of the extra problems.

## Polynomials


A polynomial is a function comprised of constants and variables. The constants and variables can be related to each other  by addition, multiplication and exponentiation to a non-negative integer power ( https://en.wikipedia.org/wiki/Polynomial ). In this notebook, we will let $P(x)$ denote a general polynomial, and we will only deal with polynomials of a single variable $x$. 

In general, a polynomial is expressed as:

$P(x) = c_0 \,  + \,c_1x \,  + ... +\,  c_{n-2}x^{n-2} +  c_{n-1}x^{n-1} + c_nx^n = \sum^n_{k=0}c_kx^k$

where $c_k$ are *constant terms*, $x$ is the variable. The largest value of $n$ ( i.e. the largest exponent of the polynomial) determines the *degree* of the polynomial. For example, some polynomials of degree *three* ($n=3$) could be:</br>

$P(x) = x^3 + 2x^2 + 5x + 4$

$P(x) = 3x^3 + 8x $

$P(x) = x^3 + x^2 + 4$

Note how the number of terms **does not** affect the degree of the polynomial, only the value of the largest exponent does. 

A polynomial with degree 0 is called a *constant polynomial*, or just a *constant*. This is because of the mathematical identity

$x^0 = 1$,

so if we have any polynomail of degree 0, we have

$P(x) = c_1x^0 + c_2 = c_1 + c_2 = C$,

which of course is just a constant (i.e. some number, $C$).

While we will only be dealing with singe variable polynomials, it is worth noting that they can exist with *multiple variables*, i.e.

$P(x,y,z) = x^3 - xy^2 + z^6 -3x^2y^6z^4 +2$


#display(Latex('...')) will print the string in the output cell, in a nice font, and allows for easily inputing Math symbos and equations
display(Latex('From the list of functions below, check which ones are polynomials:'))

#define a series of checkboxes to test knowledge of  polynomial forms

style = {'description_width': 'initial'}

a=widgets.Checkbox(
#    description= '$\ x^2+5x-8x^3$',
    description= r'$x^2$'+r'$+5x$'+r'$-8x^3$',
    value=False, #a false value means unchecked, while a checked value will be "True'" 
    style = style
)

b=widgets.Checkbox(
    value=False,
    description=r'$x$'+r'$+3$',
 #  description=r'$\ x+3$',
    style = style
)
c=widgets.Checkbox(
    value=False,
 #   description=r'$\ \sin(x) + \cos(x)$',
    description=r'$\sin$'+'('+r'$x$'+')'+r'$+\cos$'+'('+r'$x$'+')',  
    style = style
    
)
d=widgets.Checkbox(
    value=False,
#    description=r'$\ x^5-2$',
    description=r'$x^5$'+r'$-2$',
    disabled=False,
    style = style
)

e=widgets.Checkbox(
    value=False,
#    description=r'$\ \ln(x)$',
    description=r'$\ln$'+r'$(x)$',
    disabled=False,
    style = style
)

f=widgets.Checkbox(
    value=False,
#    description= r'$\ 100$',
    description= r'$100$',
    disabled=False,
    style = style
)

#to actually display the buttons, we need to use the IPython.display package, and call each button as the argument
display(a,b,c,d,e,f)

#warning
text_warning = widgets.HTML()

#create a button widget to check answers, again calling the button to display
button_check = widgets.Button(description="Check Answer")
display(button_check)


#a simple funciton to determine if user inputs are correct
def check_button(x):
    if a.value==True and b.value==True and c.value==False and d.value==True and e.value==False and f.value==True: #notebook will display 'correct'  message  IF (and only if) each of the boxes satisfy these value conditions 
         text_warning.value="Correct - these are all polynomials! Let's move on to the next cell."
    else: #if any of the checkboxes have the incorrect value, output will ask user to try again
         text_warning.value="Not quite - either some of your selections aren't polynomials, or some of the options that you didn't select are. Check your answers again!"

button_check.on_click(check_button)

display(text_warning)

## Intervals of Inequalities

### Interval Notation


Interval notation is a way of representing an interval of numbers by the two endpoints of the interval. Parentheses (  ) and brackets [  ] are used to represent whether the end points are included in the interval or not.  


For example, consider the interval between $-3$ and $4$, including $-3$, but **not** including $4$, i.e. $-3 \leq x < 4$. We can represent this on a number line as follows:

![intvl1.png](images/intvl1.png)

In **interval notation**, we would simply write: $[-3,4)$

If, however, the interval extended from $-3$ to **all** real numbers larger than $-3$, i.e. $-3 \leq x$, the number line would look like this:

![intvl2.png](images/intvl2.png)

and our interval notation representation would be: $[-3, \infty)$, where $\infty$ (infinity) essentially means all possible numbers beyond this point.

Sometimes it is also necessary to include multiple intervals. Consider an inequality in which the solution is $-3\leq x <0$ and $4 \leq x$. We can represent this solution in interval notation with the **union** symbol, which is just a capital U, and means that both intervals satisfy the inequality: $[-3,0)$ U $[4,\infty)$

### Solving Inequalities

Given a polynomial $P(x)$, we can determine the range in which that polynomial satisfies a certain inequality. For example, consider the polynomial function

$P(x) = x^2 + 4x$.

For which values of $x$ is the ploynomial $P(x)$ less than three? Or, in a mathematical representations, on which interval is the inequality $P(x) \leq -3$ satisfied?

We can solve this algebraically, as follows:

1. Write the polynomial in standard form:   $x^2 + 4x + 3 \leq 0 $
    
2. Factor the polynomial:   $(x+1)(x+3) \leq 0$

What this new expression is essential telling us is that the product of two numbers (say $a=(x+1)$ and $b=(x+3)$) is equal to zero, or negative, i.e. $a\cdot b\leq 0 $. The only way this is possible is if $a=0$, $b=0$, or $a$ and $b$ have **opposite** signs. So the inequality $P(x) \leq -3$ is satisfied if:

- $(x+1) = 0$
- $(x+3) = 0$
- $(x+1)>0$ and $(x+3)<0$
- $(x+1)<0$ and $(x+3)>0$

From these possibilities, we can see the possible solutions are:

- $x=-1$
- $x=-3$
- $x>-1$ and $x<-3$
- $x<-1$ and $x>-3$
 
If we consider the solution $x>-1$ and $x<-3$, what are the possible values of $x$? If we say $x=1$ we satisfy the first inequality, but not the second, since $1$ is **not** less than $-3$. We can see that there is no possible $x$ value that will result in  $(x+1)>0$ and $(x+3)<0$, so we can eliminate this as a possible solution.

However, we can find values of $x$ that satisfy $x<-1$ and $x>-3$. For example, $x=-2$

Thus, the solution to the inequality is $x=-1$, $x=-3$, and $x<-1$ and $x>-3$. We can plot this solution set on a number line:

![ex1.png](images/ex1.png)


or in *interval notation*, the solution is : **[-3,-1]**

## Let's work through an example together

std_form1 = "-4x^2+8x+96<=0"

display(Latex('1.Consider the inequality $(-x)(4x - 8) \leq -96$.'))
display(Latex(' Re-write the inequality in standard form (use the symbol ^ to indicate an exponent and <= for the inequality sign).'))

inpt1 = widgets.Text(placeholder='Enter inequality')
text_warning1 = widgets.HTML()
button_check1 = widgets.Button(description="Check Answer")

display(widgets.HBox([inpt1,button_check1]))

def check_button1(x):
    inpt1.value = inpt1.value.replace(" ","")
    if inpt1.value==std_form1 :
        text_warning1.value="Very good!"
    else:
        text_warning1.value="Not quite - please try again!"

button_check1.on_click(check_button1)

display(text_warning1)

std_form2 = "x^2-2x-24>=0"
display(Latex('2.Consider the inequality we obtained in the first step.'))#: $-4x^2+8x+96\leq0$'))
display(Latex('We can simplify this further by reducing the leading coefficient to 1.'))
display(Latex('This can be done by simply dividing both sides by $-4$. If we do this, what does our expression become?'))

inpt2 = widgets.Text(placeholder='Enter inequality')
text_warning2 = widgets.HTML()
button_check2 = widgets.Button(description="Check Answer")

display(widgets.HBox([inpt2,button_check2]))

def check_button2(x):
    inpt2.value = inpt2.value.replace(" ","")
    if inpt2.value==std_form2 :
        text_warning2.value="Very good!"
    else:
        text_warning2.value="Almost! It's important to remember that if we divide or multiply an inequality by a negative number, we flip the inequality sign."

button_check2.on_click(check_button2)

display(text_warning2)

std_form3_1 = '(x-6)(x+4)>=0'
std_form3_2 = '(x+4)(x-6)>=0'
display(Latex('3.The next step is to factor our simplified polynomial expression.')) #: $x^2 - 2x - 24 \geq 0$.'))
display(Latex('Input the factored expression below:'))

inpt3 = widgets.Text(placeholder='Enter inequality')
text_warning3 = widgets.HTML()
button_check3 = widgets.Button(description="Check Answer")

display(widgets.HBox([inpt3,button_check3]))

def check_button3(x):
    inpt3.value = inpt3.value.replace(" ","")
    if inpt3.value==std_form3_1 or inpt3.value==std_form3_2:
        text_warning3.value="Correct!"
    else:
        text_warning3.value="Not quite - please try again!"

button_check3.on_click(check_button3)

display(text_warning3)

display(Latex('Since we have $(x-6)(x+4)\geq 0$, there are the two sign possibilities; either'))
display(Latex('$1. ~ (x-6)\geq 0$ and $(x+4)\geq 0$'))
display(Latex('or'))
display(Latex('$2. ~ (x-6)\leq 0$ and $(x+4)\leq 0$'))

std_form4 = 'x>=6'

display(Latex('4. Consider expression $1.$'))
display(Latex(' Can you see what solution satisfies both $(x-6)\geq 0$ and $(x+4)\geq 0$? Enter your answer below in the form "x>= _"'))

inpt4 = widgets.Text(placeholder='Enter interval')
text_warning4 = widgets.HTML()
button_check4 = widgets.Button(description="Check Answer")

display(widgets.HBox([inpt4,button_check4]))

def check_button4(x):
    inpt4.value = inpt4.value.replace(" ","")
    if inpt4.value==std_form4 :
        text_warning4.value="Very good! Since we are looking for values of x that are larger than 6 and -4, and 6>-4, the first expresssion gives us one simple solution interval: x>=6"
    else:
        text_warning4.value="Not quite - please try again!"

button_check4.on_click(check_button4)

display(text_warning4)

std_form5 = 'x<=-4'

display(Latex('5.Now consider expression $2$ What is the interval satsfying these inequalities?'))

inpt5 = widgets.Text(placeholder='Enter interval')
text_warning5 = widgets.HTML()
button_check5 = widgets.Button(description="Check Answer")

display(widgets.HBox([inpt5,button_check5]))

def check_button5(x):
    inpt5.value = inpt5.value.replace(" ","")
    if inpt5.value==std_form5 :
        text_warning5.value="Very good! Since we are looking for values of x that are less than -4 and 6 and 6>-4, this expresssion also gives us one simple solution interval: x<=-4"
    else:
        text_warning5.value="Not quite - please try again!"

button_check5.on_click(check_button5)

display(text_warning5)

std_form6 = '(-inf,-4]U[6,inf)'

display(Latex('6. So, what is our final solution interval for the inequality $(-x)(4x - 8) \leq -96$?'))
display(Latex("Enter your answer in interval notation, using the following notations if necessary: 'U' for union symbol and 'inf' for infinity"))
inpt6 = widgets.Text(placeholder='Enter interval')
text_warning6 = widgets.HTML()
button_check6 = widgets.Button(description="Check Answer")

display(widgets.HBox([inpt6,button_check6]))

def check_button6(x):
    inpt6.value = inpt6.value.replace(" ","")
    if inpt6.value==std_form6 :
        text_warning6.value="Excellent! Now let's see how the solution looks like on the number line"
    else:
        text_warning6.value="Not quite - please try again!"

button_check6.on_click(check_button6)

display(text_warning6)

button7 = widgets.Button(description="Display solution on  a number line",layout=Layout(width='40%', height='50px'))

display(button7)

def display_button7(x):
        img = mpimg.imread('images/ex_soln.png')
        fig, ax = plt.subplots(figsize=(18, 3))
        imgplot = ax.imshow(img,  aspect='auto')
        ax.axis('off')
        plt.show()
        button7.disabled=True

button7.on_click(display_button7)

## Graphical visualization of inequality solutions


%matplotlib inline

display(Latex('Click on the button below to graph the polynomial $P(x) = x^2 + 4x$'))

button_graph = widgets.Button(description="Graph the ploynomial")

display(button_graph)

def display_graph(t):
    x = np.linspace(-10,10,1000); #define a vector space for the variable x
    plt.figure(3,figsize=(11,8)) #define the figure window size
    plt.plot(x,x**2 + 4*x, linewidth=2, label=r'$P(x) = x^2 + 4x$'); #plot the polynomial as a function of x
    plt.ylabel('P(x)', fontsize=20) #label the axes
    plt.xlabel('x', fontsize=20)
    plt.grid(alpha = 0.7) #place a grid on the figure for readability; alpha defines the opacity
    plt.xticks(np.arange(-10,11)) #define the xticks for easier reading
    plt.ylim([-20,40]) #adjust the limits of the y and x axes of the figure for readability
    plt.xlim([-9,9])
    plt.plot([-75,75],[0,0],'k-',alpha = 1,linewidth = 1) #plot solid lines along origin for easier reading
    plt.plot([0,0],[-75,75],'k-',alpha = 1,linewidth = 1)
    plt.legend(loc='best', fontsize = 18) #add a legend 
    button_graph.disabled=True
    
button_graph.on_click(display_graph)

display(Latex("Let's try to solve where this polynomial is $\leq -3$, or  $x^2 + 4x \leq -3$."))
display(Latex("Let's draw a line at $y=-3$ to help visualize this."))

button_draw = widgets.Button(description="Draw a line")

display(button_draw)

def draw_line(t):
    x = np.linspace(-10,10,1000); #define a vector space for the variable x
    plt.figure(3,figsize=(11,8)) #define the figure window size
    plt.plot(x,x**2 + 4*x, linewidth=2, label=r'$P(x) = x^2 + 4x$'); #plot the polynomial as a function of x
    plt.ylabel('P(x)', fontsize=20) #label the axes
    plt.xlabel('x', fontsize=20)
    plt.grid(alpha = 0.7) #place a grid on the figure for readability; alpha defines the opacity
    plt.xticks(np.arange(-10,11)) #define the xticks for easier reading
    plt.ylim([-20,40]) #adjust the limits of the y and x axes of the figure for readability
    plt.xlim([-9,9])
    plt.plot([-75,75],[0,0],'k-',alpha = 1,linewidth = 1) #plot solid lines along origin for easier reading
    plt.plot(x,np.ones(len(x))*-3, linewidth=2, label = r'$y = -3$'); #plot the y=0 line
    plt.legend(loc='best', fontsize = 18) #add a legend
    button_draw.disabled=True
    
button_draw.on_click(draw_line)
    

display(Latex('Can you see where the inequality is satisfied?'))
display(Latex('Click the button to shade the area where the inequality is satisfied'))

button_shade = widgets.Button(description="Shade")

display(button_shade)

def shade(t):
    x = np.linspace(-10,10,1000); #define a vector space for the variable x
    plt.figure(3,figsize=(11,8)) #define the figure window size
    plt.plot(x,x**2 + 4*x, linewidth=2, label=r'$P(x) = x^2 + 4x$'); #plot the polynomial as a function of x
    plt.ylabel('P(x)', fontsize=20) #label the axes
    plt.xlabel('x', fontsize=20)
    plt.grid(alpha = 0.7) #place a grid on the figure for readability; alpha defines the opacity
    plt.xticks(np.arange(-10,11)) #define the xticks for easier reading
    plt.ylim([-20,40]) #adjust the limits of the y and x axes of the figure for readability
    plt.xlim([-9,9])
    plt.plot([-75,75],[0,0],'k-',alpha = 1,linewidth = 1) #plot solid lines along origin for easier reading
    plt.plot(x,np.ones(len(x))*-3, linewidth=2, label = r'$y = -3$'); #plot the y=0 line
    plt.legend(loc='best', fontsize = 18) #add a legend 
    plt.axvspan(-3,-1,facecolor='#2ca02c', alpha=0.5)
    display(Latex("We can see that the interval for which $P(x) \leq -3$ is again [-3,-1], agreeing with our algebraic solution."))
    button_shade.disabled=True
    
button_shade.on_click(shade)

## Changing Parameters

### Constant term

The **constant term** of a polynomial is the term in which the variable does not appear (i.e. the degree $0$ term). For example, the constant term for the polynomial 

$P(x) = x^3 + 2x^2 + 5x + 4$,</br>

is $4$.

Let's look at how changing the constant term changes the graph of the polynomial. We will consider the same polynomial as before, but this time we will let $k$ be an arbitrary value for the constant term. 

display(Latex('Adjust the value of $k$ using the slider. What do you notice about the graph as the value changes?'))

x = np.linspace(-10,10, 1000)

#define function to create a graph of a polynomial
def Plot_poly(k=0): #we make the python function a function of the variable 'k', which we will use as the constant term in the polynomial
    plt.figure(figsize=(11,8))
    plt.plot(x,x**3 + 2*x**2 + 5*x + k, linewidth = 2) #here is the variable k
    plt.title(r'Graph of $P(x) = x^3 + 2x^2 + 5x + k$', fontsize = 20)
    plt.ylabel('P(x)', fontsize=20)
    plt.xlabel('x', fontsize=20)
    plt.grid(alpha = 0.7) 
    plt.xticks(np.arange(-10,11))
    plt.ylim([-20,40])
    plt.xlim([-9,9])
    plt.plot([-75,75],[0,0],'k-',alpha = 1,linewidth = 1)
    plt.plot([0,0],[-75,75],'k-',alpha = 1,linewidth = 1)
    plt.show()
    
#interact(Plot_poly,k=(-10,10)); #use the IPython interact function to create a slider to adjust the value of 'k' for the plot

interact(Plot_poly, k=slid(min=-10,max=10,step=1,value=0,continuous_update=False))
#interact_manual(Plot_poly,k=widgets.IntSlider(min=-10,max=10,step=1,value=0))


display(Latex('Try doing the same with other polynomials. Is there a similar, or different behaviour?'))

display(Markdown('**Order 1 Polynomials:**'))
display(Latex('Provide a value for $a$ in the polynomial $P(x) = ax + k$:'))    

inpt_a = widgets.Text(placeholder='Enter a')
text_warning_a = widgets.HTML()
button_check_a = widgets.Button(description="Graph")

display(widgets.HBox([inpt_a,button_check_a]))
button_check_a.disabled=False
inpt_a.disabled=False


def check_button_a(b):
    inpt_a.value = inpt_a.value.replace(" ","")
    if inpt_a.value.isdigit():
        text_warning_a.value=""
        
        button_check_a.disabled=True
        inpt_a.disabled=True
        
        x = np.linspace(-10,10,1000)
        custom_poly = int(inpt_a.value)* x
        
        
        def plot_poly1(k=0): 
            plt.figure(figsize=(11,8))
            plt.plot(x,custom_poly + k, linewidth=2) #plot the polynomial with the constant term k 
            plt.ylabel('P(x)', fontsize=20)
            plt.xlabel('x', fontsize=20)
            plt.grid(alpha = 0.7) 
            plt.xticks(np.arange(-10,11))
            plt.ylim([-20,40])
            plt.xlim([-9,9])
            plt.plot([-75,75],[0,0],'k-',alpha = 1,linewidth = 1)
            plt.plot([0,0],[-75,75],'k-',alpha = 1,linewidth = 1)
            plt.title('Graph of polynomial $P(x) ='+str(inpt_a.value) + 'x+ k$', fontsize=20)
            plt.show()
        
        #interact(plot_poly1,k=(-10,10)); 
        interact(plot_poly1, k=slid(min=-10,max=10,step=1,value=0,continuous_update=False))
        
    else:
        text_warning_a.value="Please enter numeric value"

button_check_a.on_click(check_button_a)

display(text_warning_a)

display(Markdown('**Order 2 Polynomials:**'))
display(Latex('Provide values for $a$ and $b$ in the polynomial $P(x) = ax^2 +bx + k$ using format a,b:'))

inpt_ab = widgets.Text(placeholder='Enter a,b')
text_warning_ab = widgets.HTML()
button_check_ab = widgets.Button(description="Graph")

display(widgets.HBox([inpt_ab,button_check_ab]))
button_check_ab.disabled=False
inpt_ab.disabled=False


def check_button_ab(b):
    inpt_ab.value = inpt_ab.value.replace(" ","")
    list_ab = inpt_ab.value.split(',')
    if not len(list_ab)==2:
        text_warning_ab.value="Please enter two numbers in format a,b"
    else:
        if list_ab[0].isdigit() and list_ab[1].isdigit():
            text_warning_ab.value=""

            button_check_ab.disabled=True
            inpt_ab.disabled=True

            x = np.linspace(-10,10,1000)
            custom_poly = int(list_ab[0]) * x**2 + int(list_ab[1])*x


            def plot_poly2(k=0): 
                plt.figure(figsize=(11,8))
                plt.plot(x,custom_poly + k, linewidth=2) #plot the polynomial with the constant term k 
                plt.ylabel('P(x)', fontsize=20)
                plt.xlabel('x', fontsize=20)
                plt.grid(alpha = 0.7) 
                plt.xticks(np.arange(-10,11))
                plt.ylim([-20,40])
                plt.xlim([-9,9])
                plt.plot([-75,75],[0,0],'k-',alpha = 1,linewidth = 1)
                plt.plot([0,0],[-75,75],'k-',alpha = 1,linewidth = 1)
                plt.title('Graph of polynomial $P(x) ='+str(list_ab[0]) + 'x^2 +' + str(list_ab[1]) + 'x + k$', fontsize=20)
                plt.show()
            
            #interact(plot_poly2,k=(-10,10))
            interact(plot_poly2, k=slid(min=-10,max=10,step=1,value=0,continuous_update=False))


        else:
            text_warning_ab.value="Please enter numeric values"

button_check_ab.on_click(check_button_ab)

display(text_warning_ab)

display(Markdown('**Order 3 Polynomials:**'))
display(Latex('Provide values for $a$, $b$, and $c$ in the polynomial $P(x) = ax^3 +bx^2 + cx + k$ using format a,b,c:'))

inpt_abc = widgets.Text(placeholder='Enter a,b,c')
text_warning_abc = widgets.HTML()
button_check_abc = widgets.Button(description="Graph")

display(widgets.HBox([inpt_abc,button_check_abc]))
button_check_abc.disabled=False
inpt_abc.disabled=False


def check_button_abc(b):
    inpt_abc.value = inpt_abc.value.replace(" ","")
    list_abc = inpt_abc.value.split(',')
    if not len(list_abc)==3:
        text_warning_abc.value="Please enter three numbers in format a,b,c"
    else:
        if list_abc[0].isdigit() and list_abc[1].isdigit() and list_abc[2].isdigit():
            text_warning_abc.value=""

            button_check_abc.disabled=True
            inpt_abc.disabled=True

            x = np.linspace(-10,10,1000)
            custom_poly = int(list_abc[0]) * x**3 + int(list_abc[1])*x**2 + int(list_abc[2])*x


            def plot_poly3(k=0): 
                plt.figure(figsize=(11,8))
                plt.plot(x,custom_poly + k, linewidth=2) #plot the polynomial with the constant term k 
                plt.ylabel('P(x)', fontsize=20)
                plt.xlabel('x', fontsize=20)
                plt.grid(alpha = 0.7) 
                plt.xticks(np.arange(-10,11))
                plt.ylim([-20,40])
                plt.xlim([-9,9])
                plt.plot([-75,75],[0,0],'k-',alpha = 1,linewidth = 1)
                plt.plot([0,0],[-75,75],'k-',alpha = 1,linewidth = 1)
                plt.title('Graph of polynomial $P(x) ='+str(list_abc[0]) + 'x^3 +' + str(list_abc[1]) + 'x^2+'+ str(list_abc[2]) + 'x+ k$', fontsize=20)
                plt.show()
            
            #interact(plot_poly3,k=(-10,10)); 
            interact(plot_poly3, k=slid(min=-10,max=10,step=1,value=0,continuous_update=False))

        else:
            text_warning_abc.value="Please enter numeric values"

button_check_abc.on_click(check_button_abc)

display(text_warning_abc)

In the next exercise, we will quantify how the constant term can change the interval satisfying an inequality. 

**Note**: Please press the enter key after typing in a value for the intercepts. 

display(Latex("Where are the x intercepts for the polynomial $x^2-4x+3$?"))
    
#widgets for interactive cell input
guess1_in= widgets.Text(disabled = False, description = r'$x_1$')
guess2_in = widgets.Text(disabled = False, description = r'$x_2$')
check = widgets.Button(description = 'Check Answer')
change_c = widgets.Button(description = 'Change Constant')

text_warning_check = widgets.HTML()

display(guess1_in)
display(guess2_in)
display(check)

def check_answr(b):
    int_1 = str(1)
    int_2 = str(3)
    if (guess1_in.value == int_1 and guess2_in.value == int_2) or (guess1_in.value == int_2 and guess2_in.value == int_1):
        text_warning_check.value='Correct!'
        check.disabled=True
        guess1_in.disabled=True
        guess2_in.disabled=True
        plt.figure(1,figsize=(11,8))
        plt.plot(x,x**2  - 4*x + 3, linewidth=2, label=r'$P(x) = x^2 -4x+3$');
        plt.plot([-75,75],[0,0],'k-',alpha = 1,linewidth = 1)
        plt.plot([0,0],[-75,75],'k-',alpha = 1,linewidth = 1)
        plt.plot(3,0,'ro',markersize=10)
        plt.plot(1,0,'ro',markersize=10)
        plt.ylabel('P(x)', fontsize=20)
        plt.xlabel('x', fontsize=20)
        plt.grid(alpha = 0.7)
        plt.xticks(np.arange(-10,11))
        plt.ylim([-20,20])
        plt.xlim([-9,9])
        plt.legend(loc='best', fontsize = 18)
        plt.show()
        display(Latex('Based on the previous cell, what do you think will happen if we change the constant term from $3$ to $-3$? Press the button to find out if you are correct.'))
        display(change_c)
    else:
        text_warning_check.value='Try Again!'
    return

check.on_click(check_answr)
    
def change_const(b):
    change_c.disabled=True
    plt.figure(1,figsize=(11,8))
    plt.plot(x,x**2  - 4*x - 3, linewidth=2, label=r'$P(x) = x^2 -4x-3$');
    plt.plot([-75,75],[0,0],'k-',alpha = 1,linewidth = 1)
    plt.plot([0,0],[-75,75],'k-',alpha = 1,linewidth = 1)
    plt.plot(2-np.sqrt(7),0,'yo',markersize=10)
    plt.plot(2+np.sqrt(7),0,'yo', markersize=10)
    plt.ylabel('P(x)', fontsize=20)
    plt.xlabel('x', fontsize=20)
    plt.grid(alpha = 0.7)
    plt.xticks(np.arange(-10,11))
    plt.ylim([-20,20])
    plt.xlim([-9,9])
    plt.legend(loc='best', fontsize = 18)
    plt.show()
    display(Latex('As we can see, changing the constant term shifts the graph of a polynomial up or down. This results in different x-intercepts, and therefore a different interval. '))

change_c.on_click(change_const)  

display(text_warning_check)

Another way to think about this is that changing the constant term is the same as solving for a different interval of inequality. Take, for example the polynomials we just used above.

We know that 

$x^2-4x+3 \leq 0$ 

is **not** the same as 

$x^2-4x-3\leq 0$.

However, consider a new inequality:

$x^2 - 4x - 3 \leq -6$.

If we simplify this expression, we find

$x^2 - 4x +3 \leq 0$

which is indeed equivalent to the first polynomial (plotted in blue in the cell above).

## Extra Problems

### Practice solving graphically

First, we will practice how to solve inequalities graphically. Below is a plot of the polynomial $P(x) = x^3 - x^2 - 22x + 40$. Using the graph, find the values of the three x intercepts. Based on this, determine the interval where $P(x) \leq 0 $.

This can method can be used to solve almost any polynomial inequality, provided that the x-intercepts are rational numbers which can be easily read off of the axes of the graph.

text_check_intvl = widgets.HTML()
        
intvl_1=widgets.Checkbox(
        value=False, 
        description=r'$[$'+r'$-5$'+r'$,4$'+r'$]$', 
        disabled=False
        )
intvl_2=widgets.Checkbox(
            value=False,
            description='['+'$-5$'+'$,3$'+']'+'$U$'+'['+r'$4,$'+r'$\infty$'+r')',
            disabled=False
        )
intvl_3=widgets.Checkbox(
            value=False,
            description=r'$[$'+r'$-5$'+r'$,2$'+r'$]$',
            disabled=False
        )
intvl_4=widgets.Checkbox(
            value=False,
            description=r'$($'+r'$-\infty$'+r'$,$'+r'$-5$'+'$]$'+'$U$'+ r'$[$' + r'$2$'+'$,$'+'$4$'+'$]$',
            #description=r'$(-\infty,-5] \rm U [2,4]$',
            disabled=False
        )


def check_button2(x):
            if intvl_2.value == False and intvl_1.value==False and intvl_3.value==False and intvl_4.value==True:
                text_check_intvl.value='Correct!'

            else: 
                text_check_intvl.value="Not quite - Check your answer again!"

button_check2 = widgets.Button(description="Check Answer")
button_check2.on_click(check_button2)

def slider(x1,x2,x3):
    xx = np.linspace(-10,10,300)
    p1 = plt.figure(1,figsize = (11,8))
    hold = True
    plt.plot(xx,xx**3 - 1*xx**2 - 22*xx + 40, linewidth = 2, label = r'$P(x) = x^3 - x^2 - 22x + 40$')
    plt.axhline(y=0, color = 'k', linewidth=1)
    plt.axvline(x=0, color = 'k', linewidth=1)
    plt.plot(x1,0,'ro',markersize=10)
    plt.plot(x2,0,'mo',markersize=10)
    plt.plot(x3,0,'go',markersize=10)
    if sorted([x1,x2,x3]) == sorted([-5,2,4]):
        plt.text(-7,20,'VERY GOOD!', fontsize = 25, fontweight = 'bold',color = 'r')
        plt.fill_between(xx,xx**3 - 1*xx**2 - 22*xx + 40,np.zeros(len(xx)), where=xx**3 - 1*xx**2 - 22*xx + 40<0, interpolate = True, alpha=0.5, color='g' )
        display(Latex('What interval then satisfies $P(x) \leq 0$?'))

        display(intvl_1)
        display(intvl_2)
        display(intvl_3)
        display(intvl_4)
        display(button_check2)
        display(text_check_intvl)
        
    plt.xlabel('$x$',fontsize = 14)
    plt.ylabel('$y$',fontsize = 14)
    plt.grid(alpha = 0.7)
    plt.xticks(np.arange(-10,11))
    plt.ylim([-75,75])
    plt.xlim([-9,9])
    plt.legend(loc = 'best', fontsize = 18)
    plt.show()
    
interact(slider, x1=slid(min = -10,max = 10,step = 1,continuous_update = False), x2=slid(min = -10,max = 10,step = 1,continuous_update = False), x3=slid(min = -10,max = 10,step = 1,continuous_update = False))

### Solve the inequalities

In the next two cells, we have a function that will generate a random polynomial of degree 2 and 3. Using the analytic steps shown above, try to solve the intervals of inequalities for a few polynomials. Since we can always rearrange the polynomial into standard form, without loss of generality we can always take the inequality to be $\leq 0 $ or $\geq 0 $. Re-run this function as many times as you would like, until you are comfortable with solving polynomial inequalities.

If you have trouble solving the inequality analytically, you can try to find the solution graphically, following the method in the cell above. At the bottom of this notebook, there will be some instructions on how to make basic plots with Python. Follow these steps and try to solve the inequality.

**Note**: you will need to scroll to the top of the notebook and press the '**show code**' button to be able to write your own code in a cell.

def find_interval2():
        C = np.random.randint(-5,5,2)
        C1 = -1*np.sum(C)
        C2 = C[0]*C[1]
        if C1>0:
            str1 = '+' + str(C1) + 'x'
        elif C1== 0:
            str1 = ''
        else:
            str1=  str(C1) + 'x'
        if C2>0:
            str2 = '+' + str(C2)
        elif C2== 0:
            str2=''
        else:
            str2= str(C2) 

        a = 'P(x) = x^2 ' + str1 + str2

        def poly(x):
            return x**2 + C1*x + C2
    
        Max = max(C)
        Min = min(C)
        M = [Min, Max]
        V = np.sort(C)
        eps = 0.1
 
        if Max == Min and poly(Max+eps)>0:
                interval = '(-inf,'+str(Min)+')U('+str(Min)+',inf)' #one root, convex
        elif poly(Max+eps)<0:
                interval = '('+str(Min)+','+str(Max)+')' #Two distinct roots, Concave
        elif poly(Max + eps)>0:
                interval = '(-inf,'+str(Min)+')U(' + str(Max)+',inf)' #Two distinct roots, convex
        else:
                interval = 'Nowhere' #one root, concave 
    
        x = np.linspace(-100,100,10000)
        p = poly(x)
  
        y = poly(x)
        return interval,y,a

def find_interval3():
        C = np.random.randint(-5,5,3)
        C1 = -1*np.sum(C)
        C2 = C[0]*C[1] + C[2]*(C[0]+C[1])
        C3 = -1*C[0]*C[1]*C[2]
        if C1>0:
            str1 = '+' + str(C1) + 'x^2'
        elif C1== 0:
            str1 = ''
        else:
            str1=  str(C1) + 'x^2'
        if C2>0:
            str2 = '+' + str(C2) + 'x'
        elif C2== 0:
            str2=''
        else:
            str2= str(C2) + 'x'
        if C3>0:
            str3 = '+' + str(C3)
        elif C3== 0:
            str3=''
        else:
            str3= str(C3)
            
        a = "P(x)= x^3" + str1 + str2 + str3
        
        def poly(x):
            return x**3 + C1*x**2 + C2*x + C3
        
        Max = max(C)
        Min = min(C)
        M = [Min, Max]
        V = np.sort(C)
        eps = 0.1
    
        v = V[1]
        if Max == Min and poly(Max +eps) > 0:
                          interval = '('+str(Max)+',inf)' #One single root, increasing
        if Max == Min and poly(Max +eps) < 0:
                          interval = '(-inf,' + str( Max)+')' #One single root, decreasing
                      
        if poly(Max + eps) >0:
            if v !=  Max and v!= Min:
                          interval = '('+str(Min) + ',' + str(v) + ')U(' + str(Max) + ',inf)'
            if v == Max:
                          interval = '(' + str(Min) + ',inf)'
            if v== Min:
                          interval = '(' + str(Max) + ',inf)'
    
        if poly(Max + eps) <0:
            if v != Max and v != Min:
                          interval = '(-inf,' + str(Min) + 'U('+str(v) + ','+str(Max) + ')'
            if v == Max:
                          interval = '(-inf,' + str( Max) + ')'
            if v == Min:
                          interval = '(-inf,' + str(Min) + ')'
                    
        x = np.linspace(-100,100,10000)
        y = poly(x)
        return interval, y,a

def check_answer(answer,interval,y,a,hwidget):

    if answer == interval:
        
        hwidget.value="Correct! Here's a visualization of the solution:"
        x=np.linspace(-100,100,10000)
        plt.figure(figsize=(11,8))
        plt.plot(x,y, linewidth = 2, label = '$' + str(a) + '$')
        plt.xlabel('$x$',fontsize = 14)
        plt.ylabel('$y$',fontsize = 14)
        plt.axhline(y=0, color = 'k', linewidth=1)
        plt.axvline(x=0, color = 'k', linewidth=1)
        plt.grid(alpha = 0.7)
        plt.xticks(np.arange(-10,11))
        plt.ylim([-75,75])
        plt.xlim([-9,9])
        plt.legend(loc = 'best', fontsize = 18)
        plt.fill_between(x,y,0, where=y>0, interpolate=True, alpha = 0.5, color='g')
        return True
        
    elif answer != interval:
        hwidget.value="That's not quite right, try again." 
        return False

interval2,y_values2,polynom_string2=find_interval2()

display(Markdown('**Order 2 Polynomials:**'))
display(Latex("Find the interval where $P(x) > 0$ , using 'inf' for infinity and 'U' for union:"))
display(Math(polynom_string2))

text_poly2 = widgets.Text(placeholder='Enter Interval')
display(text_poly2)

gen_button2 = widgets.Button(description="Re-generate polynomial", layout = Layout(width='30%', height='40px'))
check_button2 = widgets.Button(description="Check your answer", layout = Layout(width='30%', height='40px'),visible=False)

display(widgets.HBox([check_button2,gen_button2]))

text_check_ans2 = widgets.HTML()
display(text_check_ans2)
    
def generate_polynomial2(b):
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index(), IPython.notebook.get_selected_index()+1)'))

gen_button2.on_click(generate_polynomial2) 

def check_answer2(b):
    text_poly2.value = text_poly2.value.replace(" ","")
    result=check_answer(text_poly2.value,interval2,y_values2,polynom_string2,text_check_ans2)
    if result:
        check_button2.disabled=True
    
check_button2.on_click(check_answer2)

interval3,y_values3,polynom_string3=find_interval3()

display(Markdown('**Order 3 Polynomials:**'))
display(Latex("Find the interval where $P(x) > 0$ , using 'inf' for infinity and 'U' for union:"))
display(Math(polynom_string3))

text_poly3 = widgets.Text(placeholder='Enter Interval')
display(text_poly3)

gen_button3 = widgets.Button(description="Re-generate polynomial", layout = Layout(width='30%', height='40px'))
check_button3 = widgets.Button(description="Check your answer", layout = Layout(width='30%', height='40px'),visible=False)

display(widgets.HBox([check_button3,gen_button3]))

text_check_ans3 = widgets.HTML()
display(text_check_ans3)
    
def generate_polynomial3(b):
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index(), IPython.notebook.get_selected_index()+1)'))

gen_button3.on_click(generate_polynomial3) 

def check_answer3(b):
    text_poly3.value = text_poly3.value.replace(" ","")
    result=check_answer(text_poly3.value,interval3,y_values3,polynom_string3,text_check_ans3)
    if result:
        check_button3.disabled=True
    
check_button3.on_click(check_answer3)

## Plotting in Python


 To create a simple plot of a polynomial, we can run the following code:

First, we have to import the necessary libraries to create the plot. We can call the matplotlib library in the code by using the 'plt.' prefix. 

We will use the Python `matplotlib` library to plot the polynomials.

The` numpy` library is used to create an object called a 'vector' -- we use this to plot the  polynomial over some range of x:

```python
import matplotlib.pyplot as plt

import numpy as np 
```

From the `numpy` library, we call the 'linspace' function, which creates a list of linearly spaced numbers. The numbers in the brackets are the starting number, the final number, and the number of points between the two. In this case, we create a list of 1000 numbers equally spaced between `-10` and `10`. We will define this list as the variable `x` by typing `x=` before we call the `numpy` function:

```python
x = np.linspace(-10,10,1000) 
```

Now we can use `matplotlib` functions to create the graph. Calling the `figure()` function creates a figure box to make the graph. We can enter arguments in the brackets to specify the size of the figure window to make it easier to read. To actually draw the graph, we call `plot(x,y)`, draws the graph of y as a function of x.

```python
plt.figure(figsize=(11,8)) 

plt.plot(x,y)  
```

When you write the code for yourself, instead of typing 'y' in the brackets, write out the actual polynomial you wish to plot. For example, if we wanted to plot $y = x^2 + 2x - 3$, our code may look like:

```python
plt.figure(figsize=(11,8)) 

plt.plot(x,x**2 + 2*x - 3)  
```

Notice the *syntax* of the polynomial. Double asterisks `**` are used to exponentiate variables (i.e. $x^2$ = `x**2`), while a single asterisk `*` means multiplication in Python. Addition and subtraction are the usual `+` and `-` symbols.

We can make the intercepts easier to read by placing a grid on the figure with

```python
plt.grid(alpha=0.7)
```
and making the origin lines solid by using

```python
plt.axhline(y=0, color = 'k', linewidth=1)

plt.axvline(x=0, color = 'k', linewidth=1)
```



In the cell below, write out this code block, entering the polynomial you wish to solve as 'y'.

## Conclusion


 In this notebook, we reviewed some basics of polynomial functions:
 - what is the general form of a polynomial
 - what are some examples of polynomials
 - what defines the order (or degree) of a polynomial
 - what is the constant term of a polynomial, and what is it's role on the graph of a polynomial
 
We explored who to solve inequalities involving polynomials analytically, and demonstrated how we can search for solutions graphically as well.

You should also be familiar with some basic Python syntax and plotting routines to create simple plots of polynomial functions with the `matplotlib` library.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)