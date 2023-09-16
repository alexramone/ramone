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
st.session_state["data"] = df_data

st.sidebar.write('desenvolvido por Alex S. Carvalho')



      

st.write( " # DASHBOARD DE CONTROLE DE PRODUÇÃO DOS SETORES DE ALTA E BAIXA TENSÃO")
st.markdown(
    """
    Este é um aplicativo de visualização de dados por dashboards para o setor de controle de produção de uma empresa do ramo de transformadores elétricos,
utilizando a ferramenta *streamlit*, uma biblioteca de python. nesta ferramenta iremos mostrar a produtividade de cada funcionário dos setores
de alta tensão e de baixa tensão dos meses de janeiro a agosto e também, a média dos dois setores dos meses de janeiro a agosto.
    O foco é mostrar como esta ferramenta pode ser muito útil para tomada de decisões de uma organização, por ser uma ferramenta poderosa e de fácil
utilização, digitando os codigos em poucas linhas e sem precisar que o gestor tenha conhecimento amplo na área de programação.

"""
)



