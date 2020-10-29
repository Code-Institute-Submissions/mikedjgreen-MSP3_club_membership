# Testing script. Populating members collection with test data.
import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "msp3DB"
COLLECTION = "members"


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
#     "firstname": "Mike",
#     "lastname": "Green",
#     "email": "mike.green@anywhere.com",
#     "phone": "555-0123456789",
#     "newmember": "true",
#     "family": "false",
#     "guest": "false",
#     "paid": "false",
#     "bio": "Paints in acrylics and pastels. Favours charcoal for life class"
# }
# coll.insert(new_doc)

""" Insert multipe documents """
new_docs = [{
     "firstname": "Petunia",
     "lastname": "Pootle-Phipps",
     "email": "pet.poot@anywhere.com",
     "phone": "555-0123456798",
     "newmember": "false",
     "family": "false",
     "guest": "false",
     "paid": "true",
     "bio": "Paints in oils and collage."
 }, {
     "firstname": "Tarquin",
     "lastname": "Chalmondley-Smythe",
     "email": "tarq.chalm@anywhere.com",
     "phone": "555-0123456707",
     "newmember": "false",
     "family": "true",
     "guest": "false",
     "paid": "true",
     "bio": "Paints in guache and watercolour."
 }]
coll.insert_many(new_docs)


documents = coll.find()
for member in documents:
    print(member)
