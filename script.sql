---Script para usar no MySQL e criar o banco de dados e tabela para o projeto---

create database nomes_flask;

USE nomes_flask;

CREATE TABLE nomes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

select * from nomes;