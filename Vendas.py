import streamlit as st
import pandas as pd
import json

st.set_page_config(layout='wide')

df = pd.read_csv('kits.csv')


with open('casais.json', 'r', encoding='utf-8') as f:
    casais = json.load(f)

def atualizar_json(dicionario):
    with open('casais.json', 'w', encoding='utf-8') as f:
        json.dump(dicionario, f, indent=4, ensure_ascii=False)

def mostrar_kits(df):
    
    for i in df['ID Kit']:
        st.write(i)
    

# ------------------------------------------------- SIDEBAR
st.sidebar.image('logo.png')
casal = st.sidebar.selectbox('Selecione o casal',casais.keys())

st.title(casal)

alimentacao, lazer, financeiros, saude = st.tabs(df['Tipo'].unique().tolist())

colunas = ['ID Kit',
 'Nome do Kit',
 'Descrição',
 'Valor Mensal',
 'Valor Anual']

with alimentacao:
    df1 =df[df['Tipo'] == 'Alimentação']
    st.dataframe(df1[colunas])
    kit = st.radio('ID Kits Alimentação', df1['ID Kit'].unique().tolist(), horizontal=True)
    if st.button('Incluir Kit Alimentação'):
        if kit not in casais[casal]['id_kit']:
            casais[casal]['id_kit'].append(kit)
            atualizar_json(casais)
        else:
            st.warning('Kit já adiquirido pelo casal.')
    if st.button('Remover Kit Alimentação'):
        if kit in casais[casal]['id_kit']:
            casais[casal]['id_kit'].pop(casais[casal]['id_kit'].index(kit))
            atualizar_json(casais)

with lazer:
    df1 =df[df['Tipo'] == 'Lazer, Cultura e Compras']
    st.dataframe(df1[colunas])
    kit = st.radio('Kit Lazer, Cultura e Compras', df1['ID Kit'].unique().tolist(), horizontal=True)
    
    if st.button('Incluir Kit Lazer, Cultura e Compras'):
        if kit not in casais[casal]['id_kit']:
            casais[casal]['id_kit'].append(kit)
            atualizar_json(casais)
        else:
            st.warning('Kit já adiquirido pelo casal.')
    if st.button('Remover Kit Lazer, Cultura e Compras'):
        if kit in casais[casal]['id_kit']:
            casais[casal]['id_kit'].pop(casais[casal]['id_kit'].index(kit))
            atualizar_json(casais)

with financeiros:
    df1 =df[df['Tipo'] == 'Serviços Financeiros']
    st.dataframe(df1[colunas])
    kit = st.radio('Kit Serviços Financeiros', df1['ID Kit'].unique().tolist(), horizontal=True)
    
    if st.button('Incluir Kit Serviços Financeiros'):
        if kit not in casais[casal]['id_kit']:
            casais[casal]['id_kit'].append(kit)
            atualizar_json(casais)
        else:
            st.warning('Kit já adiquirido pelo casal.')

    if st.button('Remover Kit Financeiros'):
        if kit in casais[casal]['id_kit']:
            casais[casal]['id_kit'].pop(casais[casal]['id_kit'].index(kit))
            atualizar_json(casais)
            
with saude:
    df1 =df[df['Tipo'] == 'Saúde e Beleza']
    st.dataframe(df1[colunas])
    kit = st.radio('Kit Saúde e Beleza', df1['ID Kit'].unique().tolist(), horizontal=True)
    

    if st.button('Incluir Kit Saúde e Beleza'):
        if kit not in casais[casal]['id_kit']:
            casais[casal]['id_kit'].append(kit)
            atualizar_json(casais)
        else:
            st.warning('Kit já adiquirido pelo casal.')
    
    if st.button('Remover Kit Saúde e Beleza'):
        if kit in casais[casal]['id_kit']:
            casais[casal]['id_kit'].pop(casais[casal]['id_kit'].index(kit))
            atualizar_json(casais)

st.markdown('---')
st.subheader('Kits comprados pelo casal')
df_casal = df[df['ID Kit'].apply(lambda x: x in casais[casal]['id_kit'])]
for i in casais[casal]['id_kit']:
    st.markdown(f'{i} - {df_casal[df_casal['ID Kit'] == i]['Nome do Kit'].iloc[0].split('\n')[0]}')