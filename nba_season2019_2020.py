# load packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# NBA season we will be analyzing
year = 2019  # URL page we will scraping (see image above)
# this is the HTML from the given URL
url = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_2020.html%3Fsr%26utm_source%3Ddirect%26utm_medium%3DShare%26utm_campaign%3DShareTool&div=div_team-stats-per_game"
html = urlopen(url)

soup = BeautifulSoup(html, 'html.parser')

# use findALL() to get the column headers
# use getText()to extract the text we need into a list
soup.findAll('tr', limit=2)
# exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
headers = headers[1:]
print(headers)


# avoid the first header row
rows = soup.findAll('tr')[1:]
nba_season_2021 = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]


stats = pd.DataFrame(player_stats, columns=headers)
print(stats.head(10))