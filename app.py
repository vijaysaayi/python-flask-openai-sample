import logging
from flask import Flask, request
import os
from openai import AzureOpenAI

app = Flask(__name__)
client = AzureOpenAI(
    azure_endpoint = os.environ["Azure_OpenAi_Endpoint"], 
    api_key=os.environ["Azure_OpenAi_Key"],   
    api_version="2023-05-15"
)

@app.route("/")
def hello():
    question = request.args.get('question')
    
    if question == None:
        question = "Do other Azure AI services support this too?"
    response = client.chat.completions.create(
        model=os.environ["Azure_OpenAi_Model"],
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
            {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
            {"role": "user", "content": question}
        ]
    )
    
    return response.choices[0].message.content
