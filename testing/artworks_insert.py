"""
 Testing script. Populating gallery collection with test data.
 Adding artworks array items (objects).
"""
import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "msp3DB"
COLLECTION = "gallery"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]


"""
    Gallery contains an array of artworks.
    Each element is an object of art.
"""
agallery = coll.find_one({"year": "2021"})

print(agallery)

"""
upd_artwork = coll.update_one({"year": "2021"},
                              {"$addToSet": {"artworks": {"artist": "Mike Green",
                                                         "title": "Torso",
                                                         "media": "soft pastel",
                                                         "height": 16.0,
                                                         "width": 10.0,
                                                         "image": "../static/img/gallery/torso.jpg",
                                                         "price": "NFS",
                                                         "sold": False}}})
"""

upd_artwork = coll.update_one({"year": "2021"},
                              {"$addToSet": {"artworks": {"artist": "Mike Green",
                                                          "title": "Therapy",
                                                          "media": "soft pastel",
                                                          "height": 16.0,
                                                          "width": 10.0,
                                                          "image": "../static/img/gallery/therapy_58.jpg",
                                                          "price": "NFS",
                                                          "sold": False}}})

print(upd_artwork)
agallery = coll.find_one({"year": "2021"})

print(agallery)

upd_artwork = coll.update_one({"year": "2021"},
                              {"$addToSet": {"artworks": {"artist": "Mike Green",
                                                          "title": "Becca",
                                                          "media": "soft pastel",
                                                          "height": 10.0,
                                                          "width": 16.0,
                                                          "image": "../static/img/gallery/pict2434_becca.jpg",
                                                          "price": "NFS",
                                                          "sold": False}}})

agallery = coll.find_one({"year": "2021"})

print(agallery)
