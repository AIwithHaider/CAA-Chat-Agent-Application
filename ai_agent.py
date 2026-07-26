from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage


# import api keys
load_dotenv()

# setup llm and search tool
llm = ChatGroq(model="llama-3.3-70b-versatile",
               temperature=1.2)
search_tool = TavilySearch(max_results=2)

# create the agent
agent = create_agent(
    model=llm,
    tools=[search_tool]
)

# query = input("Ask anything: ")

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "what happens in pakistan today"
            }
        ]
    }
)
messages = response.get("messages")
ai_response = [message.content for message in messages if isinstance( message, AIMessage)]
print(ai_response)


