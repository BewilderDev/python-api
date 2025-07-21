from models.chatbot import ChatBot

class ChatBotController:
    def __init__(self):
        self.bot = ChatBot()

    def create_response(self, data):
        result = self.bot.create_response(data.question, data.answer)
        if isinstance(result, ValueError):
            raise ValueError(str(result))

        return {
            "data": {
                "id": str(result),
                "question": data.question,
                "answer": data.answer
            },
        }

    def get_answer(self, q:str):
        answer = self.bot.get_answer(q)
        if answer:
            return {
                "data": {
                    "answer": answer
                },
                "message": "Question answered successfully"
            }
        return {
            "message": "Question not found"
        }

    def get_all(self):
        results = self.bot.get_all(10)
        return {"data": results}