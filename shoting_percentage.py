
# %%
# load packages
import pandas as pd
import html5lib
from functools import reduce
import numpy as np

# %%

### three pointers attempted per game
# scrap data
x = 'three-pointers-attempted-per-game'
df2019 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2019-06-14'.format(x), index_col=1)[0]
df2017 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2017-06-13'.format(x), index_col=1)[0]
df2015 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2015-06-16'.format(x), index_col=1)[0]
df2013 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2013-06-20'.format(x), index_col=1)[0]
df2011 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2011-06-12'.format(x), index_col=1)[0]
df2009 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2009-06-15'.format(x), index_col=1)[0]
df2007 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2007-06-15'.format(x), index_col=1)[0]
df2005 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2005-06-24'.format(x), index_col=1)[0]


# merge data
dfs = [df2019, df2017, df2015, df2013, df2011, df2009, df2007, df2005]

df2005_2019 = reduce(lambda left, right: pd.merge(left, right, on='Team'), dfs)

attempts_3pts = df2005_2019[['2018', '2017', '2016', '2015', '2014', '2013',
                             '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004' ]]

# calculate mean/median
mean = attempts_3pts.mean(axis=0, skipna=False).round(2).rename('attempts_mean')
attempts_3pts = attempts_3pts.append(mean)

median = attempts_3pts.median(axis=0, skipna=False).rename('attempts_median')
attempts_3pts = attempts_3pts.append(median)

attempts_median = attempts_3pts.loc[['attempts_median']]
attmepts_mean = attempts_3pts.loc[['attempts_mean']]


# %%$
### three points made per game

# scrap data
x = 'three-pointers-made-per-game'
df2019 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2019-06-14'.format(x), index_col=1)[0]
df2017 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2017-06-13'.format(x), index_col=1)[0]
df2015 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2015-06-16'.format(x), index_col=1)[0]
df2013 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2013-06-20'.format(x), index_col=1)[0]
df2011 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2011-06-12'.format(x), index_col=1)[0]
df2009 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2009-06-15'.format(x), index_col=1)[0]
df2007 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2007-06-15'.format(x), index_col=1)[0]
df2005 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2005-06-24'.format(x), index_col=1)[0]

#merge dataframes
dfs = [df2019, df2017, df2015, df2013, df2011, df2009, df2007, df2005]

df2005_2019 = reduce(lambda left, right: pd.merge(left, right, on='Team'), dfs)

#select relevant columns
made_3pts = df2005_2019[['2018', '2017', '2016', '2015', '2014', '2013',
                         '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004' ]]


#calculate mean/median
mean = made_3pts.mean(axis=0, skipna=False).round(2).rename('made_mean')
made_3pts = made_3pts.append(mean)

median = made_3pts.median(axis=0, skipna=False).rename('made_median')
made_3pts = made_3pts.append(median)

made_median = made_3pts.loc[['made_median']]
made_mean = made_3pts.loc[['made_mean']]





# %%$

### three point percentage
# scrap data
x = 'three-point-pct'
df2019 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2019-06-14'.format(x), index_col=1)[0]
df2017 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2017-06-13'.format(x), index_col=1)[0]
df2015 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2015-06-16'.format(x), index_col=1)[0]
df2013 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2013-06-20'.format(x), index_col=1)[0]
df2011 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2011-06-12'.format(x), index_col=1)[0]
df2009 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2009-06-15'.format(x), index_col=1)[0]
df2007 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2007-06-15'.format(x), index_col=1)[0]
df2005 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2005-06-24'.format(x), index_col=1)[0]

# merge data frames
dfs = [df2019, df2017, df2015, df2013, df2011, df2009, df2007, df2005]
df2005_2019 = reduce(lambda left, right: pd.merge(left, right, on='Team'), dfs)

# select relevant data
percent_3pts = df2005_2019[['2018', '2017', '2016', '2015', '2014', '2013',
                            '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004' ]]

# Change format to numeric
percent_3pts = percent_3pts.replace({'%':''}, regex=True)
percent_3pts = percent_3pts.apply(pd.to_numeric, errors="ignore")

# Calculate mean / median
mean = percent_3pts.mean(axis=0, skipna=False).round(2).rename('percent_mean')
percent_3pts = percent_3pts.append(mean)

median = percent_3pts.median(axis=0, skipna=False).rename('percent_median')
percent_3pts = percent_3pts.append(median)

percent_median = percent_3pts.loc[['percent_median']]
percent_mean = percent_3pts.loc[['percent_mean']]

# %%$

### three point  points_made

# scrap data
x = 'three-point-rate'
df2019 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2019-06-14'.format(x), index_col=1)[0]
df2017 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2017-06-13'.format(x), index_col=1)[0]
df2015 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2015-06-16'.format(x), index_col=1)[0]
df2013 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2013-06-20'.format(x), index_col=1)[0]
df2011 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2011-06-12'.format(x), index_col=1)[0]
df2009 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2009-06-15'.format(x), index_col=1)[0]
df2007 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2007-06-15'.format(x), index_col=1)[0]
df2005 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2005-06-24'.format(x), index_col=1)[0]

# merge dfs
dfs = [df2019, df2017, df2015, df2013, df2011, df2009, df2007, df2005]

df2005_2019 = reduce(lambda left, right: pd.merge(left, right, on='Team'), dfs)

rate_3pts = df2005_2019[['2018', '2017', '2016', '2015', '2014', '2013',
                         '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004']]

# Change format to numeric
rate_3pts = rate_3pts.replace({'%':''}, regex=True)
rate_3pts = rate_3pts.apply(pd.to_numeric, errors="ignore")

# Calculate mean / median
mean = rate_3pts.mean(axis=0, skipna=False).round(2).rename('rate_mean')
rate_3pts = rate_3pts.append(mean)

median = rate_3pts.median(axis=0, skipna=False).rename('rate_median')
rate_3pts = rate_3pts.append(median)

rate_median = rate_3pts.loc[['rate_median']]
rate_mean = rate_3pts.loc[['rate_mean']]

# %%$

### points made from 3points

# scrap data
x = 'percent-of-points-from-3-pointers'
df2019 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2019-06-14'.format(x), index_col=1)[0]
df2017 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2017-06-13'.format(x), index_col=1)[0]
df2015 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2015-06-16'.format(x), index_col=1)[0]
df2013 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2013-06-20'.format(x), index_col=1)[0]
df2012 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2012-06-21'.format(x), index_col=1)[0]
    
# merge dfs
dfs = [df2019, df2017, df2015, df2013, df2012]

df2012_2019 = reduce(lambda left, right: pd.merge(left, right, on='Team'), dfs)

points_made_3pts = df2012_2019[['2018', '2017', '2016', '2015', '2014', '2013','2012', '2011_y', '2010']]

# Change format to numeric
points_made_3pts = points_made_3pts.rename(columns={'2011_y':'2011'})
points_made_3pts = points_made_3pts.replace({'%':''}, regex=True)
points_made_3pts = points_made_3pts.apply(pd.to_numeric, errors="ignore")


# Calculate mean / median
mean = points_made_3pts.mean(axis=0, skipna=False).round(2).rename('points3_made_mean')
points_made_3pts = points_made_3pts.append(mean)

median = points_made_3pts.median(axis=0, skipna=False).rename('points3_made_median')
points_made_3pts = points_made_3pts.append(median)

points_made_median = points_made_3pts.loc[['points3_made_median']]
points_made_mean = points_made_3pts.loc[['points3_made_mean']]

# %%$

### points made from 3points

# scrap data
x = 'percent-of-points-from-2-pointers'
df2019 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2019-06-14'.format(x), index_col=1)[0]
df2017 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2017-06-13'.format(x), index_col=1)[0]
df2015 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2015-06-16'.format(x), index_col=1)[0]
df2013 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2013-06-20'.format(x), index_col=1)[0]
df2012 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2012-06-21'.format(x), index_col=1)[0]
    
# merge dfs
dfs = [df2019, df2017, df2015, df2013, df2012]

df2012_2019 = reduce(lambda left, right: pd.merge(left, right, on='Team'), dfs)

points_made_2pts = df2012_2019[['2018', '2017', '2016', '2015', '2014', '2013','2012', '2011_y', '2010']]

# Change format to numeric
points_made_2pts = points_made_2pts.rename(columns={'2011_y':'2011'})
points_made_2pts = points_made_2pts.replace({'%':''}, regex=True)
points_made_2pts = points_made_2pts.apply(pd.to_numeric, errors="ignore")


# Calculate mean / median
mean = points_made_2pts.mean(axis=0, skipna=False).round(2).rename('points2_made_mean')
points_made_2pts = points_made_2pts.append(mean)

median = points_made_2pts.median(axis=0, skipna=False).rename('points2_made_median')
points_made_2pts = points_made_2pts.append(median)

points2_made_median = points_made_2pts.loc[['points2_made_median']]
points2_made_mean = points_made_2pts.loc[['points2_made_mean']]

# %%$
### field goals made

# scrap data
x = 'field-goals-made-per-game'
df2019 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2019-06-14'.format(x), index_col=1)[0]
df2017 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2017-06-13'.format(x), index_col=1)[0]
df2015 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2015-06-16'.format(x), index_col=1)[0]
df2013 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2013-06-20'.format(x), index_col=1)[0]
df2011 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2011-06-12'.format(x), index_col=1)[0]
df2009 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2009-06-15'.format(x), index_col=1)[0]
df2007 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2007-06-15'.format(x), index_col=1)[0]
df2005 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2005-06-24'.format(x), index_col=1)[0]

# merge dfs
dfs = [df2019, df2017, df2015, df2013, df2011, df2009, df2007, df2005]

df2005_2019 = reduce(lambda left, right: pd.merge(left, right, on='Team'), dfs)

fieldgoal_made = df2005_2019[['2018', '2017', '2016', '2015', '2014', '2013',
                         '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004']]


# Calculate mean / median
mean = fieldgoal_made.mean(axis=0, skipna=False).round(2).rename('fieldgoal_made_mean')
fieldgoal_made = fieldgoal_made.append(mean)

median = fieldgoal_made.median(axis=0, skipna=False).rename('fieldgoal_made_median')
fieldgoal_made = fieldgoal_made.append(median)

fieldgoal_made_median = fieldgoal_made.loc[['fieldgoal_made_median']]
fieldgoal_made_mean = fieldgoal_made.loc[['fieldgoal_made_mean']]

# %%$
### field goals attempts

# scrap data
x = 'field-goals-attempted-per-game'
df2019 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2019-06-14'.format(x), index_col=1)[0]
df2017 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2017-06-13'.format(x), index_col=1)[0]
df2015 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2015-06-16'.format(x), index_col=1)[0]
df2013 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2013-06-20'.format(x), index_col=1)[0]
df2011 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2011-06-12'.format(x), index_col=1)[0]
df2009 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2009-06-15'.format(x), index_col=1)[0]
df2007 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2007-06-15'.format(x), index_col=1)[0]
df2005 = pd.read_html(
    'https://www.teamrankings.com/nba/stat/{}?date=2005-06-24'.format(x), index_col=1)[0]

# merge dfs
dfs = [df2019, df2017, df2015, df2013, df2011, df2009, df2007, df2005]

df2005_2019 = reduce(lambda left, right: pd.merge(left, right, on='Team'), dfs)

fieldgoal_attempt = df2005_2019[['2018', '2017', '2016', '2015', '2014', '2013',
                         '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004']]


# Calculate mean / median
mean = fieldgoal_attempt.mean(axis=0, skipna=False).round(2).rename('fieldgoal_attempt_mean')
fieldgoal_attempt = fieldgoal_attempt.append(mean)

median = fieldgoal_attempt.median(axis=0, skipna=False).rename('fieldgoal_attempt_median')
fieldgoal_attempt = fieldgoal_attempt.append(median)

fieldgoal_attempt_median = fieldgoal_attempt.loc[['fieldgoal_attempt_median']]
fieldgoal_attempt_mean = fieldgoal_attempt.loc[['fieldgoal_attempt_mean']]


# %%$

agg_frames = [attempts_median,attmepts_mean,rate_mean,rate_median,
    percent_mean,percent_median,made_mean,made_median, points_made_mean,
    points_made_median, points2_made_median, points2_made_mean, fieldgoal_made_median,
    fieldgoal_made_mean, fieldgoal_attempt_median, fieldgoal_attempt_mean]
aggregated_3points = pd.concat(agg_frames)

aggregated_3points = aggregated_3points.transpose()
aggregated_3points = aggregated_3points.rename_axis('Year')

aggregated_3points.to_csv('aggregated_data_three_point.csv', index=True)


# print as csv
#made_3pts.to_csv('made_3pts.csv', index=False)
#attempts_3pts.to_csv('attempts_3pts.csv', index=False)
# points_made_3pts.to_csv(' points_made_3pts.csv', index=False)
#percent_3pts.to_csv('percent_3pts.csv', index=False)

# %%$

