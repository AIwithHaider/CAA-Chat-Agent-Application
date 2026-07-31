# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# SYSTEM_PROMPT = ChatPromptTemplate.from_template(
#     """
#     {system_prompt}.
#         Instructions:
#         - Be accurate.
#         - Be concise.
#         - Use the Tavily search tool whenever recent information is required.
#         - Never hallucinate.
# """
# )

# SYSTEM_PROMPT = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             """
#                 {system_prompt}.
#                     Instructions:
#                     - Be accurate.
#                     - Be concise.
#                     - Use the Tavily search tool whenever recent information is required.
#                     - Never hallucinate.
#             """
#         ),

#         MessagesPlaceholder(variable_name="history"),


#     ]
# )



SYSTEM_PROMPT = """
{system_prompt}.
Instructions:
- Be accurate.
- Be concise.
- Use the Tavily search tool whenever recent information is required.
- Never hallucinate.
"""