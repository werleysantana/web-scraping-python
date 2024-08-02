import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def get_mongo_client():
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise Exception("Erro: MONGO_URI não encontrada no .env")
    return MongoClient(mongo_uri)

def get_database(client, db_name):
    return client[db_name]