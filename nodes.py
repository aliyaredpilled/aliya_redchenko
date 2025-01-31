from langchain_core.messages import AIMessage
from langchain_core.prompts import PromptTemplate
from classes import *
from llms import * 
from classes import Answer_generation
from functions import ask_perplexity

async def node_clarify_question_fn(state: AnswerState):
    response = chain_clarification.invoke(state["messages"][-1].content)
    text_answer = response.question_text
    is_variant_question = response.is_variant_question
    return {"clarified_question": text_answer, "is_variant_question": is_variant_question}

async def node_perplexity_fn(state: AnswerState):
    question = state.get('clarified_question', '')
    response = await ask_perplexity(question)
    answer_text = response['choices'][0]['message']['content']
    citations = response['citations']
    return {"answer_text": answer_text, "citations": citations} 

async def node_get_final_answer_fn(state: AnswerState):
    answer_text = state.get('answer_text', '')
    user_question = state["messages"][-1].content if state["messages"] else ""
    final_answer = chain.invoke({"question": user_question, "answer": answer_text}) 
    
    result = {
        "answer": final_answer.answer,
        "reasoning": final_answer.reasoning,
        "citations": state.get('citations', [])[:3]
    }
    
    return {"final_answer": result}