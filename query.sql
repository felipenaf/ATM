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
    UNIQUE (numero),
    PRIMARY KEY (id),
    FOREIGN KEY (idPessoa) REFERENCES atm.pessoa (id)
);

CREATE TABLE atm.contaCorrente (
    id int(5) AUTO_INCREMENT,
    numero VARCHAR(11) NOT NULL,
    saldo float(18,2) NOT NULL,
    agencia char(4) NOT NULL,
    idPessoa int(5) NOT NULL,
    UNIQUE (numero),
    PRIMARY KEY (id),
    FOREIGN KEY (idPessoa) REFERENCES atm.pessoa (id)
);

INSERT INTO atm.pessoa (login, senha, nome) VALUES ('admin', 'admin', 'Administrador');