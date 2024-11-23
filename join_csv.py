import pandas as pd

f1 = pd.read_csv("./datasets/comments.csv")
f2 = pd.read_csv("./datasets/photos.csv")

merged = pd.merge(f1, f2, on="id", how="inner")

merged.to_csv('mergerd.csv',index=False)

print("CSV's merged")