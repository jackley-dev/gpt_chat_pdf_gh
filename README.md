# 项目简介
利用chatgpt api和pinecone向量数据库，基于langchain和streamlit开发的本地知识库问答系统：
- 前端采用streamlit开发，支持本地部署
- 支持在web端上传pdf文档
- 支持向量化上传的文档，并存储到pinecone数据库
- 支持基于数据库中的特定领域知识进行问答

# 使用指南
1. 需要在pinecone.io网站申请pinecone的试用版，获取pinecone api key及相关环境变量
2. 更新.env中的如下参数配置，改成实际的key和环境变量
```python
PINECONE_API_KEY='xx'
PINECONE_ENV='xx'
OPENAI_API_KEY='xx'
PINECONE_INDEX='xx'
```

# 总体思路

**1. 从本地上传pdf，并进行读取和切分**
1. 使用PyPDF2库读取pdf文件
2. 使用langchain将读取的文本切分成小段

**2. 将信息向量化，并存入向量数据库**
1. 通过openai的embedding接口，将文档转化为向量
2. 将转化后的向量存入Pinecone向量数据库

**3. 在向量数据库中搜索与query相似的内容，合并投喂给gpt进行回答**
1. 利用similarity_search函数搜索与query相似的内容
2. 利用langchain中的load_qa_chain函数，将query和查询到的相似内容作为参数传入，即可得到基于知识库的回答

# 演示实例：
1. 演示地址：https://huggingface.co/spaces/jackley86/gpt_chat_pdf
2. 由于可能有人上传大文档，演示站点的api token消耗过快，免费额度耗尽后无法继续使用，建议使用个人key在本地部署