import os
import aiohttp
from dotenv import load_dotenv

async def ask_perplexity(question: str) -> dict:
    """
    Асинхронная функция делает запрос к API Perplexity с заданным вопросом
    
    Args:
        question (str): Вопрос для отправки в API
        
    Returns:
        dict: JSON ответ от API
    """
    load_dotenv()
    api_key = os.getenv('PERPLEXITY_API_KEY')
    
    if not api_key:
        raise ValueError("PERPLEXITY_API_KEY не найден в переменных окружения")
    
    url = "https://api.perplexity.ai/chat/completions"
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "model": "sonar-reasoning"
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            return await response.json()

