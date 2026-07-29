from backend.chatbot.providers import get_llm
from backend.chatbot.prompts import  SYSTEM_PROMPT
from backend.chatbot.agent import create_chat_agent



def get_response(system_prompt, query, provider, model):

    llm = get_llm(provider, model)
    
    formatted_prompt = SYSTEM_PROMPT.format(
    system_prompt = system_prompt
)

    return create_chat_agent(llm, formatted_prompt, query)

