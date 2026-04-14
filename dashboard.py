import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard IA Brasil 2025", layout="wide")

st.title("📊 Análise de Inteligência Artificial no Brasil (2025)")
st.markdown("Monitoramento de produção acadêmica: Técnica, Ética, Epistemologia e Ensino.")

@st.cache_data
def carregar_dados():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SENHA",
        database="projeto_artigos"
    )
    query = "SELECT * FROM ArtigosIA"
    df = pd.read_sql(query, conexao)
    conexao.close()
    return df

df = carregar_dados()

col1, col2 = st.columns(2)

with col1:
    st.header("🏫 Top Instituições")
    df_inst = df[df['instituicao'] != 'Não Informada']
    top_inst = df_inst['instituicao'].value_counts().head(10)
    
    if not top_inst.empty:
        fig, ax = plt.subplots()
        top_inst.plot(kind='barh', ax=ax, color='skyblue')
        ax.set_xlabel("Quantidade de Artigos")
        st.pyplot(fig)
    else:
        st.warning("Ainda não há instituições identificadas no banco.")

with col2:
    st.header("⚖️ Foco da Pesquisa")

    contagem_termos = df['termo_pesquisa'].value_counts()
    
    if not contagem_termos.empty:
        fig2, ax2 = plt.subplots()

        cores = ['#ff9999','#66b3ff','#99ff99', '#ffcc99'] 
        ax2.pie(contagem_termos, labels=contagem_termos.index, autopct='%1.1f%%', 
                startangle=140, colors=cores)
        ax2.axis('equal') 
        st.pyplot(fig2)
    else:
        st.warning("Sem dados de classificação para exibir.")

st.divider()
st.subheader("📋 Tabela de Dados Completa")
st.dataframe(df)