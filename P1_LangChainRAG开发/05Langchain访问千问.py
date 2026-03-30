# 开发时间：2026/3/18  20:33
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

# res = model.invoke(input="你是谁？能做什么？")
res = model.stream(input="你是谁？能做什么？")  #流式输出

for trunk in res:
    print(trunk,end="",flush=True)  #结尾默认的换行改为空字符，flush实时展示
