from pessoa import Pessoa

class PessoaJuridica(Pessoa):

    __cnpj = ''
    __razaoSocial = ''
    
    # def __init__(self, cpf=None, nome=None, idade=None):
    #     super().__init__(nome, idade)
    #     self.__cpf = cpf

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    def getCnpj(self):
        return self.__cnpj

    def setRazaoSocial(self, razaoSocial):
        self.__razaoSocial = razaoSocial

    def getRazaoSocial(self):
        return self.__razaoSocial
