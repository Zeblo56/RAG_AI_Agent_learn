# 开发时间：2026/3/31  23:11
from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool


@tool(description="获取股票价格，传入股票名称，返回字符串信息")
def get_price(name:str) ->str:
    return f"股票{name}的价格为是20元"
@tool(description="获取股票信息，传入股票名称，返回字符串信息")
def get_info(name:str) ->str:
    return f"股票{name}，是一家上市公司，专注于IT职业教育"

agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_price, get_info],
    system_prompt="你是一个AI助手，可以回答股票相关问题，记住告诉我思考过程，让我知道你调用了什么工具。"
)

for chunk in agent.stream(
    {"messages":[{"role":"user","content":"联合汽车电子股价多少，并介绍一下"}]},
    stream_mode="values"
):
    latest_message = chunk["messages"][-1]

    if latest_message.content:
        print(type(latest_message).__name__,latest_message.content)

    #不是每条消息都有tool_calls
    try:
        if latest_message.tool_calls:
            print(f"工具调用：{[tc['name'] for tc in latest_message.tool_calls]}")
    except Exception as e:
        pass