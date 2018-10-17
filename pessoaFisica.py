from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade):
        super().__init__(nome, idade)
        self.cpf = cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_cpf(self):
        return self.cpf
