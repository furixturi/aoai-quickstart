# Official doc > Quickstarts > DALL-E
# https://learn.microsoft.com/en-us/azure/ai-services/openai/dall-e-quickstart?tabs=dalle3%2Ccommand-line&pivots=programming-language-python

from dotenv import load_dotenv
load_dotenv()

from openai import AzureOpenAI
import os
import requests
import json
from PIL import Image

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY_EASTUS"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_EASTUS")
)

model = os.getenv("AZURE_OPENAI_MODEL_DALLE3")

result = client.images.generate(
    model=model,
    prompt="a close-up of a bear walking through the forest",
    n=1
)

json_response = json.loads(result.model_dump_json())

# folder to store the image, create it if not exist
image_dir = os.path.join(os.curdir, 'images')
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

# initialize image path (file type shoud be png)
image_path = os.path.join(image_dir, 'generated_image.png')

# retrieve the generated image
## extract image URL from response
image_url = json_response["data"][0]["url"] 
# print(image_url)
## download the image
generated_image = requests.get(image_url).content
with open(image_path, 'wb') as image_file:
    image_file.write(generated_image)

# display the image in default image viewer
image = Image.open(image_path)
image.show()


