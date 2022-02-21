import pandas as pd
import numpy as np


class DataAnalysis:

    def __init__(self,filename):
        x = pd.read_csv(filename)
        data = pd.DataFrame(x)
        self.data = data
        self.item = data["Item"]
        self.unit_price = data["Price"]
        self.quantity = data["Quantity"]
        self.price = self.unit_price*self.quantity
        self.price_min = data.iloc[self.unit_price.idxmin()]
        self.price_max = data.iloc[self.unit_price.idxmax()]

    def GetTotalPrice(self):
        return round(sum(self.price),2)

    def StatisticalOutput(self):
        f = open("analysis.txt", 'w')
        f.write("Total Quantity of Items: " + str(len(self.data)) + "\n")
        f.write("Sub-total: $" + str(round(sum(self.price),2)) + "\n")
        f.write("")
        f.write("Cheapest Item: " + self.price_min["Item"]+" $" + str(self.price_min["Price"]) + "\n")
        f.write("Most Expensive Item: " + self.price_max["Item"]+" $" + str(self.price_max["Price"]) + "\n")
        f.close()


