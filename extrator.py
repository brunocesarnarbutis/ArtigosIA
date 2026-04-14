import requests
import mysql.connector

print("Iniciando")

# Conexão com o SQL
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SENHA", 
        database="projeto_artigos"
    )
    cursor = conexao.cursor()
    
  
    cursor.execute("TRUNCATE TABLE ArtigosIA")
    print("🧹 Banco de dados limpo para nova coleta.")

except mysql.connector.Error as err:
    print(f"Erro de conexão: {err}")
    exit()

# Filtragem
filtros_brasil = ["brasil", "brazil", "br", "universidade", "usp", "ufrj", "ufmg", "unb", "federal"]

url_api = "https://api.crossref.org/works"
parametros = {

    "query": "inteligência artificial", 
    "filter": "from-pub-date:2025-01-01,until-pub-date:2025-12-31",
    "rows": 1000
}

# Coleta JSON
resposta = requests.get(url_api, params=parametros)
lista_artigos = resposta.json()["message"]["items"]

artigos_salvos = 0

for artigo in lista_artigos:
    titulo = artigo.get("title", ["Sem título"])[0]
    
    revista = artigo.get("publisher", "Não Informada")
    if "container-title" in artigo and len(artigo["container-title"]) > 0:
        revista = artigo["container-title"][0]

    autores = artigo.get("author", [])
    if len(autores) > 0:
        autor_principal = f"{autores[0].get('given', '')} {autores[0].get('family', '')}"
        instituicao = "Não Informada"
        if "affiliation" in autores[0] and len(autores[0]["affiliation"]) > 0:
            instituicao = autores[0]["affiliation"][0].get("name", "Não Informada")
    else:
        autor_principal = "Autor Desconhecido"
        instituicao = "Não Informada"

    mes_publicacao = artigo.get("created", {}).get("date-parts", [[0,0]])[0][1]

    texto_validacao = f"{titulo} {instituicao} {revista}".lower()
    if any(termo in texto_validacao for termo in filtros_brasil):
        
# Temas
        texto_geral = f"{titulo} {revista}".lower()
        termo_pesquisa = "Técnico/Geral"
        
        if any(palavra in texto_geral for palavra in ["ética", "ethics", "moral"]):
            termo_pesquisa = "Ética"
        elif any(palavra in texto_geral for palavra in ["epistemologia", "epistemology", "conhecimento"]):
            termo_pesquisa = "Epistemologia"
        elif any(palavra in texto_geral for palavra in ["ensino", "educação", "education", "aprendizagem", "escola", "professor"]):
            termo_pesquisa = "Ensino/Educação"

        comando_sql = """
        INSERT INTO ArtigosIA (titulo, autor_principal, instituicao, revista_editora, mes_publicacao, termo_pesquisa) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (titulo[:500], autor_principal[:255], instituicao[:255], revista[:255], mes_publicacao, termo_pesquisa)
        
        cursor.execute(comando_sql, valores)
        artigos_salvos += 1
        print(f"✅ Salvo: {titulo[:50]}...")


conexao.commit()
cursor.close()
conexao.close()

print("-" * 50)
print(f" Pronto {artigos_salvos} artigos brasileiros de 2025 foram catalogados.")