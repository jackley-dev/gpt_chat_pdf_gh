# openai和pinecone key设置
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENV = os.getenv('PINECONE_ENV')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_INDEX = os.getenv('PINECONE_INDEX')
