# pinecone_utils.py
import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

load_dotenv()


def create_embeddings(index_name, docs):
    PineconeVectorStore.from_documents(
        documents=docs,
        embedding=OpenAIEmbeddings(),
        index_name=index_name
    )


def get_vectorstore(index_name):
    vs = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=OpenAIEmbeddings()
    )
    return vs
