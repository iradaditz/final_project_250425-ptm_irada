"""
Статистика запросов из MongoDB.
"""
from pymongo import MongoClient

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)

db = client["ich_edit"]
col = db["final_project_250425-ptm_irada"]

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