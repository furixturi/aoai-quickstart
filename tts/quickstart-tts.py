# Official doc > Quickstarts > Text to speech
# https://learn.microsoft.com/en-us/azure/ai-services/openai/text-to-speech-quickstart?tabs=command-line

# https://platform.openai.com/docs/guides/text-to-speech
# https://ttsopenai.com/

from dotenv import load_dotenv
load_dotenv()

from openai import AzureOpenAI
import os

# Port the following BASH example to Python:
# curl $AZURE_OPENAI_ENDPOINT/openai/deployments/YourDeploymentName/audio/speech?api-version=2024-02-15-preview \
#  -H "api-key: $AZURE_OPENAI_API_KEY" \
#  -H "Content-Type: application/json" \
#  -d '{
#     "model": "tts-1-hd",
#     "input": "I'm excited to try text to speech.",
#     "voice": "alloy"
# }' --output speech.mp3

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY_SE"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION_PREVIEW"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_SE"),
)

model = os.getenv("AZURE_OPENAI_MODEL_TTS")

response = client.audio.speech.create(
    model = model,
    voice = "alloy",
    input = "うさぎちゃん、元気？遊ぼう！"
)

with open("example.mp3", "wb") as f:
    f.write(response.content)
