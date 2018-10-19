CREATE DATABASE atm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE pessoa(
    id int(5) AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    idade int(3),
    senha varchar(50) NOT NULL
)

CREATE TABLE atm.cliente(
    id int(5) AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    idade int(3),
    cpf varchar(14),
    senha varchar(50) NOT NULL,
    PRIMARY KEY (id)
)

CREATE TABLE atm.pessoaJuridica(
    cnpj varchar(18) NOT NULL,
    senha varchar(50) NOT NULL,
    PRIMARY KEY (cnpj)
)

CREATE TABLE atm.pessoaFisica(
    cpf varchar(14) NOT NULL,
    senha varchar(50) NOT NULL
    pessoaId int(5),
    PRIMARY KEY (cpf),
    FOREIGN KEY (pessoaId) REFERENCES pessoa(id)
)

