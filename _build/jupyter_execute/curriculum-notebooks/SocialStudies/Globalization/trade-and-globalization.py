![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=SocialStudies/Globalization/trade-and-globalization.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Trade and Globalization

International trade is one of the major forces of contemporary globalization that began after World War II. With countries opening their economies to the flow of goods and services across their borders, world markets are growing rapidly. The more trading occurs between countries the more interconnected and interdependent they are.

Let's explore trade statistics associated with different countries and how they have changed over time. Various datasets used in this notebook were taken from [Our World in Data](https://ourworldindata.org/trade-and-globalization).

## Exports and imports by various countries

It would be interesting to see how international trade has fuelled economic growth of various countries. Run the code cells below to import the datasets and preview the merged dataset. 

# Import python libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Don't show warnings in output
import warnings
warnings.filterwarnings('ignore')
print('Libraries successfully imported.')

# Import the dataset
df_import = pd.read_csv('./Data/imports-of-goods-and-services-constant-2010-us.csv').dropna()
df_export = pd.read_csv('./Data/exports-of-goods-and-services-constant-2010-us.csv').dropna()

# Data clean up - remove the rows containing data for the entire World
df_export = df_export[df_export['Entity'] != 'World']

# Merge the import and export dataset based on Country and Year
final = df_export.merge(df_import, left_on=['Entity','Code','Year'], right_on=['Entity','Code','Year'], how='inner')
final = final[final['Year'] < 2017][final['Year'] > 1980]   # Keep rows for years between 1981 to 2016
print('Data successfully imported.')

# Remove the rows for Afghanistan and Albania from top and append them at the end of the dataframe
# This is required to maintain the order of frames in animated choropleth map as data for various years are missing for those two

temp1 = final[final['Entity'].isin(['Afghanistan','Albania'])]
final = final[final['Entity'] != 'World'][final['Entity'] != 'Afghanistan'][final['Entity'] != 'Albania']
final = final.append(temp1, ignore_index=True)

# Add a new column that contains total trade value i.e. imports + exports
final['Trade (in USD)'] = final['Exports of goods and services'] + final['Imports of goods and services']

# Display the top 5 rows
final.head()

Note that the all the values in the dataframe are in US dollars and [adjusted for inflation](https://dictionary.cambridge.org/dictionary/english/inflation-adjusted) (to 2010 dollars). The `Trade (in USD)` column is the sum of imports and exports. The `e+10` means [move the decimal place 10 to the right](https://en.wikipedia.org/wiki/Scientific_notation) (e.g. 3e+10 is 30 000 000 000).

Let's visualize the data using an animated [choropleth map](https://en.wikipedia.org/wiki/Choropleth_map).

# Plot an animated choropleth map

fig = px.choropleth(final,   # dataframe with required data 
                    locations="Code",   # Column containing country codes
                    color="Trade (in USD)",   # Color of country should be based on total trade value
                    hover_name="Entity",   # Title to add to hover information
                    hover_data=["Exports of goods and services","Imports of goods and services"],   # Data to add to hover information
                    color_continuous_scale=px.colors.sequential.Reds,   # Set the colorscale type
                    animation_frame = "Year",   # Values based on which animation frame will be prepared
                    range_color = [0,max(final['Trade (in USD)'])],   # Range of the colorbar
                    
                    # Title of the chart
                    title = 'Export/Import statistics for countries around the world (in constant 2010 USD)<br>\
Source: <a href="https://ourworldindata.org/trade-and-globalization">Our World in Data</a>'
                   )

fig.update_layout(geo=dict(showcountries=True))
# Show the figure
fig.show()

Click on the ▶ (play) button to animate the changes in import/export statistics. You can also drag the slider.

Note that data are not available for greyed-out countries (for e.g. China) and no data will appear when mouse is hovered over those areas in the map.

### Questions:
1. List the top three major economies in the year 2016. Has that list changed compared to 1981?
2. Which two organizations were proposed after World War II to help regulate the expansion of the international trade? *(Hint: [Bretton Woods Conference](https://en.wikipedia.org/wiki/Bretton_Woods_Conference) and [GATT](https://en.wikipedia.org/wiki/General_Agreement_on_Tariffs_and_Trade))*

### Discussion:
3. Share your thoughts on the positive/negative impacts of transnational corporations on international trade.
4. Do you think preferential trade agreements (like NAFTA) have a major contribution to the rapid growth of international trade?
5. Does growing interdependence between different countries bring stability or instability in their relationships? 

## Are you open to trade?

Trade openness of a country is measured by the ratio of its total trade to gross domestic product (GDP), also known as the [Trade Openness Index](https://en.wikipedia.org/wiki/Openness_index). The higher the ratio, the more that country is involved in international trade.

Let's visualize the variation in trade openness index among countries. Run the following cells to import the data and plot an interactive choropleth map.

# Import the dataset and remove rows with missing entries
df_openness_index = pd.read_csv('./Data/trade-as-share-of-gdp.csv').dropna()

# Data clean up - remove the rows containing data for the entire World and for years upto 2017
df_openness_index = df_openness_index[df_openness_index['Entity'] != 'World'][df_openness_index['Year'] < 2017]

# Display the bottom 5 rows
df_openness_index.tail()

# Remove the rows for Afghanistan and Albania from top and append them at the end of the dataframe
# This is required to maintain the order of frames in animated choropleth map as data for various years are missing for above mentioned countries

temp1 = df_openness_index[df_openness_index['Entity'].isin(['Afghanistan','Albania'])]
df_openness_index = df_openness_index[df_openness_index['Entity'] != 'Afghanistan'][df_openness_index['Entity'] != 'Albania']
df_openness_index = df_openness_index.append(temp1, ignore_index=True)
print('Data manipulation successful.')

# Plot animated choropleth map (Execution of this code cell will take few seconds)
import plotly.express as px

fig = px.choropleth(df_openness_index,   # dataframe with required data 
                    locations="Code",   # Column containing country codes
                    color="Trade (% of GDP)",   # Color of country should be based on trade share in GDP
                    hover_name="Entity",   # Title to add to hover information
                    hover_data=["Trade (% of GDP)"],   # Data to add to hover information
                    color_continuous_scale=px.colors.sequential.Reds,   # Set the colorscale type
                    animation_frame = "Year",   # Values based on which animation frame will be prepared
                    range_color = [0,100],   # Range of the colorbar                    
                    title = 'Trade Openness Index for countries around the world<br>\
Source: <a href="https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions">Our World in Data</a>'
                   )

fig.update_layout(geo=dict(showcountries=True))
# Show the figure
fig.show()

Hover the mouse over countries to see trade as share of GDP. Clicking on the ▶ (play) button will animate how the trade openness index changed over time.

### Questions
1. Can you identify a common trend in trade openness index for most countries in last two decades?
2. Do you agree that the higher the trade openness index, the larger the influence of international trade on domestic economic activities will be?

## Determinants of the increased international trade

Rapid expansion of international trade was possible due to reduced transportation and communication costs stemming from the technological advances such as containerization of goods and accessible mobile phones and internet.

Run the code cells below to observe the reduction in transportation and communications costs relative to 1930.

# Import the dataset
df_costs = pd.read_csv('./Data/real-transport-and-communication-costs.csv')

# Display the top 5 rows
df_costs.head()

# Create a plotly figure object (like an empty figure)
fig = go.Figure()

# Create traces
for i in df_costs.columns[3:]:
    
    # Add trace for each column (variable) in dataset
    fig.add_trace(go.Scatter(x=df_costs['Year'], y=df_costs[i],
                    mode='lines+markers',
                    name=i))
    
# Change the figure layout
fig.update_layout(
    
    # Change properties of x-axis
    xaxis=dict(
        linecolor='rgb(204, 204, 204)',   # color of x-axis
        mirror=True,   # should axis be mirrored?
        linewidth=2,   # width of x-axis
        ticks='outside',   # location of x-ticks
        tickfont=dict(
            size=14,   # size of x-ticks
            color='rgb(82, 82, 82)',   # color of x-ticks
        ),
    ),
    
    # Change properties of y-axis
    yaxis=dict(
        title=dict(   
            text = 'Cost Relative to 1930 (%)',   # y-axis title
            font=dict(
                size=16,   # size of y-axis title
            )
        ),
        linecolor='rgb(204, 204, 204)',   # color of y-axis
        mirror=True,   # should axis be mirrored?
        linewidth=2,   # width of y-axis
        ticks='outside',   # location of y-ticks
        tickfont=dict(
            size=14,   # size of y-ticks
            color='rgb(82, 82, 82)',   # color of y-ticks
        ),
    ),
    plot_bgcolor='white',   # Background color
    legend_orientation="h",   # Orientation of legend
    
    # Title for the figure (as an annotation)
    annotations=[dict(xref='paper',   
                      yref='paper', 
                      x=0.5, y=1.2,   # Position of the title
                      xanchor='center', yanchor='top',
                      text='Transport and Communication Costs relative to 1930<br>\
Source: <a href="https://ourworldindata.org/trade-and-globalization">Our World in Data</a> ',   # Text of the title
                      font=dict(size=18),   # Font size of the title
                      showarrow=False)]
)

# Show the figure
fig.show()

### Discussion Questions:

1. Discuss how the *container revolution* was able to reduce the transportation cost by a large margin.
2. Would you consider transportation and communication technologies as major *globalizing forces*? Why or why not?

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)