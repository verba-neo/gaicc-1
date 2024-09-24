# app.py => Serving Logic 
from flask import Flask, request
# pip install flask_cors
from flask_cors import CORS

from utils.llm import query_llm

app = Flask(__name__)  # flask 서버 그 자체
CORS(app)

# 특정 URL마다 어떤 응답을 줄지 정의
@app.route('/', methods=['POST'])
def index():
    user_input = request.json['message']
    ans = query_llm(user_input)
    return {'llm': ans}


@app.route('/hi')
def hi():
    return {'message': 'hello'}


app.run(debug=True)