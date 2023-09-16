import streamlit as st
import pandas as pd

df_data = st.session_state['data']

setores = df_data['SETOR'].value_counts().index
setor = st.sidebar.selectbox("ESCOLHA O SETOR:",setores)

df_func = df_data[df_data['SETOR'] == setor]
funcs = df_func['NOME'].value_counts().index
func = st.sidebar.selectbox("ESCOLHA O FUNCIONÁRIO:",funcs)

# Filtrar o DataFrame com base no funcionário selecionado
filtro_df = df_data[df_data['NOME'] == func]

# Calcular a média de produtividade por mês
media_mes = filtro_df.groupby('Mes')['PRODUTIVIDADE'].mean()
filtro_premio = df_data[df_data['NOME']== func]

#grafico do premio do funcionario
premio = filtro_premio.groupby('Mes')['PremioReceber'].mean()
st.subheader(f'Segue os Prêmios de cada mês de {func}: ')
st.bar_chart(premio)

#mostrar a informação do valor total do premio do funcionario
total = premio.sum()
valor_formatado = f"{total:.2f}"
msg= f" O TOTAL DOS PRÊMIOS É DE R$ {valor_formatado}"
st.info(msg)


#grafico da produtividade do funcionario
st.subheader(f'Média de Produtividade de {func} por Mês:')
st.bar_chart(media_mes)
