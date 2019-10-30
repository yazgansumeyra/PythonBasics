# Necessary import
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

data = pd.read_csv(
    "HFOTA2/10.24NIGHT10.25_HFOT.txt", sep="\t", header=None
)  # take last days value

data.columns = ["time", "value", "place", "type", "extraTime"]
del data["extraTime"]  # deleting invalid time
print(data.tail())  # printing new data

print(data.groupby("place")["value"].mean())
# print(data.groupby("type")["value"].mean())

dataFiltered2 = data[(data["place"] == "STUDIO")]
print(dataFiltered2)

data.plot(x="time", y="value", kind="line", color="gray")

plt.show()  # Display the plot
