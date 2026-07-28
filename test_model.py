from backend.chatbot.models import mistral_llm

response = mistral_llm.invoke("Hello!")
print(response.content)