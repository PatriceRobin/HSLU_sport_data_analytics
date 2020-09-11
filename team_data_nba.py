# %%
# load data
import pandas as pd
bb_reference = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2019.html")

# %%
western_conference = bb_reference[1]
western_conference.rename(columns={'Western Conference':'Team'}, inplace=True)
western_conference['Conference'] = 'Western'
eastern_conference = bb_reference[0]
eastern_conference.rename(columns={'Eastern Conference':'Team'}, inplace=True)
eastern_conference['Conference'] = 'Eastern'

full_nba = pd.concat([western_conference, eastern_conference], axis=0)


# %%
full_nba_short = full_nba.drop(['GB','PS/G','SRS'],axis=1)
nba_win_sorted = full_nba_short.sort_values(by=['W/L%'], ascending=False)
print(nba_win_sorted)
# %%

