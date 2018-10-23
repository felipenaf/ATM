""" import de libs """
import mysql.connector

class Connection(object):
    """ Classe Connection """

    @classmethod
    def instance(self):
        """ Instanciar conexão do banco, passando usuario e senha como parâmetro"""
        connection = mysql.connector.connect(
            user='felipe',
            password='123',
            host='127.0.0.1',
            database='atm')
        return connection
