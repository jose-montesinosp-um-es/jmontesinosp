from pymongo import MongoClient

def get_db_catalogo():
    url = "mongodb://admin:admin123@localhost:27017/catalogo_ejercicios?authSource=admin"
    client = MongoClient(url)
    return client["catalogo_ejercicios"]

def get_db_usuarios():
    url = "mongodb://admin:admin123@localhost:27017/usuarios?authSource=admin"
    client = MongoClient(url)
    return client["usuarios"]