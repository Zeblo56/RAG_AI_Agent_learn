# 开发时间：2026/3/21  22:09
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import  JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import  ChatTongyi
from langchain_core.runnables import Runnable, RunnableLambda
#在链中加入自定义函数

str_parser = StrOutputParser()
model = ChatTongyi(model="qwen3-max")

prompt_first = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了个{gender}，请起名字，直接返回我姓名"
)

prompt_second = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义"
)

#传入的形参AIMessage-> dict
my_func = RunnableLambda(lambda ai_msg:{"name":ai_msg.content})

chain = prompt_first | model | my_func | prompt_second | model | str_parser

for chunk in chain.stream({"lastname":"张","gender":"女儿"}):
    print(chunk,end="",flush=True)