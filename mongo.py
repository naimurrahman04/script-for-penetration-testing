import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://172.30.29.67:27017/")

# Get a reference to the database
db = client["mydatabase"]

# Get a reference to a collection
collection = db["mycollection"]

# Insert a document into the collection
document = {"test": "test", "test": 30}
collection.insert_one(document)

# Query the collection for documents
cursor = collection.find({})
for document in cursor:
    print(document)

# Disconnect from the server
client.close()
