from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import pandas as pd
def connect():
    try:
        username=os.environ['MONGO_USERNAME']
        password=os.environ['MONGO_PASSWORD']
        uri = f"mongodb+srv://{username}:{password}@beatbuddy.27abfpb.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        db=client['SongsBackend']
        collection=db['Songs_Data']
        cursor= collection.find()
        df=pd.DataFrame(list(cursor))
        df.to_csv('data/cleaned_dataset.csv')
    except Exception as e:
        print(f"Error while connection :: {e}")