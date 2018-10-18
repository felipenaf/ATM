""" import de libs """
import mysql.connector

class Connection(object):
    """ Classe Connection """

    @classmethod
    def instance(self, usuario, senha):
        """ Instanciar conexão do banco, passando usuario e senha como parâmetro"""
        connection = mysql.connector.connect(
            user=usuario,
            password=senha,
            host='127.0.0.1',
            database='atm')
        return connection
