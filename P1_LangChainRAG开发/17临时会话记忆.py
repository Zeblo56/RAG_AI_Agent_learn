# 开发时间：2026/3/21  22:45
from langchain_core.prompts import  PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(model="qwen3-max")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你需要根据会话历史回应客户问题。对话历史："),
        MessagesPlaceholder("chat_history"),
        ("human","请回答如下问题:{input}")
    ]
)
str_parser = StrOutputParser()

def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(),"="*20)
    return full_prompt

base_chain = prompt | print_prompt | model |str_parser

store = {}  #key就是session，value就是InMemoryChatMessageHistory类对象

#实现通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]

#创建一个新的类，对原有的链增强功能，自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain,  #被增强的原有的chain
    get_history,    #通过会话id获取InMemoryChatMessageHistory类对象
    input_messages_key="input", #表示用户输入在模板的占位符
    history_messages_key="chat_history",    #表示用户输入在模版中的占位符
)

if __name__ == "__main__":
    #固定格式，添加langchain的配置，为当前程序所属的session_id
    session_config = {
        "configurable":{
            "session_id":"user_001"
        }
    }
    res = conversation_chain.invoke({"input":"小明有2只猫"},session_config)
    print("第1次执行",res)
    res = conversation_chain.invoke({"input":"小红有3只狗"},session_config)
    print("第2次执行", res)
    res = conversation_chain.invoke({"input":"一共有几只宠物"},session_config)
    print("第3次执行", res)












