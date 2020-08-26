#import data
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

url = "https://stats.nba.com/standings/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#Identify header
header = soup.findAll('tr')
print(header)

#extract columns
columns = [col.get_text() for col in header.find_all('td')]

final_df = pd.DataFrame(columns=columns)
print(final_df)