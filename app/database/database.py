from pymongo import MongoClient
from typing import Optional, Dict, Any
import os

class MongoConnection:
    _client: Optional[MongoClient] = None

    @classmethod
    def get_client(cls) -> MongoClient:
        if cls._client is None:
            cls._client = MongoClient(
                host=os.getenv("MONGO_HOST"),
                port=int(os.getenv("MONGO_PORT")),
                username=os.getenv("MONGODB_ROOT_USERNAME"),
                password=os.getenv("MONGODB_ROOT_PASSWORD"),
                authSource="ChatBot"
            )
        return cls._client

    @classmethod
    def close_connection(cls):
        if cls._client:
            cls._client.close()
            cls._client = None

class Database:
    def __init__(self, collection_name, db_name="ChatBot"):
        self.client = MongoConnection.get_client()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert(self, data: Dict[str, Any]):
        try:
            result = self.collection.insert_one(data)
            return result.inserted_id
        except Exception as e:
            raise Exception(f"Error inserting data: {e}")

    def find_one(self, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        return self.collection.find_one(
            query,
            collation={"locale": "en", "strength": 2}
        )

    def find_many(self, limit: Optional[int] = None):
        cursor = self.collection.find()
        if limit:
            cursor = cursor.limit(limit)
        return cursor
