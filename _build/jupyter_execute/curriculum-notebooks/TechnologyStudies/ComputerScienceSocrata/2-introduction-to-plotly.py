![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=TechnologyStudies/ComputerScienceSocrata/2-introduction-to-plotly.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Plotly - introduction

by Gustaaf J Wehnes, Calgary Board of Education

There are two major parts to data science: querying the data, and then interpreting the data. For the latter, few people like to look at tables. A picture is worth a thousand words, so let's *visualize* the data! We will use a brilliant library of graphing tools called [plotly](https://plotly.com/graphing-libraries/). Many of the visualizations that you see on the internet will have been built using this library!

Again, we can just import the library here. You would need to install it locally on your device to run it there, but the install is not difficult. Note that plotly actually runs in JavaScript, and can thus be accessed through many other languages, including Java.

import plotly.express as px

We will again need our function for obtaining data and our UUIDs. That is just the nature of a Jupyter notebook; they need to be self-contained.

import requests
import pandas as pd
import io

def run_query(domain, uuid, query):
    session = requests.Session()
    results = session.get(domain + uuid +".csv?$query=" + query)
    dataframe =  pd.read_csv(io.StringIO(results.content.decode('utf-8')))
    return dataframe

### The Data

Say that we are interested in how and when the Bow River tends to peak for the spring run-off. This would be extremely useful to know for the City of Calgary. You will likely remember the floods of 2013! Can we perhaps find patterns and thereby predict if another flood is coming?

Below is a somewhat complex query. However, you should be able to see that the query is finding the maximum daily river level of the Bow River between April and October for all years since 2004.

The tricky part of the query is in the SELECT statement. That is because we want to plot the river levels for each day as a continuum. It would be simplest if we translate the *date* of each measurement to the *day of year*. That way, the data sorts itself nicely. The first two lines in the SELECT clause do exactly that through a bit of fancy calculation. Strangely enough, there is no '+' operation in SODA, so I am subtracting a negative instead. Programmers have to get creative to work around obstacles!

domain = "https://data.calgary.ca/resource/"
uuid = "5fdg-ifgr"

query = """
SELECT
    station_name,
    ((date_extract_m(to_floating_timestamp(timestamp,'UTC')) - 1) * 30) as temp,
    (temp - -date_extract_d(to_floating_timestamp(timestamp,'UTC'))) as day_of_year,
    date_extract_y(to_floating_timestamp(timestamp,'UTC')) as year,
    date_extract_m(to_floating_timestamp(timestamp,'UTC')) as month,
    date_extract_d(to_floating_timestamp(timestamp,'UTC')) as day,
    MAX(level) as level
WHERE
    station_name = 'Bow River at Calgary' AND
    year > 2004 AND
    month between 4 AND 10
GROUP BY
    station_name,
    temp,
    day_of_year,
    year,
    month,
    day
ORDER BY
    year ASC,
    day_of_year ASC
LIMIT
    10000
OFFSET
    0

"""

river_levels = run_query(domain, uuid, query)
river_levels

### The Visualization

The plotly library has the ability to quickly graph multiple data series in line graphs: [Line Charts in Python](https://plotly.com/python/line-charts/).

Note that a new object called `fig` is created, and that it takes in the dataset as the first argument. The x and the y axis are similarily mapped. The year is a third *dimension* in our data, so let's have the graph use different color lines for each year.

Ready for some magic?

import plotly.express as px

fig = px.line(river_levels, x="day_of_year", y="level", color='year')
fig.show()

That is a colorful graph! Perhaps there is a little too much data in there, but it does show you around what time of year the Bow River crests. It also clearly demonstrates how extra-ordinary the floods of 2013 was.

Note: the gaps in the 2013 data are likely from the station not reporting on those days due to the power outages that occured.

### Plot schools in Calgary on an open street map

For some further shock and awe, let's use a different type of visualization - [maps](https://plotly.com/python/maps/).

In this case, the query for the data will be very simple. The City of Calgary provides a dataset of all schools within its boundary, and includes the geographical location - i.e. the latitude and the longitude.

uuid_school_locations = "fd9t-tdn2"

query = """
SELECT
    *
"""

school_locations = run_query(domain, uuid_school_locations, query)
school_locations

We will now use the Mapbox class in plotly to visualize the data. Note that a new `fig` object is created, and that it takes in the dataset as the first argument. The `lat` argument receives the name of the column in the dataset that contains latitude values (in our case "latitude"). The `lon` argument similarly is set to 'longitude'. The other arguments should be quite obvious when we run the remaining code

figure1 = px.scatter_mapbox(school_locations, lat="latitude", lon="longitude",
                            color_discrete_sequence=["green"],
                            zoom=10, height=600,
                            hover_name="name",
                            hover_data=["type", "grades", "address_ab"],)

figure1.update_layout(mapbox_style="open-street-map")
figure1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

## Conclusion

This notebook introduced visualizations of Socrata using Plotly. Up next is [joining datasets](./3-joining-datasets.ipynb).

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)