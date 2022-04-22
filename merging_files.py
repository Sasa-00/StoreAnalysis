import pandas as pd
import os

# Here i merged all files from Sales_Data folder to Output folder


def merge_csv():

    path = "/Users/milja/PycharmProjects/StoreAnalysis/SalesAnalysis/Sales_Data/"
    path2 = "/Users/milja/PycharmProjects/StoreAnalysis/SalesAnalysis/Output/"

    file_list = [path + f for f in os.listdir(path) if f.startswith("Sales_")]
    csv_list = []
    for file in file_list:
        csv_list.append(pd.read_csv(file))
    csv_merged = pd.concat(csv_list)
    csv_merged.to_csv(path2 + "Sales_2019.csv", index=False)
