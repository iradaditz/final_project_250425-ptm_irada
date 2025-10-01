"""
Логирование поисковых запросов в MongoDB.
"""
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timezone
from pymongo import MongoClient

# Загружаем переменные окружения
load_dotenv(find_dotenv() or Path(".env"))

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB", "ich_edit")
MONGO_COLL = os.getenv("MONGO_COLL", "final_project_250425-ptm_irada")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
col = db[MONGO_COLL]

def log_search(search_type: str, params: dict, results_count: int):
    """
    Сохраняет информацию о поисковом запросе в MongoDB.
    """
    doc = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "search_type": search_type,
        "params": params,
        "results_count": int(results_count),
    }
    try:
        col.insert_one(doc)
    except Exception as e:
        # Чтобы программа не падала, если Mongo не отвечает
        print(f"(Предупреждение) Сервер статистики недоступен: {e}")
