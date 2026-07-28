from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage
from backend.chatbot.providers import get_llm

load_dotenv()




# setup search tool
search_tool = TavilySearch(max_results=2)



def get_response(system_prompt, query, provider, model):

    llm = get_llm(provider, model)

    # create the agent
    agent = create_agent(
    llm,
    tools=[search_tool],
    system_prompt= system_prompt
    
    )

    state = {"messages" : query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    print(system_prompt)
    return ai_messages[-1]
