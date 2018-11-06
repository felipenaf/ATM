"""
    Tratar quantidade de caracteres que o cliente digita !! TARTAR ESSE ERRO
    
    Implementar de forma correta os try except em todas as classes

    Só aparecer a confirmação de exclusão caso o id exista no banco !! TARTAR ESSE ERRO

    Editar pendente

    Quando deixa o float(input()) vazio da erro !! TARTAR ESSE ERRO

    salvar no banco de dados palavras todas minusculas

    ref: https://wiki.python.org.br/GeradorDeCpf
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
import gerador

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
    """ Usuário Administrador """
    user = PessoaDao.getByLoginSenha(login, senha)    
    while user[1] == 'admin' and user[2] == 'admin':
        msgAdmin('Administrador')
        teclado = ''
        opc = inputOpc(teclado, 'Administrador', 5, msgAdmin)

        if opc == '1':
            p = Pessoa()
            c = ContaCorrente()
            print('\nDados do cliente: \n')
            p.setNome(input('Nome: '))
            p.setLogin(input('Login: '))
            p.setSenha(getpass.getpass('Senha: '))
            p.setTipo(input('Tipo de pessoa ("PF" ou "PJ"): '))
            p.setDocumento(input('Número do documento: '))
            c.setNumeroAgencia(input('Agência: '))
            c.setNumeroCC(gerador.nrConta())
            c.depositar(float(input('Informar valor a ser inserido na conta: ')))

            confirmar = input('\nDigite <enter> pra confirmar ou "q" para cancelar ')
            if (confirmar != 'q'):
                pDao = PessoaDao()
                pDao.cadastrar(p, c)
            else:
                print('\nOperação cancelada !!')
                time.sleep(2)

        elif opc == '2':
            pDao = PessoaDao()
            result = pDao.listar()
            print('\n')
            for linha in result:
                print('\tNome     : ', linha[3], '\n', 
                    '\tTipo     : ', linha[5], '\n', 
                    '\tDocumento: ', linha[6], '\n',
                    '\tLogin    : ', linha[1], '\n',
                    '\tAgência  : ', linha[11], '\n',
                    '\tC/C      : ', linha[9], '\n')
            input("Pressione <enter> para voltar")
                
        elif opc == '3':
            pDao = PessoaDao()
            result = pDao.listar()
            print('\n')
            for linha in result:
                print('\tID       : ', linha[0], '\n',
                    '\tNome     : ', linha[3], '\n', 
                    '\tTipo     : ', linha[5], '\n', 
                    '\tDocumento: ', linha[6], '\n',
                    '\tLogin    : ', linha[1], '\n',
                    '\tAgência  : ', linha[11], '\n',
                    '\tC/C      : ', linha[9], '\n')
            
            p = Pessoa()
            p.setId(input('Informe o id do usuário a ser excluído: '))
            if p.getId() != '':
                pDao.excluir(p)
            else:
                print('\nNão foi informado nenhum valor !!')
                time.sleep(2)

        elif opc == '4':
            pass
        elif opc == '5':
            print('\nEncerrando seção ...')
            time.sleep(2)
            quit()
    else:
        """ Usuário Comum """
        teclado = ''
        result = Login.autenticacao(login, senha)
        user = PessoaDao.getByLoginSenha(login, senha)

        while result == True:
            msgBemVindo(user[3])
            opc = inputOpc(teclado, user[3], 4, msgBemVindo)
            

            if opc == '1':
                pass

            elif opc == '2':
                c = ContaCorrente()
                saldo = c.setSaldo(user[10])
                teclado = ''
                vl = inputValor(teclado)
                ''' parei aqui !!! '''
                sacado = c.sacar(vl)

                if(sacado == True):
                    print('\nSaque realizado com sucesso')
                    print('\nAgora seu saldo é de R$', c.getSaldo())

                input()



            elif opc == '3':
                print('\nSeu saldo em conta é de R$', user[10])
                input('\nPressione <enter> para voltar')

            elif opc == '4':
                print('\nEncerrando seção ...')
                time.sleep(2)
                quit()

        



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


