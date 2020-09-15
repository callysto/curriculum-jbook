![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/nba.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# National Basketball Association

We can get data from [ESPN NBA Stats](https://www.espn.com/nba/stats). For example, team statistics for the following variables.

- GP: Games Played
- PTS: Points Per Game
- FGM: Average Field Goals Made
- FGA: Average Field Goals Attempted
- FG%: Field Goal Percentage
- 3PM: Average 3-Point Field Goals Made
- 3PA: Average 3-Point Field Goals Attempted
- 3P%: 3-Point Field Goal Percentage
- FTM: Average Free Throws Made
- FTA: Average Free Throws Attempted
- FT%: Free Throw Percentage
- OR: Offensive Rebounds Per Game
- DR: Defensive Rebounds Per Game
- REB: Rebounds Per Game
- AST: Assists Per Game
- STL: Steals Per Game
- BLK: Blocks Per Game
- TO: Turnovers Per Game
- PF: Fouls Per Game

url = 'https://www.espn.com/nba/stats/team/_/table/offensive/sort/avgPoints/dir/desc'
import pandas as pd
page = pd.read_html(url)
team_names = page[0]
team_data = page[1]
team_points = team_names.join(team_data).set_index('RK')
team_points

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)