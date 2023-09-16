import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_data2 = pd.read_excel(
    io='./datasets/medias.xlsx',
    engine='openpyxl',
    sheet_name='med',
    usecols='A:C',
    nrows=20  
)
setor2 = df_data2['setor'].value_counts().index
setor3 = st.sidebar.selectbox('Selecione o Setor:', setor2)

filtro_df = df_data2[df_data2['setor'] == setor3]

mediasetor = filtro_df.groupby('mes')['media'].mean()

st.subheader('A Média de Produtividade do Setor Selecionado de Cada Mês:')
st.bar_chart(mediasetor)