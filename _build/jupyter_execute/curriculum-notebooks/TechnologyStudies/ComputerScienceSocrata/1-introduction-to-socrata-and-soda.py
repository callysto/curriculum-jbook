![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=TechnologyStudies/ComputerScienceSocrata/1-introduction-to-socrata-and-soda.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Socrata and Soda

by Gustaaf J Wehnes, Calgary Board of Education

We will be using Socrata open data for our forays into the rapidly emerging field of data science. Socrata is used by many governments and organisations, including our own City of Calgary. Take some time to familiarize yourself with the technology through their [home page](https://dev.socrata.com/data/)

## The SODA API
As programmers, we will want to know how to *programatically* interact with open data sources. will be using an API (Application Programming Interface) developed  Thus, you will also want to bookmark the [Socrata Open Data API (aka SODA)](https://dev.socrata.com/). Pay particular attention to the [Getting Started](https://dev.socrata.com/consumers/getting-started.html) and the [API Docs](https://dev.socrata.com/docs/endpoints.html) pages. 

If you don't know what an API is, here is a [definition](https://www.webopedia.com/TERM/A/API.html)

## The City of Calgary datasets
Also have a look at [The City of Calgary’s Open Data Portal](https://data.calgary.ca/). There are all kinds of cool data sets here, along with tools for visualizing this data. Hopefully you can already start seeing how open data provides a massive opportunity for app developers and researchers.

In particular, have a look at three datasets we will be using in our journey: [River Levels and Flows](https://data.calgary.ca/Environment/River-Levels-and-Flows/5fdg-ifgr), [School Locations](https://data.calgary.ca/Services-and-Amenities/School-Locations/fd9t-tdn2), and [School Enrolment](https://data.calgary.ca/Demographics/School-Enrolment-Data/9qye-mibh).

https://dev.socrata.com/docs/functions/#,

https://data.calgary.ca/Environment/River-Levels-and-Flows/5fdg-ifgr

## Queries in SODA

The Socrata interface allows the building of SQL-like queries: [query Parameter](https://dev.socrata.com/docs/queries/query.html). Theses queries are much more readable than the queries we were writing before using keywords in a URL

To allow the potential running of multiple queries, let's take the time to create a function that does some of the dirty work for us. We use the requests library to obtain data from an internet request based on the domain, uuid, and query. The get method returns a byte array, which we then have to convert to a dataframe

**function** *run_query*

**parameter** *domain*: refers to the organization that supplies the data

**parameter** *uuid*: universal unique ID; refers to the specific dataset.

**parameter** *query*: SODA query

**returns**: pandas dataframe


## Python tools

The last few pieces that needs introducing are the Python libraries that we will use. Again, take some time to have a look.  The first is an open source data analysis and manipulation tool called [pandas](https://pandas.pydata.org/). Two other libraries, which you only need a passing familiarity with, are [requests](https://requests.readthedocs.io/en/master/) and [Python io](https://docs.python.org/3/library/io.html).

Don't get overwhelmed; there is a lot of functionality here, and just like me, you will just learn it as you go.

The beauty of using Jupyter is that these tools are pre-installed! So, no messing with downloading and installing. We simply import them :-)

import requests as rq
import pandas as pd
import io as io

## Some terminology and a helper function

To simplify the execution of multiple queries, let's take the time to create a function that does some of the dirty work for us. We use the requests library to obtain data from an internet request based on the [domain](https://www.webopedia.com/TERM/D/domain_name.html), [uuid](https://en.wikipedia.org/wiki/Universally_unique_identifier) of the dataset, and the *query* itself. A 'session' object is created with the requests library; the get method is used to return a byte array from an [http](https://www.webopedia.com/TERM/H/HTTP.html) source, and we then covert that array to a [pandas dataframe object](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html). Note that we also import the four libraries previously mentioned.

**function** *run_query*

**parameter** *domain*: refers to the organization that supplies the data

**parameter** *uuid*: universal unique ID; refers to the specific dataset.

**parameter** *query*: SODA query

**returns**: pandas dataframe

def run_query(domain, uuid, query):
    session = rq.Session()
    results = session.get(domain + uuid +".csv?$query=" + query)
    dataframe =  pd.read_csv(io.StringIO(results.content.decode('utf-8')))
    return dataframe

## READY? Lets query some data!

You may already have come across the documentation for the SODA [query](https://dev.socrata.com/docs/queries/query.html). This will look quite familiar to the SQL statements that you have already learned about. Let's run through a pile of examples, where you can see how you can use the tools to obtain data in CSV (or JSON) format.

### simple query
Retrieve the entire dataset.

##### Note:
- A maximum of 1000 records are returned. That is probably a good thing, as the dataset itself is *huge* (5.48 million records as of April 2020, and ever growing).

domain = "https://data.calgary.ca/resource/"

uuid_river_levels = "5fdg-ifgr"
uuid_school_enrollment = "9qye-mibh"

query = """
SELECT *
"""

river_levels = run_query(domain, uuid_river_levels, query)
river_levels

### limiting the amount of data
Retrieve only the first 100 record of the dataset.

##### Note:
- You can set any limit that you like, but be aware of how much data you are going to get back. Obviously, the larger the dataset (rows * columns) the longer the download time (and the data used).

query = """
SELECT
    *
LIMIT
    100
"""

river_levels = run_query(domain, uuid_river_levels, query)
river_levels

### paging through data
Retrieve records 101 to 200. You will again receive 100 record.

##### Note:
- This is known as [paging](https://dev.socrata.com/docs/paging.html). You could, if you want, retrieve the data in small chunks. We will not be doing this in this course, but it is good to know that it can be done.

query = """
SELECT
    *
LIMIT
    100
OFFSET
    100
"""

river_levels = run_query(domain, uuid_river_levels, query)
river_levels

### select a limited number of fields
This can dramatically reduce the amount of data returned (as the dataframe is like a table, so rows x columns).

query = """
SELECT
    station_number,
    timestamp,
    level
LIMIT
    100    
"""

river_levels = run_query(domain, uuid_river_levels, query)
river_levels

### providing an alias for a field
You can rename a field with a custom name. This will be useful later when we calculate our own fields; for now, you can see the syntax is simple. Observe that the dataframe has the desired field names.

query = """
SELECT
    station_number as station,
    timestamp as time,
    level as river_level
LIMIT
    100    
"""

river_levels = run_query(domain, uuid_river_levels, query)
river_levels

### data transform functions
If you look at the dataset 'meta' data on the City of Calgary's website, you will notice that all of the fields have a type. This is no different than in most programming languages: you have text, integers, and even date types.

Unfortunately, fields are sometimes not of the desired type. This may be due to the dataset not being well designed, or for reasons of saving space. Fortunately, SODA provides a series of [Data Transform functions](https://dev.socrata.com/docs/transforms/) which allow you to transform (or 'cast') the field to a different type.

##### Note:
- Subclauses in the WHERE clause are separated by AND instead of commas, to reflect that these are boolean expressions
- OR could be used as well
- at this time, I am not certain why I cannot convert level to a number using the to_number function.  Stay tuned...


query = """
SELECT
    station_name,
    timestamp,
    date_extract_y(to_floating_timestamp(timestamp,'UTC')) as year,
    date_extract_m(to_floating_timestamp(timestamp,'UTC')) as month,
    date_extract_d(to_floating_timestamp(timestamp,'UTC')) as day,
    date_extract_hh(to_floating_timestamp(timestamp,'UTC')) as hour,
    date_extract_mm(to_floating_timestamp(timestamp,'UTC')) as minute,
    date_extract_ss(to_floating_timestamp(timestamp,'UTC')) as second,
    level
LIMIT
    10
"""

river_levels = run_query(domain, uuid_river_levels, query)
river_levels

### WHERE clause
Just like in SQL, we can filter the records returned using the WHERE clause. There are a lot of powerful operators available, as per the [documentation](https://dev.socrata.com/docs/queries/where.html). **Don't hesitate to experiment!**

##### Note:
- Subclauses in the WHERE clause are separated by AND instead of commas, to reflect that these are boolean expressions
- OR could be used as well

query = """
SELECT
    station_name,
    timestamp,
    date_extract_y(to_floating_timestamp(timestamp,'UTC')) as year,
    date_extract_m(to_floating_timestamp(timestamp,'UTC')) as month,
    date_extract_d(to_floating_timestamp(timestamp,'UTC')) as day,
    date_extract_hh(to_floating_timestamp(timestamp,'UTC')) as hour,
    date_extract_mm(to_floating_timestamp(timestamp,'UTC')) as minute,
    date_extract_ss(to_floating_timestamp(timestamp,'UTC')) as second,
    level
WHERE
    station_name = 'Bow River at Calgary' AND
    year = 2004 AND
    (month between 4 AND 5 OR month between 9 AND 10) AND
    day = 1 AND
    hour = 0 AND
    minute = 0
LIMIT
    10
"""

river_levels = run_query(domain, uuid_river_levels, query)
river_levels

### ORDER BY clause
Just like in SQL, we can order the records returned using the ORDER BY clause. You can specify multiple fields in order to create a secondary order.

query = """
SELECT
    station_name,
    timestamp,
    date_extract_y(to_floating_timestamp(timestamp,'UTC')) as year,
    date_extract_m(to_floating_timestamp(timestamp,'UTC')) as month,
    date_extract_d(to_floating_timestamp(timestamp,'UTC')) as day,
    date_extract_hh(to_floating_timestamp(timestamp,'UTC')) as hour,
    date_extract_mm(to_floating_timestamp(timestamp,'UTC')) as minute,
    date_extract_ss(to_floating_timestamp(timestamp,'UTC')) as second,
    level
WHERE
    station_name = 'Bow River at Calgary' AND
    year = 2004 AND
    (month between 4 AND 5 OR month between 9 AND 10) AND
    (day = 1 OR day = 15) AND
    hour = 0 AND
    minute = 0
ORDER BY
    month DESC,
    day DESC
LIMIT
    10
"""

river_levels = run_query(domain, uuid_river_levels, query)
river_levels

### GROUP BY clause
This is where things get interesting, as you would know if you've gone through the [w3schools'scourse](https://www.w3schools.com/sql/default.asp) on SQL. As this [group by section](https://www.w3schools.com/sql/sql_groupby.asp)  explains, grouping is most often used along with aggregate functions (COUNT, MAX, MIN, SUM, AVG).

For these next examples, we will use the school enrollment dataset. The first example below will check how many high schools existed for each school authority over three years. 

You can think of grouping as collapsing the data that would be returned if you ran the query without the GROUP BY clause. All of the records that share the same values for all of the fields are aggregated (collapsed) into a single row. The fields that you are *not* grouping by thus need to have an aggregate function of some sort in the WHERE clause: hence COUNT(level), which will do exactly that.

##### Note:
- Observe how the aggregated field is automatically named 

query = """
SELECT
    school_authority_name,
    school_year,
    COUNT(school_name)
WHERE
    (school_year = "2018_2019" OR school_year = "2017_2018" OR school_year = "2016_2017" OR school_year = "2015_2016") AND
    grade_12 > 0
GROUP BY
    school_authority_name,
    school_year
ORDER BY
    school_authority_name,
    school_year
LIMIT
    60
"""
    
school_enrollment = run_query(domain, uuid_school_enrollment, query)
school_enrollment

You can also try the MAX, MIN, AVG, and SUM functions. In this case, let's only run the query on schools that have Grade 12 students.

##### Note:
- We will provide slightly more descriptive field aliases.
- You can re-use a field to get multiple aggregations.

query = """
SELECT
    school_authority_name,
    COUNT(school_name) as total_schools,
    MAX(grade_12) as max_grade_12,
    AVG(grade_12) as avg_grade_12,
    MIN(grade_12) as min_grade_12,
    SUM(grade_12) as total_grade12
WHERE
    school_year = "2018_2019" AND
    grade_12 > 0
GROUP BY
    school_authority_name
LIMIT
    50
"""
    
school_enrollment = run_query(domain, uuid_school_enrollment, query)
school_enrollment

### AN IMPORTANT DISTINCTION
The data above begs the question of what the largest Grade 12 class in the city is! However, you do not have to use the MAX function to find this. Rather, you could simply use the SORT BY and the LIMIT function. This gets around the difficulty of having to either group or aggregate on all fields. If you grouped the above query by school_name, you would receive a maximum for each school. If you were to use an aggregate function instead, you would not get the right school name!

This also allows me to quickly discuss the [NaN](https://www.python-course.eu/dealing_with_NaN_in_python.php) value, which can be though of like a null. If you do not include the WHERE clause in the query below, you will get a record with NaN,

query = """
SELECT
    COUNT(school_name) as total_schools,
    MAX(grade_12) as max_grade_12
WHERE
    school_year = "2018_2019" AND
    grade_12 > 0
LIMIT
    1
"""
    
school_enrollment = run_query(domain, uuid_school_enrollment, query)
school_enrollment

## Conclusion

This notebook introduced Socrata and the SODA API. Up next is an [Introduction to Plotly](./2-introduction-to-plotly.ipynb).

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)