import pytest
from unittest.mock import Mock, patch
from app.models.database import Database


@pytest.fixture
def mock_collection():
    with patch('app.models.database.MongoClient') as mock_client:
        mock_coll = Mock()
        mock_client.return_value.__getitem__.return_value.__getitem__.return_value = mock_coll
        yield mock_coll


@pytest.fixture
def db(mock_collection):
    return Database("test_collection")


def test_insert(db, mock_collection):
    """Test insert function"""
    mock_collection.insert_one.return_value.inserted_id = "123"
    result = db.insert({"test": "data"})
    assert result == "123"


def test_find_one(db, mock_collection):
    """Test find_one function"""
    mock_collection.find_one.return_value = {"test": "result"}
    result = db.find_one({"test": "query"})
    assert result == {"test": "result"}


def test_find_many(db, mock_collection):
    """Test find_many function"""
    mock_cursor = Mock()
    mock_cursor.limit.return_value = [{"id": 1}, {"id": 2}]
    mock_collection.find.return_value = mock_cursor

    result = db.find_many(limit=2)
    assert list(result) == [{"id": 1}, {"id": 2}]
