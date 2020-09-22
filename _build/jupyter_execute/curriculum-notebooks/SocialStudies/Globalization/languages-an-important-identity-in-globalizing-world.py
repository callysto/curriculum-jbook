![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=SocialStudies/Globalization/languages-an-important-identity-in-globalizing-world.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Languages: An important identity in globalizing world

Language is an important identity of the people. Not only does language provide a medium to communicate, but also it binds the community together. Therefore, it is essential to preserve linguistic diversity in the globalizing world. 

Let's check out various languages that once existed or currently exist on Earth. [UNESCO](https://en.unesco.org/) has compiled an [atlas](http://www.unesco.org/languages-atlas/index.php?hl=en&page=atlasmap) which contains various statistics about languages. A [choropleth map](https://en.wikipedia.org/wiki/Choropleth_map) is used to visualize this linguistic geographical dataset. 

# You can comment out the following lines if these modules are already installed
!pip install googletrans
!pip install gTTS

# Import Python libraries
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ipywidgets import interact, fixed, widgets, Layout, Button, Box, fixed, HBox, VBox
import googletrans
import gtts
from IPython.display import Audio, display, clear_output

# Don't show warnings in output
import warnings
warnings.filterwarnings('ignore')
clear_output()

print('Libraries successfully imported.')

# Import the dataset
df = pd.read_csv('./Data/languoid.csv')

# Data clean up - keep required columns
df = df[df['level'] == 'language'] \
       [['name','child_dialect_count','latitude','longitude','status']] \
       .dropna()   # remove rows with missing entries

# Display top 5 rows
df.head()

# This cell will take at least couple of minutes to run as we are trying to plot more than 7000 languages

# Define color scheme
colors = {'safe':'rgb(61,145,64)', 'vulnerable':'rgb(31,117,254)', 'definitely endangered':'rgb(137,207,240)', \
          'severely endangered':'rgb(255,191,0)', 'critically endangered':'rgb(255,0,0)', 'extinct':'rgb(0,0,0)'}

# Create a plotly figure object (like an empty figure)
fig = go.Figure()

# Create a marker with desired properties for each language in the dataset
for i in range(0,df.shape[0]):
    df_row = df.iloc[i]   # Pass each row in the dataset
    fig.add_trace(go.Scattergeo(
        lon = [df_row['longitude']],   # longitude
        lat = [df_row['latitude']],   # latitude 
        text = 'Dialects: {0} <br>Status: {1}'.format(df_row['child_dialect_count'],df_row['status']),   # text accompanying the dataset
        name = df_row['name'],   # name of the language
        hoverinfo = 'name + text',   # specify information to be shown when a pointer is hovered over a marker
        marker = dict(
            size=9,
            color=colors[df_row['status']],
            line_width=0),   # marker properties
        showlegend = False   # remove legend
        )
    )
    
# Update figure properties    
fig.update_layout(
    # Add title (see how hyperlink is added)
    title_text = 'Languages around the world<br>\
Source: <a href="http://www.unesco.org/languages-atlas/index.php?hl=en&page=atlasmap">\
UNESCO</a>',
    # Other geological properties of the map
    geo = dict(
        resolution=50,
        showcoastlines=True,
        showframe=False,
        showland=True,
        landcolor="lightgray",
        showcountries=True,
        countrycolor="white" ,
        coastlinecolor="white",
        bgcolor='rgba(255, 255, 255, 0.0)'
    )
)

# Show the figure
fig.show()

Hover over markers in the map and see the dialects and status of various languages. Feel free to zoom in/out as necessary to spot various languages in a country of your choice.

The colors indicate the [status of a language](http://www.unesco.org/languages-atlas/en/statistics.html).

### Questions:

1. Which color indicates a language that is safe from extinction? Which are the two continents with most safe languages?
2. Why do you think languages disappear? What are possible threats to linguistic diversity?
3. Could we revive a language that is on the brink of extinction? How?
4. Do you think that having more dialects makes a language safer or more vulnerable?

## Languages spoken within a country

Now that we know about various languages, let's dive a bit deeper. We'll analyze languages spoken in various countries and how they have changed over time, using a demographic dataset from the [United Nations](http://data.un.org/Data.aspx?d=POP&f=tableCode:27).

# Import the dataset
df2 = pd.read_csv('./Data/UNdata_Countrywise.csv')
df2 = df2.iloc[:-79]   # Remove footnotes

# Display top 5 rows
df2.head()

def show_bar_chart(ev):
    clear_output(wait=True)
    
    # Define display order for the buttons and menus
    display(Box(children = [country_menu], layout = box_layout))
    display(VBox(children = [show_button], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='100%', justify_content = 'center')))
    
    # Filter the data for given country and gender type
    to_be_removed = ['Unknown','Not stated','None','Total']   # Remove these categories
    df2_sub = df2[df2['Country or Area'] == country_menu.value] \
              [df2['Sex'] == 'Both Sexes'] \
              [df2['Area'] == 'Total'] \
              [~df2['Language'].isin(to_be_removed)]
    
    # Plot the pie chart
    if(df2_sub.shape[0] == 0): 
        print('Sorry... data not available :-(')   # Show comment if data is not available
    else:
        years = df2_sub['Year'].unique()[0:2]   # Show data for two latest years
        
        # Make subplots
        fig = make_subplots(rows=1, cols=len(years), subplot_titles=['Year {}'.format(i) for i in years])

        # Add trace for each year's bar chart
        for i,j in enumerate(years):
            
            new_df = df2_sub[df2_sub['Year'] == j]   # Filter the data for each subplot
            new_df['Value'] = (100 * new_df['Value'] / new_df['Value'].sum()).round(1)   # Convert population to percent
            new_df = new_df.sort_values('Value',ascending=False)[:5]   # Sort values in descending order
            
            fig.add_trace(go.Bar(name='Year {}'.format(j),x=new_df['Language'],y=new_df['Value'],
                                 showlegend=False),1,i+1)   # Add the trace for each subplot

        # Update yaxis properties of subplots
        fig.update_yaxes(title_text="Population (%)", row=1, col=1, range=[0,100])
        fig.update_yaxes(title_text="Population (%)", row=1, col=2, range=[0,100])

        # Update the title of the figure
        fig.update_layout(title_text='Top 5 languages spoken in {}<br>\
Source: <a href="http://data.un.org/Data.aspx?d=POP&f=tableCode:27">\
United Nations</a>'.format(country_menu.value))
    
        fig.show()
print('Defined the function show_bar_chart')

Run the cell below and select the country and gender you want to visualize. Don't forget to click on `Show Bar Chart` button.

# Layout for widgets
box_layout = Layout(display='flex', flex_flow='row', align_items='center', width='100%', justify_content = 'center')
style = {'description_width': 'initial'}

# Create dropdown menu for Country and Gender
country_menu = widgets.Dropdown(options = df2['Country or Area'].unique(), description ='Country: ', style = style, disabled=False)

# Create Show Pie Chart button and define click events
show_button = widgets.Button(button_style= 'info', description="Show Bar Chart")
show_button.on_click(show_bar_chart)

# Define display order for the buttons and menus
display(Box(children = [country_menu], layout = box_layout))
display(VBox(children = [show_button], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='100%', justify_content = 'center')))

Each bar chart here is for a year in which data were collected. Move your cursor around to see how much of the total population speak a particular language and how that pattern has changed over time.

### Questions:
1. List the top 5 languages in Canada according to the latest data (2016).
2. Has use of languages other than *English* and *French* increased among Canadians over time? 
3. How do you think globalization affects the spread languages across the borders?

## Exploring other languages

Let's learn a little of some other languages. Here we will translate some English words into a language of your choice. The translation will be accompanied by an audio clip to show you how the translated word is pronounced.

all_languages = gtts.lang.tts_langs()
all_languages = {v: k for k, v in all_languages.items()}

def translate_and_pronounce(ev):
    clear_output(wait=True)
    
    # Define display order for the buttons and menus
    display(Box(children = [textbox_input, languages_menu], layout = box_layout))
    display(VBox(children = [show_button], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='100%', justify_content = 'center')))

    # Create a translator class (like a template) using Google Translator
    translator = googletrans.Translator()
    translation_data = translator.translate(textbox_input.value,\
                       dest=all_languages[languages_menu.value])   # Supply text to translate and language
    translation = translation_data.extra_data['translation'][0][0]   # Extract translated data
    
    # Extract pronunciation for the translated text
    if(len(translation_data.extra_data['translation']) == 2):
        pronunciation = translation_data.extra_data['translation'][1][-1]
    else:
        pronunciation = 'None - Speak as you read'   # For languages using Roman letters
    print('\n')
    
    # Create and display textbox for "Text" and dropdown menu for languages
    textbox_translation = widgets.Text(value = translation, description = 'Translation: ', disabled = True, style = style)
    textbox_pronunciation = widgets.Text(value = pronunciation, description = 'Pronunciation: ', disabled = True, style = style)
    display(Box(children = [textbox_translation, textbox_pronunciation], layout = box_layout))  
       
    # Create an audio file for the translated text using Google Text-to-Speech
    tts = gtts.gTTS(translation, lang=all_languages[languages_menu.value])
    tts.save('audio.mp3')
    
    # Display audio widget
    display(Audio('audio.mp3'))
print('Defined the translate_and_pronounce function, run the cell below to use it.')

# Layout for widgets
box_layout = Layout(display='flex', flex_flow='row', align_items='center', width='100%', justify_content = 'center')
style = {'description_width': 'initial'}

# Create textbox for "Text" and dropdown menu for languages
textbox_input = widgets.Text(value = '',description = 'Text: ', disabled = False)
languages_menu = widgets.Dropdown(options = list(all_languages.keys())[:-18], description ='Language: ', style = style, disabled=False)

# Create Translate button and define click events
show_button = widgets.Button(button_style= 'info', description="Translate")
show_button.on_click(translate_and_pronounce)

# Define display order for the buttons and menus
display(Box(children = [textbox_input, languages_menu], layout = box_layout))
display(VBox(children = [show_button], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='100%', justify_content = 'center')))

### Questions:

1. In this era of globalization, how important do you think it is for people to learn additional languages?
2. List some scripts (alphabets) that are different from the [Roman](https://en.wikipedia.org/wiki/Latin_script) one we use in English (e.g. [Devanagari](https://en.wikipedia.org/wiki/Devanagari)).

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)