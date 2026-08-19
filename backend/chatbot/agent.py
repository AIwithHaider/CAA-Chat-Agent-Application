from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage
from langgraph.checkpoint.memory import InMemorySaver

from backend.tools.search_tool import search_tool


# Initialize the checkpointer once at the module level so memory persists across calls
memory_saver = InMemorySaver()


def extract_text(content):
    """Normalize LangChain AIMessage content to a plain string."""

    # OpenAI/other models may return a plain string
    if isinstance(content, str):
        return content

    # Gemini may return a list of content blocks
    if isinstance(content, list):
        text_parts = []

        for block in content:
            if isinstance(block, str):
                text_parts.append(block)

            elif isinstance(block, dict):
                if block.get("type") == "text":
                    text_parts.append(block.get("text", ""))

        return "".join(text_parts)

    # Fallback
    return str(content)


def create_chat_agent(
    llm,
    formatted_prompt,
    query,
    thread_id="default-session"
):
    agent = create_agent(
        model=llm,
        tools=[search_tool],
        system_prompt=formatted_prompt,
        checkpointer=memory_saver
    )

    state = {"messages": query}

    # Attach the thread configuration so the checkpointer
    # targets the correct chat
    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    # Invoke the agent loop passing both state and config
    response = agent.invoke(state, config=config)

    messages = response["messages"]

    ai_messages = [
        extract_text(message.content)
        for message in messages
        if isinstance(message, AIMessage)
    ]

    return ai_messages[-1]