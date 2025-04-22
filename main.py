from openai import OpenAI
from dotenv import load_dotenv
from pydub import AudioSegment

arquivo_selecionado = "ja começou a jornada full stack.mp4"
extensao_arquivo = arquivo_selecionado.split(".")[1]
audio = AudioSegment.from_file(file=arquivo_selecionado, format=extensao_arquivo)

audio.export("audio.mp3", format="mp3")

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