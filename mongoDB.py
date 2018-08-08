from pymongo import MongoClient


def save_data(wargs):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.gold
    values_collection = db.values
    id_inserted = values_collection.insert_one(wargs).inserted_id
    print("Id obtenido de la insercion {0}".format(id_inserted))