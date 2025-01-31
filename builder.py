from langgraph.graph import StateGraph, START, END
from classes import *
from nodes import *
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage

builder = StateGraph(AnswerState)
builder.add_node("clarify_question", node_clarify_question_fn)
builder.add_node("perplexity", node_perplexity_fn)
builder.add_node("get_final_answer", node_get_final_answer_fn)
builder.add_edge(START, "clarify_question")
builder.add_edge("clarify_question", "perplexity")
builder.add_edge("perplexity", "get_final_answer")
builder.add_edge("get_final_answer", END)
graph = builder.compile()

