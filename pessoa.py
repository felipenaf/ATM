""" import de bibliotecas """

class Pessoa(object):
    """ Classe Pessoa """

    def __init__(self, nome, idade):
        """ Construtor """
        self.nome = nome
        self.idade = idade

    def set_nome(self, nome):
        """ Setar o nome """
        self.nome = nome

    def set_idade(self, idade):
        """ Setar a idade """
        self.idade = idade

    def get_nome(self):
        """ Pegar o nome """
        return self.nome

    def get_idade(self):
        """ Pegar a idade """
        return self.idade
