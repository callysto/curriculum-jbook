![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/gapminder.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Gapminder Data

[Gapminder](https://www.gapminder.org/) is an organization that promotes use and understanding of statistics about social, economic, and environmental development.

Most [Gapminder data](https://www.gapminder.org/data/) is available in online spreadsheets accessed from the *sourceLink* on the data page.

For example if the data are at `docs.google.com/spreadsheets/d/11mulzUH3_cueq-V9D5KIlo9oHE9YYZrUSeVyCin7_rM/edit#gid=176703676` then you copy the spreadsheet key (`11mulzUH3_cueq-V9D5KIlo9oHE9YYZrUSeVyCin7_rM`) and GID (`176703676`) and replace the values in the code cell.

# Life Expectancy

spreadsheet_key = '11mulzUH3_cueq-V9D5KIlo9oHE9YYZrUSeVyCin7_rM'
spreadsheet_gid = '176703676'

import pandas as pd
csv_link = 'https://docs.google.com/spreadsheets/d/'+spreadsheet_key+'/export?gid='+spreadsheet_gid+'&format=csv'
df = pd.read_csv(csv_link)
df

## Current Populations

If you are interested in the current populations of countries, you can use the following code.

pop_csv_url = 'https://docs.google.com/spreadsheets/d/18Ep3s1S0cvlT1ovQG9KdipLEoQ1Ktz5LtTTQpDcWbX0/export?gid=1668956939&format=csv'

import pandas as pd
populations = pd.read_csv(pop_csv_url)
current_populations = populations[populations['time']==2019]
current_populations

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)