![image](https://github.com/user-attachments/assets/ba760bb9-03fc-46c2-899c-8f48a52e1e6a)

# 🧠 AI Agent Transcription

Projeto de agente de Inteligência Artificial para **transcrição automática de áudios ou vídeos** e **geração de legendas**, com uma interface simples desenvolvida em **Streamlit**.

Esse projeto visa facilitar o consumo de conteúdos gravados (como aulas, palestras ou vídeos explicativos), tornando-os acessíveis por meio de texto transcrito.

---

## ⚙️ Tecnologias utilizadas

- **Python 3.10+**
- **[OpenAI Whisper](https://github.com/openai/whisper)** — Transcrição de áudio/vídeo com IA.
- **[Streamlit](https://streamlit.io/)** — Interface web interativa.
- **[PyDub](https://github.com/jiaaro/pydub)** — Manipulação de áudio.
- **SpeechRecognition** — Suporte adicional ao reconhecimento de fala.

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/henriqueaguiiar/AI-AGENT-TRANSCRIPTION.git
cd AI-AGENT-TRANSCRIPTION
```

### 2. Crie e ative o ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
# Ative o ambiente:
venv\Scripts\activate       # No Windows
source venv/bin/activate    # No Linux/macOS
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação com Streamlit
```bash
streamlit run main.py
```

Depois disso, acesse o app no navegador:
- http://localhost:8501

---

## 📝 Observações

- A aplicação transcreve arquivos de mídia e exibe legendas diretamente no navegador.
- É necessário ter os arquivos `.mp3`, `.wav`, `.mp4` ou similares salvos localmente para transcrição.

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais.
