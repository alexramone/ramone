import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

df_data2 = st.session_state['data1']
df_data4 = st.session_state['data2']

st.set_page_config(
    page_title="Meu Aplicativo Widescreen",
    layout="wide",  # Define o layout como widescreen
)
# Reordena os meses de janeiro a dezembro
ordem_meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

setor2 = df_data2['setor'].value_counts().index
setor3 = st.sidebar.selectbox('Selecione o Setor:', setor2)

filtro_df = df_data2[df_data2['setor'] == setor3]
mediasetor = filtro_df.groupby('mes')['media'].mean()

filtro_bob = df_data2[df_data2['setor'] ==setor3]
prod_bobina = filtro_bob.groupby('mes')['prod_bobinas'].mean()

filtro_linha = df_data2[df_data2['setor'] == setor3]
trafos = filtro_linha.groupby('mes')['media_linha_trafos'].mean()

filtro_horas = df_data4[df_data4['setor']==setor3]
horas_paradas = filtro_horas.groupby('DESCRICAO_PARADA').sum()

dados_agrupados = df_data2.groupby('setor')['total dos premios'].sum()
df_agrupado = dados_agrupados.reset_index()

# Reordena mediasetor e filtro_bobina de acordo com a ordem dos meses
mediasetor = mediasetor.reindex(ordem_meses)
prod_bobina = prod_bobina.reindex(ordem_meses)
trafos = trafos.reindex(ordem_meses)
#######################################################################################
# Cria duas colunas para exibir os gráficos lado a lado
col1, col2, col3, col4 = st.columns(4)
with col1:
    fig, ax = plt.subplots()
    ax.plot(mediasetor.index,mediasetor.values, marker='o', linestyle='-')
    ax.set_title('A Média de Produtividade do Setor por Mês:')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Média de Produtividade')
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    ax.bar(prod_bobina.index, prod_bobina.values)
    ax.set_title('Quantidade de Bobina Produzidas por Mes')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Quantidade')
    st.pyplot(fig)  
with col3:
    # Criar um gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(df_agrupado['setor'], df_agrupado['total dos premios'])
    ax.set_xlabel('Setor')
    ax.set_ylabel('Total dos Prêmios')
    ax.set_title('Total dos Prêmios por Setor')
    st.pyplot(fig)
   
with col4:
    sns.set(style='whitegrid')
    fig, ax = plt.subplots()
    sns.barplot(x=trafos.values, y=trafos.index, ax=ax)
    ax.set_xlabel('Média Linha Trafos')
    ax.set_ylabel('Mês')
    ax.set_title('Média Linha Trafos por Mês')
    st.pyplot(fig)
    

    # Gerando o gráfico de barras interativo com Altair
st.altair_chart(
alt.Chart(horas_paradas.reset_index()).mark_bar().encode(
x='DESCRICAO_PARADA',
y=alt.Y('JAN', title='Horas Paradas'),
tooltip=['DESCRICAO_PARADA', 'JAN']
).properties(
width=800,
title=f'Horas Paradas por Descrição - Setor: {setor3}'
)
)
