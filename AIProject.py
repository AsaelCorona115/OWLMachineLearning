# Importing pandas in main file and the function defined in the DataProcessor module
import pandas as pd
from pandas import DataFrame
from DataProcessor import ProcessData

# Uncomment the code below to process the data for 2018-2019,
# 2020 and 2021 are done separately

# for year in range(2018, 2020):
#     for stage in range(1, 6):
#         fileName = ('UnprocessedData/' + str(year) +
#                     '/' + str(year) + 'stage' + str(stage) + '.csv')
#         fileDestination = ('ProcessedData/' + str(year) +
#                            '/' + str(year) + 'stage' + str(stage) + '.csv')
#         if(stage == 5):
#             fileName = ('UnprocessedData/' + str(year) +
#                         '/' + str(year) + 'playoffs.csv')
#             fileDestination = ('ProcessedData/' + str(year) +
#                                '/' + str(year) + 'playoffs.csv')
#         ProcessData(fileName, fileDestination)


# Uncomment the code below to process the data for 2020
# for stage in range(1, 3):
#     fileName = ('UnprocessedData/2020/2020stage' + str(stage) + '.csv')
#     fileDestination = ('ProcessedData/2020/2020stage' + str(stage) + '.csv')
#     ProcessData(fileName, fileDestination)
