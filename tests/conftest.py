import pytest
from unittest.mock import Mock, patch
import os

@pytest.fixture(autouse=True)
def mock_env_variables():
    env_vars = {
        "MONGO_HOST": "localhost",
        "MONGO_PORT": "27017",
        "MONGODB_ROOT_USERNAME": "test_user",
        "MONGODB_ROOT_PASSWORD": "test_password"
    }
    with patch.dict(os.environ, env_vars):
        yield


@pytest.fixture
def mock_database():
    with patch('app.database.database.MongoClient') as mock_client:  # <-- updated path
        mock_collection = Mock()

        mock_cursor = Mock()
        mock_cursor.limit.return_value = [
            {"question": "q1"},
            {"question": "q2"}
        ]

        mock_collection.find.return_value = mock_cursor
        mock_collection.find_one.return_value = {"question": "test", "answer": "test answer"}
        mock_collection.insert_one.return_value.inserted_id = "123"

        mock_client.return_value.__getitem__.return_value.__getitem__.return_value = mock_collection
        yield mock_collection