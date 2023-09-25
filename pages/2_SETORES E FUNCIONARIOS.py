import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_data = st.session_state['data']

setores = df_data['SETOR'].unique()
setor = st.sidebar.selectbox("ESCOLHA O SETOR:",setores)
df_func = df_data[df_data['SETOR'] == setor]
funcs = df_func['NOME'].unique()
func = st.sidebar.selectbox("ESCOLHA O FUNCIONÁRIO:",funcs)

# Defina a ordem desejada dos meses
ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto']

# Filtrar o DataFrame com base no funcionário selecionado
filtro_df = df_data[df_data['NOME'] == func]

# Reorganize os dados do DataFrame de acordo com a ordem dos meses
filtro_df['Mes'] = pd.Categorical(filtro_df['Mes'], categories=ordem_meses, ordered=True)

# Calcular a média de produtividade por mês
media_mes = filtro_df.groupby('Mes')['PRODUTIVIDADE'].sum()
filtro_premio = df_data[df_data['NOME']== func]

#filtranto todos funcionarios e as prod. de cada setor
media_mes_setor = df_func.groupby(['Mes', 'NOME'])['PRODUTIVIDADE'].mean().unstack()

###criando colunas para os graficos
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots()
    ax.bar(media_mes.index, media_mes.values)
    ax.set_title(f'A Média de Produtividade de {func}:')
    ax.set_xlabel('Mês')
    ax.set_ylabel('media')
    ax.set_xticklabels(ordem_meses, rotation=45)  ###defina a ordem dos meses
    st.pyplot(fig) 

with col2:
    premio = filtro_premio.groupby('Mes')['PremioReceber'].mean().reindex(ordem_meses)
    sns.set(style='whitegrid')
    fig, ax = plt.subplots()
    sns.barplot(x=premio.values, y=premio.index, ax=ax)
    ax.set_xlabel('Valores em Reais (R$)')
    ax.set_ylabel('Mês')
    ax.set_title(f'Segue os Prêmios de cada mês de {func}: ')
    st.pyplot(fig)

# grafico de todos funcionarios com a prod. de cada setor
plt.figure(figsize=(20, 8))
for nome, data in media_mes_setor.iterrows():
    plt.bar(data.index, data.values, label=nome)

plt.xlabel('Mês')
plt.ylabel('Média de Produtividade')
plt.title(f'Média de Produtividade por Mês no Setor: {setor}')
plt.xticks(rotation=80)
plt.legend(loc='upper right')
st.pyplot(plt)

#mostrar a informação do valor total do premio do funcionario
total = premio.sum()
valor_formatado = f"{total:.2f}"
msg= f" # O Total dos prêmios de {func} é de R$ {valor_formatado}"
st.info(msg)
