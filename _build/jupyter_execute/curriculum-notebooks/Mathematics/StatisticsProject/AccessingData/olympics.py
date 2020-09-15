![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/olympics.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Olympics Data

[Statistics from the modern Olympic Games](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results/data#athlete_events.csv)

import pandas as pd
olympics = pd.read_csv('olympics.csv')
medals = olympics.dropna(subset=["Medal"])
medals_winter = medals[medals["Season"]=="Winter"]
medals_winter_country = medals_winter.groupby('region').count().sort_values('Medal',ascending=False)['Medal']
medals_winter_country

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)