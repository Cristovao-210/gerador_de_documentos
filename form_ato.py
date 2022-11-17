import streamlit as st
from functions import*
from documentos import*
import datetime as dt

# dicionário para guardar informações do ato
dados_ato = {}
lista_de_cargos = ["","Professor do Magistério Superior", "Assistente em Administração","Outro"]
hoje = dt.date.today() # data do dia para pegar o ano
ato_gerado = []

# Título do formulário
nome_documento = "Ato de Vacância"
st.title(f'{nome_documento}')
# Formulário para inserir informações no ato
with st.form("ato_vacancia", clear_on_submit=True):
    dados_ato['numero_ato'] = st.number_input(label="Número do Ato", format="%d", step=1, min_value=None)
    dados_ato['data_vacancia'] = st.date_input("Data da vacância")
    # colocando a data em um formato amigável (Brasil)
    dados_ato['data_vacancia'] = data_format_br(dados_ato['data_vacancia'])
    # dados_ato['cargo'] = st.selectbox("Selecione o cargo",lista_de_cargos)
    dados_ato['codigo_vaga'] = st.number_input(label="Código de vaga", format="%d", step=1, min_value=None)
    dados_ato['cargo'] = st.text_input(label="Cargo",placeholder="Informe o cargo")
    dados_ato["nome_servidor"] = st.text_input(label="Nome", placeholder="Nome do Servidor")
    dados_ato['numero_sei'] = st.text_input(label="Processo SEI", placeholder="Número do processo SEI da vacância")
    dados_ato['lotacao_servidor'] = st.text_input(label="Lotação", placeholder="Lotação do Servidor")
    st.write("")
    submitted = st.form_submit_button("Avançar")

if submitted:
    ato_gerado = gerar_ato(dados_ato)
    with open(ato_gerado[1], "rb") as file:
        # Como baixar documento gerado
        btn = st.download_button(
                    label="Gerar Ato",
                    data=file,
                    file_name=ato_gerado[1],
                    mime="text/html"
    )
        


