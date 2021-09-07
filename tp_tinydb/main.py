from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage


# Stockage ephémère
#db = TinyDB(storage=MemoryStorage)

db = TinyDB('tp_tinydb/data.json', indent=4)

db.insert({"name" : "Patrick", "Score" : 0})
db.insert_multiple([
    {"name" : "Theo", "score" : 20},
    {"name" : "Romain", "score" : 45},
    {"name" : "Damien", "score" : 124}
    ])

user = Query()

data = db.search(user.name == "Romain")
unique_data = db.get(user.name == "Romain")

print(data)
print(unique_data)

high_scores = db.search(where("score") > 0)

print(high_scores)

db.update({"score" : 69}, where('name') == "Romain")
db.update({"roles" : ["Junior"]})
db.update({"roles" : ["Pythonista", "Junior"]}, where('name') == "Romain")

#Update ou insère si condition
db.upsert({"name" : "Axelle" , "score" : 25, "roles" : ["Pouet"]}, where('name') == 'Axelle')

#Remove avec condition
db.remove(where('score') == 0)

#Drop toute la bdd
#db.truncate()