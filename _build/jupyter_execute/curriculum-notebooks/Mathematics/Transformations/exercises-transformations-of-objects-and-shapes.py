![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/Transformations/exercises-transformations-of-objects-and-shapes.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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
    
$( document ).ready(function(){ code_shown=false; $('div.input').hide() });
</script>

<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>

# Transformations of Objects and Shapes: Exercises

## Instructions - from the "Kernel" menu, select "Restart & Run All" to begin.

This notebook is intended to be used by someone who has gone through the *Transformations of Objects and Shapes* notebook and read through the material. There will be multiple examples for the reader to go through to ensure they understand the *Transformations* notebook and are able to use the information and methods learnt.

## Translations: Objects and Shapes in 2D Space

In this exercise you will be determining how far the original object has been translated on the X and Y axes. The original object is colored <span style="color:#00FF00"> green </span> and the translated object is <span style="color:#00CED1"> blue</span>. The translations will always be whole numbers. You can enter your answer in the textboxes below and click the **Submit Answer** button to check your answer. If you want a new example generated then click the **New Example** button. If no translation has occured on either the X or Y axis then leave the textbox with a value of 0.

from plotly.offline import init_notebook_mode, iplot, plot
from ipywidgets import HBox
import plotly.graph_objs as go
import numpy as np
import random
from math import radians, cos, sin, sqrt, tan, atan
import ipywidgets as widgets
from IPython.display import Markdown as md
from IPython.display import HTML, clear_output

init_notebook_mode(connected=True)

xO = []
yO = []
xT = []
yT = []

X1 = random.randint(0,17) - 10
Y1 = random.randint(0,17) - 10
X2 = random.randint(0,17) - 10
Y2 = random.randint(0,17) - 10

answerX = X2 - X1
answerY = Y2 - Y1

random_object = random.randint(0,1)

if(random_object == 0):
    xO = [X1,X1,X1+3,X1+3,X1]
    yO = [Y1,Y1+3,Y1+3,Y1,Y1]
    xT = [X2,X2,X2+3,X2+3,X2]
    yT = [Y2,Y2+3,Y2+3,Y2,Y2]
else:
    xO = [X1,X1+1.5,X1+3,X1]
    yO = [Y1,Y1+3,Y1,Y1]
    xT = [X2,X2+1.5,X2+3,X2]
    yT = [Y2,Y2+3,Y2,Y2]
    

new_button = widgets.Button(
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
)
submit_button = widgets.Button(
    description='Submit Answer',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
)

x_answer = widgets.Text(
    value='0',
    placeholder='',
    description='',
    disabled=False   
)

y_answer = widgets.Text(
    value='0',
    placeholder='',
    description='',
    disabled=False   
)

x_text = widgets.HTML("<strong>X Translation: </strong>")
y_text = widgets.HTML("<strong>Y Translation: </strong>")
answer_text = widgets.HTML("")

answer_output = widgets.HBox(children=[x_text, x_answer, y_text, y_answer, submit_button])
widget_output = widgets.VBox(children=[new_button, answer_output, answer_text])

new_button.layout.margin = '0px 0px 10px 600px'

x_answer.layout.width = '100px'
y_answer.layout.width = '100px'

def draw_plot(xO,yO,xT,yT):
    data = []
    data.append(dict(
        visible = True,
        line=dict(color='#00FF00', width=3),
        mode = 'lines+markers',
        name = 'Original',
        hoverinfo = 'x+y',
        x = xO,#[1, 2.5, 4, 1],
        y = yO))#[1, 4, 1, 1]))

    data.append(dict(
        visible = True,
        line=dict(color='#00CED1', width=3),
        mode = 'lines+markers',
        name = 'Translation',
        hoverinfo = 'x+y',
        x = xT,#[1, 2.5, 4, 1],
        y = yT))#[1, 4, 1, 1]))

    layout = go.Layout(
        title = '',
        showlegend=False,
        hovermode = 'closest',
        yaxis = dict(
            title= '',
            ticklen= 5,
            dtick= 1,
            gridwidth= 2,
            range=[-10,10],
            showgrid=True,
        
        ),
        xaxis= dict(
            title= '',
            ticklen= 5,
            dtick=1,
            gridwidth= 2,
            range=[-10,10],
            showgrid=True,
        ),
        #autosize=False,
        #width=950,
        #height=650,
        annotations=[
            dict(
                x=1.0,
                y=-0.16,
                showarrow=False,
                text='X Axis',
                xref='paper',
                yref='paper',
                font=dict(
                    size=14,
                ),
            ),
            dict(
                x=-0.06,
                y=1.0,
                showarrow=False,
                text='Y Axis',
                textangle=-90,
                xref='paper',
                yref='paper',
                font=dict(
                    size=14,
                ),
            ),
        ],
    )

    fig = dict(data=data, layout=layout)
    
    
    clear_output(wait=True)
    display(widget_output)
    iplot(fig, filename='basic-scatter')
    
def check_answer(change):
    global answerX
    global answerY
    
    error = False
    
    try:
        inputX = int(x_answer.value)
        inputY = int(y_answer.value)
    except ValueError:
        answer_text.value = "Those are not integer numbers.  Please enter integer numbers and submit your answer again."
        error = True
        
    if(not(error)):
        if((inputX == answerX) and (inputY == answerY)):
            answer_text.value = "You are right! That is the correct translation."
        else:
            answer_text.value = "That is not the correct translation."

def new_example(change):
    global answerX
    global answerY
    
    answer_text.value = ""
    x_answer.value = '0'
    y_answer.value = '0'
    
    X1 = random.randint(0,17) - 10
    Y1 = random.randint(0,17) - 10
    X2 = random.randint(0,17) - 10
    Y2 = random.randint(0,17) - 10

    answerX = X2 - X1
    answerY = Y2 - Y1

    random_object = random.randint(0,1)

    if(random_object == 0):
        xO = [X1,X1,X1+3,X1+3,X1]
        yO = [Y1,Y1+3,Y1+3,Y1,Y1]
        xT = [X2,X2,X2+3,X2+3,X2]
        yT = [Y2,Y2+3,Y2+3,Y2,Y2]
    else:
        xO = [X1,X1+1.5,X1+3,X1]
        yO = [Y1,Y1+3,Y1,Y1]
        xT = [X2,X2+1.5,X2+3,X2]
        yT = [Y2,Y2+3,Y2,Y2]
    
    draw_plot(xO,yO,xT,yT)
    
            
submit_button.on_click(check_answer)

new_button.on_click(new_example)
    
draw_plot(xO,yO,xT,yT) 

## Reflections: Objects and Shapes in 2D Space

In this exercise you will be determining the horizontal and vertical lines that the original object has been reflected by. The original object is colored <span style="color:#00FF00"> green </span> and the reflected object is <span style="color:#00CED1"> blue</span>. The line of reflection will be integer numbers including negative values. You can enter your answer in the textboxes below and click the **Submit Answer** button to check your answer. If you want a new example generated then click the **New Example** button.

from plotly.offline import init_notebook_mode, iplot, plot
from ipywidgets import HBox
import plotly.graph_objs as go
import numpy as np
import random
from math import radians, cos, sin, sqrt, tan, atan
import ipywidgets as widgets
from IPython.display import Markdown as md
from IPython.display import HTML, clear_output

init_notebook_mode(connected=True)

xO = []
yO = []
xR = []
yR = []

X1 = random.randint(0,17) - 10
Y1 = random.randint(0,17) - 10

if(X1 % 2 == 0):
    upperLimitX = ((10 - X1) / 2) + X1
    lowerLimitX = ((-7 - (X1 - 1)) / 2) + X1
else:
    upperLimitX = ((10 - X1 - 1) / 2) + X1
    lowerLimitX = ((-7 - X1) / 2) + X1

if(Y1 % 2 == 0):
    upperLimitY = ((10 - Y1) / 2) + Y1
    lowerLimitY = ((-7 - (Y1 - 1)) / 2) + Y1
else:
    upperLimitY = ((10 - Y1 - 1) / 2) + Y1
    lowerLimitY = ((-7 - Y1) / 2) + Y1

    
reflectionX = random.randint(lowerLimitX,upperLimitX)
reflectionY = random.randint(lowerLimitY,upperLimitY)

random_object = random.randint(0,1)

if(random_object == 0):
    xO = [X1,X1,X1+3,X1+3,X1]
    yO = [Y1,Y1+3,Y1+3,Y1,Y1]
    xR = [X1,X1,X1+3,X1+3,X1]
    yR = [Y1,Y1+3,Y1+3,Y1,Y1]
    for i in range(len(xR)):
        xR[i] = reflectionX - (xR[i] - reflectionX)
        yR[i] = reflectionY - (yR[i] - reflectionY)
else:
    xO = [X1,X1+1.5,X1+3,X1]
    yO = [Y1,Y1+3,Y1,Y1]
    xR = [X1,X1+1.5,X1+3,X1]
    yR = [Y1,Y1+3,Y1,Y1]
    for i in range(len(xR)):
        xR[i] = reflectionX - (xR[i] - reflectionX)
        yR[i] = reflectionY - (yR[i] - reflectionY)
    

new_button2 = widgets.Button(
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
)
submit_button2 = widgets.Button(
    description='Submit Answer',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
)

x_answer2 = widgets.Text(
    value='',
    placeholder='',
    description='',
    disabled=False   
)

y_answer2 = widgets.Text(
    value='',
    placeholder='',
    description='',
    disabled=False   
)

x_text2 = widgets.HTML("<strong>Vertical Axis: </strong>")
y_text2 = widgets.HTML("<strong>Horizontal Axis: </strong>")
answer_text2 = widgets.HTML("")

answer_output2 = widgets.HBox(children=[x_text2, x_answer2, y_text2, y_answer2, submit_button2])
widget_output2 = widgets.VBox(children=[new_button2, answer_output2, answer_text2])

new_button2.layout.margin = '0px 0px 10px 600px'

x_answer2.layout.width = '100px'
y_answer2.layout.width = '100px'

def draw_plot2(xO,yO,xR,yR):
    data = []
    data.append(dict(
        visible = True,
        line=dict(color='#00FF00', width=3),
        mode = 'lines+markers',
        name = 'Original',
        hoverinfo = 'x+y',
        x = xO,#[1, 2.5, 4, 1],
        y = yO))#[1, 4, 1, 1]))

    data.append(dict(
        visible = True,
        line=dict(color='#00CED1', width=3),
        mode = 'lines+markers',
        name = 'Translation',
        hoverinfo = 'x+y',
        x = xR,#[1, 2.5, 4, 1],
        y = yR))#[1, 4, 1, 1]))

    layout = go.Layout(
        title = '',
        showlegend=False,
        hovermode = 'closest',
        yaxis = dict(
            title= '',
            ticklen= 5,
            dtick= 1,
            gridwidth= 2,
            range=[-10,10],
            showgrid=True,
        
        ),
        xaxis= dict(
            title= '',
            ticklen= 5,
            dtick=1,
            gridwidth= 2,
            range=[-10,10],
            showgrid=True,
        ),
        #autosize=False,
        #width=950,
        #height=650,
        annotations=[
            dict(
                x=1.0,
                y=-0.16,
                showarrow=False,
                text='X Axis',
                xref='paper',
                yref='paper',
                font=dict(
                    size=14,
                ),
            ),
            dict(
                x=-0.06,
                y=1.0,
                showarrow=False,
                text='Y Axis',
                textangle=-90,
                xref='paper',
                yref='paper',
                font=dict(
                    size=14,
                ),
            ),
        ],
    )

    fig = dict(data=data, layout=layout)
    
    
    clear_output(wait=True)
    display(widget_output2)
    iplot(fig, filename='basic-scatter')
    
def check_answer2(change):
    global reflectionX
    global reflectionY
    
    error = False
    
    try:
        inputX = int(x_answer2.value)
        inputY = int(y_answer2.value)
    except ValueError:
        answer_text2.value = "Those are not integer numbers.  Please enter integer numbers and submit your answer again."
        error = True
        
    if(not(error)):
        if((inputX == reflectionX) and (inputY == reflectionY)):
            answer_text2.value = "You are right! Those are the correct reflections."
        else:
            answer_text2.value = "Those are not the correct reflections."

def new_example2(change):
    global reflectionX
    global reflectionY
    
    answer_text2.value = ""
    x_answer2.value = ''
    y_answer2.value = ''
    
    X1 = random.randint(0,17) - 10
    Y1 = random.randint(0,17) - 10

    if(X1 % 2 == 0):
        upperLimitX = ((10 - X1) / 2) + X1
        lowerLimitX = ((-7 - (X1 - 1)) / 2) + X1
    else:
        upperLimitX = ((10 - X1 - 1) / 2) + X1
        lowerLimitX = ((-7 - X1) / 2) + X1

    if(Y1 % 2 == 0):
        upperLimitY = ((10 - Y1) / 2) + Y1
        lowerLimitY = ((-7 - (Y1 - 1)) / 2) + Y1
    else:
        upperLimitY = ((10 - Y1 - 1) / 2) + Y1
        lowerLimitY = ((-7 - Y1) / 2) + Y1
    
    reflectionX = random.randint(lowerLimitX,upperLimitX)
    reflectionY = random.randint(lowerLimitY,upperLimitY)

    random_object = random.randint(0,1)

    if(random_object == 0):
        xO = [X1,X1,X1+3,X1+3,X1]
        yO = [Y1,Y1+3,Y1+3,Y1,Y1]
        xR = [X1,X1,X1+3,X1+3,X1]
        yR = [Y1,Y1+3,Y1+3,Y1,Y1]
        for i in range(len(xR)):
            xR[i] = reflectionX - (xR[i] - reflectionX)
            yR[i] = reflectionY - (yR[i] - reflectionY)
    else:
        xO = [X1,X1+1.5,X1+3,X1]
        yO = [Y1,Y1+3,Y1,Y1]
        xR = [X1,X1+1.5,X1+3,X1]
        yR = [Y1,Y1+3,Y1,Y1]
        for i in range(len(xR)):
            xR[i] = reflectionX - (xR[i] - reflectionX)
            yR[i] = reflectionY - (yR[i] - reflectionY)
    
    draw_plot2(xO,yO,xR,yR)
    
            
submit_button2.on_click(check_answer2)

new_button2.on_click(new_example2)
    
draw_plot2(xO,yO,xR,yR) 

## Rotations: Objects and Shapes in 2D Space

In this exercise you will be determining the point the original object has been rotated around and the amount of degrees it has been rotated. The points an object can be rotated around are on the images below. The amount of degrees an object can be rotated by are 90°, 180° or 270° **clockwise (CW)** or **counter-clockwise (CCW)**. The original object is colored <span style="color:#00FF00"> green </span> and the reflected object is <span style="color:#00CED1"> blue</span>. You can enter your answer in the dropdown boxes below and click the **Submit Answer** button to check your answer. Please note that there can be more than one correct rotation point and the degrees of rotation for a rotation shown and they will all be correct. As an example an object rotated 90° clockwise is the same as rotating an object 270° counter-clockwise and both answer will be correct. If you want a new example generated then click the **New Example** button.

<table>
<tr>
    <td><img src="images/exercisePlot1.png" alt="Old" width="475"/></td>
    <td><img src="images/exercisePlot2.png" alt="New" width="475"/></td>
</tr>
</table>

from plotly.offline import init_notebook_mode, iplot, plot
from ipywidgets import HBox
import plotly.graph_objs as go
import numpy as np
import random
from math import radians, cos, sin, sqrt, tan, atan
import ipywidgets as widgets
from IPython.display import Markdown as md
from IPython.display import HTML, clear_output

init_notebook_mode(connected=True)

xO = []
yO = []
xRo = []
yRo = []

X1 = random.randint(-5,5)
Y1 = random.randint(-5,5)

random_degree = random.randint(1,3)

random_object = random.randint(0,1)

if(random_object == 0):
    random_point = random.randint(1,5)
    
    xO = [X1,X1,X1+3,X1+3,X1]
    yO = [Y1,Y1+3,Y1+3,Y1,Y1]
    
    temp_degrees = radians(90*random_degree)
    if(random_point == 1):
        rotationX = xO[0]
        rotationY = yO[0]
        x0 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        y0 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        x1 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        y1 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        x2 = rotationX + cos(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
        y2 = rotationY + sin(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
        x3 = rotationX + cos(temp_degrees+atan((yO[3]-rotationY)/(yO[3]-rotationX)))*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))
        y3 = rotationY + sin(temp_degrees+atan((yO[3]-rotationY)/(yO[3]-rotationX)))*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))     
    elif(random_point == 2):
        rotationX = xO[1]
        rotationY = yO[1]
        x0 = rotationX + cos(temp_degrees-1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        y0 = rotationY + sin(temp_degrees-1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        x1 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        y1 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))         
        x2 = rotationX + cos(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
        y2 = rotationY + sin(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
        x3 = rotationX + cos(temp_degrees+atan((yO[3]-rotationY)/(xO[3]-rotationX)))*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))
        y3 = rotationY + sin(temp_degrees+atan((yO[3]-rotationY)/(xO[3]-rotationX)))*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))     
    elif(random_point == 3):
        rotationX = xO[2]
        rotationY = yO[2]
        x0 = rotationX - cos(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        y0 = rotationY - sin(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        x1 = rotationX - cos(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        y1 = rotationY - sin(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        x2 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
        y2 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
        x3 = rotationX + cos(temp_degrees-1.5707963268)*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))
        y3 = rotationY + sin(temp_degrees-1.5707963268)*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2)) 
    elif(random_point == 4):
        rotationX = xO[3]
        rotationY = yO[3]
        x0 = rotationX - cos(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        y0 = rotationY - sin(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        x1 = rotationX - cos(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        y1 = rotationY - sin(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        x2 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
        y2 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))            
        x3 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))
        y3 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))      
    elif(random_point == 5):
        tempXR = xO[:]
        tempYR = yO[:]
        temp = []
        if(random_degree == 1):
            temp = tempXR[:]
            tempXR = tempYR[:]
            tempYR = temp[:]
            
            for i in range(len(tempXR)):
                tempXR[i] = -1*tempXR[i]
                
            x0 = tempXR[0]
            x1 = tempXR[1]
            x2 = tempXR[2]
            x3 = tempXR[3]
            y0 = tempYR[0]
            y1 = tempYR[1]
            y2 = tempYR[2]
            y3 = tempYR[3]
        elif(random_degree == 2):
            for i in range(len(tempYR)):
                tempYR[i] = -1*tempYR[i]
                tempXR[i] = -1*tempXR[i]
            
            x0 = tempXR[0]
            x1 = tempXR[1]
            x2 = tempXR[2]
            x3 = tempXR[3]
            y0 = tempYR[0]
            y1 = tempYR[1]
            y2 = tempYR[2]
            y3 = tempYR[3]
        elif(random_degree == 3):
            temp = tempXR[:]
            tempXR = tempYR[:]
            tempYR = temp[:]
            
            for i in range(len(tempYR)):
                tempYR[i] = -1*tempYR[i]
            
            x0 = tempXR[0]
            x1 = tempXR[1]
            x2 = tempXR[2]
            x3 = tempXR[3]
            y0 = tempYR[0]
            y1 = tempYR[1]
            y2 = tempYR[2]
            y3 = tempYR[3]
    
    xRo = [x0,x1,x2,x3,x0]
    yRo = [y0,y1,y2,y3,y0]
else:
    random_point = random.randint(1,3)
    
    xO = [X1,X1+1.5,X1+3,X1]
    yO = [Y1,Y1+3,Y1,Y1]
    
    temp_degrees = radians(90*random_degree)
    if(random_point == 1):
        rotationX = xO[0]
        rotationY = yO[0]
        xT0 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        yT0 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        xT1 = rotationX + cos(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        yT1 = rotationY + sin(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        xT2 = rotationX + cos(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
        yT2 = rotationY + sin(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))     
    elif(random_point == 2):
        rotationX = xO[1]
        rotationY = yO[1]    
        xT0 = rotationX - cos(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        yT0 = rotationY - sin(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        xT1 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        yT1 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))         
        xT2 = rotationX + cos(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
        yT2 = rotationY + sin(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))     
    elif(random_point == 3):
        rotationX = xO[2]
        rotationY = yO[2]
        xT0 = rotationX - cos(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        yT0 = rotationY - sin(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
        xT1 = rotationX - cos(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        yT1 = rotationY - sin(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
        xT2 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
        yT2 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
    elif(random_point == 4):
        tempXR = xO[:]
        tempYR = yO[:]
        temp = []
        if(random_degree == 1):
            temp = tempXR[:]
            tempXR = tempYR[:]
            tempYR = temp[:]
            
            for i in range(len(tempXR)):
                tempXR[i] = -1*tempXR[i]
                
            xT0 = tempXR[0]
            xT1 = tempXR[1]
            xT2 = tempXR[2]
            yT0 = tempYR[0]
            yT1 = tempYR[1]
            yT2 = tempYR[2]
        elif(random_degree == 2):
            for i in range(len(tempYR)):
                tempYR[i] = -1*tempYR[i]
                tempXR[i] = -1*tempXR[i]
            
            xT0 = tempXR[0]
            xT1 = tempXR[1]
            xT2 = tempXR[2]
            yT0 = tempYR[0]
            yT1 = tempYR[1]
            yT2 = tempYR[2]
        elif(random_degree == 3):
            temp = tempXR[:]
            tempXR = tempYR[:]
            tempYR = temp[:]
            
            for i in range(len(tempYR)):
                tempYR[i] = -1*tempYR[i]
            
            xT0 = tempXR[0]
            xT1 = tempXR[1]
            xT2 = tempXR[2]
            yT0 = tempYR[0]
            yT1 = tempYR[1]
            yT2 = tempYR[2]
            

    xRo = [xT0,xT1,xT2,xT0]
    yRo = [yT0,yT1,yT2,yT0]
    

new_button3 = widgets.Button(
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
)
submit_button3 = widgets.Button(
    description='Submit Answer',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
)

degree_choice3 = widgets.Dropdown(
        options=[('',0),('90° CW', 1), ('180° CW', 2), ('270° CW', 3), ('90° CCW', 4), ('180° CCW', 5), ('270° CCW', 6)],
        value=0,
        description='',
)

rotation_choice3 = widgets.Dropdown(
        options=[('',0),('Point A', 1), ('Point B', 2), ('Point C', 3), ('Point D', 4), ('Origin', 5)],
        value=0,
        description='',
)

if(random_object == 1):
    rotation_choice3.options = [('',0),('Point A', 1), ('Point B', 2), ('Point C', 3), ('Origin', 4)]

rp_text3 = widgets.HTML("<strong> Rotation Point: </strong>")
rd_text3 = widgets.HTML("<strong> Rotation Degrees: </strong>")
answer_text3 = widgets.HTML("")

answer_output3 = widgets.HBox(children=[rp_text3, rotation_choice3, rd_text3, degree_choice3, submit_button3])
widget_output3 = widgets.VBox(children=[new_button3, answer_output3, answer_text3])

new_button3.layout.margin = '0px 0px 10px 600px'

degree_choice3.layout.width = '100px'
rotation_choice3.layout.width = '100px'

def draw_plot3(xO,yO,xRo,yRo):
    data = []
    data.append(dict(
        visible = True,
        line=dict(color='#00FF00', width=3),
        mode = 'lines+markers',
        name = 'Original',
        hoverinfo = 'x+y',
        x = xO,#[1, 2.5, 4, 1],
        y = yO))#[1, 4, 1, 1]))

    data.append(dict(
        visible = True,
        line=dict(color='#00CED1', width=3),
        mode = 'lines+markers',
        name = 'Translation',
        hoverinfo = 'x+y',
        x = xRo,#[1, 2.5, 4, 1],
        y = yRo))#[1, 4, 1, 1]))

    layout = go.Layout(
        title = '',
        showlegend=False,
        hovermode = 'closest',
        yaxis = dict(
            title= '',
            ticklen= 5,
            dtick= 1,
            gridwidth= 2,
            range=[-10,10],
            showgrid=True,
        
        ),
        xaxis= dict(
            title= '',
            ticklen= 5,
            dtick=1,
            gridwidth= 2,
            range=[-10,10],
            showgrid=True,
        ),
        #autosize=False,
        width=750,
        height=750,
        annotations=[
            dict(
                x=1.0,
                y=-0.10,
                showarrow=False,
                text='X Axis',
                xref='paper',
                yref='paper',
                font=dict(
                    size=14,
                ),
            ),
            dict(
                x=-0.10,
                y=1.0,
                showarrow=False,
                text='Y Axis',
                textangle=-90,
                xref='paper',
                yref='paper',
                font=dict(
                    size=14,
                ),
            ),
        ],
    )

    fig = dict(data=data, layout=layout)
    
    
    clear_output(wait=True)
    display(widget_output3)
    iplot(fig, filename='basic-scatter')
    
def check_answer3(change):
    global random_degree
    global random_object
    global random_point
        
    answer_point = random_point
    answer_degree = random_degree
            
    input_degree = degree_choice3.value
    if(input_degree == 6):
        input_degree = 1
    elif(input_degree == 5):
        input_degree = 2
    elif(input_degree == 4):
        input_degree = 3

    input_point = rotation_choice3.value
    if(random_object == 0):
        if(answer_degree == 3):
            answer_degree = 1
        elif(answer_degree == 1):
            answer_degree = 3
        
        if((input_point == 4) and (input_degree == 1)):
            input_point = 3
            input_degree = 3
        elif((input_point == 3) and (input_degree == 1)):
            input_point = 2
            input_degree = 3
        elif((input_point == 2) and (input_degree == 1)):
            input_point = 1
            input_degree = 3
        elif((input_point == 4) and (input_degree == 3)):
            input_point = 1
            input_degree = 1
            
        if((answer_point == 4) and (answer_degree == 1)):
            answer_point = 3
            answer_degree = 3
        elif((answer_point == 3) and (answer_degree == 1)):
            answer_point = 2
            answer_degree = 3
        elif((answer_point == 2) and (answer_degree == 1)):
            answer_point = 1
            answer_degree = 3
        elif((answer_point == 4) and (answer_degree == 3)):
            answer_point = 1
            answer_degree = 1

        if(input_point == answer_point and input_degree == answer_degree):  
            answer_text3.value = "You are right! That is the correct rotation and point."
        else:
            answer_text3.value = "That is not the correct rotation and point."
    else:   
        if(answer_degree == 3):
            answer_degree = 1
        elif(answer_degree == 1):
            answer_degree = 3
            
        if(input_point == answer_point and input_degree == answer_degree):  
            answer_text3.value = "You are right! That is the correct rotation and point."
        else:
            answer_text3.value = "That is not the correct rotation and point."
            
    #display("Answer Degree: " + str(answer_degree))
    #display("Answer Point: " + str(answer_point))
    #display("Input Degree: " + str(input_degree))
    #display("Input Point: " + str(input_point))

def new_example3(change):
    global random_degree
    global random_object
    global random_point
    
    answer_text3.value = ""
    rotation_choice3.value = 0
    degree_choice3.value = 0
            
    X1 = random.randint(-5,5)
    Y1 = random.randint(-5,5)

    random_degree = random.randint(1,3)

    random_object = random.randint(0,1)

    if(random_object == 0):
        rotation_choice3.options = [('',0),('Point A', 1), ('Point B', 2), ('Point C', 3), ('Point D', 4), ('Origin', 5)]
    else:
        rotation_choice3.options = [('',0),('Point A', 1), ('Point B', 2), ('Point C', 3), ('Origin', 4)]
    
    if(random_object == 0):
        random_point = random.randint(1,5)
    
        xO = [X1,X1,X1+3,X1+3,X1]
        yO = [Y1,Y1+3,Y1+3,Y1,Y1]
    
        temp_degrees = radians(90*random_degree)
        if(random_point == 1):
            rotationX = xO[0]
            rotationY = yO[0]
            x0 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            y0 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            x1 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            y1 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            x2 = rotationX + cos(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
            y2 = rotationY + sin(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
            x3 = rotationX + cos(temp_degrees+atan((yO[3]-rotationY)/(yO[3]-rotationX)))*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))
            y3 = rotationY + sin(temp_degrees+atan((yO[3]-rotationY)/(yO[3]-rotationX)))*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))     
        elif(random_point == 2):
            rotationX = xO[1]
            rotationY = yO[1]
            x0 = rotationX + cos(temp_degrees-1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            y0 = rotationY + sin(temp_degrees-1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            x1 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            y1 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))         
            x2 = rotationX + cos(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
            y2 = rotationY + sin(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
            x3 = rotationX + cos(temp_degrees+atan((yO[3]-rotationY)/(xO[3]-rotationX)))*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))
            y3 = rotationY + sin(temp_degrees+atan((yO[3]-rotationY)/(xO[3]-rotationX)))*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))     
        elif(random_point == 3):
            rotationX = xO[2]
            rotationY = yO[2]
            x0 = rotationX - cos(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            y0 = rotationY - sin(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            x1 = rotationX - cos(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            y1 = rotationY - sin(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            x2 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
            y2 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
            x3 = rotationX + cos(temp_degrees-1.5707963268)*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))
            y3 = rotationY + sin(temp_degrees-1.5707963268)*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2)) 
        elif(random_point == 4):
            rotationX = xO[3]
            rotationY = yO[3]
            x0 = rotationX - cos(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            y0 = rotationY - sin(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            x1 = rotationX - cos(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            y1 = rotationY - sin(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            x2 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
            y2 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))            
            x3 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))
            y3 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[3]-rotationX)**2+(yO[3]-rotationY)**2))      
        elif(random_point == 5):
            tempXR = xO[:]
            tempYR = yO[:]
            temp = []
            if(random_degree == 1):
                temp = tempXR[:]
                tempXR = tempYR[:]
                tempYR = temp[:]
            
                for i in range(len(tempXR)):
                    tempXR[i] = -1*tempXR[i]
                
                x0 = tempXR[0]
                x1 = tempXR[1]
                x2 = tempXR[2]
                x3 = tempXR[3]
                y0 = tempYR[0]
                y1 = tempYR[1]
                y2 = tempYR[2]
                y3 = tempYR[3]
            elif(random_degree == 2):
                for i in range(len(tempYR)):
                    tempYR[i] = -1*tempYR[i]
                    tempXR[i] = -1*tempXR[i]
            
                x0 = tempXR[0]
                x1 = tempXR[1]
                x2 = tempXR[2]
                x3 = tempXR[3]
                y0 = tempYR[0]
                y1 = tempYR[1]
                y2 = tempYR[2]
                y3 = tempYR[3]
            elif(random_degree == 3):
                temp = tempXR[:]
                tempXR = tempYR[:]
                tempYR = temp[:]
            
                for i in range(len(tempYR)):
                    tempYR[i] = -1*tempYR[i]
            
                x0 = tempXR[0]
                x1 = tempXR[1]
                x2 = tempXR[2]
                x3 = tempXR[3]
                y0 = tempYR[0]
                y1 = tempYR[1]
                y2 = tempYR[2]
                y3 = tempYR[3]
    
        xRo = [x0,x1,x2,x3,x0]
        yRo = [y0,y1,y2,y3,y0]
    else:
        random_point = random.randint(1,4)
    
        xO = [X1,X1+1.5,X1+3,X1]
        yO = [Y1,Y1+3,Y1,Y1]
    
        temp_degrees = radians(90*random_degree)
        if(random_point == 1):
            rotationX = xO[0]
            rotationY = yO[0]
            xT0 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            yT0 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            xT1 = rotationX + cos(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            yT1 = rotationY + sin(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            xT2 = rotationX + cos(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
            yT2 = rotationY + sin(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))     
        elif(random_point == 2):
            rotationX = xO[1]
            rotationY = yO[1]    
            xT0 = rotationX - cos(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            yT0 = rotationY - sin(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            xT1 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            yT1 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))         
            xT2 = rotationX + cos(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
            yT2 = rotationY + sin(temp_degrees+atan((yO[2]-rotationY)/(xO[2]-rotationX)))*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))     
        elif(random_point == 3):
            rotationX = xO[2]
            rotationY = yO[2]
            xT0 = rotationX - cos(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            yT0 = rotationY - sin(temp_degrees+atan((yO[0]-rotationY)/(xO[0]-rotationX)))*(sqrt((xO[0]-rotationX)**2+(yO[0]-rotationY)**2))
            xT1 = rotationX - cos(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            yT1 = rotationY - sin(temp_degrees+atan((yO[1]-rotationY)/(xO[1]-rotationX)))*(sqrt((xO[1]-rotationX)**2+(yO[1]-rotationY)**2))
            xT2 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))
            yT2 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xO[2]-rotationX)**2+(yO[2]-rotationY)**2))      
        elif(random_point == 4):
            tempXR = xO[:]
            tempYR = yO[:]
            temp = []
            if(random_degree == 1):
                temp = tempXR[:]
                tempXR = tempYR[:]
                tempYR = temp[:]
            
                for i in range(len(tempXR)):
                    tempXR[i] = -1*tempXR[i]
                
                xT0 = tempXR[0]
                xT1 = tempXR[1]
                xT2 = tempXR[2]
                yT0 = tempYR[0]
                yT1 = tempYR[1]
                yT2 = tempYR[2]
            elif(random_degree == 2):
                for i in range(len(tempYR)):
                    tempYR[i] = -1*tempYR[i]
                    tempXR[i] = -1*tempXR[i]
            
                xT0 = tempXR[0]
                xT1 = tempXR[1]
                xT2 = tempXR[2]
                yT0 = tempYR[0]
                yT1 = tempYR[1]
                yT2 = tempYR[2]
            elif(random_degree == 3):
                temp = tempXR[:]
                tempXR = tempYR[:]
                tempYR = temp[:]
            
                for i in range(len(tempYR)):
                    tempYR[i] = -1*tempYR[i]
            
                xT0 = tempXR[0]
                xT1 = tempXR[1]
                xT2 = tempXR[2]
                yT0 = tempYR[0]
                yT1 = tempYR[1]
                yT2 = tempYR[2]
            
        xRo = [xT0,xT1,xT2,xT0]
        yRo = [yT0,yT1,yT2,yT0]
    
    draw_plot3(xO,yO,xRo,yRo)

def erase_output(change):
    answer_text3.value = ""
    

submit_button3.on_click(check_answer3)

new_button3.on_click(new_example3)

degree_choice3.observe(erase_output, names='value')

rotation_choice3.observe(erase_output, names='value')

draw_plot3(xO,yO,xRo,yRo) 

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)