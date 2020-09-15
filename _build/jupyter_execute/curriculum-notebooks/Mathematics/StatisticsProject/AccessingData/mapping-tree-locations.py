![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/mapping-tree-locations.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Mapping Tree Locations

As an example of mapping data, we can look at [tree locations from Lethbridge Open Data](http://opendata.lethbridge.ca/datasets/82841132047d47659508f60c52f6346a_0/data).

import folium
from folium.plugins import MarkerCluster
import pandas as pd

csv_link = 'https://opendata.arcgis.com/datasets/82841132047d47659508f60c52f6346a_0.csv'
df = pd.read_csv(csv_link, low_memory=False)
df

print('Tree map with terrain and a sample of 200 data points.')
lat = df['Y'].mean()
lon = df['X'].mean()
tree_map = folium.Map(location=[lat,lon], zoom_start=12, tiles='Stamen Terrain')
for row in df.sample(n=200).itertuples():
    tree_map.add_child(folium.Marker(location=[row.Y,row.X], popup=row.AssetID, tooltip=row.species))
tree_map

print('Tree map with data points clustered (this will take a while to run).')
lat = df['Y'].mean()
lon = df['X'].mean()
tree_map_mc = folium.Map(location=[lat,lon], zoom_start=12)
marker_cluster = MarkerCluster()
for row in df.itertuples():
    marker_cluster.add_child(folium.Marker(location=[row.Y,row.X], popup=row.AssetID, tooltip=row.species))
tree_map_mc.add_child(marker_cluster)
tree_map_mc

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)