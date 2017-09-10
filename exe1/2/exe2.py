import pandas as pd
# from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer

f = open('reviews_Automotive_5.json', 'rb')
stopWord = pd.read_csv("stop-word-list.csv")
data = f.readlines()
data = map(lambda x: x.rstrip(), data)

dataJsonStr = "[" + ','.join(data) + "]"
dataDf = pd.read_json(dataJsonStr)

dataDf['reviewText'] = dataDf['reviewText'].str.lower()

dataDf["reviewText"] = dataDf['reviewText'].str.replace('[^\w\s]','')
dataDf["summary"] = dataDf['summary'].str.replace('[^\w\s]','')

dataDf['reviewText']=dataDf['reviewText'].apply(lambda x: [item for item in x if item not in stopWord])
dataDf['summary']=dataDf['summary'].apply(lambda x: [item for item in x if item not in stopWord])

stemmer = SnowballStemmer("english")
df["reviewText"] = df["reviewText"].map(lambda x: [stemmer.stem(word) for word in x])

df[df["overall"]>=4].to_csv("pos.txt")
df[df["overall"]<=2].to_csv("neg.txt")

print dataDf