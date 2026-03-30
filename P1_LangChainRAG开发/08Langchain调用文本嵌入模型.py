# 开发时间：2026/3/18  21:11
#Embeddings Models(文本嵌入模型)：将字符串作为输入，返回一个浮点数的列表（即向量）
#在NLP中，Embedding的作用就是将数据进行文本向量化

from langchain_community.embeddings import DashScopeEmbeddings

#创建模型对象
model = DashScopeEmbeddings()

#调用
print(model.embed_query('你好啊'))  #单次转换
print(model.embed_documents(['你好啊','吃饭了吗','我稀饭你'])) #批量转换