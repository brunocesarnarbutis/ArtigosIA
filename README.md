# ArtigosIA
Análise de dados de produção científica em IA

Este projeto utiliza **Python** e **SQL** para monitorar a produção acadêmica brasileira sobre Inteligência Artificial, com foco em classificar os artigos entre recortes Técnicos, Éticos, Epistemológicos e de Ensino.

Objetivo do Projeto
Unir a reflexão crítica da Filosofia com a automação da Engenharia de Dados para entender: *Sobre o que o Brasil está pesquisando quando o assunto é IA em 2025?*

Tecnologias Utilizadas
- **Python:** Extração, limpeza e classificação semântica (Keyword Matching) dos dados consumidos via API global do Crossref.
- **MySQL:** Armazenamento dos metadados extraídos.
- **Streamlit e Pandas:** Construção de um Dashboard interativo para análise de tendências e geração de insights visuais.

Desafios e Soluções
- **Soberania de Dados:** Implementação de filtros linguísticos rigorosos para isolar a produção nacional em um oceano de dados internacionais.
- **Tratamento de Metadados:** Gestão de "Data Completeness" para lidar com afiliações institucionais ausentes em publicações recentes.
