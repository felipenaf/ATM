from os import system
import getpass

def msgBemVindo():
  print ("""\t\t\t## Bem vindo ao Caixa Eletronico ##
        \t\t###################################
        \t\t### 1 ## Deposito.              ###
        \t\t### 2 ## Saque.                 ###
        \t\t### 3 ## Saldo.                 ###
        \t\t### 4 ## Sair.                  ###
        \t\t###################################
      """)

def msgLogar():

  system("clear")

  print ("""\t\t\t## Bem vindo ao Caixa Eletronico ##
        \t\t###################################
        \t\t###      Informe seu Login      ###
        \t\t###              e              ###
        \t\t###            Senha            ###
        \t\t###################################
      """)

def loginSenha(self, login, senha):
  self.login = login
  self.senha = senha
  
