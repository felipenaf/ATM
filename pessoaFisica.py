from pessoa import Pessoa

class PessoaFisica(Pessoa):

    __cpf = ''
    __nome = ''
    
    def setCpf(self, cpf):
        self.__cpf = cpf

    def getCpf(self):
        return self.__cpf

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
