import pytest
from app.models.chatbot import ChatBot


@pytest.fixture
def chatbot(mock_database):
    """Create a ChatBot instance for testing"""
    return ChatBot()


def test_chatbot_initialization(chatbot):
    """Test that ChatBot is initialised correctly"""
    assert isinstance(chatbot, ChatBot)


def test_create_response(chatbot, mock_database):
    """Test creating a response"""
    mock_database.find_one.return_value = None
    mock_database.insert_one.return_value.inserted_id = "123"

    result = chatbot.create_response("test question", "test answer")
    assert result == "123"


def test_get_answer(chatbot, mock_database):
    """Test getting an answer"""
    mock_database.find_one.return_value = {"question": "test", "answer": "test answer"}

    result = chatbot.get_answer("test")
    assert result == "test answer"


def test_get_all(chatbot, mock_database):
    """Test getting all questions"""
    result = chatbot.get_all(limit=2)
    assert result == ["q1", "q2"]
