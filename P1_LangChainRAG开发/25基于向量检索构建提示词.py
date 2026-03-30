# 开发时间：2026/3/25  22:30
from idlelib.searchengine import search_reverse
from xml.dom.minidom import Document

from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

def print_prompt(prompt):
    print(prompt.to_string())
    print('='*20)
    return  prompt

model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料：{context}"),
        ("user","用户提问:{input}")
    ]
)

vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

#准备一下资料(向量库的数据)
#add_texts 传入一个 list[str]
vector_store.add_texts(
    ['减肥要少吃多练','在减肥期间要少吃油腻的东西','跑步是一个很好的运动']
)

input_text = "如何减肥？"

#langchain中向量存储对象，有一个方法:as_retriever,可以返回一个Runnable接口的子类实例对象
retriever = vector_store.as_retriever(search_kargs={"k":2})

def format_func(docs:list[Document]):
    if not docs:
        return "无相关资料"
    formatted_str = "["
    for doc in docs:
        formatted_str += doc.page_content
        formatted_str += "]"
    return formatted_str

#构建chain
chain = (
    {"input":RunnablePassthrough(),"context":retriever | format_func} | prompt | print_prompt | model | StrOutputParser()
)

res = chain.invoke(input_text)
print(res)
"""
retriever:
    -输入：用户的提问  str
    -输出：向量库的检索结果  list[Document]
    
prompt:
    -输入：用户的提问 + 向量库的检索结果  dict
    -输出：完整的提示词  PromptValue
    
以上实例的chain的流程：input_text传入retriever进行向量库检索（同时RunnablePassthrough()也同时传入input_text）-> format_func:组装成完整字符串 ->
{"input":RunnablePassthrough(),"context":retriever | format_func} 生成完整的字典 -> 传入prompt -> model -> 输出解析为字符串
"""


