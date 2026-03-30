# 开发时间：2026/3/21  19:33
# 开发时间：2026/3/21  19:13

from langchain_core.prompts import  ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

chat_pormpt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个边塞诗人"),
        MessagesPlaceholder("history"),  #占位符，注入历史消息
        ("human","请再来一首唐诗")
    ]
)

history_data = [
    ("human","你来为我写一首诗"),
    ("ai","床前明月光，疑是地上霜。举头望明月，低头思故乡。"),
    ("human","好诗，再来一首"),
    ("ai","锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。")
]

model = ChatTongyi(model="qwen3-max")

#组成链，要求每一个组件都是runnable接口的子类
chain = chat_pormpt_template | model

#通过链来调用invoke,一次性输出
# res = chain.invoke({"history":history_data})
# print(res.content)

#stream流式输出
for chunk in chain.stream({"history":history_data}):
    print(chunk.content,end='',flush=True)