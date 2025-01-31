from builder import graph
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Union
from classes import AnswerState
import json

app = FastAPI()

class RequestData(BaseModel):
    query: str
    id: int
    is_variant_question: bool

class ResponseData(BaseModel):
    id: int
    answer: Optional[Union[int, str]]  # Если is_variant_question=False, будет null
    reasoning: str
    sources: List[str]

@app.post("/api/request")
async def handle_request(data: RequestData):
    """
    Эндпоинт принимает запрос, передаёт его в LangGraph и возвращает JSON-ответ в виде строки
    """
    try:
        # Запуск графа
        test_state = AnswerState(messages=[data.query])
        result = await graph.ainvoke(test_state)
        
        # Формируем JSON-ответ
        final_answer = result.get("final_answer", {})
        answer = final_answer.get("answer") if data.is_variant_question else None
        reasoning = final_answer.get("reasoning", "") + " Ответ сгенерирован ChatGPT 4o"
        sources = final_answer.get("citations", [])

        response_data = {
            "id": data.id,
            "answer": answer,
            "reasoning": reasoning,
            "sources": sources
        }

        # Возвращаем JSON-объект как строку
        return json.dumps(response_data, ensure_ascii=False)

    except Exception as e:
        error_response = {"error": str(e)}
        return json.dumps(error_response, ensure_ascii=False)
