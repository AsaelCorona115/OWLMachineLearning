# Importing Pandas
import pandas as pd


# how to import data from a csv file using panda.
stats = pd.read_csv('OW_ProPlayersStats/2018/phs_2018_stage_1.csv')


# How to select only certain columns from the file and with a range
# print(stats[['player', 'stat_name', 'stat_amount']][0:5])


# Select single row
# print(stats.iloc[0])

# Select range of rows
# print(stats.iloc[0:1])

# Select specific part of a single row
# print(stats.iloc[0, 9])

# Iterate through all the rows and do something there
# for i, row in stats.iterrows():
#     print(row['player'])

# Access rows that return true for a specific condition:
# print(stats.loc[stats['hero'] == "All Heroes"])

# Sorting the data
# print(stats.sort_values('player'))
