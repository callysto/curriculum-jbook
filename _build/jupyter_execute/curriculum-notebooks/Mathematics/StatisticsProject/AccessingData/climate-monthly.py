![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/climate-monthly.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Monthly Climate Data

We can get temperature and precipitation data averaged by month for 1901 to 2016 from [World Bank Climate Change Knowledge Portal](https://climateknowledgeportal.worldbank.org). You will need the latitude and longitude of a location from a site such as [latlong.net](https://www.latlong.net).

latitude = 43.7521
longitude = -79.7614

import pandas as pd
temperature_url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1901-2016/'+str(latitude)+'$cckp$'+str(longitude)+'/'+str(latitude)+'$cckp$'+str(longitude)
temperature_all = pd.read_csv(temperature_url)
temperature = temperature_all.replace(' Average','',regex=True).replace(' ','',regex=True).rename(columns={'Temperature - (Celsius)':'Temperature (°C)', ' Statistics':'Month'})
precipitation_url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/pr/1901-2016/'+str(latitude)+'$cckp$'+str(longitude)+'/'+str(latitude)+'$cckp$'+str(longitude)
precipitation_all = pd.read_csv(precipitation_url)
precipitation = precipitation_all.replace(' Average','',regex=True).replace(' ','',regex=True).rename(columns={'Rainfall - (MM)':'Precipitation (mm)', ' Statistics':'Month'})
climate = pd.merge(temperature, precipitation).drop(columns=[' Longitude',' Latitude'])
climate

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)