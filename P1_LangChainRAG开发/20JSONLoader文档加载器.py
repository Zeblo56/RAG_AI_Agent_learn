# 开发时间：2026/3/24  22:35
from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path='',
    json_file_path='.name',#json提取的公式   .表示json根  []表示数组
    text_content=False, #默认为True，代表抽取内容为字符串
    json_lines=False,#默认为false，代表抽取内容不为json_lines（每一行都是独立的json）
)

document = loader.load()
print(document)