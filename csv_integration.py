import pandas as pd             #Basic imports
import pymongo
import json

#Establishing a conection
client = pymongo.MongoClient("mongodb+srv://ajithkhan:9789861061@cluster1.jc7p2iv.mongodb.net/?retryWrites=true&w=majority")
db = client.test

#database and collection
database = client['boston'] # boston is a database name
collection = database['boston_data']  # b_data is a collection name

df = pd.read_csv('/Users/ajithsmacbookair/Downloads/Data Science /LMS/Python/Python Notes /datasets/boston.csv')
df.to_json('boston_json.json')                               # saving to json file
jdf = open('boston_json.json').read()                        # loading the json file
data = json.loads(jdf)

#Inserting into Mongodb
collection.insert_many([data])