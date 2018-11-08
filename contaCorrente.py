""" import de libs """

class ContaCorrente(object):
    """ Classe ContaCorrente """

    __numeroCC = ''
    __saldo = 0
    __numeroAgencia = ''
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

    def getNumeroAgencia(self):
        """ Pegar o numero da agência """
        return self.__numeroAgencia

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

    def setNumeroAgencia(self, numeroAgencia):
        """ Setar o número da agência """
        self.__numeroAgencia = numeroAgencia

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
            input('\nPressione <enter> para voltar')
        elif self.__saldo < valor or self.__saldo <= 0:
            print('\nVocê não tem saldo suficiente para realizar o saque')
            input('\nPressione <enter> para voltar')
        else:
            self.__saldo -= valor
            return True

    def depositar(self, valor):
        """ Depositar o dinheiro """

        if valor > 0:
            self.__saldo += valor
            return True
        else:
            print('\nInforme um valor a ser depositado')
