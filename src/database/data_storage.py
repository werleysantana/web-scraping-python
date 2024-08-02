from .mongo_client import get_mongo_client, get_database

def store_data_in_db(data):
    client = get_mongo_client()
    db = get_database(client, "scraping_python")
    collection = db["youtube_ads"]
    
    if isinstance(data, list) and data:
        collection.insert_many(data)
    elif isinstance(data, dict):
        collection.insert_one(data)
    else:
        print("Nenhum dado para armazenar no banco de dados")