# 开发时间：2026/3/21  20:48
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import  JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import  ChatTongyi

str_parser = StrOutputParser()
json_parser = JsonOutputParser()  #AIMessage输入，JSON输出
model = ChatTongyi(model="qwen3-max")
prompt_first = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了个{gender}，请起名字，并且返回json格式，键为name,值为你起的名字"
)

prompt_second = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义"
)


chain = prompt_first | model | json_parser | prompt_second | model | str_parser

for chunk in chain.stream({"lastname":"张","gender":"儿子"}):
    print(chunk,end="",flush=True)


