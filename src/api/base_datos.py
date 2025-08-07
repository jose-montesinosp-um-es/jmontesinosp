from pymongo import MongoClient

def get_db_catalogo():
    url = "mongodb://admin:admin123@localhost:27017/catalogo_ejercicios?authSource=admin"
    client = MongoClient(url)
    return client["catalogo_ejercicios"]