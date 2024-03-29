# Official Doc Quickstarts > Completion > Python
# https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=bash%2Cpython-new&pivots=programming-language-python

from dotenv import load_dotenv
load_dotenv()


import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

model = os.getenv("AZURE_OPENAI_MODEL_GPT35_INSTRUCT")

print("Sending a test completion job")
start_phrase = "Write a tagline for an ice cream shop."
response =client.completions.create(model=model, 
                                    prompt=start_phrase, 
                                    max_tokens=10)
print(start_phrase+response.choices[0].text)
