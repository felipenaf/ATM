""" import de libs """
import mysql.connector

""" Classe Connection """
class Connection(object):
    
    """ Instanciar conexão do banco """
    def instance(self, usuario, senha):
        connection = mysql.connector.connect(
            user=usuario,
            password=senha,
            host='127.0.0.1',
            database='atm')
        return connection
