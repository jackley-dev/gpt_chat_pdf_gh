import streamlit as st
import pinecone
import config

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to chat with pdf files 👋")

st.sidebar.success("Index page")

st.markdown(
    """
    ### 利用chatgpt api和pinecone向量数据库，基于langchain开发的本地知识库问答系统
    - 支持上传本地目录下的pdf文档
    - 向量化该文档，并存储到pinecone数据库
    - 基于数据库中的特定领域知识进行问答
"""
)

# 获取配置信息
PINECONE_API_KEY = config.PINECONE_API_KEY
PINECONE_ENV = config.PINECONE_ENV
OPENAI_API_KEY = config.OPENAI_API_KEY
PINECONE_INDEX = config.PINECONE_INDEX


# 初始化pinecone接口
@st.cache_resource
def init_connection():
    return pinecone.init(
        api_key=PINECONE_API_KEY,  # find at app.pinecone.io
        environment=PINECONE_ENV  # next to api key in console
    )


conn = init_connection()
index_name = PINECONE_INDEX

pinecone.Index(index_name)
