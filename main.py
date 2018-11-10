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

    p = Pessoa()
    c = ContaCorrente()
    pDao = PessoaDao()

    while user[1] == 'admin' and user[2] == 'admin':
        msgAdmin()
        teclado = ''
        opc = inputOpc(teclado, 5, msgAdmin)

        if opc == '1':
            
            print('\nDados do cliente:\n')
            p.setNome(validaInput(teclado,"Nome: ",5, 'Digite um número!'))
            p.setLogin(input('Login: '))
            p.setSenha(getpass.getpass('Senha: '))
            p.setTipo(input('Tipo de pessoa ("PF" ou "PJ"): '))
            p.setDocumento(input('Número do documento: '))
            c.setNumeroAgencia(input('Agência: '))
            c.setNumeroCC(gerador.nrConta())
            c.depositar(inputFloat(teclado, "Valor inicial da conta: "))

            confirmar = input('\nDigite <enter> pra confirmar ou "q" para cancelar ')

            if (confirmar != 'q'):
                pDao.cadastrar(p, c)
            else:
                print('\nOperação cancelada !!')
                time.sleep(2)

        elif opc == '2':
            result = pDao.listar()
            print('\n')
            for linha in result:
                print('\tNome     : ', linha[3].capitalize(), '\n', 
                    '\tTipo     : ', linha[5].upper(), '\n', 
                    '\tDocumento: ', linha[6], '\n',
                    '\tLogin    : ', linha[1], '\n',
                    '\tAgência  : ', linha[11], '\n',
                    '\tC/C      : ', linha[9], '\n')
            input("Pressione <enter> para voltar")
                
        elif opc == '3':
            result = pDao.listar()
            print('\n')
            for linha in result:
                print('\tID       : ', linha[0], '\n',
                    '\tNome     : ', linha[3].capitalize(), '\n', 
                    '\tTipo     : ', linha[5].upper(), '\n', 
                    '\tDocumento: ', linha[6], '\n',
                    '\tLogin    : ', linha[1], '\n',
                    '\tAgência  : ', linha[11], '\n',
                    '\tC/C      : ', linha[9], '\n')
            
            p.setId(input('Informe o id do usuário a ser excluído: '))

            idVerificado = pDao.getById(p.getId())
            if idVerificado == None:
                print('\nUsuário não existe em nosso banco de dados!!')
                input('\nPressione <enter> para voltar')
            elif p.getId() != '':
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

        c = ContaCorrente()
        p = Pessoa()
        pDao = PessoaDao()

        p.setNome(user[3])
        c.setSaldo(user[10])
        c.setIdPessoa(user[0])

        while result == True:
            msgBemVindo(p.getNome())
            opc = inputOpc(teclado, 4, msgBemVindo)
            
            if opc == '1':
                teclado = ''
                vl = inputFloat(teclado, "Informe um valor a ser depositado: ")
                depositado = c.depositar(vl)
                if depositado == True:
                    pDao.atualizaSaldo(c, "Depósito")

            elif opc == '2':
                teclado = ''
                vl = inputFloat(teclado, "Informe um valor a ser sacado: ")
                sacado = c.sacar(vl)
                if sacado == True:
                    pDao.atualizaSaldo(c,"Saque")

            elif opc == '3':
                print('\nSeu saldo em conta é de R$', c.getSaldo())
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


