![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/nhl.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# National Hockey League Statistics

We can look at NHL statistics by team or by player, using data from [hockey-reference.com](https://www.hockey-reference.com) or [ESPN NHL Statistics](http://www.espn.com/nhl/statistics).


## Statistics by Team

team = 'EDM'
year = '2019'

# download the data
import pandas as pd
team_stats_url = 'https://www.hockey-reference.com/teams/'+team+'/'+year+'_games.html'
team_stats = pd.read_html(team_stats_url)[0]
# clean up the data
team_stats = team_stats[team_stats['Date']!='Date'].set_index('GP').drop(columns=['W','L','OL','Streak','Notes'])
team_stats.columns = ['Date', 'Away', 'Opponent', 'Goals For', 'Goals Against', 'Win', 'Overtime', 'Attendance', 'Duration']
team_stats = team_stats.fillna(0).replace('@', 1).replace('OT', 1).replace('W',1).replace('SO',1).replace('L',0)
# convert text string columns to number columns
team_stats['Goals For'] = pd.to_numeric(team_stats['Goals For'])
team_stats['Goals Against'] = pd.to_numeric(team_stats['Goals Against'])
team_stats['Attendance'] = pd.to_numeric(team_stats['Attendance'])
# convert duration in h:mm to duration in minutes
duration_values = team_stats['Duration'].str.split(':', expand=True).astype(int)
team_stats['Duration'] = duration_values[0]*60 + duration_values[1]
# display the data
team_stats

## Statistics by Player

This data set contains the following columns for each player in the NHL:
- GP: Games Played
- G: Goals
- A: Assists
- PTS: Points
- +/-: Plus/Minus Rating
- PIM: Penalty Minutes
- PTS/G: Points Per Game
- SOG: Shots on Goal
- PCT: Shooting Percentage
- GWG: Game-Winning Goals
- G.1: Power-Play Goals
- A.1: Power-Play Assists
- G.2: Short-Handed Goals
- A.2: Short-Handed Assists

This will take a while to run, since it needs to get data from multiple pages.

# download the data
points_url = 'http://www.espn.com/nhl/statistics/player/_/stat/points'
import pandas as pd
for i in range(20):
    try:
        p = pd.read_html(points_url+'/count/'+str(1+40*i), header=1)[0]
        p = p[p['PLAYER']!='PLAYER'].dropna(subset=['PLAYER']).fillna(method='ffill')
        if i == 0:
            points = p
        else:
            points = points.append(p).reset_index().drop(columns='index')
    # if the site has run out of data
    except:
        pass
# convert text string columns to number columns
for column in points.columns:
    if column != 'PLAYER' and column != 'TEAM':
        points[column] = pd.to_numeric(points[column])
# split the player name and position into two columns
points['POSITION'] = points['PLAYER'].str.split(',', expand=True)[1]
points['PLAYER'] = points['PLAYER'].str.split(',', expand=True)[0]
# display the data
points

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)