![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/fruit-tree-popularity.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Fruit Tree Popularity

Using [tree data from Vancover Open Data](https://opendata.vancouver.ca/explore/dataset/community-gardens-and-food-trees/export/) we can see which public fruit trees are the most common.

csv_url = 'https://opendata.vancouver.ca/explore/dataset/community-gardens-and-food-trees/download/?format=csv'

import pandas as pd
df =  pd.read_csv(csv_url, sep=';') # Vancouver Open Data uses a ; between each column instead of a ,
df.dropna(subset=['food_tree_varieties'], inplace=True) # drop a row if it is NA in that column
df

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)