![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/example-project-soccer.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Stats Project - Soccer

#### by Flor Nightgale

For this project we used secondary data about [Premier League (Soccer)](https://www.premierleague.com/tables).

## Team Statistics

import pandas as pd
data = pd.read_html('https://www.espn.com/soccer/table/_/league/eng.1')
teams = data[0].join(data[1]) # join the two data tables together
teams

Columns in the data set are:
* GP: Games Played
* W: Wins
* D: Draws
* L: Losses
* F: Goals For
* A: Goals Against
* GD: Goal Difference
* P: Points

Notice that the ranking (index values) start at zero. As well, the team names got combined with their ranks and abbreviations, let's cut those out and leave just the team names.

For each team name, the second character is a lowercase letter, so we'll find the first lowercase letter then take just the characters from one before that until the end of the name.

We'll also rename the columns.

for i, row in teams.iterrows():
    for character in row[0]:
        if character.islower(): # we've found the first lowercase letter
            start_here = row[0].index(character)-1
            team_name = row[0][start_here:]
            break # stop looking through the team name
    teams.iloc[i,0] = team_name
teams.columns = ['Team','Games Played','Wins','Draws','Losses','Goals For','Goals Against','Goal Difference','Points']
teams

### Statistical Calculations

The `describe()` method does some statisical calculations for us.

team_stats = teams.describe()
team_stats

We can also find the median values.

teams.median()

The `Goal Difference` column is probably the most interesting, since it has the largest range and highest standard deviation. The top teams scored a lot more than they were scored on, and the bottom teams were scored on a lot more than they scored.



Since we are looking at data for all of the teams, we see that the mean number of wins is equal to the mean number of losses. The same goes for goals scored and goals scored against.



import plotly_express as px
fig = px.bar(team_stats.iloc[3:], y='Goal Difference', title='')
fig.show()

If we want to see which teams scored more than the mean value of "Goals For", we can use the following code.

gf_mean = teams['Goals For'].mean()
teams[teams['Goals For'] > gf_mean]

In general, but not always, the top teams scored more than the average number of goals.

Mean is probably the best measure of central tendency here, since using the median would just give us the top half of the teams. Mode wouldn't be useful because there aren't a lot of repeated values in the column.

Let's see if the top teams had fewer than the mean number of goals scored against them.

ga_mean = teams['Goals Against'].mean()
teams[teams['Goals Against'] < gf_mean]

Again, it is generally true that the top teams that had fewer goals scored against them.

### Teams Visualizations

Let's create some plots of `Wins`, `Losses`, `Draws` versus team rank.

columns = ['Wins', 'Losses', 'Draws']
for column in columns:
    fig = px.scatter(teams, x=teams.index, y=column, title=column+' vs Rank', hover_data=['Team'])
    fig.show()

## Player Data

We are also going to look at individual player data for scoring and assists. We'll download both and then look first at the top 10, `head(10)`, of the `scorers` data table.

stats = pd.read_html('https://www.espn.com/soccer/stats/_/league/ENG.1/view/scoring')
scorers = stats[0]
assists = stats[1]
scorers.head(10)

Columns:
* RK: Ranking
* P: Games played
* G: Goals scored
* A: Assists

There are quite a few missing (`NaN`) values, which means that player is tied with the player above them, so we can use `fillna(method='ffill')` which means "forward fill" values to replace missing values.

scorers = scorers.fillna(method='ffill')
scorers.head(10)

assists = assists.fillna(method='ffill')
assists.head()

Let's create histograms for these two data sets.

fig1 = px.histogram(scorers, x='G', title='Histogram of Goals Scored by Top Players')
fig1.show()
fig2 = px.histogram(assists, x='A', title='Histogram of Assists by Top Players')
fig2.show()

Both of these histograms show that there are many more players that scored (or assisted) fewer goals, so the data are not normally distributed.

## Research Question

**Does having more top scoring or top assisting players on a team mean that team has a higher standing?**

To answer this question, we will need to group the player data by team and merge the two data tables together. We'll also drop the columns that we don't need.

# group the data by team
scorers_team = scorers.groupby('Team').count().drop(columns=['RK', 'Name', 'P'])
assists_team = assists.groupby('Team').count().drop(columns=['RK', 'Name', 'P'])
# merge the players data tables
players = scorers_team.merge(assists_team, on='Team')
# create a column that adds goals and assists
players['Goals and Assists'] = players['G']+players['A']
# sort the values, create an index column, and display the data
players = players.sort_values('Goals and Assists', ascending=False).reset_index()
players

Now we need to merge this data table with the `Teams` data table from earlier.

combined_data = teams.merge(players, on='Team', how='left') # left means keep the order from the teams data table
combined_data

To see if there is a relationship between `Goals and Assists` and team rank, let's create another scatterplot.

fig = px.scatter(combined_data, y='Goals and Assists', x=combined_data.index, hover_data=['Team'], title='Goals and Assists vs Team Rank')
fig.show()

## Conclusion

It looks like higher ranked teams (lower $x$ values) tend to have more players with more goals and assists, although there is a fair amount of variation in the data.

Perhaps we could look at a similar analysis using a larger data set from a league such as the [National Hockey League](https://www.nhl.com) where there are more games played by more teams.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)