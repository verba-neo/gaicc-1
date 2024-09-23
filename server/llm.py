# langchain/llm.py
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


def llm_rag(user_input):
    loader = PyMuPDFLoader('./data.pdf')
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents=split_docs, embedding=embeddings)
    retriever = vectorstore.as_retriever()

    text = '''
    넌 질문-답변을 도와주는 AI 비서야.
    아래 제공되는 Context를 통해서 사용자 Question에 대해 답을 해줘야해.

    Context에는 직접적으로 없어도, 추론하거나 계산할 수 있는 답변은 최대한 만들어 봐.
    그리고 관련 내용을 말할때는, pdf 몇 페이지이서 찾은 내용인지도 말해줘.

    답은 적절히 \n를 통해 문단을 나눠줘 한국어로 만들어 줘. 
    # Question:
    {question}

    # Context:
    {context}


    # Answer:
    '''
    prompt = PromptTemplate.from_template(text)

    # 7. LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    parser = StrOutputParser()
    # 8. Chain
    chain = (
        {'context': retriever, 'question': RunnablePassthrough()}
        | prompt
        | llm
        | parser
    )

    ans = chain.invoke(user_input)
    return ans
