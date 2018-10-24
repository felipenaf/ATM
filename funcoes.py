from os import system
import getpass

def msgBemVindo(nome):
      
  system("clear")

  print ("""\t\t\t## Bem vindo Sr(a).""", nome, """
        \t\tEscolha uma das opções a seguir
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

def msgAdmin(nome):
      
  system("clear")

  print ("""\t\t\t## Bem vindo Sr(a).""", nome, """
            \t\tEscolha uma das opções a seguir
            \t\t###################################
            \t\t### 1 ## Cadastrar              ###
            \t\t### 2 ## Consultar              ###
            \t\t### 3 ## Excluir                ###
            \t\t### 4 ## Editar                 ###
            \t\t### 5 ## Sair                   ###
            \t\t###################################
        """)

def isInt(value):
  try:
    int(value)
  except ValueError:
    return False
  return True

def inputOpc(numero):
  
  while isInt(input('Escolha uma opção: ')) == False:
    print('Digite apenas números inteiros ou ')
  else:
    True
