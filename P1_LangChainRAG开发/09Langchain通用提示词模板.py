# 开发时间：2026/3/18  21:37
#通用提示词模板（PromptTemplate）
from langchain_core.prompts import  PromptTemplate
from langchain_community.llms.tongyi import Tongyi


#zero-shot(没有示例，全靠模型本身能力)
prompt_template = PromptTemplate.from_template(
    "我的朋友姓{lastname}，刚生了{gender},帮我取个名字"
)

# prompt_text = prompt_template.format(lastname='张',gender='女儿')
# model = Tongyi(model='qwen-max')  #LLM模型
# res = model.invoke(input=prompt_text)
# print(res)


model = Tongyi(model='qwen-max')
chain = prompt_template | model  #链式写法

res = chain.invoke(input={"lastname":"张","gender":"女儿"})
print(res)