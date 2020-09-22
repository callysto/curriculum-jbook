![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=SocialStudies/Globalization/migration-necessity-for-diversity.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Migration: Necessity for diversity

Early trade routes such as the Silk Road existed in the third century BCE. Not only goods, but also people and ideas travelled those routes. However migration rates increased in 1492 when Columbus made a maiden voyage to the Caribbean. Post World War II, with the evolution of technology, people have been travelling around the world - an era which is often referred to as **Contemporary Globalization**.

Let's analyze the current trends of migration around the world. [Organisation for Economic Co-operation and Development (OECD)](https://www.oecd.org/) maintains an [International Migration Database](https://stats.oecd.org/Index.aspx?DataSetCode=MIG#) for member countries. The dataset used in this notebook is a customized version downloaded from that database.

## Migration chart for various countries
Let's first check out what information is available in our dataset. Run the code cells below to see the top 5 rows.

# Import python libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import interact, fixed, widgets, Layout, Button, Box, fixed, HBox, VBox
from IPython.display import clear_output

# Don't show warnings in output
import warnings
warnings.filterwarnings('ignore')
print('Libraries successfully imported.')

# Import the dataset (remove rows with missing entries)
df = pd.read_csv('./Data/OECD_Full_Data.csv')

# Data clean up - remove the rows for which countries are not available, rename columns
df = df[~df['Country of birth/nationality'].isin(['Unknown','Not stated','Stateless','Total'])]\
       .rename(columns={'Value':'Migrated Population','CO2':'Country Code'})

# Display the top 5 rows
df.head()

The dataset comprises of *inflow of foreign population (along with their nationalities)* in a country for various years. 

Run the code cells below and select the **Country** and **Year** for which you want to analyze data. Then click on `Show Migration Chart` button to see the [choropleth map](https://en.wikipedia.org/wiki/Choropleth_map).

# Define a callback function for "Show Migration Chart" button
def show_migration_chart(ev):
    
    clear_output(wait=True)
    
    # Define display order for the buttons and menus
    display(Box(children = [country_menu, year_menu], layout = box_layout))
    display(VBox(children = [show_button], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='100%', justify_content = 'center')))

    # Find rows in the dataset for user-selected country and year
    subset = df[df['Country'] == country_menu.value][df['Year'] == year_menu.value]
    
    # Is data available for user-selected entries?
    if(subset.shape[0] == 0):
        print('Data not available... :-(')
    else:
        # Plot choropleth map
        fig = px.choropleth(subset,   # dataframe with required data 
                    locations="Country Code",   # Column containing country codes
                    color="Migrated Population",   # Color of country should be based on population migrated
                    hover_name="Country of birth/nationality", # title to add to hover information
                    hover_data=["Migrated Population"],   # data to add to hover information
                    color_continuous_scale=px.colors.sequential.Reds,
                            
                    # Title of the chart
                    title='Inflow of foreign population to {} (Year {})<br>\
Source: <a href="https://stats.oecd.org/Index.aspx?DataSetCode=MIG#">OECD</a>'\
.format(country_menu.value, year_menu.value)
                   )
        
        # Show the figure
        fig.show()
print('Successfully defined the show_migration_chart, now run the next cell and click the button to see the map.')

# Layout for widgets
box_layout = Layout(display='flex', flex_flow='row', align_items='center', width='100%', justify_content = 'center')
style = {'description_width': 'initial'}

# Create dropdown menu for Country and Year
country_menu = widgets.Dropdown(options = df['Country'].unique(), description ='Country: ', style = style, disabled=False)
year_menu = widgets.Dropdown(options = df['Year'].unique(), description ='Year: ', style = style, disabled=False)

# Create Show Migration Flow button and define click events
show_button = widgets.Button(button_style= 'info', description="Show Migration Chart")
show_button.on_click(show_migration_chart)

# Define display order for the buttons and menus
display(Box(children = [country_menu, year_menu], layout = box_layout))
display(VBox(children = [show_button], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='100%', justify_content = 'center')))

Hover the mouse around and check out how many people migrated to your selected country.

### Questions:
1. List the top 3 countries with most inflow of population to Canada in 2017. (Hint: One of the countries is an island)

#### Discussion Questions:
2. How have immigrants contributed economically, politically, and socially in Canada? 
3. Why do people migrate to another country despite the various challenges associated with migration? Discuss how those reasons present bright ro dark side of globalization.

## Migration statistics for Alberta

Let's take a look at the migration data for Alberta made available by the [Alberta Government](https://open.alberta.ca/dataset/mobility-migrants-alberta-census-divisions-and-economic-regions/resource/f4832d23-430e-4b49-a324-560e6a404efb). First we'll see what parameters are in the dataset.

# Import the dataset (remove unnecessary columns)
df2 = pd.read_csv('./Data/AB_Migrants_Data.csv').dropna().drop(columns=['Net Intraprovincial Migrants','SGC'])

# Convert "Year" in the data from interval format to a number
df2['Year'] = df2['Year'].str[-4:].astype('int')

# Show top 5 rows
df2.head()

Before we go ahead, it would be helpful to understand each parameter in the dataset. Please go through the [glossary](https://www150.statcan.gc.ca/n1/pub/91-528-x/2015001/gloss-eng.htm) page of [Statistics Canada](https://www.statcan.gc.ca/eng/start) to get familiar with the parameters. If you are interested in how they are calculated, more information is available [here](https://www150.statcan.gc.ca/n1/en/pub/91-528-x/91-528-x2015001-eng.pdf?st=iYlctk02).

# Create a plotly figure object (like an empty figure)
fig = go.Figure()

# Create traces
for i in df2.columns[1:]:
    
    # Add trace for each column (variable) in dataset
    fig.add_trace(go.Scatter(x=df2['Year'], y=df2[i],
                    mode='lines+markers',
                    name=i))

# Change the figure layout
fig.update_layout(
    
    # Change properties of x-axis
    xaxis=dict(
        linecolor='rgb(204, 204, 204)',   # color of x-axis
        mirror=True,   # should axis be mirrored?
        linewidth=2,   # width of x-axis
        ticks='outside',   # location of x-ticks
        tickfont=dict(
            size=14,   # size of x-ticks
            color='rgb(82, 82, 82)',   # color of x-ticks
        ),
    ),
    
    # Change properties of y-axis
    yaxis=dict(
        title=dict(   
            text = 'Migrant Population<br>(in thousands)',   # y-axis title
            font=dict(
                size=16,   # size of y-axis title
            )
        ),
        linecolor='rgb(204, 204, 204)',   # color of y-axis
        mirror=True,   # should axis be mirrored?
        linewidth=2,   # width of y-axis
        ticks='outside',   # location of y-ticks
        tickfont=dict(
            size=14,   # size of y-ticks
            color='rgb(82, 82, 82)',   # color of y-ticks
        ),
    ),
    plot_bgcolor='white',   # Background color
    legend_orientation="h",   # Orientation of legend
    
    # Title for the figure (as an annotation)
    annotations=[dict(xref='paper',   
                      yref='paper', 
                      x=0.5, y=1.2,   # Position of the title
                      xanchor='center', yanchor='top',
                      text='Migration Statistics for Alberta<br>(1971-2019)',   # Text of the title
                      font=dict(size=18),   # Font size of the title
                      showarrow=False)]
)

# Show the figure
fig.show()

Hover the mouse around the graph to see the annual data for the parameter you like. Also, you can enable or disable particular dataset by clicking on the legend for that dataset. 

### Questions

1. Which two parameters have similar trends? Why do you think that might be?
2. Which trend has mostly gone upwards since the year 2000?

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)