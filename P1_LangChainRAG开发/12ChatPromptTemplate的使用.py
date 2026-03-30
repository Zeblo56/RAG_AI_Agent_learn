# 开发时间：2026/3/21  19:13

#聊天提示词模板实例使用
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

#stringpromptvalue  to_string()
prompt_text = chat_pormpt_template.invoke({"history":history_data}).to_string()
# print(prompt_text)
model = ChatTongyi(model="qwen3-max")

res = model.invoke(prompt_text)
print(res.content)