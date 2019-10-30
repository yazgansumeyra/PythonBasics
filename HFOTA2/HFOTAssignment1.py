# Necessary import
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# used when all data needs to merge
data1 = pd.read_csv("HFOTA2/10.21_HFOT.txt", sep="\t", header=None)
data2 = pd.read_csv("HFOTA2/10.22_HFOT.txt", sep="\t", header=None)
out1 = data1.append(data2)
data3 = pd.read_csv("HFOTA2/10.23_HFOT.txt", sep="\t", header=None)
out2 = out1.append(data3)
print(out2.shape)
data4 = pd.read_csv("HFOTA2/10.24NIGHT10.25_HFOT.txt", sep="\t", header=None)
data = out2.append(data4)
# used when all data needs to merge
print(data.shape)

data.columns = ["time", "value", "place", "type", "extraTime"]

del data["extraTime"]  # deleting invalid time
print(data.tail())  # printing new data

# print(data.groupby("place")["value"].mean())
# print(data.groupby("type")["value"].mean())

# plot before removing outliers
data.plot.line(x="place", y="value")
plt.show()  # Display the plot

data_filtered = data[data["value"] <= 200]  # filter data
print(data_filtered.groupby("type")["value"].mean())
print(data_filtered.groupby("place")["value"].mean())

# plot after removing outliers
data_filtered.plot(x="place", y="value", kind="line")
plt.show()  # Display the plot

dataFiltered2 = data[
    (data["place"] == "B SPACE") | (data["place"] == "B SPACE AFTER LECTURE")
]  # filter data to just get B Space and After lecture values

dataFiltered2.plot(x="time", y="value", kind="line", color="gray")
plt.show()  # Display the plot

data_filtered3 = data[data["type"] != "LECTURE"]  # filter data get rid of lecture type

data_filtered3.groupby("type")["value"].mean().plot(
    x="type",
    y="value",
    kind="bar",
    rot=0,
    color=["#d5e8d4", "#fad7ac", "#fad9d5", "#fad9d5"],
)  # plot type of places as bar chart
plt.show()  # Display the plot
