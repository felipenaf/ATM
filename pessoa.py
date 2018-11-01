from contaCorrente import ContaCorrente
""" import de bibliotecas """

class Pessoa(object):
    """ Classe Pessoa """

    __id = 0
    __login = ''
    __senha = ''
    __nome = ''
    __tipo = ''
    __documento = ''

    ''' ### '''
    ''' GET '''
    ''' ### '''

    def getId(self):
        """ Pegar o id """
        return self.__id

    def getLogin(self):
        """ Pegar o login """
        return self.__login

    def getSenha(self):
        """ Pegar a senha """
        return self.__senha

    def getNome(self):
        """ Pegar o nome """
        return self.__nome

    def getTipo(self):
        """ Pegar o tipo de pessoa "PF" ou "PJ" """
        return self.__tipo

    def getDocumento(self):
        """ Pegar o número do documento """
        return self.__documento

    ''' ### '''
    ''' SET '''
    ''' ### '''
    
    def setId(self, id):
        """ Setar o id """
        self.__id = id

    def setLogin(self, login):
        """ Setar o login """
        self.__login = login

    def setSenha(self, senha):
        """ Setar a senha """
        self.__senha = senha

    def setNome(self, nome):
        """ Setar o nome """
        self.__nome = nome

    def setTipo(self, tipo):
        """ Setar o tipo de pessoa "PF" ou "PJ" """
        self.__tipo = tipo

    def setDocumento(self, documento):
        """ Setar o número do documento """
        self.__documento = documento