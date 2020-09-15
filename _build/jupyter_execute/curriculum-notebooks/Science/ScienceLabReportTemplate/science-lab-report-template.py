![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/ScienceLabReportTemplate/science-lab-report-template.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Science Lab Report Template

You can add, remove, and reorganize cells and content as necessary. Before handing it in you should probably delete this cell.

For another more detailed template check out [this one](https://github.com/callysto/getting-started/tree/master/LabTemplates).

## Science Lab Report:  title

## Name and Class


## Problem


## Hypothesis


## Answers to Prelab Questions


## Materials


## Procedure
1. 
2. 
3. 

## Observations and Results


### Data Table

# change these two variables as necessary, then run this cell to store them
number_of_observations = 15
columns = ['Variable1','Variable2','Variable3']

print('We are ready to make a data table with', number_of_observations, 'rows for', columns)

# Run this cell to create your data table
import pandas as pd
import qgrid
df = pd.DataFrame(columns=pd.Series(columns))
for row_number in range(number_of_observations): # create a row for each potential observation
    df = df.append({columns[0]:0}, ignore_index=True)
df = qgrid.QgridWidget(df=df, show_toolbar=True)
df

# Run this cell to display a "Click to save data" button that saves what you added to the table above
from IPython.display import Javascript, display
from ipywidgets import widgets
def run_all(ev):
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,IPython.notebook.get_selected_index()+2)'))
button = widgets.Button(description="Click to save data")
button.on_click(run_all)
display(button)

## Analysis


### Graph

graph_title = ''
xaxis_column = 'Variable1'
yaxis_column = 'Variable2'
mode = 'markers'  # change this to 'lines' for a line graph

import plotly.graph_objects as go
recorded_data = df.get_changed_df()
fig = go.Figure(data=[go.Scatter(x=recorded_data[xaxis_column], y=recorded_data[yaxis_column], mode=mode)])
fig.update_layout(title=graph_title, xaxis_title=xaxis_column, yaxis_title=yaxis_column)
fig.show()

## Conclusion


[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)