![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/COVID-19/world-cases/COVID-19-world-cases-sunburst.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# COVID-19
## Visualizing live data from around the world

In this notebook we will have an opportunity to visualize the latest number of confirmed cases of COVID-19 around the world. 

Use this notebook to explore each affected country and continent. 

Press the Run button to run the next cell.

Note: You only need to install dependencies once. If you receive Success! after running the cell below, comment out the dependencies as follows

    # !pip install pycountry_convert
    # !pip install requests
    # !pip install pandas
    # !pip install plotly

#!pip install pycountry_convert 
#!pip install requests 
#!pip install pandas 
#!pip install plotly 
import requests as r
import pandas as pd
# Need to remove this if we upgrade to pandas 1.0.1 
from pandas.io.json import json_normalize
import pycountry_convert as pc
import plotly.offline as offline 
import plotly.graph_objs as go
print("Success!")

We are now going to download the data. 

Run the cell below to download the number of confirmed cases, the number of deaths and the latest updates. 

# Get the latest data
# Confirmed
try:
    API_response_confirmed = r.get("https://covid19api.herokuapp.com/confirmed")
    data = API_response_confirmed.json() 
    # If using pandas 1.0.1 use json_normalize(data,record_path=["locations"])
    confirmed_df = json_normalize(data,record_path=["locations"])
except:
    print("Error: check GitHub is functioning appropriately, check https://covid19api.herokuapp.com/ is not down, check fields were not renamed")
# Deaths
try:
    API_response_death = r.get("https://covid19api.herokuapp.com/deaths")
    data = API_response_death.json() 
    # If using pandas 1.0.1 use json_normalize(data,record_path=["locations"])
    death_df = json_normalize(data,record_path=["locations"])
except:
    print("Error: check GitHub is functioning appropriately, check https://covid19api.herokuapp.com/ is not down, check fields were not renamed")
# Latest
try:
    API_summary = r.get("https://covid19api.herokuapp.com/latest")
    data2 = API_summary.json()
    # If using pandas 1.0.1 use json_normalize(data2)
    summary  = json_normalize(data2)
    print("Data downloaded")
except:
    print("Error: check GitHub is functioning appropriately, check https://covid19api.herokuapp.com/ is not down, check fields were not renamed")


COVID-19 confirmed cases (first five entries)

confirmed_df.head(5)

Confirmed deaths as a result of COVID-19 (first five entries)

death_df.head(5)

Let's assign a continent code to our tables. Run the cell below to do so. 

# Assign continent codes for sunburst plot
cont_codes = []
for item in confirmed_df["country_code"]:
    try:
        cont_code = pc.country_alpha2_to_continent_code(item)
        cont_codes.append(cont_code)
    except:
        cont_codes.append(item)
        
confirmed_df["continent code"] = cont_codes
death_df["continent code"] = cont_codes
print("Continent codes appended.")

COVID-19 confirmed cases (first five entries)

confirmed_df.head(5)

Confirmed deaths as a result of COVID-19 (first five entries)

death_df.head(5)

Time to visualize! 

We will build a [sunburst chart](https://plotly.com/python/sunburst-charts/), where we display the latest number of confirmed cases in each country, as well as the latest number of deaths in each continent. 

We will need to manipulate our data a bit to create a plot. It may look like overwhelming at first, but don't worry - we separated each step. 

# Build sub DataFrame for each
conf_df = confirmed_df[['country','continent code','latest']]
deat_df = death_df[['country','continent code','latest']]

# The sunburst plot requires weights (values), labels, and parent (region, or World)
# We build the corresponding table here
# Inspired and adapted from https://pypi.org/project/world-bank-data/ 
columns = ['labels','parents',  'values']

# Build the levels 
# Level 1 - Countries
level1 = conf_df.copy()
# Rename columns
level1.columns = columns
# Add a text column - format values column
level1['text'] = level1['values'].apply(lambda pop: 'Conf {:,.0f}'.format(pop))

# Create level 2 - Continents
# Group by continent code
death_by_cont = deat_df.groupby('continent code').latest.sum().reset_index()[['continent code', 'continent code', 'latest']]
# Group by continent code
level2 = conf_df.groupby('continent code').latest.sum().reset_index()[['continent code', 'continent code', 'latest']]
# Rename columns
level2.columns = columns
level2['parents'] = 'World'
# move value to text for this level
level2['text'] = level2['values'].apply(lambda pop: ' Confirmed {:,.0f}'.format(pop))
level2['values'] = death_by_cont["latest"]

# Create level 3 - world total as of latest date
level3 = pd.DataFrame({'parents': [''], 'labels': ['World'],
                       'values': [0.0], 'text': ['{:,.0f}'.format(summary["confirmed"].sum())]})
# Create master dataframe with all levels
all_levels = pd.concat([level1,level2,level3], axis=0,sort=True).reset_index(drop=True)
print("Data manipulated")

Run the cell below to display the sunburst plot. 

Click on each continent to look at each country's COVID-19 confirmed cases. To go back, click on the continent code. 

The codes are as follows:

    EU: Europe
    AS: Asia
    NA: North America
    SA: South America
    AF: Africa
    OC: Oceania
    TL and XX contain various items not recognized by Python - the Diamond Princess Cruise ship can be found there. 

#Sunburst plot
last_date = pd.to_datetime('today').date()
fig = offline.iplot(dict(
    data=[dict(type='sunburst', hoverinfo='values', **all_levels)],
    layout=dict(title='COVID-19 Confirmed Cases as of ' + str(last_date),
                width=800,height=800,insidetextorientation='radial')),validate=False)

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)