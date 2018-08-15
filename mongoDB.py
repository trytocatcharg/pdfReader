from pymongo import MongoClient


def save_data(wargs):
    # client = MongoClient('mongodb://localhost:27017/')
    # https://mlab.com/databases/mongo_bd#users
    client = MongoClient('mongodb://userPython:userPython123@ds121382.mlab.com:21382/mongo_bd')
    db = client.mongo_bd
    values_collection = db.values
    id_inserted = values_collection.insert_one(wargs).inserted_id
    print("Id obtenido de la insercion {0}".format(id_inserted))
