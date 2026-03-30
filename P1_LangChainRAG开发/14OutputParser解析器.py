# 开发时间：2026/3/21  20:48
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import  ChatTongyi
#AIMessage输入，字符串输出


parser = StrOutputParser()   #
model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了个{gender}，请起名字，仅仅告知我名字无需其他内容"
)

#parser为了将大模型输出的格式为AIMessage类型转为大模型可以接收的格式（字符串），并且为Runnable的子类
chain = prompt | model | parser | model

res = chain.invoke({"lastname":"张","gender":"儿子"})
print(res.content)

