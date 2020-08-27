# ATM

# Sobre
Simulação de um caixa eletrônico, com usuario master e usuários comuns que podem depositar, sacar, ver o saldo e ver seus dados cadastrais

# Iniciando
## Pré-requisitos
- `Python 3.6`
- `pip3`
- `Mysql`

# Instalação
- ## 1. Clonar o repositório
  `git clone https://github.com/felipenaf/ATM`
- ## 2. Instalar o pip
  [Nesse Link](https://pypi.org/project/pip/)
- ## 3. Atualização do setuptools e instalação de libs
  `pip3 install --upgrade setuptools`

  `pip3 install mysql-connector`
- ## 5. Criação e configuração da base de dados
  `mysql -u usuario_mysql -psenha < query.sql`
  **(Na raiz do projeto)**

  **Configurar o arquivo `connection.py`** com os dados da base.

## Observação
  - **Login e senha padrão** 
  
    **login**: admin
  
    **senha**: admin

# Extras

## Classes 
- Pessoa
- PessoaDao
- Conta Corrente
- Conexão
- Login
