# 开发时间：2026/3/24  22:58
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path='',
    mode='page',  #读取模式，可选page(按页面划分不同Document)/single(单个Document)
    password='password',
)

i=0
for doc in loader.lazy_load():
    i+=1
    print(doc)
    print("="*20,i)