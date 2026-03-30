# 开发时间：2026/3/24  22:06

#文档加载器，返回Document类型对象
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="",
    csv_args={
        "delimiter": ",",
        "quotechar": "'",
        "fieldnames":['name','age','gender']
    },
    encoding="utf-8",
)
#
# #批量加载 .load()  ->   [Document,Document,...]
# documents = loader.load()

#懒加载  .lazy_load()  迭代器[document]
for document in loader.lazy_load():
    print(document)

