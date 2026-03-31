# 开发时间：2026/3/22  14:38
import os
from typing import Sequence
import json

from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import message_to_dict,messages_from_dict,BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory


#message_to_dict :单个消息对象（BaseMessage类实例） --> 字典
#message_from_dict: [字典,字典,...] --> [消息,消息,...]
#AIMessage,HumanMessage,SystemMessage 都是BaseMessage的子类


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id,storage_path):
        self.session_id = session_id  #会话id
        self.storage_path = storage_path    #不同会话id的存储文件，所在的文件夹路径

        #完整的文件路径
        self.file_path = os.path.join(self.storage_path,self.session_id)

        #确保文件存在
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        #Sequence序列，类似于list、tuple
        all_messages = list(self.messages)  #已有的消息列表
        all_messages.extend(messages) #新的和已有的融合成一个list

        #将数据同步写入到本地文件中
        #类对象写入文件 --> 一堆二进制
        #为了方便可以将BaseMessage消息转入字典
        #官方message_to_dict：单个消息对象(BaseMessage类实例) -->字典
        # new_messages = []
        # for message in messages:
        #     d = message_to_dict(message)
        #     new_messages.append(d)
        new_messages = [message_to_dict(message) for message in all_messages]

        #将数据写入文件
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump(new_messages,f)


    @property     #@property装饰器将messages方法变成成员属性用
    def messages(self) -> list[BaseMessage]:
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                message_data = json.load(f) #返回值就是：list[字典]
                return messages_from_dict(message_data)
        except FileNotFoundError:
            return []

    def clear(self):
        with open(self.file_path,'w',encoding="utf-8") as f:
            json.dump([],f)









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


def get_history(session_id):
    return FileChatMessageHistory(session_id, './chat_history')

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
    # res = conversation_chain.invoke({"input":"小明有2只猫"},session_config)
    # print("第1次执行",res)
    # res = conversation_chain.invoke({"input":"小红有3只狗"},session_config)
    # print("第2次执行", res)
    res = conversation_chain.invoke({"input":"一共有几只宠物"},session_config)
    print("第3次执行", res)