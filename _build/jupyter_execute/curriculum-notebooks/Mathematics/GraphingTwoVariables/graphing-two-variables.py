![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/GraphingTwoVariables/graphing-two-variables.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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
<p> Code is hidden for ease of viewing. Click the Show/Hide button to see. </>
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>

from IPython.display import display, Math, Latex, HTML
from helper import *
%matplotlib inline

# Graphing two variables 

** or **

## Understanding the Relationship Between Two Variables Using Graphs 
***




![Math_Gif](https://media.giphy.com/media/BmmfETghGOPrW/giphy.gif)
<center>*GIF taken from https://giphy.com/gifs/reaction-BmmfETghGOPrW, June 11th, 2018.*</center>

***

## **Introduction**

You may have heard the old saying, "you get what you give".  It means what you get is worth the same as what you give up for it.  But have you ever noticed that if you *change* what you give, it can *change* what you get?  Like when you eat more food, you get more energy, or when you spend more time on homework, you get better grades.

In these examples, the things you get (or give) are like **variables**—they are amounts that are allowed to change.  Sometimes, changing the value of one variable can affect the value of another.  Think about this example:

> ### Example  
> Say you have a job that pays you 10 dollars per hour. The amount of money you earn after working 5 hours depends on this wage (5 hours)x(10 dollars per hour) = 50 dollars. If your wage goes up to 12 dollars per hour, the amount of money you would make in 5 hours would change as well (5 hours)x(12 dollars per hour) = 60 dollars. So, your wage is a *variable* that determines how much money you are going to make.  

Variables are a part of our lives every day, but their exact effect can be hard to understand on their own.  A useful tool to help us see how variables affect results is called a **graph**, which is simply a visual way to show how variables are related.

This lesson will focus on how we can use graphs to improve our understanding of how two variables interact with each other. There are many different types of graphs, but we will focus on line graphs in this lesson to show you how to work with **linear functions**. We will go through:
- how to create a graph of a linear function 
- how to analyze some important features of a graph

Take a look at the graph shown below. This is a line graph that shows the relationship between a person's wage and how much money they earn after working 5 hours. You can use the toolbar at the top of the graph to play with it.

wages = np.linspace(0,50,11)
money = []
for item in wages:
    y = item*5
    money.append(y)

layout = go.Layout(
    title = "Money Earned After Working 5 Hours",
    yaxis = dict(
        title="Money Earned (Dollars)"
    ),
    xaxis = dict(
        title="Wage (Dollars per hour)",
    ),
)

trace1 = go.Scatter(
    x = wages,
    y = money,
    mode = "lines+markers",
    name = "Plot 1",
    line=dict(
        color = ('rgb(205, 12, 24)'),
        shape = "spline",
        dash = "dot"
    )
    
)

fig = go.Figure(data = [trace1], layout = layout)
py.offline.iplot(fig)

<center> Figure 1: This graph shows the relationship between a person's wage, and the money they will make after working for 5 hours. </center>


***

## **Background**

### **Algebraic Equations**

In mathematics, the relationship between variables can be written as an **equation**. An equation is like a sentence—it uses an 'equals' sign to connect two expressions, like how a sentence uses a verb to connect a subject and an object.  For example, the relationship between wage and the amount of money made after working for 5 hours, as described above, can be written like this:

\begin{equation} 
\label{1}
\rm MONEY\: MADE = 5\: HOURS \times WAGE
\end{equation}

Here is the same equation, only now it is expressed using **algebra** (with letters in place of the words):

\begin{equation} 
\label{2}
M = 5W
\end{equation}

This is an example of an **algebraic equation**.  It compresses all the information about the variables into a very small space that's easy to work with. The $W$ corresponds to wage, and the $M$ corresponds to the resulting amount of money made.

When creating an algebraic expression, the letters that you use for variables really doesn't matter. A good choice is to use the first letter of the word (like how we used $M$ for money and $W$ for wage). However, in mathematics, the default letters are $x$ and $y$, especially when a graph will be used.

In most of the equations you'll see in class, the variables may not have any real-world meaning, but that's okay. Take a look at the examples below—each one is an algebraic equation.

>#### **Examples**
>
>\begin{equation}
y = 3x + 9
\end{equation}
>
>\begin{equation}
y = -5x
\end{equation}
>
>\begin{equation}
y = \frac{x}{4} + 3
\end{equation}
>
>\begin{equation}
x = \frac{y + 7}{2}
\end{equation}
***

### **Linear Functions**

If an equation says a variable is equal to something that doesn't involve that variable, that equation is called a **function**. For example, the equation $y=2x-3$ says that $y$ (a variable) is equal to $2x-3$ (which uses $x$, but not $y$). In this case, we say $y$ is a *function* of $x$.  A **linear function** has the form

\begin{equation}
y = mx + b
\end{equation}

where both $x$ and $y$ are variables, while $m$ and $b$ are **constants**. A *constant* is a number in an equation that does not change—in other words, it is not a variable. A constant can be any number—positive, negative, a fraction, etc.  It can even be zero!

Take another look at the equations shown in the section above, these are all linear functions! When a linear function is used to create a graph, the graph will look like a straight line (hence the name *linear* function).

Use the section below to better your understanding of the difference between a *linear* function, and a *non-linear* function.





display("Is this function linear or non-linear?")
display(Math('y = 12x -3'))

interact(lin_or_non1, val = widgets.Dropdown(options=[' ', 'Linear', 'Non-Linear'],value = ' ',description = 'Choose One:',disabled = False));


display("Is this function linear or non-linear?")
display(Math('y = 2x^2 + 17'))
    
interact(lin_or_non2, val = widgets.Dropdown(options=[' ', 'Linear', 'Non-Linear'],value = ' ',description = 'Choose One:',disabled = False));


x = np.linspace(-10,10,21)
y = []
for num in x:
    y_val = num**2
    y.append(y_val)

layout = go.Layout(
    title = "<i>Y</i> as a Function of <i>X</i>",
    yaxis = dict(
        title="<i>Y</i> Values"
    ),
    xaxis = dict(
        title="<i>X</i> Values"
    ),
)

trace1 = go.Scatter(
    x = x,
    y = y,
    mode = "lines+markers",
    name = "Plot 1",
    line=dict(
        color = ('rgb(22, 96, 167)'),
        shape = "spline",
        dash = "dot"
    )
    
)

fig = go.Figure(data = [trace1], layout = layout)
py.offline.iplot(fig)

display("Is the above function linear or non-linear?")

interact(lin_or_non3, val = widgets.Dropdown(options=[' ', 'Linear', 'Non-Linear'],value = ' ',description = 'Choose One:',disabled = False));

x = np.linspace(-10,4,10)
y = []
for num in x:
    y_val = -num - 6
    y.append(y_val)
    
    
layout = go.Layout(
    title = "<i>Y</i> as a Function of <i>X</i>",
    yaxis = dict(
        title="<i>Y</i> Values"
    ),
    xaxis = dict(
        title="<i>X</i> Values"
    ),
)

trace1 = go.Scatter(
    x = x,
    y = y,
    mode = "lines+markers",
    name = "Plot 1",
    line=dict(
        color = ('rgb(100, 100, 100)'),
        shape = "spline",
        dash = "dot"
    )
    
)

fig = go.Figure(data = [trace1], layout = layout)
py.offline.iplot(fig)
   

display("Is the above function linear or non-linear?")
    
interact(lin_or_non4, val = widgets.Dropdown(options=[' ', 'Linear', 'Non-Linear'],value = ' ',description = 'Choose One:',disabled = False));

Now that we know how linear functions can look, let's talk about how we can draw them on a graph!

## **Creating a Graph**

### **Independent and Dependent Variables**

When you want to graph a linear function, you need to figure out which variable is **independent** and which one is **dependent**. The *independent* variable is the one that is allowed to change freely; the *dependent* variable is the one that responds to those changes—in other words, it *depends* on the independent variable. The two variables form an "if-then" pair: "*IF* the independent variable is this, *THEN* the dependent variable must be that." The difference between the two types of variables may be difficult to understand at first, so here is an example that may help.
***
>#### **Example**
Let's say you want to measure how many push-ups you can do in a certain amount of time. There are two variables here: the amount of time, and the number of push-ups you do in that time. In this scenario, you are able to freely change how much time you have to do push-ups. You could give yourself 30 seconds, an hour, or a day! Therefore, *time is the independent variable*. 
But the number of push-ups you are actually able to do *depends* on the amount of time you have to do them. If you give yourself more time, you can do more push-ups.  Therefore, the *dependent variable is the number of push-ups you do*. 
***
When the two variables in an equation are $x$ and $y$, we usually treat $x$ as the independent variable, and $y$ as the dependent variable.
***


display("From the wage example shown in the section above, which variable do you think is the independent variable?")
display(Math('M = 5W'))
    
interact(wage, val = widgets.Dropdown(options=[' ', 'W (Wage)', 'M (Money Made)'],value = ' ',description = 'Choose One:',disabled = False));


***
### **The Cartesian Plane**

Once we have established the independent and dependent variables in our linear function, we are ready to set up a graph of their relationship. When graphing two variables, we use what is called the **Cartesian Plane**. You have probably seen a graph on the Cartesian Plane before, but here is what it looks like:

layout = go.Layout(
    title = "The Cartesian Plane",
    yaxis = dict(
        title="<i>Y</i> Axis",
        range = [-10,10],
        dtick = 1.00
    ),
    xaxis = dict(
        title="<i>X</i> Axis",
        range = [-10,10],
        dtick = 1.00
    ),
)

trace1 = go.Scatter(
    x = [5,-5,-5,5],
    y = [5,5,-5,-5],
    mode = "markers+text",
    name = "Plot 1",
    text=['Quadrant 1', 'Quadrant 2', 'Quadrant 3', 'Quadrant 4'],
    textposition='bottom center'
)

fig = go.Figure(data = [trace1], layout = layout)
py.offline.iplot(fig)

<center> Figure 2: This is the standard layout for the Cartesian Plane, where you will plot all linear functions. The point where $x = 0$ and $y = 0$ is called the origin. </center>

On the Cartesian Plane, there are two **axes**: the $x$ axis (horizontal), and the $y$ axis (vertical). When we want to graph a certain function, we label the $y$ axis with the dependent variable, and the $x$ axis with the independent variable. When you aren't given a specific name for what the independent and dependent variable represent, it is okay to just label the $x$ axis "$X$" and the $y$ axis "$Y$". 

When making a title for the graph, just describe what is being shown. Your title should allow whoever is looking at the graph to understand what is being shown. In most cases, you will describe the dependent variable as a function of the independent variable, or "$Y$ as a Function of $X$". 

The Cartesian Plane consists of four **quadrants**, or sections. The top right section, where both $x$ and $y$ are positive (+,+), is quadrant 1. Then going counter-clockwise, quadrant 2 is the section where $x$ is negative and $y$ is positive (-,+), in quadrant 3 both $x$ and $y$ are negative (-,-), and in quadrant 4, $x$ is positive and $y$ is negative (+,-).

Now that we have established how a graph should look, let's talk about how we decide which values we want to plot on the graph!

### **Finding the Data Points**

The data points that are shown on a graph don't just appear out of nowhere; they can come from scientific observations, measurements, or mathematical relationships. When graphing on the Cartesian Plane, each data point has an $x$-value and a $y$-value (sometimes called an $x$-coordinate and a $y$-coordinate), and these values are what determine where the point will appear on the graph.

The best way to describe how we find the $x$-value and $y$-value for each data point is through an example.

***
#### **Example:** Plot a graph of $y = 3x + 2$ with 5 data points, starting from $x = 1$ up to $x = 5$.

To begin, we pick 5 $x$-values between $1$ and $5$. 

For simplicity, let's pick 1, 2, 3, 4, and 5.

\begin{array}{| c | c |}
\hline
  X\: Value & Y\: Value  \\
  \hline
  1 & ? \\\hline
  2 & ? \\\hline
  3 & ? \\\hline
  4 & ? \\\hline
  5 & ? \\\hline
\end{array}

Now we need to find the value of $y$ at each one of the chosen values for $x$. We can do this by plugging our chosen $x$-values into the equation that we have been given: $y = 3x + 2$.

Let's take our first $x$-value, which is 1, and plug it into the equation:

\begin{equation} 
y = 3x + 2
\end{equation}


\begin{equation} 
y = 3(1) + 2
\end{equation}
\begin{equation}
y = 3 + 2
\end{equation}
\begin{equation}
y = 5
\end{equation}

We now have the $y$-value of our first data point! When $x = 1$, $y = 5$. We would write this data point down as (1,5). Let's fill in the table so we can keep track of the data points we find:

\begin{array}{| c | c |}
\hline
  X\: Value  & Y\: Value  \\
  \hline
  1 & 5 \\\hline
  2 & ? \\\hline
  3 & ? \\\hline
  4 & ? \\\hline
  5 & ? \\\hline
\end{array}


In the section below, use the above method to find the remaining $y$ values.

check_input_numbers()

Good job! Now that we have all of the data points, we are ready to plot them on the graph.


### **Plotting the Data Points on the Graph**

To plot our data points on a graph, we will need our Cartesian Plane, with the $x$-axis and $y$-axis labelled as follows:

layout = go.Layout(
    title = "<i>Y</i> as a Function of <i>X</i>",
    yaxis = dict(
        title="<i>Y</i> Values",
        range = [-1,20],
        dtick = 1.00
    ),
    xaxis = dict(
        title="<i>X</i> Values",
        range = [-1,10],
        dtick = 1.00
    )
)

trace1 = go.Scatter(
    x = [],
    y = [],
    mode = "lines+markers",
    name = "Plot 1",
    line=dict(
        color = ('rgb(205, 12, 24)'),
        shape = "spline",
        dash = "dot"
    )
    
)

fig = go.Figure(data = [trace1], layout = layout)
py.offline.iplot(fig)


<center> Figure 3: The layout of our graph. As all of our data points have positive $x$ and $y$ values, we only need to focus on the first quadrant (top right corner).</center>

Now, using our chart of data points, let's plot our first point. The $x$-value of our first point is 1, and the $y$-value is 5. So let's find the point on the graph where $x=1$ and $y=5$ and mark this point


layout = go.Layout(
    title = "<i>Y</i> as a Function of <i>X</i>",
    yaxis = dict(
        title="<i>Y</i> Values",
        range = [-1,20],
        dtick = 1.00
    ),
    xaxis = dict(
        title="<i>X</i> Values",
        range = [-1,10],
        dtick = 1.00
    )
)

trace1 = go.Scatter(
    x = [1],
    y = [5],
    mode = "lines+markers",
    name = "Plot 1",
    line=dict(
        color = ('rgb(205, 12, 24)'),
        shape = "spline",
        dash = "dot"
    )
    
)

fig = go.Figure(data = [trace1], layout = layout)
py.offline.iplot(fig)

<center> Figure 4: Here is the location of our first data point.</center>

That is your first data point!

In the section below, use the above methods to create a graph and plot all of the data points.

\begin{array}{| c | c |}
\hline
  X\: Value & Y\: Value \\
  \hline
  1 & 5 \\\hline
  2 & 8 \\\hline
  3 & 11 \\\hline
  4 & 14 \\\hline
  5 & 17 \\\hline
\end{array}

g = User_Graph([-1,10],[-1,20])
g.run_it()

If done correctly, your graph should look something like this:

layout = go.Layout(
    title = "<i>Y</i> as a Function of <i>X</i>",
    yaxis = dict(
        title="<i>Y</i> Values",
        range = [-1,20]
    ),
    xaxis = dict(
        title="<i>X</i> Values",
        range = [-1,10]
    )
)

trace1 = go.Scatter(
    x = [1,2,3,4,5],
    y = [5,8,11,14,17],
    mode = "lines+markers",
    name = "Plot 1",
    line=dict(
        color = ('rgb(205, 12, 24)'),
        shape = "spline",
        dash = "dot"
    )
    
)

fig = go.Figure(data = [trace1], layout = layout)
py.offline.iplot(fig)

If the graph you made looks significantly different, try running the code segment again to re-try!


Now that you know how to create a graph, let's talk about some of the important things that a graph can tell us.

***

**Features of a Linear Graph: Slope**

An important characteristic of a linear function is **slope**. The *slope* of a function can be thought of as the steepness or the angle of the function as it appears on a graph. What it really represents is the **rate of change** as you move along the graph. 

That may sound complicated at first, but here is an example that might make it easier to understand what slope is.

***

> ### **Example**

Say you have been given a set of data points describing how far a car has travelled in a given amount of time:


\begin{array}{| c | c |}
\hline
  Time(seconds) & Distance Travelled(meters) \\
  \hline
  0 & 0 \\\hline
  20 & 400 \\\hline
  40 & 800 \\\hline
  60 & 1200 \\\hline
  80 & 1600 \\\hline
  100 & 2000 \\\hline
  120 & 2400 \\\hline
  140 & 2800 \\\hline
  160 & 3200 \\\hline
  180 & 3600 \\\hline
  200 & 4000 \\\hline
\end{array}


If you want to find out how fast the car is travelling, you are really trying to find out how quickly the distance travelled increases, or rather, the **rate** at which it is changing. 

Let's set up a graph of this data to take a closer look.





time = np.linspace(0,200,11)
distance = np.linspace(0,4000,11)

layout = go.Layout(
    title = "Distance Travelled as a Function of Time",
    yaxis = dict(
        title="Distance Travelled (Meters)"
    ),
    xaxis = dict(
        title="Time (Seconds)"
    ),
)

trace1 = go.Scatter(
    x = time,
    y = distance,
    mode = "lines+markers",
    name = "Plot 1",
    line=dict(
        color = ('rgb(22, 96, 167)'),
        shape = "spline",
        dash = "dot"
    )
    
)

fig = go.Figure(data = [trace1], layout = layout)
py.offline.iplot(fig)

<center> Figure 6: This graph shows the distance a car travels after a given amount of time.</center>

We want to find how fast the car is travelling. Knowing that speed is a measurement of distance over time, let's use the total distance travelled and the total amount of time to find the average speed of the car.
From the graph, we can see that the car initially started at position 0 meters, and travelled a total of 4000 meters. We also know that the car started moving at time 0 seconds, and stopped moving after 200 seconds. Using this information, we can set up the following equations to find the speed of the car:

\begin{equation}
Speed = \frac{Total\: Distance}{Total\: Time}
\end{equation}

and we know that:

\begin{equation}
Total\: Distance = Final\: Distance - Initial\: Distance
\end{equation}
\begin{equation}
Total\: Time = Final\: Time - Initial\: Time
\end{equation}

so:

\begin{equation} 
Speed = \frac{Final\: Distance - Initial\: Distance}{Final\: Time - Initial\: Time}
\end{equation}

\begin{equation} 
Speed = \frac{4000m - 0m}{200s - 0s}
\end{equation}

\begin{equation}
Speed = \frac{4000m}{200s}
\end{equation}

\begin{equation} 
 Speed = 20 m/s
\end{equation}



From the equations above, we can see that the car travels 20 meters every second. While it may not be obvious, we just found the slope of the graph! By finding the average speed of the car, we identified the rate at which the dependent variable (Distance Travelled) changes with respect to the independent variable (Time).

***


When looking at a graph, the general equation used to find the slope of a linear function from one point: ($x_1$,$y_1$), to a second point: ($x_2$,$y_2$), is given as follows:

\begin{equation} 
Slope = \frac{y_2 - y_1}{x_2 - x_1}
\end{equation}

When looking at a linear function that has the form:
\begin{equation} 
y = mx + b
\end{equation}
the value of the slope is the same as the value of $m$.

Use the section below to see the effect that slope can have on a function.

def slider(slope):
    
    x_list = [0,1,2,3,4,5,6,7,8,9,10]
    y_list = []
    for i in x_list:
        y_val = slope*(i)
        y_list.append(y_val)
    
    
    layout = go.Layout(
        showlegend = True,
        title ='y = ' + str(slope) + 'x',
        yaxis = dict(
            title="<i>X</i> Values",
            range = [-1,20]
        ),
        xaxis = dict(
            title="<i>Y</i> Values",
            range = [-1,20]
        ),
    )

    trace1 = go.Scatter(
        x = x_list,
        y = y_list,
        mode = "lines+markers",
        name = str('$y = ' + str(slope) + 'x$'),
        line=dict(
            color = ('rgb(22, 96, 167)'),
            shape = "spline",
            dash = "dot"
        )
    
    )

    fig = go.Figure(data = [trace1], layout = layout)
    py.offline.iplot(fig, filename = 'show-legend')
    
interactive(slider, slope=(0,5,0.5))



<center> Figure 7: This graph shows the way in which slope can affect the shape of a function. The larger the slope, the "steeper" the graph is.</center>

When dealing with a single linear function, the slope will be constant across the entire graph. However, if a graph consists of more than one linear function, the slope may change at some point. 
Take a look at the following graph to see what a graph with more than one linear function may look like:

x1 = [0,1,2,3,4,5]
y1 = []

for num in x1:
    y1_val = num + 1
    y1.append(y1_val)
    
x2 = [6,7,8,9,10]
y2 = []

for num in x2:
    y2_val = 3*(num) - 9
    y2.append(y2_val)

x_list = x1 + x2
y_list = y1 + y2
    
layout = go.Layout(
    title = "<i>Y</i> as a Function of <i>X</i>",
    yaxis = dict(
        title="<i>Y</i> Values"
    ),
    xaxis = dict(
        title="<i>X</i> Values"
    ),
)

trace1 = go.Scatter(
    x = x_list,
    y = y_list,
    mode = "lines+markers",
    name = "Plot 1",
    line=dict(
        color = ('rgb(22, 96, 167)'),
        dash = "dot"
    )
    
)

fig = go.Figure(data = [trace1], layout = layout)
py.offline.iplot(fig)

    

<center> Figure 8: On this plot, notice the distinct change in steepness at $x = 5$. The slope increases at this point.</center>

As you can see above, the graph has two distinct sections: one from $x = 0$ to $x = 5$, and the other from $x = 5$ to $x = 10$. As we have seen from the equations of linear functions, we know that the slope of one function has a constant value. Because these sections each have a different slope, they must represent two distinct linear functions.

You may be wondering how one graph can show two different functions at the same time, but consider our example of the car shown above. What if halfway through the trip, the car began to move at a faster speed? If this were the case, the slope of the graph would increase at the halfway point, much like the graph shown above.

## **Questions**

The following section is meant to test your understanding and improve your familiarity with the concepts we have gone over in this lesson.


### **Question 1.**

Use the following table of data points describing the motion of a car driving to a destination and complete the following tasks:
- Plot a graph (be sure to label the axes, and to give the graph a title!)
- Find the slope of the graph
- Create an equation for the linear function

\begin{array}{| c | c |}
\hline
  Time\: (seconds) & Distance\: Away\: from\: Destination\: (meters) \\
  \hline
  0 & 10 \\\hline
  1 & 8 \\\hline
  2 & 6 \\\hline
  3 & 4 \\\hline
  4 & 2 \\\hline
  5 & 0 \\\hline
  6 & -2 \\\hline
  7 & -4 \\\hline
  8 & -6 \\\hline
  9 & -8 \\\hline
\end{array}


Use the section below to create the graph:

q1 = User_Graph([-1,10], [-10,12])
q1.run_it()

Use the following sections to answer some questions about the graph you just made:

ask_slope()

ask_equation()

ask_question1()

###### Question 2.

Quentin and Isabelle both earn their allowance by doing exercise. Quentin's parents pay him $\$8.00$ each time he goes for a run, plus an additional $\$0.50$ for every kilometer he runs.

Isabelle gets paid $\$5.00$ every time she goes for a run, and an additional $\$1.00$ for every kilometer she runs.

At what distance do Quentin and Isabelle make the same amount of money?
Who makes the most money after running for 10 kilometers?

To help answer these questions, here are the linear equations that describe Quentin's and Isabelle's allowance:

Quentin: 
\begin{equation}
y = \frac{1}{2}x + 8
\end{equation}

Isabelle:
\begin{equation}
y = x + 5
\end{equation}

Create a graph that shows both of these functions at the points: 

\begin{array}{| c | c |}
\hline
  Distance\: (km) & Money\: Made\: (Dollars)\\
  \hline
  0 & ? \\\hline
  1 & ? \\\hline
  2 & ? \\\hline
  3 & ? \\\hline
  4 & ? \\\hline
  5 & ? \\\hline
  6 & ? \\\hline
  7 & ? \\\hline
\end{array}

*Hint*: Create one table for each of the equations and find the corresponding $y$-values, then use the section below to enter the points.

D = Double_Graph([0,8],[0,15])
D.run_it()

ask_question2()

ask_question3()

## **Conclusion**

In this lesson, we have highlighted some of the many ways that a graph can help us understand the relationship between two variables in a linear function. Some of the important methods that you should remember include:

- Defining a Linear Function
- Identifying the Independent and Dependent Variables
- Setting up a Graph on the Cartesian Plane
- Creating and Plotting Data Points
- Finding the slope of a graph

Throughout your life, you will be presented with all sorts of statistics, data, charts and graphs. It is important that you have the skills required to analyze what a graph is trying to tell you, not just so you can pass your math class, but to enable you to make informed decisions when you need to consider how different variables can interact and affect results.



[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)