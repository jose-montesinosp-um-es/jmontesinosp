from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

def get_db_catalogo():
    return cliente["catalogo_ejercicios"]

def get_db_gimnasio():
    return cliente["gimnasio"]