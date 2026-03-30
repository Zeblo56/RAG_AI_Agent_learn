# 开发时间：2026/3/30  21:54
#向量存储服务
from langchain_chroma import Chroma
import config_data as config

class VetorStoreService(object):
    def __init__(self,embedding):
        """
        :param embedding: 嵌入模型的传入
        """
        self.embedding = embedding

        self.vector_store = Chroma(
            collection_name=config.COLLECTION_NAME,
            embedding_function=self.embedding,
            persist_directory=config.PERSIST_DIRECTORY,
        )

    def get_retriever(self):
        '''返回向量检索器，方便加入chain'''
        return self.vector_store.as_retriever(search_kwargs={"k":config.similarity_threshold})

if __name__ == '__main__':
    from langchain_community.embeddings import DashScopeEmbeddings
    #检索器对象
    retriever = VetorStoreService(DashScopeEmbeddings(model="text-embedding-v4")).get_retriever()

    res = retriever.invoke("新能源汽车有什么优点？")
    print(res)
