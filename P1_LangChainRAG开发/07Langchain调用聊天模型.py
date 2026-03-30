# 开发时间：2026/3/18  20:54
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
#得到模型对象，qwen3-max为聊天模型
model = ChatTongyi(model='qwen3-max')

#准备消息列表
# messages = [
#     SystemMessage(content='你是一位边塞诗人'),
#     HumanMessage(content='请为我写一首诗'),
#     AIMessage(content='锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。'),
#     HumanMessage(content='根据你给我提供的样式重新写一首唐诗')
#     ]

#简写以上代码
messages = [
    ('system','你是一位边塞诗人'),
    ('human','请为我写一首诗'),
    ('ai','锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。'),
    ('human','根据你给我提供的样式重新写一首唐诗')
    ]

res = model.stream(input=messages)

for trunk in res:
    print(trunk.content,end="",flush=True)    #聊天模型需要.content