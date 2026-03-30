# 开发时间：2026/3/24  22:50
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_loader = TextLoader(
    file_path='',
    encoding='utf-8',
)

document = text_loader.load()   #类型为[Document]


#递归字符文本分割器
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,#分段最大字符数
    chunk_overlap=50,#分段之间允许重叠字符数
    separators=["\n\n","\n",".",",","。","，"," ",""],  #文本自然段落分隔依据符号
    length_function=len  #统计字符的依据函数
)

spilit_docs = splitter.split_documents(document) #类型为[Document,Document,...]