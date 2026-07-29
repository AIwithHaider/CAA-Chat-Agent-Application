from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = ChatPromptTemplate.from_template(
    """
    {system_prompt}.
        Instructions:
        - Be accurate.
        - Be concise.
        - Use the Tavily search tool whenever recent information is required.
        - Never hallucinate.
"""
)