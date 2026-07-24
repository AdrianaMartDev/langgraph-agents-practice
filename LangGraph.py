from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

tool = TavilySearchResults(max_results = 4)

class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]