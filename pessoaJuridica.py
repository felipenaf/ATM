from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    
    # def __init__(self, cnpj=None, nome=None, idade=None):
    #     super().__init__(nome, idade)
    #     self.__cnpj = cnpj

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    def getCnpj(self):
        return self.__cnpj
