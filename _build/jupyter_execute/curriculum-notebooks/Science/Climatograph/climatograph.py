![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/Climatograph/climatograph.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Climatograph

A climatograph (or [climograph](https://en.wikipedia.org/wiki/Climograph)) is a visualization of the monthly average [precipitation](https://simple.wikipedia.org/wiki/Precipitation) and [temperature](https://simple.wikipedia.org/wiki/Temperature) at a particular location to show the climate there.

In this notebook we are using climate data from [The World Bank](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets) because we are [allowed to share and remix](https://creativecommons.org/licenses/by/4.0/) their content.

Select the next cell and click the `▶Run` button to import the code libraries that we will use.

!pip install geopy
import pandas as pd
import plotly.graph_objs as go
import numpy as np
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='Callysto Climatograph')
print('Libraries successfully imported.')

## Data

In the following cell, change the city or town name in `location = 'Calgary, AB'` to something like `location = 'Honolulu'`.

You can also change `year = 2016` to any year between `1991` and `2016`.

`Run` the cell to get and show the data.

location = 'Calgary, AB'

coordinates = geolocator.geocode(location)
latitude = coordinates.latitude  # if geolocator isn't working, you can manually set the lat and long here
longitude = coordinates.longitude

precipitation_url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/pr/1901-2016/'+str(latitude)+'$cckp$'+str(longitude)+'/'+str(latitude)+'$cckp$'+str(longitude)
df_precipitation_all = pd.read_csv(precipitation_url)
df_precipitation = df_precipitation_all.drop(columns=[' Longitude', ' Latitude', ' Year']).replace(' Average','',regex=True).replace(' ','',regex=True).rename(columns={'Rainfall - (MM)':'Precipitation (mm)', ' Statistics':'Month'})
dfp = df_precipitation.groupby('Month').aggregate(np.mean)

temperature_url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1991-2016/'+str(latitude)+'$cckp$'+str(longitude)+'/'+str(latitude)+'$cckp$'+str(longitude)
df_temperature_all = pd.read_csv(temperature_url)
df_temperature = df_temperature_all.drop(columns=[' Longitude', ' Latitude', ' Year']).replace(' Average','',regex=True).replace(' ','',regex=True).rename(columns={'Temperature - (Celsius)':'Temperature (°C)', ' Statistics':'Month'})
dft = df_temperature.groupby('Month').aggregate(np.mean)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
climate_data = dfp.join(dft)
climate_data.index = pd.CategoricalIndex(climate_data.index, categories=months, ordered=True)
climate_data = climate_data.sort_index()
climate_data

## Graph

`Run` the next cell to make a graph.

trace1 = go.Bar(x=climate_data.index.values.tolist(),y=climate_data['Precipitation (mm)'],name='Precipitation')
trace2 = go.Scatter(x=climate_data.index.values.tolist(),y=climate_data['Temperature (°C)'],name='Average Temperature (°C)',yaxis='y2')
layout = go.Layout(
    title= ('Climatograph for '+location+' ('+str(latitude)+','+str(longitude)+')'),
    yaxis=dict(title='Total Precipitation (mm)', titlefont=dict(color='blue'), tickfont=dict(color='blue')),
    yaxis2=dict(title='Average Temperature (°C)', titlefont=dict(color='red'), tickfont=dict(color='red'), overlaying='y', side='right'),
    showlegend=False)
fig = go.Figure(data=[trace1, trace2], layout=layout)
fig.update_yaxes(showgrid=False)
fig.show()

On the graph you can mouseover to check values and also zoom in and out.

You can download your climatograph using the 📷 button.

### Climateograph for a Single Year

Run the following code if you'd prefer a single-year climatograph.

location = 'Calgary, AB'
year = 2016
# year can be any between 1901 and 2016

coordinates = geolocator.geocode(location)
latitude = coordinates.latitude  # if geolocator isn't working, you can manually set the lat and long here
longitude = coordinates.longitude

precipitation_url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/pr/1901-2016/'+str(latitude)+'$cckp$'+str(longitude)+'/'+str(latitude)+'$cckp$'+str(longitude)
df_precipitation_all = pd.read_csv(precipitation_url)
df_precipitation = df_precipitation_all[df_precipitation_all[' Year']==year].drop(columns=[' Longitude', ' Latitude', ' Year']).replace(' Average','',regex=True).replace(' ','',regex=True)
dfp = df_precipitation.rename(columns={'Rainfall - (MM)':'Precipitation (mm)', ' Statistics':'Month'}).set_index('Month')

temperature_url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1991-2016/'+str(latitude)+'$cckp$'+str(longitude)+'/'+str(latitude)+'$cckp$'+str(longitude)
df_temperature_all = pd.read_csv(temperature_url)
df_temperature = df_temperature_all[df_temperature_all[' Year']==year].drop(columns=[' Longitude', ' Latitude', ' Year']).replace(' Average','',regex=True).replace(' ','',regex=True)
dft = df_temperature.rename(columns={'Temperature - (Celsius)':'Temperature (°C)', ' Statistics':'Month'}).set_index('Month')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
climate_data = dfp.join(dft)
climate_data.index = pd.CategoricalIndex(climate_data.index, categories=months, ordered=True)
climate_data = climate_data.sort_index()

trace1 = go.Bar(x=climate_data.index.values.tolist(),y=climate_data['Precipitation (mm)'],name='Precipitation')
trace2 = go.Scatter(x=climate_data.index.values.tolist(),y=climate_data['Temperature (°C)'],name='Average Temperature (°C)',yaxis='y2')
layout = go.Layout(
    title= (str(year)+' Climatograph for '+location+' ('+str(latitude)+','+str(longitude)+')'),
    yaxis=dict(title='Total Precipitation (mm)', titlefont=dict(color='blue'), tickfont=dict(color='blue')),
    yaxis2=dict(title='Average Temperature (°C)', titlefont=dict(color='red'), tickfont=dict(color='red'), overlaying='y', side='right'),
    showlegend=False)
fig = go.Figure(data=[trace1, trace2], layout=layout)
fig.update_yaxes(showgrid=False)
fig.show()

### Animated Climatograph

If you are interested in [animating graphs](https://plot.ly/python/animations/) over time, the following two code cells might be a good place to start.

import plotly.express as px
max_rainfall = df_precipitation_all['Rainfall - (MM)'].max()
fig = px.bar(df_precipitation_all.replace(' Average','',regex=True), x=' Statistics', y='Rainfall - (MM)', animation_frame=' Year', range_y=[0,max_rainfall])
fig.show()

max_temperature = df_temperature_all['Temperature - (Celsius)'].max()
min_temperature = df_temperature_all['Temperature - (Celsius)'].min()
fig = px.line(df_temperature_all.replace(' Average','',regex=True), x=' Statistics', y='Temperature - (Celsius)', animation_frame=' Year', range_y=[min_temperature,max_temperature])
fig.show()

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)