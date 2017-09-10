import pandas as pd
import random
# read from train.csv
df = pd.read_csv("train.csv")
# delete unused data
del df['Name']
# separate the cabin number into nubmer and string
df['Deck'] = df['Cabin'].astype(str).str[0]
# make deck into numberic
df['Deck'] = pd.Categorical(df['Deck'])
df['Deck'].cat.codes
# replace the age nan with mean of the column
mean = df['Age'].mean().round(0)
df['Age'].fillna(mean,inplace=True)
# replace the cabin nan with mode of the column
mode = df['Cabin'].mode()
df['Cabin'].fillna(mode[random.randint(0, 2)],inplace=True)
# save to train1.csv
df.to_csv("train_reorder.csv", sep='\t', encoding='utf-8')
# save to json
df.to_json("train.json",orient='records')
print df



