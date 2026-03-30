# 开发时间：2026/3/18  20:37
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3:4b")

# res = model.invoke(input="你是谁？")
res = model.stream(input="你是谁")   #流式输出
for trunk in res:
    print(trunk,end="",flush=True)