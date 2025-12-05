import streamlit as st
import pandas as pd
import json
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('kits.csv')


with open('casais.json', 'r', encoding='utf-8') as f:
    casais = json.load(f)



# ------------------------------------------------- SIDEBAR
st.sidebar.image('logo.png')
casal = st.sidebar.selectbox('Selecione o casal',casais.keys())
df_casal = df[df['ID Kit'].apply(lambda x: x in casais[casal]['id_kit'])]

st.title(casal)

with st.container():
    col1, col2 , col3 = st.columns(3)
    with col1:
        with st.container(border=True, height='stretch'):
            st.metric('Saldo Inicial', f'R$ 1800')
    
    with col2:
        with st.container(border=True, height='stretch'):
            st.metric('Saldo Atual', f'R$ {df_casal['Valor Mensal'].sum()}')
    
    with col3:
        with st.container(border=True, height='stretch'):
            st.metric('Pontuação Final', df_casal['Pontuação (oculto)'].sum())

with st.container(border=True):
    df_aux = df_casal.groupby('Tipo')['Valor Mensal'].sum().reset_index()
    fig = px.pie(df_aux, names='Tipo', values='Valor Mensal', title='Gastos por Tipo de Kit')
    st.plotly_chart(fig)

with st.container():
    st.subheader('Gasto Total por Tipo')
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        with st.container(border=True, height='stretch'):
            st.metric('Alimentação', f'R$ {df_casal[df_casal['Tipo'] == 'Alimentação']['Valor Mensal'].sum()}')
    with col2:
        with st.container(border=True, height='stretch'):
            st.metric('Lazer, Cultura e Compras', f'R$ {df_casal[df_casal['Tipo'] == 'Lazer, Cultura e Compras']['Valor Mensal'].sum()}')
    with col3:
        with st.container(border=True, height='stretch'):
            st.metric('Serviços Financeiros', f'R$ {df_casal[df_casal['Tipo'] == 'Serviços Financeiros']['Valor Mensal'].sum()}')
    with col4:
        with st.container(border=True, height='stretch'):
            st.metric('Saúde e Beleza', f'R$ {df_casal[df_casal['Tipo'] == 'Saúde e Beleza']['Valor Mensal'].sum()}')

df_casal = df[df['ID Kit'].apply(lambda x: x in casais[casal]['id_kit'])]
st.markdown('# Kits comprados')
for i in sorted(casais[casal]['id_kit']):
    st.markdown(f'## {i} - {df_casal[df_casal['ID Kit'] == i]['Nome do Kit'].iloc[0].split('\n')[0]} | Valor Mensal: R$ {df_casal[df_casal['ID Kit'] == i]['Valor Mensal'].iloc[0]} ({df_casal[df_casal['ID Kit'] == i]['Tipo'].iloc[0]})')
    st.markdown(f'- ### Pontuação: {df_casal[df_casal['ID Kit'] == i]['Pontuação (oculto)'].iloc[0]}')