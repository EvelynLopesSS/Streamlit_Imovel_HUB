import streamlit as st
from streamlit_option_menu import option_menu

#st.sidebar.image("https://media-blog.genialinvestimentos.com.br/wp-content/uploads/2021/01/11141457/como-investir-em-fundos-imobiliarios.jpg", use_column_width=True)

st.sidebar.title('Navegação')
st.image("https://i2.wp.com/pmcaonline.org/wp-content/uploads/2021/05/Real-Estate-Industry.jpg", use_column_width=True)
    
st.sidebar.page_link("pages/predict_page.py", label="Previsão de Preços", icon="💲")
st.sidebar.page_link("pages/chatbot.py", label="Chatbot", icon="💬")
st.sidebar.page_link("pages/insta_post.py", label="Criar Post Instagram", icon="📸")

st.write("""
# 🏠 Bem-vindo ao Imovél HUB""")  
st.divider()
 
st.write("""
Este é um aplicativo desenvolvido com Streamlit para ajudar os Corretores de imóveis.
         
Por aqui é possível fazer  uma previsão de preços de imóveis, criação de post de anúncio de imóvel em segundos, além de oferecer o chatbot Nelson para responder perguntas relacionadas ao mercado imobiliário.

**Recursos do Chatbot Nelson:**

- 📄 Recebe documentos de vários formatos, como PDFs, DOCs, TXTs, etc.
- 🖼️ Realiza OCR (Reconhecimento Óptico de Caracteres) para extrair texto de documentos não editáveis, como PDFs e imagens.
- 💬 Responde perguntas e fornece informações sobre os documentos enviados.
- 📝 Ajuda a redigir Contratos  variados.
- 🔢 Ajuda a realaizar operações matemáticas.  
         

Use a barra lateral para navegar entre as diferentes funcionalidades:

- **Previsão de Preços**: Faça uma previsão do preço de um imóvel com base em suas características.
- **Chatbot Nelson**: Interaja com Nelson, o assistente virtual, para lhe auxiliar no que for preciso.
- **Criar Post Instagram"**: Criação de post de anúncio de imóvel a partir de imagem, usando o Gemini.

Divirta-se explorando as funcionalidades do aplicativo! 🎉
""")
