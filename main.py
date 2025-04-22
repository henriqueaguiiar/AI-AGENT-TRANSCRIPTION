from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

cliente  = OpenAI()

with open("audio.mp3", "rb") as arquivo:
    transcricao = cliente.audio.transcriptions.create(
        file=arquivo,
        model="whisper-1",
        language="pt"
    )

print(transcricao)