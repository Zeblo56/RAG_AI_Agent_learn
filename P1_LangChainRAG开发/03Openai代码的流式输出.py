# 开发时间：2026/3/10  22:59
from openai import OpenAI

#1.获取client对象，Openai类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
#2.调用模型
response = client.chat.completions.create(
    model="qwen3.5-flash",
    messages=[
        {"role":"system","content":"你是一个python编程专家"},
        {"role":"assistant","content":"好的，我是编程专家，你要问什么？"},
        {"role":"user","content":"输出1-10的数字，使用python代码"}
    ],
    stream=True  #开启流式输出
)
#3.处理结果
# print(response.choices[0].message.content)
for chunk in response:
    if chunk is not None:
        print(
            chunk.choices[0].delta.content,
              end=' ', #每一段之间用空格分隔
              flush=True #立刻刷新缓冲区
              )