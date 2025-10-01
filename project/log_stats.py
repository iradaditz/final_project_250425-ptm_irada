"""
Статистика запросов из MongoDB.
"""
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

# Загружаем переменные окружения из .env
load_dotenv(find_dotenv() or Path(".env"))

# Получаем данные из .env
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB", "ich_edit")
MONGO_COLL = os.getenv("MONGO_COLL", "final_project_250425-ptm_irada")

# Подключение к MongoDB
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
col = db[MONGO_COLL]

# --- функции статистики ---
def top_popular(limit=5):
    pipeline = [
        {"$group": {
            "_id": {"type": "$search_type", "params": "$params"},
            "count": {"$sum": 1},
            "last_time": {"$max": "$timestamp"}
        }},
        {"$sort": {"count": -1, "last_time": -1}},
        {"$limit": limit}
    ]
    return list(col.aggregate(pipeline))

def last_unique(limit=5):
    pipeline = [
        {"$sort": {"timestamp": -1}},
        {"$group": {
            "_id": {"type": "$search_type", "params": "$params"},
            "doc": {"$first": "$$ROOT"}
        }},
        {"$replaceWith": "$doc"},
        {"$limit": limit}
    ]
    return list(col.aggregate(pipeline))


# --- проверка соединения (опционально, для отладки) ---
if __name__ == "__main__":
    try:
        client.admin.command("ping")
        print("MongoDB подключение успешно")
        print("Документов в коллекции:", db[MONGO_COLL].count_documents({}))
    except Exception as e:
        print("Ошибка подключения к Mongo:", e)
