from pessoa import Pessoa

class PessoaFisica(Pessoa):

    __cpf = ''
    __nome = ''
    
    # def __init__(self, cpf=None, nome=None, idade=None):
    #     super().__init__(nome, idade)
    #     self.__cpf = cpf

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getCpf(self):
        return self.__cpf

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
