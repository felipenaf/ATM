""" 
    Tratar quantidade de caracteres que o cliente digita
    Implementar de forma correta os try except em todas as classes

"""

from login import Login
from connection import Connection
from pessoa import Pessoa
from pessoaDao import PessoaDao
from contaCorrente import ContaCorrente
from os import system
from funcoes import *
import getpass
import time

msgLogar()
login = input('Login: ')
senha = getpass.getpass('Senha: ')
result = Login.autenticacao(login, senha)

while result != True:
    print("\nSenha incorreta")
    time.sleep(2)
    msgLogar()
    login = input('Login: ')
    senha = getpass.getpass('Senha: ')
    result = Login.autenticacao(login, senha)
else:
    user = PessoaDao.getByLoginSenha(login, senha)    
    while user[1] == 'admin' and user[2] == 'admin':
        msgAdmin('Administrador')
        teclado = ''
        opc = inputOpc(teclado, 'Administrador', 5, msgAdmin)

        if opc == '1':
            p = Pessoa()
            print('\nDados do cliente: \n')
            p.setLogin(input('Login: '))
            p.setSenha(getpass.getpass('Senha: '))
            
            p.setNome(input('Nome: '))
            p.setTipo(input('Tipo de documento ("PF" ou "PJ"): '))
            p.setDocumento(input('Número do documento: '))

            confirmar = input('\nDigite <enter> pra confirmar ou "q" para cancelar ')
            if (confirmar != 'q'):
                pDao = PessoaDao()
                pDao.cadastrar(p)
            else:
                print('\nOperação cancelada !!')
                time.sleep(2)

        elif opc == '2':
            pDao = PessoaDao()
            result = pDao.listar()
            print('\n')
            for linha in result:                
                print('\tNome         : ', linha[3], '\n', 
                    '\tTipo         : ', linha[5], '\n', 
                    '\tNr documento : ', linha[6], '\n',
                    '\tLogin        : ', linha[1], '\n')
            input("Pressione <enter> para voltar")
                
        elif opc == '3':
            pDao = PessoaDao()
            result = pDao.listar()
            print('\n')
            for linha in result:                
                print('\tID           : ', linha[0], '\n',
                    '\tNome         : ', linha[3], '\n', 
                    '\tTipo         : ', linha[5], '\n', 
                    '\tNr documento : ', linha[6], '\n',
                    '\tLogin        : ', linha[1], '\n')
            
            p = Pessoa()
            p.setId(input('Informe o id do usuário a ser excluído: '))
            if p.getId() != '':
                pDao.excluir(p)
            else:
                print('Não foi informado nenhum valor !!')

        elif opc == '4':
            pass
        elif opc == '5':
            print('\nEncerrando seção ...')
            time.sleep(2)
            quit()
    else:
        result = Login.autenticacao(login, senha)
        
    
        user = PessoaDao.getByLoginSenha(login, senha)

        msgBemVindo(user[2])
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


