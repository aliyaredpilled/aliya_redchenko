from langgraph.graph import MessagesState
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, Field

class Answer_generation(BaseModel):
    answer: str = Field(
        ...,
        description="числовое значение, содержащее номер правильного ответа на вопрос (если вопрос подразумевает выбор из вариантов). Если вопрос не предполагает выбор из вариантов, значение должно быть null",
    )
    reasoning: str = Field(
        ...,
        description="текстовое поле, содержащее объяснение или дополнительную информацию по запросу.",
    )

class question_clarification(BaseModel):
    question_text: str = Field(
        ...,
        description="текст вопроса",
    )
    is_variant_question: bool = Field(
        ...,
        description="логическое значение, содержащее признак того, что вопрос подразумевает выбор из вариантов.",
    )


class AnswerState(MessagesState):
    clarified_question: str = ''
    is_variant_question: bool = False
    answer_text: str = ''
    citations: list = []
    final_answer: dict = {}
    
