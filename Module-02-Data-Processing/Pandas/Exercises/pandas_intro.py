import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/Pandas/data.csv')
#print(df)
print(df.head()) # this show the top some values of dataset.

#print(df.head(10)) # this print the top 10 value.

#print(df.tail()) # this print bottom some values.

#print(df.sample(5)) # this randomly print numbers.

#print(df.shape)

#df.Pulse # to print one object.

#type(df.Pulse) # pandas.core.series.Series --> in pandas to column we called series.

#df.Pulse.max() # to find the maximum value in pulse series
#df.Pulse.min() # to find the minimum values in Pulse series