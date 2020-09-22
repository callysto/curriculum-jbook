![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/weather-hourly-canada.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Hourly Weather in Canada

[The National Office of Climate Services at Environment and Climate Change Canada](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services.html) has a dataset of weather measurements at monthy, daily, or even hourly intervals for almost 9000 weather stations. Check out [this example for YEG Christmas 2019](https://climate.weather.gc.ca/climate_data/hourly_data_e.html?hlyRange=2012-04-10%7C2020-05-26&dlyRange=2012-04-12%7C2020-05-26&mlyRange=%7C&StationID=50149&Prov=AB&urlExtension=_e.html&searchType=stnProx&optLimit=specDate&StartYear=2019&EndYear=2020&selRowPerPage=25&Line=1&txtRadius=25&optProxType=navLink&selCity=53%7C33%7C113%7C30%7CEdmonton&selPark=&txtCentralLatDeg=&txtCentralLatMin=0&txtCentralLatSec=0&txtCentralLongDeg=&txtCentralLongMin=0&txtCentralLongSec=0&txtLatDecDeg=53.490013888889&txtLongDecDeg=-113.53777777778&timeframe=1&Year=2019&Month=12&Day=25).

## List of Weather Stations

Let's start by importing and mapping the locations of all of the weather stations.

import pandas as pd
import requests
from io import StringIO
stations_url = 'https://drive.google.com/uc?export=download&id=1egfzGgzUb0RFu_EE5AYFZtsyXPfZ11y2'
stations = pd.read_csv(StringIO(requests.get(stations_url).text), header=3)
stations.drop(columns=['Latitude','Longitude'], inplace=True)
stations.rename(columns={'Latitude (Decimal Degrees)':'Latitude','Longitude (Decimal Degrees)':'Longitude'}, inplace=True)
stations

print('This will map will take a minute or two to create with', len(stations), 'weather stations.')
import folium
from folium.plugins import MarkerCluster
latitude = stations['Latitude'].mean()
longitude = stations['Longitude'].mean()
station_map = folium.Map(location=[latitude,longitude], zoom_start=3)
marker_cluster = MarkerCluster()
for row in stations.itertuples():
    marker_cluster.add_child(folium.Marker(location=[row.Latitude,row.Longitude], tooltip=row.Name, popup=row._4))
station_map.add_child(marker_cluster)
print('You can zoom, pan, and click to expand markers. Clicking on a marker will display its station ID.')
station_map

### Station Data Availability

You can check out the data available for a particular station.

station_id = 6454
stations[stations['Station ID']==station_id]

### Filtering Station Data

You can select just a subset of the data. For example, finding stations that are currently collecting hourly weather data.

stations[stations['HLY Last Year']>2019]

#### Mapping Filtered Data

Let's make a map of that filtered dataset.

current_hourly = stations[stations['HLY Last Year']>2019]
print('Creating a map for', len(current_hourly), 'stations with current hourly weather.')
current_hourly_map = folium.Map(location=[latitude,longitude], zoom_start=3)
ch_marker_cluster = MarkerCluster()
for row in current_hourly.itertuples():
    ch_marker_cluster.add_child(folium.Marker(location=[row.Latitude,row.Longitude], tooltip=row.Name, popup=row._4))
current_hourly_map.add_child(marker_cluster)
current_hourly_map

## Weather Data

Once you have selected a station, you can then import a month worth of hourly weather data.

station_id = 50149
year = 2019
month = 12
url_start = 'https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID='
url = url_start+str(station_id)+'&Year='+str(year)+'&Month='+str(month)+'&Day=14&timeframe=1&submit=Download+Data'
weather = pd.read_csv(url)
weather

You can also look at just one day of weather data from that data set.

weather_day = weather[weather['Day']==25]
weather_day

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)