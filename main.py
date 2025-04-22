from legenda import legendar
import streamlit as st

#legenda = legendar("ja começou a jornada full stack.mp4", prompt = "Esse audio é de um anuncio da jornada full-stack da hashtag, um conteúdo completaçõ sobre desenvolvimento")
 

def app():
    st.header("Legendador", divider=True)
    st.markdown("#### Gere a legenda de qualquer áudio ou vídeo automaticamente.")
    
    prompt = st.text_input("Digite o contexto do video para ajudar na legenda")
    arquivo = st.file_uploader("Selecione um vídeo.pm4 ou áudio.mp3 para legendar", type=["mp4", "mp3"])
    if arquivo:
        legenda = legendar(arquivo, prompt)
        st.write(f"Arquivo {arquivo.name} legendado com sucesso")
        st.write(legenda)

if __name__ =="__main__":
    app()