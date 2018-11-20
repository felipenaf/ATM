""" import de libs """
from funcoes import voltar

class ContaCorrente(object):
    """ Classe ContaCorrente """

    __numeroCC = ''
    __saldo = 0
    __agencia = ''
    __idPessoa = 0

    '''
        ### 
        GET 
        ### 
    '''
    
    def getNumeroCC(self):
        """ Setar o número da conta """
        return self.__numeroCC

    def getSaldo(self):
        """ Pegar o saldo """
        return self.__saldo

    def getAgencia(self):
        """ Pegar o numero da agência """
        return self.__agencia

    def getIdPessoa(self):
        return self.__idPessoa

    '''
        ### 
        SET 
        ### 
    '''

    def setNumeroCC(self, numeroCC):
        """ Setar o número da conta """
        self.__numeroCC = numeroCC

    def setAgencia(self, agencia):
        """ Setar o número da agência """
        self.__agencia = agencia

    def setSaldo(self, saldo):
        """ Setar o saldo """
        self.__saldo = saldo

    def setIdPessoa(self, idPessoa):
        self.__idPessoa = idPessoa

    '''
        ### 
        DEMAIS
        ### 
    '''

    def sacar(self, valor):
        """ Sacar o dinheiro """
        
        if valor <= 0:
            print('\nInforme um valor maior que zero')
            voltar()
        elif self.__saldo < valor or self.__saldo <= 0:
            print('\nVocê não tem saldo suficiente para realizar o saque')
            voltar()
        else:
            self.__saldo -= valor
            return True

    def depositar(self, valor):
        """ Depositar o dinheiro """

        if valor > 0:
            self.__saldo += valor
            return True
        else:
            print('\nInforme um valor maior que zero')
            voltar()
