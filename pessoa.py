from contaCorrente import ContaCorrente
""" import de bibliotecas """

class Pessoa(object):
    """ Classe Pessoa """

    __id = 0
    __nome = ''
    __idade = 0
    __senha = ''

    # """ Construtor / Aceita vazio ou os dois valores preenchidos"""
    # def __init__(self, nome = None, idade = None):
    #     if (nome is not None) and (idade is not None):
    #         self.__nome = nome
    #         self.__idade = idade
    def setId(self, id):
        """ Setar o id """
        self.__id = id

    def setNome(self, nome):
        """ Setar o nome """
        self.__nome = nome

    def setIdade(self, idade):
        """ Setar a idade """
        self.__idade = idade

    def setSenha(self, senha):
        """ Setar a senha """
        self.__senha = senha

    def getId(self):
        """ Pegar o id """
        return self.__id

    def getNome(self):
        """ Pegar o nome """
        return self.__nome

    def getIdade(self):
        """ Pegar a idade """
        return self.__idade

    def getSenha(self):
        return self.__senha
