![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=SocialStudies/Globalization/communication-and-globalization.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Communication and Globalization

Advances in communication technology has made the world a global village. Digital gadgets such as computers and mobile phones have revolutionized the exchange of information, affecting global diversity, identity, and culture. With the internet providing access to vast amount of information, the effects of digital advances have become increasingly more swift and complex.

Let's try to gauge the spread of digital advances around the world. The datasets from [Our World in Data](https://ourworldindata.org/internet) are used to visualize access to mobile phones, the internet, and social media platforms.

## Internet access across the globe

Let's check out the proportion of a population in a given country that has internet access. Run the following code cells to import the data and preview it.

# Import Python libraries
import pandas as pd
import plotly_express as px
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ipywidgets import interact, fixed, widgets, Layout, Button, Box, fixed, HBox, VBox
from IPython.display import clear_output
from IPython.display import HTML

# Don't show warnings in output
import warnings
warnings.filterwarnings('ignore')
print('Libraries successfully imported.')

# Import the dataset
df = pd.read_csv('./Data/share-of-individuals-using-the-internet.csv')

# Data clean up - consider the data between 2001 and 2016
df=df[df['Year'] > 2000][df['Year'] < 2017]

# Display the bottom 5 rows
df.tail()

# Plot an animated choropleth map

fig = px.choropleth(df,   # dataframe with required data 
                    locations="Code",   # Column containing country codes
                    color="Internet Access<br>(% of population)",   # Color of country should be based on internet access
                    hover_name="Entity",   # Title to add to hover information
                    hover_data=['Internet Access<br>(% of population)'],   # Data to add to hover information
                    color_continuous_scale=px.colors.sequential.Reds,   # Set the colorscale type
                    animation_frame = "Year",   # Values based on which animation frame will be prepared
                    range_color = [0,100],   # Range of the colorbar
                    
                    # Title of the chart
                    title = 'Population with internet access in various countries<br>\
Source: <a href="https://ourworldindata.org/internet">Our World in Data</a>'
                   )

# Show the figure
fig.show()

Hover your mouse over different countries on the choropleth map and see the share of population that has access to the internet.

### Discussion Questions:

1. Why do you think internet access is unequal among the countries in the world? 
2. How can we improve this [digital divide](https://en.wikipedia.org/wiki/Digital_divide)? Are you aware of any organizations working on this issue? 
3. Is high-speed internet access generally available in First Nations communities? Discuss the digital divide within Canada.

## Mobile phone access across the globe

Mobile (or cellular) phones have emerged as a disruptive digital technology due to their multiple uses and portability.

Let's visualize how many people have access to this technology. Run the following code cells to import the dataset and plot an animated choropleth map.

# Import the dataset
df2 = pd.read_csv('./Data/mobile-cellular-subscriptions-per-100-people.csv')

# Data clean up - consider the data from 1991
df2=df2[df2['Year'] > 1990]

# Show the bottom 5 rows
df2.tail()

# Plot animated choropleth map

fig = px.choropleth(df2,   # dataframe with required data 
                    locations="Code",   # Column containing country codes
                    color="Cellular subscriptions<br>(per 100 people)",   # Color of country should be based on cellular subscriptions
                    hover_name="Entity",   # Title to add to hover information
                    hover_data=["Cellular subscriptions<br>(per 100 people)"],   # Data to add to hover information
                    color_continuous_scale=px.colors.sequential.Reds,   # Set the colorscale type
                    animation_frame = "Year",   # Values based on which animation frame will be prepared
                    range_color = [0,200],   # Range of the colorbar
                    
                    # Title of the chart
                    title = 'Cellular subscriptions (per 100 people) around the world<br>\
Source: <a href="https://ourworldindata.org/internet">Our World in Data</a>'
                   )

# Show the figure
fig.show()

### Questions:

1. How does the availability of mobile phones compare to internet access?
2. How can diversity or identity be affected by communication technologies such as mobile phones?

## Are social media platforms changing the world?

With the internet and mobile phones being increasingly integrated into our lives, the use of social media platforms is increasing. One in three people of the world's 7.7 billion population is using social media. 

Let's create a bar chart animation showing monthly active users by platform since 2003. Run the code cells below.

# Import the dataset and remove an empty column
df3 = pd.read_csv('./Data/users-by-social-media-platform.csv').drop('Code',1)

# Data transformation - convert the monthly active users in billion
df3['Monthly active users'] = df3['Monthly active users']/1000000000

# Define the colors - to be used in bar chart
colors = ['violet', 'tomato', 'chocolate', 'teal', 'forestgreen', 'dodgerblue',\
          'lightcoral', 'limegreen', 'darkorange', 'goldenrod']

# Show the top 5 rows
df3.head()

# Define the function to draw a bar chart for a given year
def draw_barchart(current_year,colors=colors):
    # Find rows in the dataset for a given year
    dff = df3[df3['Year'].eq(current_year)].sort_values(by='Monthly active users', ascending=True)\
          .tail(top_x_platforms_slider.value)
    
    ax.clear()   # Clear the figure (in case any plot exists already)
    ax.barh(dff['Entity'], dff['Monthly active users'],color=colors)   # plot the horizontal bar chart
    dx = dff['Monthly active users'].max() / 200   # margin for the text in plot
    
    # Specify annotations for each row in the dataframe
    for i, (value, name) in enumerate(zip(dff['Monthly active users'], dff['Entity'])):
        ax.text(value-dx, i-0.12, name, ha='right', size=14, weight=600)   # Text/formatting for the name of the social media platform
        ax.text(value+dx, i-0.12, "{0:.3f} billion".format(value), ha='left', size=14)   # Text/formatting for monthly active users
    ax.text(1, 0.4, current_year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)   # Text/formatting for the corresponding year
    ax.text(0, 1.06, 'Monthly active users (billion)', transform=ax.transAxes, size=14, color='#777777')   # Specify y-axis title
    ax.xaxis.set_ticks_position('top')   # Set position of x-ticks
    ax.tick_params(axis='x', colors='#777777', labelsize=14)   # Set parameters for x-ticks
    ax.set_yticks([])   # Set empty y-ticks
    ax.set_xlim([0,2.5])   # Set x-axis limits
    ax.margins(0, 0.01)   # Set margins
    ax.grid(which='major', axis='x', linestyle='-')   # Set gridline properties
    ax.set_axisbelow(True)   # Specify axis location
    ax.text(0, 1.15, 'Most used social media platforms (2004 to 2017)',
            transform=ax.transAxes, size=24, weight=600, ha='left', va='top')   # Specify plot title
    plt.box(False)   # Disable box surrounding the plot

# Define a callback function for "Show Bar Chart" button
def draw_barchart2(ev):
    clear_output(wait=True)
    
    # Define display order for the buttons and menus
    display(Box(children = [top_x_platforms_slider,show_button1], \
                layout = Layout(display= 'flex', flex_flow= 'column', \
                                align_items= 'center', width='100%', \
                                justify_content = 'center')))
    
    global fig, ax   # Set figure as a global object
    
    # Create an empty figure object with given size
    fig, ax = plt.subplots(figsize=(15, 8)) 
    
    # Create animation - each frame shows data for one year
    animator = animation.FuncAnimation(fig, draw_barchart, frames=range(2002,2018),interval=750, repeat=False)
    ANI = HTML(animator.to_jshtml())
    plt.close()
    display(ANI)
print('We have defined the functions draw_barchart and draw_barchart2.')

Run the cell below and select how many top social media platforms you want to see in the animation. Then click the `Show Animation` button.

# Layout for widgets
box_layout = Layout(display='flex', flex_flow='row', align_items='center', width='100%', justify_content = 'center')
style = {'description_width': 'initial'}

# Create dropdown menu for Artist and slider for How Many Top Platforms
top_x_platforms_slider = widgets.IntSlider(value = 5, min = 5, max = 10, description = "Number of Top Platforms", style = style)

# Create Show Top Artists button and define click events
show_button1 = widgets.Button(button_style= 'info', description="Show Animation")
show_button1.on_click(draw_barchart2)

# Define display order for the buttons and menus
display(Box(children = [top_x_platforms_slider,show_button1], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='100%', justify_content = 'center')))

Run the animation by clicking on the ▶ (play) button. 

### Discussion Questions:
1. Based on the trend in recent years, do you think Whatsapp might soon have more users than YouTube?
2. Discuss how social media use has changed people's sense of community and socialization practices. Do you think we are we becoming "high-tech hermits" or creating a new kind of social connection?

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)