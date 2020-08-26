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
page
# %%
#look at the content and type of the page
page.content
type(page.content)
# %%
#make the page content better visible
soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify()