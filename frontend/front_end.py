# 1. Setup UI with streamlit (system prompt, query)
import streamlit as sl
import requests


sl.set_page_config(page_title="CAA-Chat Agent Application", layout="centered")
sl.title("Ali Haider's personal AI Agent Chatbot")
sl.write("Simple Search Agent tool chatbot")

system_prompt = sl.text_area("Define your AI Agent", height=70, placeholder="Type your system prompt here...")
user_query = sl.text_area("Enter your query", height=150, placeholder="Ask anything")

API_URL = "http://127.0.0.1:9999/chat"

if sl.button("Ask anything"):
    # Get response from the backend on frontend
    if user_query.strip():
        # Connect with backend via url
        payload = {
            "system_prompt": system_prompt,
            "messages": [user_query]
        }

        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            sl.subheader("Agent Response")
            sl.markdown(f"**Final Response:** {response_data}")

        else:
            sl.error(f"Status Code: {response.status_code}")
            sl.json(response.json())