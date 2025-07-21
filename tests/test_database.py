import pytest
from unittest.mock import Mock, patch
from app.database.database import Database


@pytest.fixture
def mock_collection():
    with patch('app.database.database.MongoClient') as mock_client:  # <-- updated path
        mock_coll = Mock()
        mock_client.return_value.__getitem__.return_value.__getitem__.return_value = mock_coll
        yield mock_coll


@pytest.fixture
def db(mock_collection):
    return Database("test_collection")


def test_insert(db, mock_collection):
    mock_collection.insert_one.return_value.inserted_id = "123"
    result = db.insert({"test": "data"})
    assert result == "123"


def test_find_one(db, mock_collection):
    mock_collection.find_one.return_value = {"test": "result"}
    result = db.find_one({"test": "query"})
    assert result == {"test": "result"}


def test_find_many(db, mock_collection):
    mock_cursor = Mock()
    mock_cursor.__iter__.return_value = iter([
        {"question": "q1"},
        {"question": "q2"},
    ])
    mock_cursor.limit.return_value = mock_cursor  # Support .limit()
    mock_collection.find.return_value = mock_cursor

    result = db.find_many(limit=2)
    assert list(result) == [
        {"question": "q1"},
        {"question": "q2"}
    ]