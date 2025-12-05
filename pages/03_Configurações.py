import streamlit as st
import json

st.set_page_config(layout='wide')
st.sidebar.image('logo.png')

with open('casais.json', 'r', encoding='utf-8') as f:
    casais = json.load(f)

def atualizar_json(dicionario):
    with open('casais.json', 'w', encoding='utf-8') as f:
        json.dump(dicionario, f, indent=4, ensure_ascii=False)


adicionar, remover = st.tabs(['Adicionar Casal', 'Remover Casal'])

with adicionar:
    nome_casal = st.text_input('Digite o nome do casal')
    if st.button('Adicionar Casal'):
        if nome_casal not in casais.keys():
            casais[nome_casal] = {'id_kit' : []}
            atualizar_json(casais)
        else:
            st.warning('Casal já existente')

with remover:
    nome_casal = st.radio('Casais', casais.keys(), horizontal=True)
    if st.button('Remover Casal'):
        casais.pop(nome_casal)
        atualizar_json(casais)


