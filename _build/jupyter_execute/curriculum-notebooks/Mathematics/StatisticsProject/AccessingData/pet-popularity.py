![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/pet-popularity.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Pet Popularity

Using [Pet Licenses data from the City of Edmonton Open Data Portal](https://data.edmonton.ca/Community-Services/Pet-Licenses-by-Neighbourhood/5squ-mg4w) we can see which (licensed) pets are the most popular.

domain = 'https://data.edmonton.ca/resource/'
uuid = '5squ-mg4w'
query = 'SELECT *'

import requests
import io
import pandas as pd

session = requests.Session()
results = session.get(domain + uuid +'.csv?$query=' + query)
df =  pd.read_csv(io.StringIO(results.content.decode('utf-8')))
df

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)