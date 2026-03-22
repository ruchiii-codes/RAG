from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI         # Extract text and sending to LLM for summarization
from langchain_core.output_parsers import StrOutputParser   # To parse the output from LLM to string format
from langchain_core.prompts import PromptTemplate      # To create a prompt template for summarization
from dotenv import load_dotenv           # To load environment variables from a .env file

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('her.txt', encoding='utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(len(docs[0].page_content))

print(type(docs[0]))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))