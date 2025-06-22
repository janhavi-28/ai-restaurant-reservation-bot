
AI Restaurant Reservation Bot

An intelligent restaurant booking assistant powered by LLM (LLaMA 3-8B). This bot can search for restaurants or book a table using natural language queries like:

Book a table for 4 at 7pm in HSR Layout for Chinese food

Features

-  Natural Language Interface to search or book restaurants.  
-  LLM-based intent parsing and tool calling.
-  Search from 50+ restaurants across locations, cuisines, time slots.
-  Book a table based on real-time query data.
-  Frontend: Built using Streamlit.
-  Model: `meta-llama/Llama-3-8b-chat-hf` via Together API.
-  Tool calling handled manually without LangChain or similar frameworks.

Setup Instructions

1. Clone the repository

cd restaurant-reservation-bot

2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate   # For Windows


3. Install dependencies
bash
pip install -r requirements.txt

4. Set your API key
Create a `.env` file:
TOGETHER_API_KEY=your_together_api_key

5. Run the app
bash
streamlit run main.py

6. Prompt Engineering Approach

- The system prompt: "You are a helpful AI assistant that helps users search or book restaurant tables".
- LLM is allowed to auto-select the tool(`search_restaurants` or `book_table`) based on parsed intent.
- Arguments like `location`, `cuisine`, `guests`, and `time` are extracted and validated through schema-based parsing.
- If no exact match is found, the bot provides alternate suggestions using fallback logic.

7. Sample Conversations

8. Booking

User: Book a table for 4 at 7pm in HSR Layout for Chinese food

9. Response:
Table for 4 at 7pm in HSR Layout for Chinese food has been booked!
No Match
User: Book a table for 8 at 5pm in Whitefield for Mexican food

Response:
Sorry, no Mexican restaurants in Whitefield with seating for 8 at 5pm.


10.Search & Suggestions
User: Need 3 seats at 8pm for North Indian food in Koramangala

Response:
Recommendations:
1. Punjab Grill – Available at 8pm
2. Tandoor House – Available at 8pm

11.Business Strategy Summary

This AI bot can be scaled into a restaurant SaaS platform:

- Used by food delivery startups or individual restaurant chains.
- Real-time conversational interface reduces dependency on static reservation systems.
- Easily extendable to include online ordering, feedback, and loyalty systems.

11.Project Structure
restaurant-reservation-bot
 main.py              (Streamlit frontend and LLM interaction)
 tools.py             (search_restaurants & book_table logic)
 restaurants.json     (Restaurant data (50–100 entries))
 requirements.txt
 .env
 AI_Restaurant_Bot_README

12.Final Notes

- No LangChain or similar frameworks were used.
- All tool calls are manually defined and validated.
- Tested with Together.ai’s hosted LLaMA 3-8B model.
