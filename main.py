from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

cliente  = OpenAI()

prompt = "Esse audio é de um anuncio da jornada full-stack da hashtag, um conteúdo completaçõ sobre desenvolvimento"

with open("audio.mp3", "rb") as arquivo:
    transcricao = cliente.audio.transcriptions.create(
        file=arquivo,
        model="whisper-1",
        language="pt",
        response_format="srt",
        prompt=prompt
    )

print(transcricao)

with open("legenda.srt", "w", encoding="utf-8") as arquivo_legenda:
    arquivo_legenda.write(transcricao)