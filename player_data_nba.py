# NBA scraper
#import nba_scraper.nba_scraper as ns

# test scrap
#nba_df = ns.scrape_date_range('2020-01-01', '2020-01-01', data_format='csv')

#nba_df = ns.scrape_date_range('2019-01-01', '2019-01-01')


# nba_df.head(3)
# nba_df.dtypes


# self build scraper
# based on https://towardsdatascience.com/web-scraping-nba-stats-4b4f8c525994

# load packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# NBA season we will be analyzing
year = 2019  # URL page we will scraping (see image above)
# this is the HTML from the given URL
url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(
    year)
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
player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]


stats = pd.DataFrame(player_stats, columns=headers)
print(stats.head(10))
