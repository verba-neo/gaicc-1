# app.py
import os
from dotenv import load_dotenv 
from flask import Flask, request  # 들어온 요청정보(server)
from utils import send_message
from openai import OpenAI


load_dotenv()
app = Flask(__name__)


@app.route('/telegram', methods=['POST'])
def telegram():
    OPENAI_KEY = os.getenv('OPENAI_KEY')
    # 텔레그램에서 들어온 요청정보 중 메시지만 추출
    chat_id = request.json['message']['chat']['id']
    msg = request.json['message'].get('text')
    # 텔레그램으로 요청 보내기
    if msg:
        client = OpenAI(api_key=OPENAI_KEY)# msg 에 담긴 내용에 따라 다른 행동을 하도록.
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are a badass chatbot."},
                {"role": "user", "content": msg},
            ]
        )
        reply = response.choices[0].message.content
        send_message(reply, chat_id)
    else:
        send_message('메세지를 보내주세요', chat_id)



    return ''


if __name__ == '__main__':
    app.run(debug=True)