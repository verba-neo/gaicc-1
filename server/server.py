'''
1. GAICC-1 에 server 폴더를 만듬
2. langchain 폴더 내의 server.py, llm.py 를 server 폴더로 옮김
3. data.pdf, .env 파일은 복사해서 server 폴더에 넣음
4. server/ 폴더 안에는 .env, data.pdf, llm.py, server.py 파일 4개만
'''

# langchain/server.py
from flask import Flask, request
from llm import llm_rag

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    user_message = request.json['message']
    ans = llm_rag(user_message)
    return {'message': ans}

app.run(debug=True)


