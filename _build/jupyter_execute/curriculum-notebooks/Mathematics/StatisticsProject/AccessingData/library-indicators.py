![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/library-indicators.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Public Library Performance Indicators

Using [data from the Strathcona County Open Data Portal](https://data.strathcona.ca/Recreation-Culture/Library-Key-Performance-Indicators/ep8g-4kxs) we can see which public library services might be necessary.

csv_url = 'https://data.strathcona.ca/api/views/ep8g-4kxs/rows.csv'

import pandas as pd
df =  pd.read_csv(csv_url)
df

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)