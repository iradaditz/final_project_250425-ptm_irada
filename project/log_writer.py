"""
Логирование поисковых запросов в MongoDB (учебное подключение).
"""
from datetime import datetime, timezone
from pymongo import MongoClient

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)

db = client["ich_edit"]
col = db["final_project_250425-ptm_irada"]

def log_search(search_type, params, results_count):
    doc = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "search_type": search_type,
        "params": params,
        "results_count": int(results_count)
    }
    col.insert_one(doc)