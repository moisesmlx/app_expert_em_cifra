
import streamlit as st
import google.generativeai as genai


def chat_bot():
    # 1. Configurar a chave de API do Gemini
    GOOGLE_API_KEY = ''
    genai.configure(api_key=GOOGLE_API_KEY)

    # 2. Inicializar o modelo Gemini
    model = genai.GenerativeModel('gemini-2.5-flash')

    # 4. Manter o histórico de mensagens
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 5. Exibir o histórico de mensagens ao recarregar a página
    st.markdown('''<svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://w3.org">
  <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM12 20C7.59 20 4 16.41 4 12C4 7.59 7.59 4 12 4C16.41 4 20 7.59 20 12C20 16.41 16.41 20 12 20Z" fill="#1A73E8"/>
  <path d="M12 6C8.69 6 6 8.69 6 12C6 15.31 8.69 18 12 18C15.31 18 18 15.31 18 12C18 8.69 15.31 6 12 6ZM12 16C9.79 16 8 14.21 8 12C8 9.79 9.79 8 12 8C14.21 8 16 9.79 16 12C16 14.21 14.21 16 12 16Z" fill="#1A73E8"/>
</svg>Pesquisa na Ia''', unsafe_allow_html=True
)
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 6. Capturar a entrada do usuário
    if user_prompt := st.chat_input("Como posso ajudar você hoje?"):
        
        # Exibir a mensagem do usuário na tela
        st.chat_message("user").markdown(user_prompt)
        
        # Adicionar a mensagem do usuário ao histórico
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        # Gerar a resposta do Gemini
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                response = model.generate_content(user_prompt)
                st.markdown(response.text)
                
        # Adicionar a resposta do assistente ao histórico
        st.session_state.messages.append({"role": "assistant", "content": response.text})

if __name__ == '__main__':
    chat_bot()
    
