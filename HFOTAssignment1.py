# Necessary import
import pandas as pd

data = pd.read_csv("10.22_HFOT.txt", sep="\t", header=None)
data.columns = ["a", "b", "c", "d", "e"]
# Have a look at it
print(data.head())
# print(list(data.columns))
del data["a"]  # deleting date
del data["e"]  # deleting invalid time
print(data.head())  # printing new data

print(data.groupby("d")["c"].mean())
