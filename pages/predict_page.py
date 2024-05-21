# main.py
import streamlit as st
import pandas as pd
import joblib
from mapping import cidade_mapping, bairro_mapping, tipo_imovel_mapping, andar_mapping, status_mapping
from babel.numbers import format_currency

def predict_price(Area, Beira_Mar, Valor_M, Closet, Qtde_Quartos, Qtde_Suites, WC, DCE, Vaga_Garagem,
                  Elevador, Portaria_24h, Gerador, Central_Gas, Bicicletario, Cidade_encoded, Bairro_encoded,
                  Tipo_Imovel_encoded, Andar_encoded, Status_encoded):
    
    model = joblib.load('Imoveismodelo.pkl')

    example = [[Area, Beira_Mar, Valor_M, Closet, Qtde_Quartos, Qtde_Suites, WC, DCE, Vaga_Garagem,
                Elevador, Portaria_24h, Gerador, Central_Gas, Bicicletario, Cidade_encoded, Bairro_encoded,
                Tipo_Imovel_encoded, Andar_encoded, Status_encoded]]

    predicted_price = model.predict(example)

    return predicted_price[0]




def main():
    # Set the cover image
    st.image("https://imageio.forbes.com/specials-images/imageserve/5f0c98c0147a4f0006753d4b/Houses-of-different-size-with-different-value-on-stacks-of-coins--Concept-of-/960x0.jpg?height=355&width=711&fit=bounds", use_column_width=True)
    
    # Application description
    st.title('Previsão de Preço de Imóveis')
    st.write("""
    Este aplicativo permite prever o preço de um imóvel com base em diversas características. 
             
    Insira os detalhes do imóvel no formulário abaixo para obter uma estimativa de preço.
    """)

    # Sidebar form for input
    with st.form(key='predict_form'):
        # Create columns with custom spacing
        col1, col2, col3 = st.columns(3)

        with col1:
            Cidade_encoded = st.selectbox('Cidade', options=list(cidade_mapping.keys()), format_func=lambda x: x)
            Bairro_encoded = st.selectbox('Bairro', options=list(bairro_mapping.keys()), format_func=lambda x: x)
            Tipo_Imovel_encoded = st.selectbox('Tipo de Imóvel', options=list(tipo_imovel_mapping.keys()), format_func=lambda x: x)
            Andar_encoded = st.selectbox('Andar', options=list(andar_mapping.keys()), format_func=lambda x: x)
            Status_encoded = st.selectbox('Status', options=list(status_mapping.keys()), format_func=lambda x: x)
            WC = st.number_input('WC', min_value=0, max_value=10, value=1)
            DCE = st.number_input('DCE', min_value=0, max_value=10, value=1)
        with col2:
            Area = st.number_input('Área (m²)', min_value=50, max_value=50000, value=100)
            Valor_M = st.number_input('Valor do m²', min_value=0, max_value=100000, value=2000)
            Beira_Mar = st.selectbox('Beira Mar', [0, 1], format_func=lambda x: 'Sim' if x == 1 else 'Não')
            Closet = st.selectbox('Closet', [0, 1], format_func=lambda x: 'Sim' if x == 1 else 'Não')
            Qtde_Quartos = st.number_input('Quartos', min_value=0, max_value=100, value=1)
            Qtde_Suites = st.number_input('Suítes', min_value=0, max_value=10, value=1)


        with col3:
            Vaga_Garagem = st.number_input('Vaga de Garagem', min_value=0, max_value=10, value=1)
            Elevador = st.selectbox('Elevador', [0, 1], format_func=lambda x: 'Sim' if x == 1 else 'Não')
            Portaria_24h = st.selectbox('Portaria 24h', [0, 1], format_func=lambda x: 'Sim' if x == 1 else 'Não')
            Gerador = st.selectbox('Gerador', [0, 1], format_func=lambda x: 'Sim' if x == 1 else 'Não')
            Central_Gas = st.selectbox('Central de Gás', [0, 1], format_func=lambda x: 'Sim' if x == 1 else 'Não')
            Bicicletario = st.selectbox('Bicicletário', [0, 1], format_func=lambda x: 'Sim' if x == 1 else 'Não')
        
        submit_button = st.form_submit_button(label='Calcular Preço')

    if submit_button:
        predicted_price = predict_price(Area, Beira_Mar, Valor_M, Closet, Qtde_Quartos, Qtde_Suites, WC, DCE,
                                        Vaga_Garagem, Elevador, Portaria_24h, Gerador, Central_Gas, Bicicletario,
                                        cidade_mapping[Cidade_encoded], bairro_mapping[Bairro_encoded], 
                                        tipo_imovel_mapping[Tipo_Imovel_encoded], andar_mapping[Andar_encoded], 
                                        status_mapping[Status_encoded])
        
        formatted_price = format_currency(predicted_price, 'BRL', locale='pt_BR')
        st.success(f'Preço Previsto: {formatted_price}')

if __name__ == '__main__':
    main()