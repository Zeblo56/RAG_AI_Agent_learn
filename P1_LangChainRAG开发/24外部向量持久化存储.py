# 开发时间：2026/3/24  23:23
# 开发时间：2026/3/24  23:14
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

#chroma 向量数据库（轻量级）
from langchain_chroma import Chroma

#持久化存储
vector_store = Chroma(
    collection_name='test',  #类似于数据库表名
    embedding_function=DashScopeEmbeddings(), #嵌入模型
    persist_directory='./chroma_db'  #指定数据存放地址
)

loader = CSVLoader(
    file_path='',
    encoding='utf-8',
    source_column="", #指定本条数据的来源是哪里
)

documents = loader.load()  #类型为[Document,Document,...]

#向量存储的新增
vector_store.add_documents(
    documents = documents,  #被添加的文件，类型：list[Document]
    ids=["id"+str(i) for i in range(1,len(documents)+1)]  #给添加的文档提供id（字符串）,list[str]
)

#删除  传入[id,id,...]
vector_store.delete(['id1','id2'])

#检索
result = vector_store.similarity_search(
    "question1",  #提出的问题
    3   ,#检索的结果返回几个
    filter={"source":"test"}  #过滤，我只保留source为test的数据。对应于上面的source_column制定的source
)
print(result)