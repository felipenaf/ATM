from contaCorrente import ContaCorrente
""" import de bibliotecas """

class Pessoa(object):
    """ Classe Pessoa """

    __id = 0
    __login = ''
    __senha = ''

    # """ Construtor / Aceita vazio ou os dois valores preenchidos"""
    # def __init__(self, nome = None, idade = None):
    #     if (nome is not None) and (idade is not None):
    #         self.__nome = nome
    #         self.__idade = idade
    
    def setId(self, id):
        """ Setar o id """
        self.__id = id

    def setLogin(self, login):
        """ Setar o login """
        self.login = login

    def setSenha(self, senha):
        """ Setar a senha """
        self.__senha = senha

    def getId(self):
        """ Pegar o id """
        return self.__id

    def getLogin(self):
        """ Pegar o login """
        return self.__login

    def getSenha(self):
        return self.__senha
