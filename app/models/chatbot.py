from .database import Database
from typing import Optional, List
from .chuck_norris import ChuckNorris

class ChatBot:
    def __init__(self):
        self.db = Database('questions')

    def create_response(self, question: str, answer: str):
        exists = self.db.find_one({"question": question})
        if exists:
            return ValueError("Question already exists")

        data = {
            "question": question,
            "answer": answer
        }
        return self.db.insert(data)

    def get_answer(self, question: str) -> Optional[str]:
        # convert to lower and check if the question contains the string chuck norris
        question = question.lower()
        if "chuck norris" in question:
            chuck_api = ChuckNorris()
            chuck_joke = chuck_api.get_joke()
            if chuck_joke:
                return chuck_joke
        result = self.db.find_one({"question": question})
        return result["answer"] if result else None

    def get_all(self, limit: int = 10) -> List[str]:
        results = self.db.find_many(limit)
        return [result["question"] for result in results]
