# load packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
import requests

# NBA season we will be analyzing
year = 2019  # URL page we will scraping (see image above)
# this is the HTML from the given URL
url = "https://www.basketball-reference.com/boxscores/"

page = requests.get(url)
data = page.text


soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify

soup


# use findALL() to get the column headers

row = soup.find_all('tr', attrs = {'class': 'poptip right'})
print(row)


for data in row.find_all('td'):
    print(data.get_text())



headers = headers[0:4]
print(headers)

soup.findAll('tr', limit=3)# use getText()to extract the text we need into a list


header = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]# exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
print(headers)

# avoid the first header row
rows = soup.findAll('tr')[1:]
game_results = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

print(game_results)

game_stats = pd.DataFrame(game_results, columns=headers)
