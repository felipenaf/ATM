# ATM
Simulação de um caixa eletrônico, com usuario master(responsável pela execução do CRUD) e usuários comuns que podem depositar, sacar, ver o saldo e ver seus dados cadastrais

## Ambiente
- Linux Mint 19 Tara
- Python 3.6
- Mysql

## Ações necessárias:
> Executar os seguintes comandos no terminal:
* sudo apt install python3-pip 
* pip3 install --upgrade setuptools
* pip3 install mysql-connector 
* mysql -u usuario_mysql -psenha < query.sql (Na raiz do projeto)
Ex. mysql -u felipe -p123 < query.sql (Na raiz do projeto)

* Configurar o arquivo connection.py:
-- user='nome_de_usuario_do_banco',
-- password='senha_do_usuario_banco',
-- host='ip_servidor',
-- database='base_de_dados'
Ex.
-- user='felipe',
-- password='123',
-- host='127.0.0.1',
-- database='atm'


## Classes 
- Pessoa
- PessoaDao
- Conta Corrente
- Conexão

## O que falta 

- gerador em funções

- ref: https://wiki.python.org.br/GeradorDeCpf