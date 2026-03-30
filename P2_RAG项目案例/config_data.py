# 开发时间：2026/3/29  21:12
from ollama import embeddings

md5_path = './md5.txt'

#Chroma
COLLECTION_NAME = 'rag'
PERSIST_DIRECTORY = './chroma_db'

#spliter
CHUNK_SIZE = 1000
CHUNK_OVERLAP_SIZE = 100
SEPARATORS = ["\n\n",'\n','.',',','|','，','。','！','？',' ','']
min_split_char_number = 1000 #文本分隔的阈值

#检索返回匹配的文档数量
similarity_threshold = 1

embedding_model_name = "text-embedding-v4"
chat_model_name = "qwen3-max"