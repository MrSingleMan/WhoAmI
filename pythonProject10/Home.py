import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

uniq_val = data['whoAmI'].unique()

newdata = pd.DataFrame()
for val in uniq_val:
    newdata[val] = data['whoAmI'].apply(lambda x: 1 if x == val else 0)

newdata.head()

print(data.head())
print(newdata.head())
