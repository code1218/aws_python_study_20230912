import pandas as pd
import numpy as np

########################[Series]#########################
a = pd.Series({"a":1, "b":2, "c":3})
print(a)
print(a.index.values)

a = np.array([1,2,3,4])
b = pd.Series(a)
print(b)
print(b.index.values)

########################[DataFrame]#########################
a = {"a":[1,2,3,0], "b":[4,5,6,0], "c":[7,8,9,0], "d":[10,11,12,0]}
b = pd.Series(a)
c = pd.DataFrame(a, index=a.keys())
print(b)
print(c)

print(c.index.values)
print(c.columns)

a = pd.DataFrame({"a":(1,2,3), "b":1, "c":3})
print(a)
a.index=["x", "y", "z"]
a.columns=["i","j","k"]
print(a)

# loc = location
# iloc = index_location
print(a.loc[a["j"] == 1])
print(a.iloc[2])

a = {"a":[1,2,3], "b":[4,5,6], "c":[7,8,9], "d":[10,11,12]}
b = pd.DataFrame(a)
print(b.describe())

print(b.sum())
print(b.sum(axis=1))
print(b.min())
print(b.max())
print(b.mean()) #평균
print(b.std(), b.var()) ## 표준편차, 분산







