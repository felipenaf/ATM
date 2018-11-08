from os import system
import getpass
import time

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

def isFloat(value):
  try:
    float(value)
  except ValueError:
    return False
  return True

def inputOpc(teclado, user, qtdOpc, msg):
  while (isInt(teclado) == False) or (int(teclado) > qtdOpc) or (int(teclado) <= 0):
    if teclado != '':
      print('Digite uma opção válida!')
    teclado = input('Opção: ')
  else:
    return teclado

def inputFloat(teclado):
  while (isFloat(teclado) == False):
    if teclado != '':
      print('Digite um número!')
    teclado = input("Informe um valor a ser sacado: ")
  else:
    return float(teclado) 

def inputValor(teclado):
    while (isFloat(teclado) == False):
      print('\nInforme um número válido')
      teclado = input('\nValor a ser sacado: ')
    else:
      return teclado
    
