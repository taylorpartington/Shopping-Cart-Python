import pandas as pd
import numpy as np


class DataAnalysis:

    def __init__(self,filename):
        x = pd.read_csv(filename)
        data = pd.DataFrame(x)
        self.data = data
        self.item = data["Item"]
        self.price = data["Price"]

    def GetTotalPrice(self):
        return round(sum(self.price),2)

    def StatisticalOutput(self):
        f = open("analysis.txt", 'w')
        f.write("Total Items: " + str(len(self.data)) + "\n")
        f.write("Sub-total: $" + str(round(sum(self.price),2)) + "\n")
        f.write(self.price.describe())
        f.close()


