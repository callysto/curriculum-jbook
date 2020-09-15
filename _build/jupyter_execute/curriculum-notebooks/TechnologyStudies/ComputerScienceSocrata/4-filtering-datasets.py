![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=TechnologyStudies/ComputerScienceSocrata/4-filtering-datasets.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Filtering Datasets

We have experimented with visualizing open source data in a browser. However, lets broaden our perspective and consider how designing queries is an important part of designing any data-drive applications, including many of those that run on phones and tablets. For example, consider a mobile app that plots schools within walking distance to the user on a map. We want to plot only a small subset of all schools in Calgary. How should this application filter the data?

There are two general approaches, named after the location where the data actually gets filtered: the server (i.e. where the data is stored) or the client (where the data is used). These may be on same device, or they may be separated. They are also very likely running on different technologies. Filtering on either side has its pros and cons:

### Server-side filtering

You have already seen this type of filter through the use of tht WHERE clause in SODA. This approach reduces the amount of data that you receive from wherever that data is stored. The data is likely being sent across a network (in the case of cloud-based data) or from a different application (in the case of a more traditional database system). If the speed of the data transmission is limited (e.g. slow internet) or if the data transmission is costly (e.g. the user's data plan is limited), then you may very well wish to use a server-side filter.

For example, below is our familiar SODA query for obtaining all schools within Calgary. I've created a WHERE clause that finds all schools within a 'square' around the 'current' location, which we will assume to be William Aberhart High School (51.07866950960592°, -114.11533747920511°). To keep things simple, I will make my square 2 $\times$ 0.01 degree latitude by 2 $\times$ 0.01 degree longitude.

if you are curious, according to [this calculator](http://www.csgnetwork.com/degreelenllavcalc.html), 0.01 degree latitude equals about 1.112 km, and one minute longitude at Calgary's latitude equals about 0.702 kilometres, so this would be a box about 2.2 by 1.4 km

import requests as rq
import pandas as pd
import io as io

domain = "https://data.calgary.ca/resource/"
uuid_school_locations = "fd9t-tdn2"

def run_query(domain, uuid, query):
    session = rq.Session()
    results = session.get(domain + uuid +".csv?$query=" + query)
    dataframe =  pd.read_csv(io.StringIO(results.content.decode('utf-8')))
    return dataframe

latitude = 51.07866950960592
longitude = -114.11533747920511

query_template = """
SELECT
    *
WHERE
    latitude BETWEEN '{0}' AND '{1}' AND
    longitude BETWEEN '{2}' AND '{3}'
"""
#    longitude BETWEEN '-114.10533747920511' AND '-114.12533747920511'

query = query_template.format(latitude - 0.01, latitude + 0.01, longitude + 0.01, longitude - 0.01)

local_schools = run_query(domain, uuid_school_locations, query)
local_schools

##### Note
- We can easily re-create the query by changing the latitude and the longitude, and creating a newly formatted query using the `query_template`.
- But then we would have to resubmit the query, and this may take quite some time.

### Client-side filtering

The opposite approach is to obtain an entire dataset and to then programatically filter using your native language. The pandas library provides various tools that allow you to easily select specific records in a dataframe. In this case, we will use the [panda dataframe's **loc** function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html) on  the *entire* dataset. The output should be equivalent to the server-side filter's output

query = """
SELECT
    *
"""

all_schools = run_query(domain, uuid_school_locations, query)

local_schools = all_schools.loc[(all_schools ['latitude'] > latitude - 0.01) 
                                & (all_schools ['latitude'] < latitude + 0.01)
                                & (all_schools ['longitude'] > longitude - 0.01)
                                & (all_schools ['longitude'] < longitude + 0.01)]
local_schools

### Visualization
So, with all that work done, let's do the visualization.

import plotly.express as px

figure1 = px.scatter_mapbox(local_schools, lat="latitude", lon="longitude",
                            color_discrete_sequence=["blue"],
                            zoom=13, height=600,
                            size='latitude',
                            size_max = 15,
                            hover_name="name",
                            hover_data=["type", "grades", "address_ab"],)

figure1.update_layout(mapbox_style="open-street-map")
figure1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

But if we then changed our current location to be Sir Winston Churchill High School (51.10011269545306°, -114.1399900255147°), we can very quickly change our results without having to re-query the City of Calgary server! It may still take some time to re-plot the data, but latency is not a concern.

local_schools2 = all_schools.loc[(all_schools ['latitude'] > 51.09011269545306) 
                                & (all_schools ['latitude'] < 51.11011269545306)
                                & (all_schools ['longitude'] < -114.1299900255147)
                                & (all_schools ['longitude'] > -114.1499900255147)]
local_schools2

figure1 = px.scatter_mapbox(local_schools2, lat="latitude", lon="longitude",
                            color_discrete_sequence=["blue"],
                            zoom=13, height=600,
                            size='latitude',
                            size_max = 15,
                            hover_name="name",
                            hover_data=["type", "grades", "address_ab"],)

figure1.update_layout(mapbox_style="open-street-map")
figure1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#### Note
There are many many functions within the [pandas dataframe class](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html) that allow you to filter, combine, and transform data. Learning these would take time, and is outside of our scope here. This course is about learning how to query for data.


## Which approach is best?

That depends, of course!

If your application will show multiple views of the data set within a short time, it makes sense to download it once in its entirety. Re-querying for the data for each view would obviously be inefficient.

However, loading the data in its entirety will cost more bandwidth, and may take time up front. Also, your data will at some point go stale; hence the 'within a short time' qualifier.

So why not just query for little chunks of data only when needed? Well, you probably have already noticed that executing a query takes some time. The query has to pass from your local device to a remote server, the server has to retrieve the data and format it, and the the server has to pass it back across a network. The lag in time between query and response is known as *latency*. Latency may make your application appear to freeze. This may be frustrating to your user. Never mind what your user may experience if they lose their network connection completely. 

The time gaps in between the various steps may be fractions of seconds, but that is an eternity compared to how fast your local device can process locally stored data. Thus, loading your data up front *may* be a good design decision.

In the above example, the client-side approach would probably be best. The dataset is relatively small, so data usage is reasonable, unless the data plan really is restrictive. Also, the data is highly static, as not many schools will get added in the next month, and none will change location. Thus, it would be good design to download the dataset, and perhaps even store it locally in a csv file. You can then move all around the city, and the map can be updated very quickly and without extra data transmission. Of course, your app will still want to update the dataset once in a while, and may need to load the Edmonton data if we change cities!

An alternate example could be an app that checks if any of your friends are within walking distance. Perhaps this app has a few million users, and their locations are being stored on a server somewhere in Silicon Valley. You would not want to download the entire dataset, as 99.99% of it would be useless to you. Furthermore, the data is highly dynamic, and if you don't update continuously, you will have a useless app. In this example, the server-side approach would undoubtedly be best.

## Final Thoughts

- Hopefully you appreciate the point that you can 'massage' your data both locally and remotely. and that you choose which way you go based on performance.
- The technology you work with will also have an impact on which approach you take. Other open data APIs do not have the ability to perform server-side filtering (and aggregation), and you may be forced to go client-side.
- To be quite honest, there will also be times where it is just easier to do your filtering (and aggregation) on the client side, instead of breaking your brain in writing the perfect SQL statement!
- Whereas the previous lessons dealt with 'big data' (aggregating finding patterns in large sets), this lesson dealt with 'specific data' (querying for specific information).

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)