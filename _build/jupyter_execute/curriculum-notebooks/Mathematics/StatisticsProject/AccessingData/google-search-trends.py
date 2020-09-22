![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/google-search-trends.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Google Trends

Google Trends has data going back to January 1, 2004 about the frequencies of search terms, which can be imported into a pandas DataFrame using the [pytrends](https://github.com/GeneralMills/pytrends) library.

We can use various [methods](https://github.com/GeneralMills/pytrends#api-methods) such as `interest_over_time()` or `interest_by_region`.

#install the pytrends package
!pip install --user pytrends                     

from pytrends.request import TrendReq
import pandas as pd

pytrend = TrendReq()
pytrend.build_payload(kw_list=['Mars', 'Venus'])
df = pytrend.interest_over_time()
df

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)