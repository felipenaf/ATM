DROP DATABASE IF EXISTS atm;

CREATE DATABASE atm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE atm.pessoa (
    id int(5) AUTO_INCREMENT,
    login VARCHAR(50) NOT NULL,
    senha varchar(50) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    UNIQUE (login),
    PRIMARY KEY (id)
);

CREATE TABLE atm.documento (
    id int(5) AUTO_INCREMENT,
    tipo VARCHAR(2) NOT NULL,
    numero varchar(18) NOT NULL,
    idPessoa int(5) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (idPessoa) REFERENCES atm.pessoa (id)
);

CREATE TABLE atm.contaCorrente (
    id int(5) AUTO_INCREMENT,
    numero VARCHAR(11) NOT NULL,
    saldo float(18,2) NOT NULL,
    agencia int(4) NOT NULL,
    idPessoa int(5) NOT NULL,
    UNIQUE (numero),
    PRIMARY KEY (id),
    FOREIGN KEY (idPessoa) REFERENCES atm.pessoa (id)
);

INSERT INTO atm.pessoa (login, senha, nome) VALUES ('admin', 'admin', 'Administrador');

-- CREATE TABLE atm.pessoaFisica(
--     cpf varchar(14) NOT NULL,
--     nome VARCHAR(50) NOT NULL,
--     idPessoa int(5) NOT NULL,
--     PRIMARY KEY (cpf),
--     FOREIGN KEY (idPessoa) REFERENCES atm.pessoa(id)
-- )

-- CREATE TABLE atm.pessoaJuridica(
--     cnpj varchar(18) NOT NULL,
--     razaoSocial VARCHAR(50) NOT NULL,
--     idPessoa int(5) NOT NULL,
--     PRIMARY KEY (cnpj),
--     FOREIGN KEY (idPessoa) REFERENCES atm.pessoa(id)
-- )

-- select * from atm.pessoaFisica 
-- inner join 
--     atm.pessoa 
-- on
--     atm.pessoaFisica.idPessoa = atm.pessoa.id
-- where
--     cpf = '402' and senha = '123';

-- CREATE TABLE pessoa(
--     id int(5) AUTO_INCREMENT PRIMARY KEY,
--     nome VARCHAR(50) NOT NULL,
--     idade int(3),
--     senha varchar(50) NOT NULL
-- )

-- CREATE TABLE atm.pessoaJuridica(
--     cnpj varchar(18) NOT NULL,
--     senha varchar(50) NOT NULL,
--     PRIMARY KEY (cnpj)
-- )

-- CREATE TABLE atm.pessoaFisica(
--     cpf varchar(14) NOT NULL,
--     senha varchar(50) NOT NULL
--     pessoaId int(5),
--     PRIMARY KEY (cpf),
--     FOREIGN KEY (pessoaId) REFERENCES pessoa(id)
-- )