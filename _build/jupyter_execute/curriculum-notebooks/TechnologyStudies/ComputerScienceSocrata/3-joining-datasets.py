![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=TechnologyStudies/ComputerScienceSocrata/3-joining-datasets.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Joining Datasets

Unlike standard SQL, SODA does not (currently) support the joining of separate datasets. As you recall, this is a fundamental part of working with data. Often, there are different sets of data for the same entity, and it doesn't make sense to store them all in one dataset. Even if you wanted to, this would quickly increase the # of columns in a dataset.

For example, the [School Locations](https://data.calgary.ca/Services-and-Amenities/School-Locations/fd9t-tdn2) dataset we have already looked at stores both the geographical information of schools in Calgary. The [School Enrolment](https://data.calgary.ca/Demographics/School-Enrolment-Data/9qye-mibh) dataset stores the enrollment information for schools. It should be quite obvious that these two datasets should remain separate. Most often, you would not need enrollment #s when looking for locations, and vice versa. If the datasets were permanently combined, you likely have a lot of redundant columns. Moreover, the school enrollment dataset is *keyed* on the school year. You would have to repeat the geographical data in each row, which would be a poor use of space.

But, what if we wanted to demonstrate additional features of the scattermapbox by visualizing school enrollment? We will need to obtain data from the two seperate datasets, and dynamically *join* them together. As mentioned, we can't do it in SODA, but we can do so programatically using the pandas 'merge' function.

import requests as rq
import pandas as pd
import io as io

domain = "https://data.calgary.ca/resource/"

uuid_school_locations = "fd9t-tdn2"
uuid_school_enrollment = "9qye-mibh"

def run_query(domain, uuid, query):
    session = rq.Session()
    results = session.get(domain + uuid +".csv?$query=" + query)
    dataframe =  pd.read_csv(io.StringIO(results.content.decode('utf-8')))
    return dataframe

The first dataset contains latitude and longitude 

query = """
SELECT
    *
"""

calgary_school_location = run_query(domain, uuid_school_locations, query)
calgary_school_location

The second dataset contains enrollment data. Note that the enrollment dataset also contains a school_year column, which makes sense, as enrollment values do change. However, our intent is to visualize enrollment at a specific point in time, so we use the WHERE clause to filter out rows that do not match that time. 

query = """
SELECT
    *
WHERE
    school_year = '2019-2020'
"""

calgary_school_enrollment = run_query(domain, uuid_school_enrollment, query)
print(calgary_school_enrollment)

## Data from CSV files

We could instead use pandas to import data from CSV ([comma separated values](https://en.wikipedia.org/wiki/Comma-separated_values)) files.

import pandas as pd

calgary_school_location = pd.read_csv("https://data.calgary.ca/resource/64t2-ax4d.csv")
calgary_school_enrollment = pd.read_csv("https://data.calgary.ca/resource/9qye-mibh.csv?$where=School_Year%20=%20'2019-2020'")

calgary_school_location

## Joining data sets

Whichever method we use to import the data, we can now *join* the two datasets on the school name (`school_name` in `calgary_school_location` and `name` or `NAME` in `calgary_school_enrollment`) as the values in these fields match up. In proper SQL parlance, they share a *key*. Again, the dataset has already been filtered for a single school year. This means that there should be no duplicates of school name in the school enrollment dataset.

Thus, we can do a simple left join with the enrollment on the left and the locations on the right. That way, our resulting dataframe will only have data on schools that have enrollment data. We would run into problems later on if there are NaN (aka null) values in the total field.

calgary_school_location_enrollment = pd.merge(left=calgary_school_enrollment, 
                                              right=calgary_school_location, 
                                              how='left', 
                                              left_on='school_name', 
                                              right_on='NAME' )
                                              # right_on='name' ) #use this line if you imported data using Requests

calgary_school_location_enrollment

## Visualizing the data

We will now visualize the resulting dataset, and use the `size` and `color` to add two extra dimensions of data - the total enrollment and the school authority.

##### Note

- the `showlegend` parameter is used to hide the legend, but this is only to clean up the presentation!

import plotly.express as px

figure1 = px.scatter_mapbox(calgary_school_location_enrollment, 
                            size="total",
                            color="school_authority_name", 
                            #showlegend= False,
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            size_max=45, 
                            lat="latitude", 
                            lon="longitude", 
                            hover_name="school_name", 
                            hover_data=["TYPE", "GRADES", "ADDRESS_AB"],
                            #hover_data=["type", "grades", "address_ab"], #use this line if you imported data using Requests
                            zoom=10, 
                            height=600)

figure1.update_layout(mapbox_style="open-street-map")
figure1.update_layout(showlegend= False)
figure1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

## Conclusion

This notebook introduced the ability to join datasets. The last notebook in this series is [filtering datasets](./4-filtering-datasets.ipynb).

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)