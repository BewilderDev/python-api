import pytest
from unittest.mock import Mock, patch
from app.models.chatbot import ChatBot


@patch("app.models.chatbot.Database")
def test_chatbot_initialization(mock_db_class):
    """Test that ChatBot is initialised correctly"""
    mock_db_class.return_value = Mock()
    chatbot = ChatBot()
    assert isinstance(chatbot, ChatBot)


@patch("app.models.chatbot.Database")
def test_create_response(mock_db_class):
    """Test creating a new response"""
    mock_db = Mock()
    mock_db.find_one.return_value = None  # Simulate new question
    mock_db.insert.return_value = "123"   # Simulate insert returning ID
    mock_db_class.return_value = mock_db

    chatbot = ChatBot()
    result = chatbot.create_response("test question", "test answer")
    assert result == "123"


@patch("app.models.chatbot.Database") 
def test_create_response_duplicate(mock_db_class):
    mock_db = Mock()
    mock_db.find_one.return_value = {"question": "test question"}  # Simulate existing record
    mock_db_class.return_value = mock_db

    chatbot = ChatBot()

    with pytest.raises(ValueError, match="Question already exists"):
        chatbot.create_response("test question", "test answer")


@patch("app.models.chatbot.Database")
def test_get_answer(mock_db_class):
    """Test retrieving an answer"""
    mock_db = Mock()
    mock_db.find_one.return_value = {"question": "test", "answer": "test answer"}
    mock_db_class.return_value = mock_db

    chatbot = ChatBot()
    result = chatbot.get_answer("test")
    assert result == "test answer"


@patch("app.models.chatbot.Database")
def test_get_answer_not_found(mock_db_class):
    """Test getting an answer for a non-existent question"""
    mock_db = Mock()
    mock_db.find_one.return_value = None
    mock_db_class.return_value = mock_db

    chatbot = ChatBot()
    result = chatbot.get_answer("unknown")
    assert result is None


@patch("app.models.chatbot.Database")
def test_get_all(mock_db_class):
    mock_db = Mock()

    mock_cursor = Mock()
    mock_cursor.__iter__.return_value = iter([
        {"question": "q1"},
        {"question": "q2"},
    ])
    mock_db.find_many.return_value = mock_cursor
    mock_db_class.return_value = mock_db

    chatbot = ChatBot()
    result = chatbot.get_all(limit=2)
    assert result == ["q1", "q2"]