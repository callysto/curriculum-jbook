![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/example-project-income-per-person.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Stats Project - Income Per Person

#### by Annya Marx

For this project we used secondary data from [Gapminder](https://www.gapminder.org) about [countries' gross domestic product (GDP) per person](http://gapm.io/dgdppc).

## Research Question

Are there more countries with a high GDP per person or a low GDP per person? How does Canada compare to other countries?

## Getting Data

spreadsheet_key = '10vHiHnBQre07TwX75vTc_H1lf-w5-hbe5mZH4ro6QNE'
spreadsheet_gid = '140930349'

import pandas as pd
csv_link = 'https://docs.google.com/spreadsheets/d/'+spreadsheet_key+'/export?gid='+spreadsheet_gid+'&format=csv'
data = pd.read_csv(csv_link, skiprows=2)
data = data.dropna()
data

We have data for 201 countries or regions, for the years 1800 to 2040 (which includes projections).

## 2019 Statistics

Let's look at statistical calculations for the year 2019.

columns = ['Country Name', '2019']
data[columns].describe()

Since that doesn't include the median let's find that.

data['2019'].median()

The mode is not a useful measure of central tendency here, since there are all unique values in this column.

len(data['2019'].unique())

We do see a large range in the data (631 to 113331), meaning that there is a large difference between the poorest countries and riches countries in terms of GDP per person.

## Visualizations

### Bar Charts

Let's create a bar chart of our sorted 2019 GDP per person data.

import plotly_express as px
fig = px.bar(data.sort_values('2019'), x='Country Name', y='2019', title='2019 GDP Per Person')
fig.show()

It looks like there are three countries that may be considered outliers for their high GDP per person (Qatar, Luxembourg, and Singapore). However they are probably not skewing the results significantly, and don't need to be removed before looking at central tendency and dispersion.

To compare some countries, let's make a bar chart comparing 2019 GDP per person Canada to the top five and bottom five countries.

sorted_data = data.sort_values('2019')
bottom_five = sorted_data.head()['Country Name'].tolist()
top_five = sorted_data.tail()['Country Name'].tolist()
countries = ['Canada']
countries.extend(bottom_five)
countries.extend(top_five)
px.bar(sorted_data[sorted_data['Country Name'].isin(countries)], x='Country Name', y='2019', title='2019 GDP Per Person')

It looks like Canada's GDP per person is closer to the top five. Let's compare it to the mean and median.

print('Mean', data['2019'].mean())
print('Median', data['2019'].median())

canada_row = data[data['Country Name']=='Canada'].index[0]
print('Canada', data.loc[canada_row]['2019'])

We can see that Canada's GDP per person is more than twice the mean value, and almost four times the median value.

### Histogram

Next let's create a histogram with 6 bins.

px.histogram(data, x='2019', nbins=6, title='Histogram of 2019 GDP Per Person')

The histogram shows that the data are not normally distributed. There are a lot more countries with a lower GDP per person than in the higher categories.

## Conclusion

Based on 2019 data, there are many more countries in our world with a low gross domestic product per person. Canada's GDP per person is well above average.

It would be interesting to see if and how this has changed over the years, and how it is predicted to change over time.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)