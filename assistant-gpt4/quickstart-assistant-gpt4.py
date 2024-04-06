# Official Doc Quickstarts > Assistants (preview)
# https://learn.microsoft.com/en-us/azure/ai-services/openai/assistants-quickstart?tabs=command-line&pivots=programming-language-python

# Using Australia East region

from dotenv import load_dotenv

load_dotenv()

import os
import time
import json
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY_AU"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION_PREVIEW"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_AU"),
)

model = os.getenv("AZURE_OPENAI_MODEL_GPT4")

# create an assistant
assistant = client.beta.assistants.create(
    name="Math Assist",
    instructions="You are an AI assistant that can write code to help answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model=model,
)

# create a thread
thread = client.beta.threads.create()

# add a user question to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?",
)

# run the thread
run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant.id)

# retrieve the status of the run
run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
status = run.status

# wait till the assistant has responded
while status not in ["completed", "cancelled", "expired", "failed"]:
    time.sleep(5)
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    status = run.status

messages = client.beta.threads.messages.list(thread_id=thread.id)

print(messages.model_dump_json(indent=2))
