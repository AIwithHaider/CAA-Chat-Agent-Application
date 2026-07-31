from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage
from langgraph.checkpoint.memory import InMemorySaver

from backend.tools.search_tool import search_tool

# Initialize the checkpointer once at the module level so memory persists across calls
memory_saver = InMemorySaver()

def create_chat_agent(llm, formatted_prompt, query, thread_id="default-session"):

    agent = create_agent(
        model=llm,
        tools=[search_tool],
        system_prompt=formatted_prompt,
        checkpointer=memory_saver # <-- Wires short-term memory into the graph loop
    )

    state = {"messages" : query}

    # 4. Attach the thread configuration so the checkpointer targets the correct chat
    config = {"configurable": {"thread_id": thread_id}}

     # 5. Invoke the agent loop passing both state and config
    response = agent.invoke(state, config=config)
    messages = response["messages"]
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]