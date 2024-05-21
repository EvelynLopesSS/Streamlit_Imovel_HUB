import streamlit as st
import streamlit.components.v1 as components


page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: url("https://media-blog.genialinvestimentos.com.br/wp-content/uploads/2021/01/11141457/como-investir-em-fundos-imobiliarios.jpg");
    background-size: cover;
    background-attachment: local;
}
</style>
"""
#st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    st.title('Assistente Imobiliário Nelson')
    
    # Código HTML para incorporar o chatbot com largura e altura máximas
    chatbot_html = """
    <iframe src="https://stack-ai.com/internal_ui/c4944f22-cfd1-4bbd-a09e-f5cc4b2b257b/dd31e746-b2ad-44f0-a68d-ca685cbd319f/664bdb09b6ad9db5c569158c" 
            width="100%" height="650px" style="border:none;"></iframe>
    """
    
    # Incorporando o chatbot na página
    components.html(chatbot_html, height = 650)
    
    
if __name__ == '__main__':
    main()
