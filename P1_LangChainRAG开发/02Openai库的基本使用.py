# 开发时间：2026/3/10  22:45
from openai import OpenAI

#1.获取client对象，Openai类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
#2.调用模型
response = client.chat.completions.create(
    model="qwen3.5-flash",
    messages=[
        {"role":"system","content":"你是一个python编程专家，并且不说废话简单回答"},#设置模型的行为规则
        {"role":"assistant","content":"好的，我是编程专家，并且话不多，你要问什么？"},#设置模型的回答
        {"role":"user","content":"输出1-10的数字，使用python代码"}#用户提问
    ]
)
#3.处理结果
print(response.choices[0].message.content)
