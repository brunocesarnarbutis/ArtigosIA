DROP DATABASE IF EXISTS projeto_artigos;
CREATE DATABASE projeto_artigos;
USE projeto_artigos;
CREATE TABLE ArtigosIA (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(500),
    autor_principal VARCHAR(255),
    instituicao VARCHAR(255),
    revista_editora VARCHAR(255), 
    mes_publicacao INT,
    termo_pesquisa VARCHAR(100)  
);