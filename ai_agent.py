from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage
from langchain_core.prompts import ChatPromptTemplate


# import api keys
load_dotenv()

# setup llm and search tool
llm = ChatGroq(model="llama-3.3-70b-versatile",
               temperature=1.2)
search_tool = TavilySearch(max_results=2)
# search_tool = [TavilySearchResults(max_results=2)]







def get_response(system_prompt, query):

    # create the agent
    agent = create_agent(
    model=llm,
    tools=[search_tool],
    system_prompt= system_prompt,
    
    )

    state = {"messages" : query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    print(system_prompt)
    return ai_messages[-1]



