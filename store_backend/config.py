import pymongo

mongo_url = "mongodb+srv://shvkii:acndelgado0811@cluster0.azfkp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url)

# get the specific database
db = client.get_database("ShopFlowBox")