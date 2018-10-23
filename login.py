from connection import Connection
from cliente import Cliente

class Login(object):

    __login = ''
    __senha = ''

    @classmethod
    def autenticacao(self, login, senha):
        self.login = login
        self.senha = senha
        con = Connection.instance()
        cursor = con.cursor()
        query = "SELECT COUNT(*) FROM cliente WHERE cpf = %s and senha = %s;"
        cursor.execute(query, (self.login, self.senha))
        resultado = ("%s" % cursor.fetchone())
        con.close()

        if resultado == '1':
            return True
        else:
            return False
