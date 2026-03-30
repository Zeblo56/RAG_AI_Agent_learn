# 开发时间：2026/3/18  22:10
#FewShot提示词模版（FewShotPromptTemplate）
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_community.llms.tongyi import Tongyi

#示例的模板
example_template = PromptTemplate.from_template("单词:{word},反义词:{antonym}")

#示例的动态数据注入，要求是list内部套字典
example_data = [
    {"word":"大","antonym":"小"},
    {"word":"上","antonym":"下"}
]

few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template, #示例数据的模版
    examples=example_data,  #示例的数据（用来注入动态数据的）,list内套字典
    prefix="告知我单词的反义词，我提供以下示例：",  #示例之前的提示词
    suffix="基于前面示例告知我，{input_word}的反义词",    #示例之后的提示词
    input_variables=['input_word']      #声明在前后缀的提示词中需要注入的变量名
)
prompt_text = few_shot_template.invoke(input={"input_word":"完美无缺"}).to_string()
print(prompt_text)

model = Tongyi(model='qwen-max')
print(model.invoke(input=prompt_text))