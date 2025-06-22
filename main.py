import streamlit as st
from tools import search_restaurants, book_table
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv("TOGETHER_API_KEY")

st.set_page_config(page_title="🍽️ AI Restaurant Reservation Bot")
st.title("🍽️ AI Restaurant Reservation Bot")
st.markdown("Chat with the bot to search or book a restaurant!")

user_query = st.chat_input("Type your request and press Enter")

if user_query:
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        tools_payload = [
            {
                "type": "function",
                "function": {
                    "name": "search_restaurants",
                    "description": "Search restaurants based on location, cuisine, guests and time",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {"type": "string"},
                            "cuisine": {"type": "string"},
                            "guests": {"type": "integer"},
                            "time": {"type": "string"}
                        },
                        "required": ["location", "cuisine", "guests", "time"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "book_table",
                    "description": "Book a restaurant table",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {"type": "string"},
                            "cuisine": {"type": "string"},
                            "guests": {"type": "integer"},
                            "time": {"type": "string"}
                        },
                        "required": ["location", "cuisine", "guests", "time"]
                    }
                }
            }
        ]

        body = {
            "model": "meta-llama/Llama-3-8b-chat-hf",
            "max_tokens": 200,
            "temperature": 0.7,
            "messages": [
                {"role": "system", "content": "You are a helpful AI assistant that helps users search or book restaurant tables."},
                {"role": "user", "content": user_query}
            ],
            "tools": tools_payload,
            "tool_choice": "auto"
        }

        try:
            response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=body)
            response.raise_for_status()
            data = response.json()

            # ✅ Check if any tool_calls were returned
            tool_calls = data["choices"][0]["message"].get("tool_calls", [])

            if tool_calls:
                tool_call = tool_calls[0]
                tool_name = tool_call["function"]["name"]
                arguments_str = tool_call["function"]["arguments"]
                parsed_json = json.loads(arguments_str)

                st.markdown(f"✅ Parsed user request successfully!\n```json\n{json.dumps(parsed_json, indent=2)}\n```")

                if tool_name == "search_restaurants":
                    results = search_restaurants(
                        location=parsed_json.get("location"),
                        cuisine=parsed_json.get("cuisine"),
                        guests=parsed_json.get("guests"),
                        time=parsed_json.get("time")
                    )
                    st.markdown(results)

                elif tool_name == "book_table":
                    msg = book_table(
                        location=parsed_json.get("location"),
                        cuisine=parsed_json.get("cuisine"),
                        guests=parsed_json.get("guests"),
                        time=parsed_json.get("time")
                    )
                    st.markdown(msg)
            else:
                # Fallback: just show the message if no tool was called
                content = data["choices"][0]["message"].get("content", "❌ No tool calls or reply found.")
                st.markdown(content)

        except Exception as e:
            st.error(f"❌ Unexpected error: {e}")
