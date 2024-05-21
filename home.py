import streamlit as st

st.sidebar.image("https://media-blog.genialinvestimentos.com.br/wp-content/uploads/2021/01/11141457/como-investir-em-fundos-imobiliarios.jpg", use_column_width=True)

st.sidebar.title('Navegação')
st.image("https://imageio.forbes.com/specials-images/imageserve/5f0c98c0147a4f0006753d4b/Houses-of-different-size-with-different-value-on-stacks-of-coins--Concept-of-/960x0.jpg?height=355&width=711&fit=bounds", use_column_width=True)
    
st.sidebar.page_link("pages/predict_page.py", label="Previsão de Preços", icon="🏠")
st.sidebar.page_link("pages/chatbot.py", label="Chatbot", icon="💬")

st.write("""
# 🏠 Bem-vindo ao Imovél HUB""")  
st.divider()
btn_login_clicked = False
btn_register_clicked = False
col1, col2 = st.columns(2)

with col1:
    if st.button("Entrar"):
        btn_login_clicked = True

with col2:
    if st.button("Cadastrar"):
        btn_register_clicked = True

if btn_login_clicked:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    btn_confirm_login = st.button("Confirmar")

if btn_register_clicked:
    new_username = st.text_input("Novo Username")
    new_password = st.text_input("Nova Password", type="password")
    btn_confirm_register = st.button("Confirmar")

st.divider()  
st.write("""
Este é um aplicativo desenvolvido com Streamlit para ajudar os Corretores de imóveis.
         
Por aqui é possível fazer  uma previsão de preços de imóveis, além de oferecer o chatbot Nelson para responder perguntas relacionadas ao mercado imobiliário.

**Recursos do Chatbot Nelson:**

- 📄 Recebe documentos de vários formatos, como PDFs, DOCs, TXTs, etc.
- 🖼️ Realiza OCR (Reconhecimento Óptico de Caracteres) para extrair texto de documentos não editáveis, como PDFs e imagens.
- 💬 Responde perguntas e fornece informações sobre os documentos enviados.
- 📝 Ajuda a redigir Contratos  variados.
- 🔢 Ajuda a realaizar operações matemáticas.  
         

Use a barra lateral para navegar entre as diferentes funcionalidades:

- **Previsão de Preços**: Faça uma previsão do preço de um imóvel com base em suas características.
- **Chatbot Nelson**: Interaja com Nelson, o assistente virtual, para lhe auxiliar no que for preciso.

Divirta-se explorando as funcionalidades do aplicativo! 🎉
""")
