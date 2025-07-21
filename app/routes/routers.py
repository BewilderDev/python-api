from fastapi import APIRouter, HTTPException, Query
from schemas.schemas import CreateQuestionRequest
from controllers.chatbot_controller import ChatBotController

router = APIRouter(prefix="/chat", tags=["chatbot"])

@router.post("/questions")
async def create(data: CreateQuestionRequest):
    try:
        bot_controller = ChatBotController()
        result = bot_controller.create_response(data)
        return result
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

@router.get("/questions/search")
async def get_answer(q: str = Query(..., description="Question to search for")
):
    try:
        bot_controller = ChatBotController()
        result = bot_controller.get_answer(q)
        return result
        raise HTTPException(status_code=404, detail="Question not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/questions")
async def get_all():
    try:
        bot_controller = ChatBotController()
        result = bot_controller.get_all()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))