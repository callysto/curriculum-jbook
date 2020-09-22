![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=SocialStudies/Globalization/sustainability-a-side-effect-of-globalization.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Sustainability - A side-effect of globalization?

Globalization promises prosperity, but this may impact the health of the natural environment. Economic activities across the globe have reduced earth's ability to provide necessary resources. [Global warming](https://en.wikipedia.org/wiki/Global_warming) is one of the major environmental concerns which has been largely influenced by the emission of greenhouse gases like carbon dioxide (CO<sub>2</sub>).

Let us try to find the connection between globalization and CO<sub>2</sub> emissions across the world. The [dataset](https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions) was obtained from [Our World in Data](https://ourworldindata.org/), and contains [per capita](https://en.wikipedia.org/wiki/Per_capita) CO<sub>2</sub> emission by various countries since the early 1800s.


## CO<sub>2</sub> emissions contributions of an average person in around the world

Let's check out how people in different countries contributed to the CO<sub>2</sub> emissions. Run the following cells to see a preview of the data and an animated [choropleth map](https://en.wikipedia.org/wiki/Choropleth_map).

# Import Python libraries
import pandas as pd
import plotly_express as px
from ipywidgets import interact, fixed, widgets, Layout, Button, Box, fixed, HBox, VBox
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import clear_output

# Don't show warnings in output
import warnings
warnings.filterwarnings('ignore')
print('Libraries successfully imported.')

# Import the dataset
df = pd.read_csv('./Data/co-emissions-per-capita.csv')

# Data clean up - keep rows pertaining to 1851-current and rename the columns
df = df[df['Year'] > 1850]\
     .rename(columns={'Code':'Country Code',
                         'Per capita CO₂ emissions (tonnes per capita)':'CO₂ emissions<br>(tonnes per capita)'})

# Display the top 5 rows
df.head()

# Plot an animated choropleth map (Execution of this code cell will take a little while)

fig = px.choropleth(df,   # dataframe with required data 
                    locations="Country Code",   # Column containing country codes
                    color="CO₂ emissions<br>(tonnes per capita)",   # Color of country should be based on per capita CO₂ emission
                    hover_name="Entity",   # Title to add to hover information
                    hover_data=["CO₂ emissions<br>(tonnes per capita)"],   # Data to add to hover information
                    color_continuous_scale=px.colors.sequential.Reds,   # Set the colorscale type
                    animation_frame = "Year",   # Values based on which animation frame will be prepared
                    range_color = [0,20],   # Range of the colorbar
                    
                    # Title of the chart
                    title = 'Per capita CO₂ emissions for countries around the world<br>\
Source: <a href="https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions">Our World in Data</a>'
                   )

fig.update_layout(geo=dict(showcountries=True))
# Show the figure
fig.show()

Click on the ▶ (play) button to see it change over time. Move your mouse around the map to see values for the per capita CO<sub>2</sub> emission by different countries.

### Questions
1. Before 1900, which country had the highest per capita emission? Why might that be?
2. According to the latest data, how would you rate Canada's per capita emission as compared to other countries with large populations?
3. Is there significant inequality in per capita emissions around the world? How does this relate to globalization? 

## Global CO<sub>2</sub> emissions shares of countries around the world

Now that we've seen the per capita CO<sub>2</sub> emissions for different countries, let's see if the overall emission growth trend is the same. It would also be beneficial to compare the share of different countries for different years.

Let's pull out the annual emission data from the same [source](https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions). Run the code blocks below to see pie charts showing comparison for the years you choose.

# Import the dataset and remove rows with missing values
df2 = pd.read_csv('./Data/annual-co2-emissions-per-country.csv').dropna()

# Data clean up - keep rows pertaining to 1851-current and remove entities named 'World' and 'Micronesia'
df2 = df2[df2['Year'] > 1850][df2['Entity'] != 'World'][df2['Code'] != 'FSM']

# Display top 5 rows
df2.head()

# Define a callback function for "Show CO₂ Emissions" button
def compare_annual_emissions(ev):
    
    clear_output(wait=True)
    
    # Define display order for the buttons and menus
    display(Box(children = [year1_menu, year2_menu], layout = box_layout))
    display(VBox(children = [show_button], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='100%', justify_content = 'center')))

    # Filter the rows for user-selected years and convert them to percentage
    subset1 = df2[df2['Year'] == year1_menu.value]
    subset1['Annual CO₂ emissions (tonnes)'] = (100 * subset1['Annual CO₂ emissions (tonnes)'] / subset1['Annual CO₂ emissions (tonnes)'].sum()).round(1)
    subset1 = subset1.sort_values('Annual CO₂ emissions (tonnes)',ascending=False)[:5]
    
    subset2 = df2[df2['Year'] == year2_menu.value]
    subset2['Annual CO₂ emissions (tonnes)'] = (100 * subset2['Annual CO₂ emissions (tonnes)'] / subset2['Annual CO₂ emissions (tonnes)'].sum()).round(1)
    subset2 = subset2.sort_values('Annual CO₂ emissions (tonnes)',ascending=False)[:5]
    
    # Make subplots
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Year {}'.format(year1_menu.value), 'Year {}'.format(year2_menu.value)])
    
    # Add trace for each year's bar chart
    fig.add_trace(go.Bar(name='Year {}'.format(year1_menu.value),
                         x=subset1['Entity'],
                         y=subset1['Annual CO₂ emissions (tonnes)'],
                         showlegend=False),1,1)
    
    # Add trace for each year's bar chart
    fig.add_trace(go.Bar(name='Year {}'.format(year2_menu.value),
                         x=subset2['Entity'],
                         y=subset2['Annual CO₂ emissions (tonnes)'],
                         showlegend=False),1,2)
    
    # Update yaxis properties of subplots
    fig.update_yaxes(title_text="Share in Global CO₂ Emissions (%)", row=1, col=1, range=[0,max(subset1['Annual CO₂ emissions (tonnes)'].max(),subset2['Annual CO₂ emissions (tonnes)'].max())])
    fig.update_yaxes(title_text="Share in Global CO₂ Emissions (%)", row=1, col=2, range=[0,max(subset1['Annual CO₂ emissions (tonnes)'].max(),subset2['Annual CO₂ emissions (tonnes)'].max())])
    
    # Update the title of the figure
    fig.update_layout(title_text='Top 5 countries with highest annual share in global CO₂ Emissions<br>\
Source: <a href="https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions">Our World in Data</a>')
    
    fig.show()
print('Successfully defined the compare_annual_emissions function. Run the cell below and click the button.')

# Layout for widgets
box_layout = Layout(display='flex', flex_flow='row', align_items='center', width='100%', justify_content = 'center')
style = {'description_width': 'initial'}

# Create dropdown menu for Year to be used for comparison
year1_menu = widgets.Dropdown(options = df2['Year'].sort_values().unique(), description ='Year 1: ', style = style, disabled=False)
year2_menu = widgets.Dropdown(options = df2['Year'].sort_values().unique(), description ='Year 2: ', style = style, disabled=False)

# Create "Show CO₂ Emissions" button and define click events
show_button = widgets.Button(button_style= 'info', description="Show CO₂ Emitters")
show_button.on_click(compare_annual_emissions)

# Define display order for the buttons and menus
display(Box(children = [year1_menu, year2_menu], layout = box_layout))
display(VBox(children = [show_button], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='100%', justify_content = 'center')))

Hover the mouse around to see the comparative annual contribution of the countries towards global CO<sub>2</sub> emissions for the selected years. 

### Questions:
1. Compare the CO<sub>2</sub> emissions of countries after World War I (1919) and II (1945). How have the shares changed for countries on different sides of those conflicts?
2. Have the top 5 contributors to global CO<sub>2</sub> emissions changed in the era of contemporary globalization (from 1945 to 2017)?

### Discussion:
3. What steps could governments take to reduce their share of CO<sub>2</sub> emissions and ensure sustainable globalization?

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)