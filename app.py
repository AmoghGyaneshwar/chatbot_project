# app.py

import streamlit as st
from chatbot import Chatbot  # Import Chatbot class
import os

st.set_page_config(page_title="Chatbot Interface", page_icon=":robot_face:")

# Hide the hamburger menu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Chatbot Interface")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

chatbot = Chatbot()

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

user_input = get_text()

if user_input:
    bot_response = chatbot.get_response(user_input, st.session_state.chat_history)
    st.session_state.chat_history.append({'sender': chatbot.bot_name, 'message': bot_response})

if st.session_state.chat_history:
    for chat in st.session_state.chat_history:
        if chat['sender'] == chatbot.user_name:
            st.write(f"**You:** {chat['message']}")
        else:
            st.write(f"**{chatbot.bot_name}:** {chat['message']}")
