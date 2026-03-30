# 开发时间：2026/3/18  22:43
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate


template = PromptTemplate.from_template("我的邻居叫{name},她喜欢{hobby}")

#format
res = template.format(name='lucy',hobby='singing')
print(res,type(res))  #返回字符串


#invoke
res2 = template.invoke({'name':'lucy','hobby':'singing'})
print(res2,type(res2))  #返回PromptValue类对象