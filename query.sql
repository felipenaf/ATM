CREATE DATABASE atm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE pessoa(
    id int(5) AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    idade int(3)
)

CREATE TABLE pessoaFisica(
    cpf varchar(14) NOT NULL,
    pessoaId int(5),
    PRIMARY KEY (cpf),
    FOREIGN KEY (pessoaId) REFERENCES pessoa(id)
)

CREATE TABLE pessoaJuridica(
    cnpj varchar(18) NOT NULL,
    pessoaId int(5),
    PRIMARY KEY (cpf),
    FOREIGN KEY (pessoaId) REFERENCES pessoa(id)
)

