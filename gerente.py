from pessoa import Pessoa

class Gerente(Pessoa):
    
    __login = ''

    def getLogin(self):
        return self.__login

    def setLogin(self, login):
        self.__login = login
