# 开发时间：2026/3/10  23:19
from openai import OpenAI

#1.获取client对象，Openai类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
#2.调用模型
response = client.chat.completions.create(
    model="qwen3.5-35b-a3b",
    messages=[
        {"role":"system","content":"你是一个AI专家，说话很简明"},
        {"role":"user","content":"小明有两只小狗"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"小红有三只小猫"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"请问一共有几只宠物？"},

    ],
    stream=True  #开启流式输出
)
#3.处理结果
# print(response.choices[0].message.content)
for chunk in response:
    delta = chunk.choices[0].delta
    if delta.content:
        print(
            delta.content,
            end="",
            flush=True
        )