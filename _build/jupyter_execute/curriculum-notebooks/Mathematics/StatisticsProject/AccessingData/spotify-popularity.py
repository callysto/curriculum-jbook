![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/spotify-popularity.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Spotify Popularity

Using [Spotify data](https://spotifycharts.com/regional) we can see which songs are the most popular.

To look at just Canadian data, use the url `https://spotifycharts.com/regional/ca/daily/latest`

csv_url = 'https://spotifycharts.com/regional/global/daily/latest/download'

import pandas as pd
import requests
import io

r = requests.get(csv_url)
df = pd.read_csv(io.StringIO(r.text), skiprows=1)
df

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)