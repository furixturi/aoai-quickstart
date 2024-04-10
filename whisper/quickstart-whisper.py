# Official doc > Quickstarts > Whisper
# https://learn.microsoft.com/en-us/azure/ai-services/openai/whisper-quickstart?tabs=command-line%2Cpython-new&pivots=rest-api

from dotenv import load_dotenv
load_dotenv()

from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY_SE"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_SE")
)

model = os.getenv("AZURE_OPENAI_MODEL_WHISPER")

# https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/sampledata/audiofiles
audio_test_file = "./TalkForAFewSeconds16.wav"

result = client.audio.transcriptions.create(
    file = open(audio_test_file, "rb"),
    model = model
)

print(result)