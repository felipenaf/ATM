""" import de libs """

class ContaCorrente(object):
    """ Classe ContaCorrente """

    __numeroCC = ''
    __saldo = 0
    __status = False

    def setNumeroCC(self, numeroCC):
        """ Setar o número da conta """
        
        self.__numeroCC = numeroCC

    def getNumeroCC(self):
        """ Setar o número da conta """

        return self.__numeroCC

    def setStatus(self, status):
        """ Setar o número da agência """

        self.__status = status

    def getStatus(self):
        """ Pegar o número da agência """

        return self.__status

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
