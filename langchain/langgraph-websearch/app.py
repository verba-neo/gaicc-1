from flask import Flask, request
from flask_cors import CORS
from utils.graph import websearch_rag

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['message']
    # utils/graph.py 에서 최종 질문 검색하는 함수
    ans = websearch_rag(question)
    return {'llm': ans}

app.run(debug=True)