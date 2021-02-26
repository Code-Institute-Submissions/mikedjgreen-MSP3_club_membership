# Testing script. Populating activities collection with test data.
import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE =  os.environ.get("MONGO_DBNAME")
COLLECTION = "activities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

documents = coll.find()

""" Insert a single document """
# new_doc = {
#     "activity_date": "01 February, 2021",
#     "activity_time": "19:30",
#     "activity_duration": "2 Hours",
#     "lead_member_firstname": "Mike",
#     "lead_member_lastname": "Green",
#     "description": "Demonstration of post-Euclidian perspective"
# }
# coll.insert(new_doc)

""" Insert multipe documents """
new_docs = [{
    "activity_date": "11 February, 2021",
    "activity_time": "19:30",
    "activity_duration": "2 Hours",
    "lead_member_firstname": "Tarquin",
    "lead_member_lastname": "Chalmondley-Smythe",
    "description": "Demonstration of pre-raphaelite naivety"
 },
 {
    "activity_date": "25 February, 2021",
    "activity_time": "19:30",
    "activity_duration": "2 Hours",
    "lead_member_firstname": "Petunia",
    "lead_member_lastname": "Pootle-Phipps",
    "description": "Monet in Giverny"
 }]
coll.insert_many(new_docs)


documents = coll.find()
for activity in documents:
    print(activity)
