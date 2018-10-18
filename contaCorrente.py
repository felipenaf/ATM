""" Classe Pessoa """

class ContaCorrente(object):
    """ Classe Pessoa """

    __numero = ''
    __agencia = ''
    __saldo = 0

    def setNr(self, numero):
        """ Setar o número da conta """
        
        self.__numero = numero

    def getNr(self):
        """ Setar o número da conta """

        return self.__numero

    def setAgencia(self, agencia):
        """ Setar o número da agência """

        self.__agencia = agencia

    def getAgencia(self):
        """ Pegar o número da agência """

        return self.__agencia

    def getSaldo(self):
        """ Pegar o saldo """

        return self.__saldo

    def sacar(self, valor):
        """ Sacar o dinheiro """
        
        if valor <= 0:
            print('Informe um valor a ser sacado')
        elif self.__saldo < valor or self.__saldo <= 0:
            print('Você não tem saldo suficiente para realizar o saque')
        else:
            self.__saldo -= valor

    def depositar(self, valor):
        """ Depositar o dinheiro """

        if valor > 0:
            self.__saldo += valor
        else:
            print('Informe um valor a ser depositado')
