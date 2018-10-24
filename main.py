from login import Login
from cliente import Cliente
from connection import Connection
from clienteDao import ClienteDao
from contaCorrente import ContaCorrente
from os import system
import funcoes
import getpass
import time

funcoes.msgLogar()
login = input('Login: ')
senha = getpass.getpass('Senha: ')
result = Login.autenticacao(login, senha)

while result != True:
    print("\nSenha incorreta")
    time.sleep(2)
    funcoes.msgLogar()
    login = input('Login: ')
    senha = getpass.getpass('Senha: ')
    result = Login.autenticacao(login, senha)
else:
    user = ClienteDao.getByLoginSenha(login, senha)

    if user[1] == 'admin':
        funcoes.msgAdmin(user[2])
        if funcoes.inputOpc(5):
            print ('deu certo')
    else:
        funcoes.msgBemVindo(user[2])
        print(user)


# c = Cliente()
# c.setNome('felipe')
# cDao = ClienteDao()
# cDao.cadastrar(c)
    

# CON = Connection.instance('felipe', '123')
# CURSOR = CON.cursor()

# query = "SELECT COUNT(*) FROM cliente WHERE nome = %s and senha = %s;"
# info = (login, senha)

# resultado = CURSOR.execute(query, info)

# resultado = ("%s" % CURSOR.fetchone())

# while (resultado != '1'):
#     print("\nSenha incorreta")
#     time.sleep(3)
#     msgLogar()
#     login = input('Login: ')
#     senha = getpass.getpass('Senha: ')
# else:
#     print('oi')
    
# if (resultado == '1'):
#     print ("Bem vindo", login, "!")
# else:
#     msgLogar()

# CON.commit()
# print(CURSOR.rowcount, "record inserted.")
# CON.close()


# if login != 1:
#     print('Opção inválida')
# else:
#     print('Boa meninão')

# p = Cliente()
# p.setCpf('147')
# p.setNome('bipao')
# p.setIdade(25)
# p.setSenha('123')

# print(p.getCpf())
# print(p.getNome())
# print(p.getIdade())
# print(p.getSenha())

# query = "INSERT INTO cliente (nome, idade, cpf, senha) VALUES (%s, %s, %s, %s);"
# info = (p.getNome(), p.getIdade(), p.getCpf(), p.getSenha())

# p.depositar(5)
# p.sacar(2)
# print(p.getSaldo())

# cc = ContaCorrente()
# print (cc.getSaldo())



# CURSOR.execute("DROP TABLE pessoaFisica;")

# CURSOR.execute(
#     "CREATE TABLE pessoaFisica("
#     "cpf VARCHAR(50) NOT NULL PRIMARY KEY,"
#     "nome varchar(50),"
#     "idade INT(5)"
#     ");"
# )


