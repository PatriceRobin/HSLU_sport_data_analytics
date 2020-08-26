# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# load packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
# %%
# ask for player
first_name = input('ENTER FIRST NAME (no speacial characters)')
last_name = input('ENTER LAST NAME (no speacial characters)')

fullname = last_name[0:5] + first_name[0:2] + '01'
print(fullname)

# %%
# ask for Season
season = input('ENTER SEASON (e.g. for season 2017/2018 enter 2018')
# %%
# get website
# in this
url = 'https://www.basketball-reference.com/players/s/{}/gamelog/{}/'.format(fullname, season)
print(url)
page = requests.get(url)
# %%
#look at the content and type of the page
page.content
type(page.content)
# %%
#make the page content better visible
soup = BeautifulSoup(page.content, 'html.parser')
#soup.prettify()
# %%
#add the stats list
stats = ['game_season', 'date_game', 'age', 'team_id', 'game_location', 'opp_id', 'game_result','gs', 'mp', 'fg',
'fga', 'fg_pct', 'fg3', 'fg3a', 'fg3_pct', 'ft', 'fta', 'ft_pct', 'orb','drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'game_score', 'plus_minus']

stats_list = [[td.getText() for td in soup.findAll('td',{'data-stat': stat})] for stat in stats]
# %%
stats_left = [[td.getText() for td in soup.findAll('td', {'data-stat': stat})] for stat in stats[:7]]
stats_right = [[td.getText() for td in soup.findAll('td', {'data-stat': stat})] for stat in stats[7:]]
# %%
df_left = pd.DataFrame(stats_left).T
df_left.columns = stats[:7]
#df_left.head(5)
# %%
for i in range(len(df_left)): # exclude inaktive games
    if df_left['game_season'][i]=="":
        [stats_right[x].insert(i, '') for x in range(len(stats_right))]
# %%
df_right = pd.DataFrame(stats_right).T
df_right.columns = stats[7:]
df = pd.concat([df_left, df_right], axis=1)
print(df)

# %%

avgpts = df[df.game_season!='']['pts'].astype(int).mean().round(1)
print('average points in ' +str(season) + ': ' + str(avgpts))

avgfg = df[df.game_season!='']['fg'].astype(int).mean().round(1)
print('average field goals ' + str(season) + ': ' + str(avgfg))
# %%