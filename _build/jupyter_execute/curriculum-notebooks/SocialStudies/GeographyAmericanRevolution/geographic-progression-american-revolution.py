![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=SocialStudies/GeographyAmericanRevolution/geographic-progression-american-revolution.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Geographic Progression of The American Revolution


The American Revolution (1775-83) is also known as the American Revolutionary War and the U.S. War of Independence. 

On July 4, 1776, America's Thirteen Colonies declared that they were no longer part of Britain. The British disagreed. A war between Britain and the Thirteen Colonies began as a result of this disagreement. This war was known as the American Revolution or the War of Independence. (From "Our Land and People", Patricia Shields-Ramsay, Douglas Ramsay)


> ![map of colonies](images/13_colonies.jpg)
>
> The location of the original thirteen English Colonies on the east coast of what is now known as the United States of America. 

In order to understand the origins and progression of the American Revolutionary War, we will look at the locations of various battles during each stage of the war. From this data, we can begin to understand where the battles were taking place, where they moved to, and try and understand the events surrounding them. To begin, we first need to download [an open data set from Wikipedia](https://en.wikipedia.org/wiki/List_of_American_Revolutionary_War_battles) that contains the locations and other information about the battles.

Select the code cell below, then click the `▶Run` button in the toolbar to download and display the data.

url = 'https://en.wikipedia.org/wiki/List_of_American_Revolutionary_War_battles'
import pandas as pd
revolution_data = pd.read_html(url)[17] # get the 18th table from the page
revolution_data

From the table above we see that there is a lot of information to digest. There are 253 rows and four columns. The columns are the name of the battle, the date of the battle, where it took place, and the consequences of that battle.

Next we are going to look up latitude and longitude values for each of the listed locations.

# import and set up libraries
!pip install geopy --user
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
locator = Nominatim(user_agent='Callysto Geocoder')
geocode = RateLimiter(locator.geocode, min_delay_seconds=.1)
location_data_dictionary = {} # an empty dictionary that we will add to
# loop through the unique locations in the previous dataframe and geocode their location
for place in revolution_data['Colony/State'].unique():
    #location = locator.geocode(place) # without rate limiting
    location = geocode(place)
    print(location)
    location_data_dictionary.update({place:location})
# clear the screen of the progress we were printing
from IPython import display
display.clear_output()
# create the dataframe
location_data = pd.DataFrame(data=location_data_dictionary).transpose()
location_data.rename(columns={0:'Location', 1:'Coordinates'}, inplace=True)
location_data

## Geographic View of The American Revolution

Now that we have some location data about the Revolutionary War battles, let's put it on a map.

# join our two dataframes together
map_data = revolution_data.join(location_data, on='Colony/State')
# split the Coordinates column into Latitude and Longitude
map_data[['Latitude','Longitude']] = pd.DataFrame(map_data['Coordinates'].tolist(), index=map_data.index)
# create the map
import folium
battle_map = folium.Map(location=[50, -50], zoom_start=2)
for i, row in map_data.iterrows():
    location=[row['Latitude'], row['Longitude']]
    battle_map.add_child(folium.Marker(location, tooltip=row['Battle'], popup=row['Date']))
battle_map

It is interesting to note that that not all of the battles took place in the United States.

We can list the battles that took place in Canada.

map_data[map_data['Location'].str.contains('Canada')]

We are also interested in looking at the battles by year, so we will create a `year` column from the last four characters of the `Date` column.

map_data['Year'] = map_data['Date'].str[-4:]
map_data

We can now animate those battles by the year that they took place. The year can be controlled by adjusting the slider on the bottom of the map below, or by simply pressing the play button. Look at the map below and observe the progress of battles that took place.

If you hover your mouse over the battle location, you can see the name of the battle. You can also zoom in and out with the buttons at the top right.

import plotly.express as px
fig = px.scatter_geo(map_data, lat='Latitude', lon='Longitude', animation_frame='Year', hover_name='Battle')
fig.show()

Using this interactive map, you can observe the progression of the American Revolution in North America in terms of the battles fought each year. Pay particular attention to the battles taking place in Quebec, the Maritime provinces, and along the Saint Lawrence River. 


### Questions
1. Use the slider and hover over the battles on the map above, which battles were fought in what is now Canada?
2. Why did some battles of the American Revolution take place in Quebec? 
3. Choose one of those battles and study it further. How might that battle have shaped Canada as we know it today?



## The Progression of the War
While the map above makes it easy to see where and when various battles were fought during the American Revolution, sometimes it's to look at different visualizations. The following bar chart displays how many battles took place each year.

import cufflinks as cf
cf.go_offline()
by_year = map_data.groupby('Year').count()['Battle']
by_year.iplot(kind='bar', yTitle='Number of Battles', xTitle='Year', title='Battles per Year')

We can see that the year 1777 had the most battles out of the entire war. This is because 1776-1777 was the beginning of the British counter offensive, and British forces made considerable progress against the Americans. 

### Questions
1. 1778 has about half as many battles as 1777, the year of the British counter offensive. What is the reason for this?
2. 1780 has the second most battles in a year. What events lead to this year having as many battles as it did?

## American Revolution Battle Locations

We can also chart the number of battles by location.

by_location = map_data.groupby('Location').count()['Battle'].sort_values()
by_location.iplot(kind='barh', margin=(400,0,0,50), dimensions=(800,1100), xTitle='Number of Battles', title='Battles by Location',)

## Summary

Using data from Wikipedia, we were able to visualize the locations and progress of the American Revolution, and also discover how many battles took place each year.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)