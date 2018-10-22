from connection import Connection
from cliente import Cliente

class Login(object):

    __login = ''
    __senha = ''

    @classmethod
    def autenticacao(self, login, senha):
        self.login = login
        self.senha = senha
        con = Connection.instance('felipe', '123')
        cursor = con.cursor()
        query = "SELECT COUNT(*) FROM cliente WHERE nome = %s and senha = %s;"
        cursor.execute(query, (self.login, self.senha))
        resultado = ("%s" % cursor.fetchone())
        con.close()

        if resultado == '1':
            return True
            return self.login
        else:
            return False
