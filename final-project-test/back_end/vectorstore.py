# vectorstore.py => Pinecone 에 데이터 추가하기

import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()
# Pinecone Index Name 과 맞아야 함.
index_name = os.environ.get('INDEX_NAME')  # .env 파일에서 가져올 때 쓰는 코드

# 1. Load
loader = PyMuPDFLoader('./llm-data.pdf')
docs = loader.load()
# 2. Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(docs)
# 3. Embed Setting
embeddings = OpenAIEmbeddings()
# 4. Add Data To Pinecone Index
PineconeVectorStore.from_documents(
    documents=split_docs,
    embedding=embeddings,
    index_name=index_name
)