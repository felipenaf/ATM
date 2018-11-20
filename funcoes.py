from os import system
from getpass import getpass
import time
import random

def msgBemVindo(nome):
      
  system("clear")

  print ("""\t\t\t## Bem vindo """, nome.title(), """
        \t\tEscolha uma das opções a seguir
        \t\t###################################
        \t\t### 1 ## Deposito.              ###
        \t\t### 2 ## Saque.                 ###
        \t\t### 3 ## Saldo.                 ###
        \t\t### 4 ## Meus dados.            ###
        \t\t### 5 ## Sair.                  ###
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

def msgAdmin():
      
  system("clear")

  print ("""\t\t\t## Bem vindo Administrador
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

def inputOpc(qtdOpc, msg):
  teclado = ''
  while (isInt(teclado) == False) or (int(teclado) > qtdOpc) or (int(teclado) <= 0):
    teclado = input('Opção: ')
    if (isInt(teclado) == False) or (int(teclado) > qtdOpc) or (int(teclado) <= 0):
      print('Digite uma opção válida!')
  else:
    return teclado

def inputFloat(msg):
  teclado = ''
  while (isFloat(teclado) == False):
    teclado = input(msg)
    if isFloat(teclado) == False:
      print('Digite um número!')
  else:
    return float(teclado)

def validaInput(msg, min, aviso):
  teclado = ''
  while (len(teclado) < min):
    teclado = input(msg)
    if len(teclado) < min:
      print(aviso)
  else:
    return teclado

def validaSenha(msg, min, aviso):
  teclado = ''
  while (len(teclado) < min):
    teclado = getpass(msg)
    if len(teclado) < min:
      print(aviso)
  else:
    return teclado

def validaTipoPessoa(msg, aviso):
  teclado = ''
  while (teclado != 'pf' and teclado != 'pj'):
    teclado = input(msg).lower()
    if teclado != 'pf' and teclado != 'pj':
      print(aviso)
  else:
    return teclado

def validaCpf(msg):
  teclado = ''
  while (not teclado.isdigit() or len(teclado) != 11):
    teclado = input(msg)
    if not teclado.isdigit():
      print("Informe apenas números!")
    if len(teclado) != 11:
      print("CPF possui onze dígitos!")
  else:
    return teclado

def validaCnpj(msg):
  teclado = ''
  while (not teclado.isdigit() or len(teclado) != 14):
    teclado = input(msg)
    if not teclado.isdigit():
      print("Informe apenas números!")
    if len(teclado) != 14:
      print("CNPJ possui quatorze dígitos")
  else:
    return teclado

def validaAgencia(msg, aviso):
  teclado = ''
  while (len(teclado) != 4 or not teclado.isdigit()):
    teclado = input(msg)
    if len(teclado) != 4 or not teclado.isdigit():
      print(aviso)
  else:
    return teclado

def voltar():
  input("\nPressione <enter> para voltar")

def xrange(x):
    return iter(range(x))

def geradorConta():                                                                                             
    n = [random.randrange(10) for i in xrange(9)]                                                                                              
    return "%d%d.%d%d%d%d%d%d.%d" % tuple(n)
