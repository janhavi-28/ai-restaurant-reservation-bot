# File: llm_utils.py

import re
import json
import streamlit as st

def extract_json(text):
    """
    Tries to extract JSON content from an LLM response string.
    Returns a Python dict if successful, else None.
    """
    try:
        json_string = re.search(r"\{.*\}", text, re.DOTALL).group()
        return json.loads(json_string)
    except Exception as e:
        st.error(f"Error parsing LLM response: {e}")
        return None
