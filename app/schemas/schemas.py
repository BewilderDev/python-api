from pydantic import BaseModel

class CreateQuestionRequest(BaseModel):
    question: str
    answer: str

    class Config:
        json_schema_extra = {
            "example": {
                "question": "What is the weather like?",
                "answer": "Sunny, hopefully!"
            }
        }