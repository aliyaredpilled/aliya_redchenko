from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from classes import *
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


tagging_prompt_clarification = ChatPromptTemplate.from_template(
    """
    Привет!) Нам задали вопрос.\n\n
    {question}
    Если в нем есть варианты ответов, пожалуйста, отдели текст вопроса и вариантов ответа.
    Введи только текст cамого вопроса. 
    Не пиши "Вот вопрос:"."""
)

openai_api_key = os.getenv("OPENAI_API_KEY")

llm_clarification = ChatOpenAI(
    openai_api_key=openai_api_key,
    temperature=0,
    model="gpt-4o"  
).with_structured_output(question_clarification)

chain_clarification = tagging_prompt_clarification | llm_clarification



tagging_prompt = ChatPromptTemplate.from_template(
    """
Привет!) Нам задали вопрос \n\n\ {question}
Ты получаешь ответ от умной поисковой модели:
{answer}
Пожалуйста, верни номер правильного ответа и небольшое обоснование.
Сегодня 1 февраля 2025 года.
"""
)
openai_api_key = os.getenv("OPENAI_API_KEY")

llm_with_struct = ChatOpenAI(
    openai_api_key=openai_api_key,
    temperature=0,
    model="gpt-4o"  
).with_structured_output(Answer_generation)

chain = tagging_prompt | llm_with_struct


llm_clarify = ChatOpenAI(
    openai_api_key=openai_api_key,
    temperature=0,
    model="gpt-4o"  
)

