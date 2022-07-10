import os
import pandas as pd
import numpy as np


def formatData(dataPath, resultsPath):
    print("Formatting Data:")
    results = pd.read_csv(resultsPath)
    results = results[["match_id", "match_winner"]].groupby(["match_id"]).aggregate("first")

    data = pd.read_csv(dataPath)
    
    data = data[data["team"] != data["player"]]


    data = data.groupby(["match_id", "team", "stat_name"])['stat_amount'].aggregate("mean").unstack().reset_index()

    data = data.join(results, on="match_id", how='left')
    data["win"] = np.where(data["team"] == data["match_winner"], 1, 0);
    data = data.drop(columns=["team", "match_winner"])

    data = data.set_index("match_id")
    data = data.diff().groupby(["match_id"]).aggregate("last")
    data["win"] = np.where(data["win"] == 1, "Win", "Loss")

    data = data.dropna(axis=1);
    data = data.drop(columns=["time_played"])
    data.to_csv("formattedData.csv")
    print("Data formatted successfully")

def combineData():
    print("Combining Data:")
    data = pd.DataFrame();
    dirs = os.listdir("./UnprocessedData")
    
    for i in dirs:
        if not (os.path.isdir("./UnprocessedData/" + i)): continue
        files = os.listdir("./UnprocessedData/" + i)
        if (files == None): continue

        for j in files:
            if (data.empty):
                data =  pd.read_csv("./UnprocessedData/" + i + "/" + j)
                print("Reading File: " + j)
            else:
                dataFile = pd.read_csv("./UnprocessedData/" + i + "/" + j)
                print("Reading File: " + j)
                data = pd.concat([data, dataFile], join="inner", ignore_index=True, sort=False)

    data = data.loc[data['hero'] == "All Heroes"]
    data = data.drop(columns=["start_time", "stage", "map_type", "map_name", "hero"])
    data.to_csv("CombinedData.csv")
    print("Data combined successfully.")
        
def main():
    combineData()
    formatData("./CombinedData.csv", "./match_map_stats.csv")

if (__name__ == "__main__"):
    main()
