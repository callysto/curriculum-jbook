![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=SocialStudies/Globalization/music-is-ubiquitous.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Music is ubiquitous

Music is one of the ways we humans express ourselves. Not only can music help form your identity, it has also helps people to connect in this globalizing world. Sharing an interest for a particular kind of music has allowed artists to travel across the globe. 

With online streaming platforms it has become easier ever to listen music from artists from different countries. Let's analyse the dataset from [Spotify](https://spotifycharts.com/regional), an audio streaming platform, which is available on [Kaggle](https://www.kaggle.com/datasets). 

The [original dataset](https://www.kaggle.com/edumucelli/spotifys-worldwide-daily-song-ranking/version/3) (with more than 3 million rows!) contained information about top 200 artists in daily charts in various countries for 2017. It has been modified to contain only top 10 artists which reduced the number of rows to 191848, still a [big dataset](https://en.wikipedia.org/wiki/Big_data) to work with. Als, note that the top artists were selected based on the *streams* of their tracks i.e. *number of times* songs were played by Spotify users.

## Popularity of an artist across the globe 
Let's check how many times tracks from a user-selected artist were streamed on Spotify. 

Run the code cells below and check what our dataset contains.

# You can comment out the following line if the module is already installed
!pip install wikipedia

# Import Python libraries
import pandas as pd
import calendar
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import interact, fixed, widgets, Layout, Button, Box, fixed, HBox, VBox
import wikipedia
from IPython.display import clear_output
import random

# Don't show warnings in output
import warnings
warnings.filterwarnings('ignore')
clear_output()

print('Libraries successfully imported.')

# Import the dataset and remove rows with missing entries
df = pd.read_csv('./Data/top_10_artists_spotify_2017_final.csv').dropna()

# Import country codes (required for the choropleth map)
country_codes = pd.read_csv('./Data/country_codes.csv',sep='\t')
country_codes['2let'] = country_codes['2let'].str.lower()   # Convert country codes to lower case

# Display the top 5 rows
df.head()

# Define a callback function for "Show Popularity" button
def show_popularity(ev):
    clear_output(wait=True)
    
    # Define display order for the buttons and menus
    display(Box(children = [artist_menu], layout = box_layout))
    display(Box(children = [show_button], layout = Layout(display= 'flex', flex_flow= 'row', align_items= 'center', width='100%', justify_content = 'center')))

    # Find total streams for a user-selected artist across countries
    subset = df[df['Artist'] == artist_menu.value].groupby('Region')
    total_streams = subset['Streams'].sum().to_frame('Streams').reset_index()
    
    # Merge the 3 letter country codes (required in plotly express) with the data
    final = total_streams.merge(country_codes, left_on='Region', right_on='2let', how='inner')\
            .drop('2let',1)\
            .rename(columns={'3let':'Country Code'})
    
    # Find the wikipedia page for the artist 
    try:
        p = wikipedia.page(artist_menu.value)
    # If can't find the exact page, get the closest one    
    except wikipedia.exceptions.DisambiguationError as e:
        s = e.options[0]
        p = wikipedia.page(s)
    
    # Plot the choropleth map for the user-selected artist
    fig = px.choropleth(final,   # dataframe with required data 
                    locations="Country Code",   # Column containing country codes
                    color="Streams",   # Color of country should be based on number of streams
                    hover_name="Countrylet", # title to add to hover information
                    hover_data=["Streams"],   # data to add to hover information
                    projection='natural earth',   # preferred view of choropleth map
                    
                    # Add title for the map (hyperlinks for wiki page of artist and dataset are added)    
                    title = 'Popularity of<a href="{}" > {} </a>by streams of tracks in daily Top 10 chart (2017)<br>Source: \
<a href="https://www.kaggle.com/edumucelli/spotifys-worldwide-daily-song-ranking/version/3">\
Spotify through Kaggle Datasets</a>'.format(p.url,artist_menu.value))
    fig.update_layout(geo=dict(showcountries=True))
    # Show the figure
    fig.show()
print('Defined the show_popularity function.')

Run the code cell below and select the artist you want to analyze popularity of. Don't forget to click on `Show Popularity` button.

# Layout for widgets
box_layout = Layout(display='flex', flex_flow='row', align_items='center', width='100%', justify_content = 'center')
style = {'description_width': 'initial'}

# Create dropdown menu for Artist
artist_menu = widgets.Dropdown(options = df['Artist'].sort_values().unique(), description ='Artist: ', style = style, disabled=False)

# Create Show Popularity button and define click events
show_button = widgets.Button(button_style= 'info', description="Show Popularity")
show_button.on_click(show_popularity)

# Define display order for the buttons and menus
display(Box(children = [artist_menu], layout = box_layout))
display(Box(children = [show_button], layout = Layout(display= 'flex', flex_flow= 'row', align_items= 'center', width='100%', justify_content = 'center')))

Try it for various artists. If you don't know much about the artist, click the link in the title of the map which will take you to the *Wikipedia* page of the artist. Hover your mouse over different countries and see how many times tracks were streamed.

### Questions:
1. Which artists were popular in North America, Europe, as well as the Asia-Pacific region?
2. Share your thoughts on how music (and media in general) has brought people together and become the globalizing force.

## Artists popular in different countries
Let's try to gauge the effect of globalization on music listened by people of various countries. We will plot the top artists streamed on Spotify.

Run the code cells below and see that the additional columns (`Country Name` and `Country Code`) are added to the dataset.

# Add Country Name and 3 letter Country Code to the dataset
df_with_country_names = df.merge(country_codes, left_on='Region', right_on='2let', how='inner')\
                    .drop('2let',1)\
                    .rename(columns={'3let':'Country Code','Countrylet':'Country Name'})

# Display top 5 rows
df_with_country_names.head()

# Create a dataframe containing names of 12 months and number
months_all = pd.DataFrame(calendar.month_name[1:],columns={'Name'})
months_all['Number'] = list(range(1,13))

# Define a callback function for "Show Top Artists" button
def show_top_3_artists(ev):
    clear_output(wait=True)
    
    # Define display order for the buttons and menus
    display(Box(children = [country_menu], layout = box_layout))
    display(Box(children = [top_x_artists_slider,show_button1], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='100%', justify_content = 'center')))
    
    # How many top artists will be shown in the chart (user-selected value)
    top_x_artists = top_x_artists_slider.value
    
    # Query the data for the user-selected country
    subset = df_with_country_names[df_with_country_names['Country Name'] == country_menu.value]
    
    # Convert Dates column to pandas datetime format and identify in which month the date falls in
    # (This is required as we are trying to plot a bar chart on a monthly basis)
    subset['Date'] = pd.to_datetime(subset['Date'])
    subset['Month'] = [months_all['Name'][months_all['Number'] == i.month].iloc[0] for i in subset['Date']]
    
    total_streams = []   # Create an empty list
    
    # Import colors to be assigned to each artist
    df_colors = pd.read_csv('./Data/colors_plotly.csv', header=None)   # Import list of colors available in plotly
    count = 0   # Initiate count
    colors = {}   # Create an empty dictionary
    
    # Create a plotly figure object (like an empty figure)
    fig = go.Figure()
    
    # Get the number of streams for all artists for each month in Year 2017
    for i in range(0,months_all.shape[0]):
        month_curr = months_all['Name'][i]   # Get the month name
        top_artists = subset[subset['Month'] == month_curr].groupby('Artist')   # Group data by the artists
        
        # Calculate total streams 
        total_streams = top_artists['Streams'].sum().sort_values(ascending=False).to_frame('Streams').reset_index()[:top_x_artists]
        
        # Add a trace in the bar chart 
        if(total_streams.shape[0] > 0):
            for j in range(0,top_x_artists):
                
                # Assign color to an artist
                if total_streams['Artist'].iloc[j] not in colors.keys():
                    colors[total_streams['Artist'].iloc[j]] = list(df_colors[0])[count]   # Assign color in order from the list
                    count += 1   # Increase count
                
                fig.add_trace(go.Bar(name=total_streams['Artist'].iloc[j], x=[(month_curr)], y=[total_streams['Streams'].iloc[j]], \
                                     showlegend = False, width = 0.8, offset=[0,0], text = total_streams['Artist'].iloc[j], textposition='auto',
                                     marker={'color':colors[total_streams['Artist'].iloc[j]]}))
                                    
    # Change the chart layout
    fig.update_layout(xaxis_tickangle=-45,   # Angle of x-axis ticks
                      xaxis_tickmode='linear',   # Tickmode of x-axis ticks
                      yaxis=dict(title='Streams<br>(k=thousand, M=million)'),   # Title for y-axis
                      
                      
                      # Title for the bar chart
                      title_text='Top {} artist(s) in {} by streams of tracks in \
daily Top 10 chart (2017)<br>Source: <a href="https://www.kaggle.com/edumucelli/spotifys-worldwide-daily-song-ranking/version/3">\
Spotify through Kaggle Datasets</a>'.format(top_x_artists_slider.value, country_menu.value))

    # Show figure 
    fig.show()
print('Successfully defined the show_top_3_artists function.')

Run the cell below. Select the country and move the slider to choose how many top artist you want to see in the bar chart. Then click on `Show Top Artists` button.

# Layout for widgets
box_layout = Layout(display='flex', flex_flow='row', align_items='center', width='100%', justify_content = 'center')
style = {'description_width': 'initial'}

# Create dropdown menu for Artist and slider for How Many Top Artists
country_menu = widgets.Dropdown(options = df_with_country_names['Country Name'].sort_values().unique(), description ='Country: ', style = style, disabled=False)
top_x_artists_slider = widgets.IntSlider(value = 3, min = 1, max = 5, description = "How Many Top Artists", style = style)

# Create Show Top Artists button and define click events
show_button1 = widgets.Button(button_style= 'info', description="Show Top Artists")
show_button1.on_click(show_top_3_artists)

# Define display order for the buttons and menus
display(Box(children = [country_menu], layout = box_layout))
display(Box(children = [top_x_artists_slider,show_button1], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='100%', justify_content = 'center')))

Hover the mouse to see artist names and the number of times their tracks were streamed. 

### Questions:
1. Are the top three artists in Canada all Canadians?
2. Do you think music can affect the cultural identity of various communities?
3. Are you aware of steps taken by countries, particularly Canada, to protect local artists or performers in this era of globalization?

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)