import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar dados
@st.cache
def carregar_dados(arquivo_excel):
    df = pd.read_excel(arquivo_excel)
    return df

# Carregando os dados
st.title("Dashboard Climático - Dados para Prevenção da Dengue")

# Upload do arquivo Excel
arquivo = st.file_uploader("Envie o arquivo Excel contendo os dados climáticos", type=["xlsx"])

if arquivo:
    # Carregando os dados
    dados = carregar_dados(arquivo)
    
    # Exibindo os dados brutos
    st.subheader("Dados Brutos")
    st.dataframe(dados)

    # Filtro para colunas relevantes
    colunas_interesse = ["Data", "Hora UTC", "Precipitação Total (mm)", "Temp. Bulbo Seco (°C)", "Umidade Rel. (%)"]
    dados_filtrados = dados[colunas_interesse]

    st.subheader("Dados Filtrados: Precipitação, Temperatura e Umidade")
    st.dataframe(dados_filtrados)

    # Seção para gráficos
    st.subheader("Análises Gráficas")

    # Gráfico de Precipitação Total (mm)
    st.write("Precipitação Total (mm) ao longo do tempo")
    fig_precip, ax = plt.subplots()
    ax.plot(pd.to_datetime(dados_filtrados['Data']), dados_filtrados['Precipitação Total (mm)'], label='Precipitação (mm)', color='blue')
    ax.set_xlabel('Data')
    ax.set_ylabel('Precipitação Total (mm)')
    ax.legend()
    st.pyplot(fig_precip)

    # Gráfico de Temperatura do Ar (°C)
    st.write("Temperatura do Ar (Bulbo Seco - °C) ao longo do tempo")
    fig_temp, ax = plt.subplots()
    ax.plot(pd.to_datetime(dados_filtrados['Data']), dados_filtrados['Temp. Bulbo Seco (°C)'], label='Temperatura (°C)', color='orange')
    ax.set_xlabel('Data')
    ax.set_ylabel('Temperatura (°C)')
    ax.legend()
    st.pyplot(fig_temp)

    # Gráfico de Umidade Relativa (%)
    st.write("Umidade Relativa (%) ao longo do tempo")
    fig_umd, ax = plt.subplots()
    ax.plot(pd.to_datetime(dados_filtrados['Data']), dados_filtrados['Umidade Rel. (%)'], label='Umidade Relativa (%)', color='green')
    ax.set_xlabel('Data')
    ax.set_ylabel('Umidade Relativa (%)')
    ax.legend()
    st.pyplot(fig_umd)

    # Análise de condições ideais para Aedes aegypti
    st.subheader("Análise das Condições Favoráveis ao Aedes aegypti")

    # Filtro para temperaturas entre 25°C e 30°C e umidade acima de 70%
    condicoes_ideais = dados_filtrados[
        (dados_filtrados['Temp. Bulbo Seco (°C)'] >= 25) & 
        (dados_filtrados['Temp. Bulbo Seco (°C)'] <= 30) & 
        (dados_filtrados['Umidade Rel. (%)'] >= 70)
    ]

    st.write("Períodos com condições ideais para proliferação do mosquito Aedes aegypti:")
    st.dataframe(condicoes_ideais)

else:
    st.write("Por favor, envie um arquivo Excel para continuar.")
