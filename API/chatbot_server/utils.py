# utils.py
import os
from dotenv import load_dotenv
import requests

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'


def send_message(message, chat_id):
    p = {
        'chat_id': chat_id,
        'text': message,
    }
    URL = BASE_URL + '/sendMessage'
    requests.get(URL, params=p)