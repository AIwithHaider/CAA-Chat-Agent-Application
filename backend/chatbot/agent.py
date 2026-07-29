from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage

from backend.chatbot.prompts import SYSTEM_PROMPT
from backend.tools.search_tool import search_tool


def create_chat_agent(llm, formatted_prompt, query):

    agent = create_agent(
        model=llm,
        tools=[search_tool],
        system_prompt=formatted_prompt
    )

    state = {"messages" : query}
    response = agent.invoke(state)
    # messages = response.get("messages")
    messages = response["messages"]
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]