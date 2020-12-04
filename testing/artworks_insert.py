"""
 Testing script. Populating gallery collection with test data.
 Adding artworks array items (objects).
"""
import os
import pymongo
from bson.objectid import ObjectId
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


upd_artwork = coll.update_one({"year": "2021"},
                              {"$addToSet": {"artworks": { "art_id": ObjectId(),
                                                         "artist": "Mike Green",
                                                         "title": "Torso",
                                                         "media": "soft pastels",
                                                         "height": 16.0,
                                                         "width": 10.0,
                                                         "image": "../static/img/gallery/torso.jpg",
                                                         "price": "NFS",
                                                         "sold": False}}})


print(upd_artwork)


upd_artwork = coll.update_one({"year": "2021"},
                              {"$addToSet": {"artworks": {  "art_id": ObjectId(),
                                                          "artist": "Mike Green",
                                                          "title": "Therapy",
                                                          "media": "soft pastels",
                                                          "height": 16.0,
                                                          "width": 10.0,
                                                          "image": "../static/img/gallery/therapy_58.jpg",
                                                          "price": "NFS",
                                                          "sold": False}}})


print(upd_artwork)


upd_artwork = coll.update_one({"year": "2021"},
                              {"$addToSet": {"artworks": {  "art_id": ObjectId(),
                                                            "artist": "Mike Green",
                                                          "title": "Becca",
                                                          "media": "soft pastels",
                                                          "height": 10.0,
                                                          "width": 16.0,
                                                          "image": "../static/img/gallery/pict2434_becca.jpg",
                                                          "price": "NFS",
                                                          "sold": False}}})


print(upd_artwork)


upd_artwork = coll.update_one({"year": "2021"},
                              {"$addToSet": {"artworks": {  "art_id": ObjectId(),
                                                            "artist": "Tarquin Chalmondley-Smythe",
                                                          "title": "The Age of Anxiety",
                                                          "media": "soft pastels",
                                                          "height": 16.0,
                                                          "width": 10.0,
                                                          "image": "../static/img/gallery/no_image.jpg",
                                                          "price": "NFS",
                                                          "sold": False}}})


print(upd_artwork)


upd_artwork = coll.update_one({"year": "2021"},
                              {"$addToSet": {"artworks": {  "art_id": ObjectId(),
                                                            "artist": "Petunia Pootle-Phipps",
                                                          "title": "Vox",
                                                          "media": "soft pastels",
                                                          "height": 16.0,
                                                          "width": 10.0,
                                                          "image": "../static/img/gallery/voxserene_27.jpg",
                                                          "price": "NFS",
                                                          "sold": False}}})


print(upd_artwork)

agallery = coll.find_one({"year": "2021"})


print(agallery)
