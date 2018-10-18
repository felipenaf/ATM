""" import de bibliotecas """

class Pessoa(object):
    """ Classe Pessoa """

    # """ Construtor / Aceita vazio ou os dois valores preenchidos"""
    # def __init__(self, nome = None, idade = None):
    #     if (nome is not None) and (idade is not None):
    #         self.__nome = nome
    #         self.__idade = idade

    """ Setar o nome """
    def setNome(self, nome):
        self.__nome = nome

    """ Setar a idade """
    def setIdade(self, idade):
        self.__idade = idade

    """ Pegar o nome """
    def getNome(self):
        return self.__nome

    """ Pegar a idade """
    def getIdade(self):
        return self.__idade
