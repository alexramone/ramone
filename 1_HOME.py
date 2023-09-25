import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# criar data frame     
df_data = pd.read_excel(
    io='./datasets/indicador_at_bt.xlsx',
    engine='openpyxl',
    sheet_name='Planilha1',
    usecols='A:F',
    nrows=240
)
df_data2 = pd.read_excel(
    io='./datasets/indicador_at_bt.xlsx',
    engine='openpyxl',
    sheet_name='Med_AT_BT',
    usecols='A:F',
    nrows=100  
)
df_data4 = pd.read_excel(
    io='./datasets/indicador_at_bt.xlsx',
    engine='openpyxl',
    sheet_name='Hora_BT',
    usecols='A:L',
    nrows=100
)
st.session_state["data"] = df_data
st.session_state['data1'] = df_data2
st.session_state['data2'] = df_data4

st.write( " # DASHBOARD DE CONTROLE DE PRODUÇÃO DOS SETORES DE ALTA E BAIXA TENSÃO")
st.markdown(
    
    """ 
        Este é um aplicativo de visualização de dados por dashboards para o setor de controle de produção de uma empresa do ramo de transformadores elétricos,
    utilizando a ferramenta *streamlit*, uma biblioteca de python. nesta ferramenta iremos mostrar na pagina *SETORES E FUNCIONÁRIOS*, o gráfico da produtividade de cada funcionário dos setores
    de alta tensão e de baixa tensão, o gráfico dos valores ganhos por mês de cada funcionário, o gráfico da média de produtividade de todos os funcionários de cada setor e uma informação da soma de todos os prêmios ganhos do funcionário.
        Na página *MÉDIA DOS SETORES*, exibe os gráficos de cada setor como: a média de produtivade de cada mes, a média de quantidades de bobinas produzidas por mes, o valor total gasto de prêmios por setor, a média de transformadores por mês
    e o ultimo gráfico mostrando as horas paradas não programadas de cada setor por mês.
        O foco é mostrar como esta ferramenta pode ser muito útil para tomada de decisões de uma organização, por ser uma ferramenta versatil e de fácil utilização, digitando os codigos em poucas linhas e sem precisar que o gestor 
    tenha conhecimento amplo na área de programação.""")


