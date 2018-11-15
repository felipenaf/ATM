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
    print("\nLogin ou senha incorretos")
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
        opc = inputOpc(5, msgAdmin)

        if opc == '1':
            
            print('\nDados do cliente:\n')
            p.setNome(validaInput("Nome: ",5, "O nome deve possuir no mínimo 5 caracteres!").lower())
            p.setLogin(validaInput("Login: ", 5, "O login deve possuir no mínimo 5 caracteres!"))
            p.setSenha(validaSenha("Senha: ", 3, "A senha deve possuir no mínimo 3 caracteres!"))
            p.setTipo(validaTipoPessoa('Tipo de pessoa ("PF" ou "PJ"): ', 'Informe "PF" ou "PJ" !!').lower())
            if p.getTipo() == 'pf':
                p.setDocumento(validaCpf("CPF: "))
            else:
                p.setDocumento(validaCnpj("CNPJ: "))
            c.setAgencia(validaAgencia("Agência: ", "Agência possui apenas 4 números"))
            c.setNumeroCC(gerador.nrConta())
            c.setSaldo(inputFloat("Valor inicial da conta: "))

            confirmar = input('\nDigite <enter> pra confirmar ou "c" para cancelar ')

            if (confirmar != 'c'):
                pDao.cadastrar(p, c)
            else:
                print('\nOperação cancelada !!')
                voltar()

        elif opc == '2':
            result = pDao.listar()
            print('\n')
            for linha in result:
                print('\tID       : ', linha[0], '\n',
                    '\tNome     : ', linha[3].title(), '\n', 
                    '\tTipo     : ', linha[5].upper())
                if linha[5] == 'pf':
                    print('\tCPF      : ', linha[6])
                else:
                    print('\tCNPJ     : ', linha[6])
                print('\tLogin    : ', linha[1], '\n',
                    '\tAgência  : ', linha[11], '\n',
                    '\tC/C      : ', linha[9], '\n')
            voltar()
                
        elif opc == '3':
            print("\nExcluir registro")

            p.setId(input('Id cliente: '))

            idVerificado = pDao.getById(p.getId())
            if idVerificado == None or p.getId() == '1' or p.getId() == '':
                print('\nUsuário informado não existe em nosso banco de dados!!')
                voltar()
            else:
                pDao.excluir(p)

        elif opc == '4':
            print("\nAtualizar registro")

            p.setId(input('Id cliente: '))

            idVerificado = pDao.getById(p.getId())

            if idVerificado == None or p.getId() == '1' or p.getId() == '':
                print('\nUsuário informado não existe em nosso banco de dados!!')
                voltar()
            else:
                p.setId(idVerificado[0])
                p.setLogin(idVerificado[1])
                p.setSenha(idVerificado[2])
                c.setAgencia(idVerificado[11])

                print("\nLogin atual:",p.getLogin())
                decisao = input("Deseja alterar o login? (s ou n) ")
                if decisao == 's':
                    p.setLogin(validaInput("Novo login: ", 5, "O login deve possuir no mínimo 5 caracteres!"))

                decisao = input("\nDeseja alterar a senha? (s ou n) ")
                if decisao == 's':
                    senha = validaSenha("Senha Atual: ", 3, "A senha deve ter mais que três caracteres!")
                    if senha == p.getSenha():
                        p.setSenha(validaSenha("Nova senha: ", 3, "A senha deve ter mais que três caracteres!"))
                    else:
                        print("Senha incorreta!")

                print("\nAgência atual:",c.getAgencia())
                decisao = input("Deseja alterar a agência? (s ou n) ")
                if decisao == 's':
                    c.setAgencia(validaAgencia("Nova agência: ", "Agência possui apenas 4 números"))

                pDao.editar(p, c)

        elif opc == '5':
            print('\nEncerrando seção ...')
            time.sleep(2)
            quit()
    else:
        """ Usuário Comum """
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
            opc = inputOpc(5, msgBemVindo)
            
            if opc == '1':
                vl = inputFloat("Valor do deposito: ")
                depositado = c.depositar(vl)
                if depositado == True:
                    pDao.atualizaSaldo(c, "Depósito")

            elif opc == '2':
                vl = inputFloat("Valor do saque: ")
                sacado = c.sacar(vl)
                if sacado == True:
                    pDao.atualizaSaldo(c,"Saque")

            elif opc == '3':
                print('\nSeu saldo em conta é de R$', c.getSaldo())
                voltar()

            elif opc == '4':
                print("\nMeus Dados\n")

                print('\tID       : ', user[0], '\n',
                    '\tNome     : ', user[3].title(), '\n', 
                    '\tTipo     : ', user[5].upper())
                if user[5] == 'pf':
                    print('\tCPF      : ', user[6])
                else:
                    print('\tCNPJ     : ', user[6])
                print('\tLogin    : ', user[1], '\n',
                    '\tAgência  : ', user[11], '\n',
                    '\tC/C      : ', user[9], '\n')
                
                voltar()

            elif opc == '5':
                print('\nEncerrando seção ...')
                time.sleep(2)
                quit()
