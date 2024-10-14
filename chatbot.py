# chatbot.py

import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Chatbot:
    def __init__(self, bot_name='Bot', user_name='User'):
        """
        Initialize the chatbot with bot and user names.
        """
        self.memory = "I am Bot, and this is my mind."
        self.prompt = "An engaging conversation with Bot."
        self.bot_name = bot_name
        self.user_name = user_name

        self.api_url = 'https://guanaco-submitter.chai-research.com/endpoints/onsite/chat'
        self.headers = {
            'Authorization': f'Bearer {os.getenv("CHAI_API_KEY")}',
            'Content-Type': 'application/json'
        }

    def get_response(self, user_message, chat_history):
        """
        Send the user message to the API and get the bot's response.
        """
        logger.info(f"User message received: {user_message}")
        chat_history.append({'sender': self.user_name, 'message': user_message})

        payload = {
            'memory': self.memory,
            'prompt': self.prompt,
            'bot_name': self.bot_name,
            'user_name': self.user_name,
            'chat_history': chat_history
        }

        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            bot_reply = response.json().get('response', '')
            chat_history.append({'sender': self.bot_name, 'message': bot_reply})
            return bot_reply
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            return "Sorry, I couldn't process your request."
        except Exception as err:
            print(f"An error occurred: {err}")
            return "Sorry, something went wrong."
