import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl


# Configuração da página
st.set_page_config(page_title="Tabela Acidentes", layout="wide")


def carregar_dados(path):
    acidentes_bruto = pd.read_excel(path, header=None)
    
    #somente configuração de planilha
    dia_semana = acidentes_bruto.iloc[3:36, 0:10].copy()


    # tudo que precisa conter dentro da lista 
    dia_semana.columns = [
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira",
        "sábado",
        "domingo"
    ]
    
    # Tira espaços extra dos nome de estados e regiões
    dia_semana["Dias da semana"] = dia_semana["Dias da semana"].astype(str).str.strip()


    # faz com que os valores sejam transformados Int
    colunas_numericas = dia_semana.columns.drop("Dias da semana")
    for coluna in colunas_numericas:
        dia_semana[coluna] = pd.to_numeric(dia_semana[coluna], errors="coerce")


    # Retorna a tabela pra ser usada no resto do código
    return dia_semana
path = "acidentes.xlsx"   

acidentes = ["acidentes.xlsx"]

# Cria uma lista que tem os nomes dos estados, pra isso tira da planilha Brasil e regiões
acidentes_bruto = ["Brasil"] + acidentes

st.title("TABELA ACIDENTES")
st.header("Soma total de acidentes de cada dia")

st.sidebar.divider()
acidentes_bruto = st.sidebar.selectbox(
    "Dias da semana",
    ["Todos", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
)