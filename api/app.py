from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ollama
from langserve import add_routes
import uvicorn 
import os
from langchain_community.llms import Ollama

from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title='Langchain Server', version ='1.0', description='simple API server')

model1 = Ollama(model='deepseek-r1')
model2 = Ollama(model='codellama')

prompt1 = ChatPromptTemplate.from_template("Write an essay about {topic} in 100 words")
prompt2 = ChatPromptTemplate.from_template(" give code about {topic}")

def generate_output(prompt, model):
    def inner(request: dict):
        topic = request.get('topic')
        if topic:
            prompt_text = prompt.format(topic=topic)
            response = model.invoke(prompt_text)
            return {"result": response}
        return {"error": "No topic provided"}
    return inner


app.add_api_route("/essay", generate_output(prompt=prompt1, model=model1),methods=['POST'])
app.add_api_route("/code", generate_output(prompt=prompt2, model=model2),methods=['POST'])


if __name__ == "__main__":
    uvicorn.run(app,host='localhost', port=8000)
    