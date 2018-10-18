from connection import Connection
from pessoaFisica import PessoaFisica
from contaCorrente import ContaCorrente

class Login(object):

    def validaLogin(self, login, senha):

        query = 'SELECT * FROM pessoaFisica where cpf = %s and senha = %s'
        query2 = 'SELECT * FROM pessoaJuridica where cnpj = %s and senha = %s'
        info = (login, senha)

        con = Connection.instance('felipe', '123')
        cursor = con.cursor()

        cursor.execute(query, info)
       
        con.close()
