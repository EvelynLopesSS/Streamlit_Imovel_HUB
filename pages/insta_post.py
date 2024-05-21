import streamlit as st
from pathlib import Path
import google.generativeai as genai
import os

if not os.path.exists("img"):
    os.makedirs("img")

# Configuração do modelo
generation_config = {
  "temperature": 1,
}

# Configure your API key
api_key = st.secrets["google"]["api_key"]

# Configurando a chave de API para genai
genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest",
                              generation_config=generation_config,
                             )

def generate_instagram_post(image_path, user_input):
    prompt_parts = [
        "Você é um assistente de marketing de uma imobiliária de João Pessoa, Paraíba.\nSeu trabalho é gerar um post para o Instagram a partir das imagens enviadas ou criar a imagem do post de acordo com a descrição do usuário.",
        "input: ",
        genai.upload_file(image_path),
        "output: Apartamento em Manaíra, a partir de R$ 407.000,00.\n👉 Características:\n- Playgroud\n- Piscina\n-Elevador\n- Salão de Festas\n- Espaço Gourmet\n#apartamentoavendamanaira #apartamentoavendajp\n#imovelavendapb\n#corretoreldersantos",
        "input: gere um post para o instagram de anuncio de venda desse imóvel ",
        user_input,
        "output: ",
    ]

    response = model.generate_content(prompt_parts)
    return response.text





def main():
    st.image('https://images.tv9hindi.com/wp-content/uploads/2023/11/instagram-past-name.jpg', use_column_width=True)
    st.header("📸 Gerar Post para Instagram com o Gemini ✨")
    st.write("""
             Esta ferramenta permite gerar automaticamente posts para o Instagram de anúncios imobiliários. 
             Siga essas instruções:

             - Envie uma imagem do imóvel ou a imagem do anúncio.
             - Descreva o que deseja brevemente ou de forma bastante detalhada.
             A ferramenta irá criar um post com base nessas informações.
             """)

    uploaded_file = st.file_uploader("Envie uma imagem do imóvel ou o post do anúncio", type=["png", "jpg", "jpeg"])
    user_input = st.text_area("Descrição do imóvel")

    if st.button("Gerar Post"):
        with st.spinner('Gerando Post ...😮‍💨🫨🤪🤯'):

            if uploaded_file is not None and user_input:
                image_path = f"temp_{uploaded_file.name}"
                with open(image_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                post_text = generate_instagram_post(image_path, user_input)
                st.balloons()
                st.subheader("Texto Gerado para o Post:")
                st.write(post_text)
                
                # Optionally, display the uploaded image
                st.image(image_path, caption="Imagem do Imóvel", use_column_width=True)
                
                # Remove the temporary file after processing
                Path(image_path).unlink()
            else:
                st.warning("Por favor, envie uma imagem e insira a descrição do imóvel.")
                        
if __name__ == '__main__':
    main()
