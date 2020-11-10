# MongoDB indexes created for searches

## Further support document
[Text Indexes](https://docs.mongodb.com/manual/core/index-text/)

### using the python interpreter
- python3

### import mongo instance

- from club_admin import mongo 

## members collection

- mongo.db.members.create_index([("firstname","text"),("lastname","text"),("email","text")])

- mongo.db.members.index_information()
{'_id_': {'v': 2, 'key': [('_id', 1)], 'ns': 'msp3DB.members'},
 'firstname_text_lastname_text_email_text': {'v': 2,
  'key': [('_fts', 'text'), ('_ftsx', 1)],
  'ns': 'msp3DB.members',
   'weights': SON([('email', 1),
    ('firstname', 1), ('lastname', 1)]),
     'default_language': 'english',
      'language_override': 'language', 
      'textIndexVersion': 3}}

### Ended session

- quit()

