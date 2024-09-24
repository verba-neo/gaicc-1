import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_pinecone import PineconeVectorStore

load_dotenv()

text = '''
넌 질문-답변을 도와주는 AI 비서야.
아래 제공되는 Context를 통해서 사용자 Question에 대해 답을 해줘야해.

Context에는 직접적으로 없어도, 추론하거나 계산할 수 있는 답변은 최대한 만들어 봐.
그리고 관련 내용을 말할때는, [파일명.pdf - 3p] 의 형식으로 출처를 말해줘.

답은 적절히 \n를 통해 문단을 나눠줘 한국어로 만들어 줘. 
# Question:
{question}

# Context:
{context}

# Answer:
'''

def query_llm(user_input):
    vectorstore = PineconeVectorStore.from_existing_index(
        index_name=os.environ.get('INDEX_NAME'),
        embedding=OpenAIEmbeddings()
    )
    # 5. Retriever
    retriever = vectorstore.as_retriever()
    # 6. Prompting
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
