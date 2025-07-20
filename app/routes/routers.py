from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from models.chatbot import ChatBot

router = APIRouter(prefix="/chat", tags=["chatbot"])
bot = ChatBot()

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


@router.post("/questions")
async def create(data: CreateQuestionRequest):
    try:
        result = bot.create_response(data.question, data.answer)
        if isinstance(result, ValueError):
            raise ValueError(str(result))

        return {
            "data": {
                "id": str(result),
                "question": data.question,
                "answer": data.answer
            },
        }
    except ValueError as e:
        raise HTTPException(
            status_code=409,
            detail={"message": str(e)}
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": f"Internal server error: {str(e)}"}
        )


class QuestionRequest(BaseModel):
    question: str

@router.get("/questions/search")
async def get_answer(q: str = Query(..., description="Question to search for")
):
    try:
        answer = bot.get_answer(q)
        if answer:
            return {
            "data": {
                "answer": answer
            },
            "message": "Question answered successfully"
        }
        raise HTTPException(status_code=404, detail="Question not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/questions")
async def get_all():
    try:
        results = bot.get_all(10)
        return {"data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))