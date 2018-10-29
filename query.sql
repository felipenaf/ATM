CREATE DATABASE atm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE atm.pessoa(
    id int(5) AUTO_INCREMENT,
    login VARCHAR(50) NOT NULL,
    senha varchar(50) NOT NULL,
    UNIQUE (login),
    PRIMARY KEY (id)
);

CREATE TABLE atm.pessoaFisica(
    cpf varchar(14) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    idPessoa int(5) NOT NULL,
    PRIMARY KEY (cpf),
    FOREIGN KEY (idPessoa) REFERENCES atm.pessoa(id)
)

CREATE TABLE atm.pessoaJuridica(
    cnpj varchar(18) NOT NULL,
    razaoSocial VARCHAR(50) NOT NULL,
    idPessoa int(5) NOT NULL,
    PRIMARY KEY (cnpj),
    FOREIGN KEY (idPessoa) REFERENCES atm.pessoa(id)
)


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

