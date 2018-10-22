#!/bin/env python
# -*- coding: iso-8859-1 -*-
import os

os.system("clear")

saldo = 100

print ("""\t\t\t###BEM-VINDO AO BANCO JIROMBA#####
         \t\t###################################
         \t\t### 1 ## Deposito.              ###
         \t\t### 2 ## Saque.                 ###
         \t\t### 3 ## Saldo.                 ###
         \t\t### 4 ## Sair.                  ###
         \t\t###################################
       """)

while True:
    try:
        op = int(input("\nOpcao: "))
    except:
        print ("\nOpção inválida! Digite apenas valores numéricos.\n")
        quit()
    
    if (op==1):
        print('Deposito Selecionado !')
        print('Deposito Somente com notas inteiras, R$2.00, R$5.00, R$10.00, R$20.00, R$50.00, R$100.00 ')    
        valor_dep=int(input("Qual valor que gostaria de depositar?\n"))
        if valor_dep!=2 and valor_dep!=5 and valor_dep!=10 and valor_dep!=20 and valor_dep!=50 and valor_dep!=100: 
            #corrigir o float com os numeros da condição
            print ('Valor inválido, somente números inteiros ou notas de: R$2.00, R$5.00, R$10.00, R$20.00, R$50.00, R$100.00, Para depósito')
            op==1
        else:   
            saldo=saldo+valor_dep
        print ('Seu saldo e:',saldo)
    elif(op==2):
        print('Saque Selecionado !')
        print('Saque Somente com notas de R$5,00, R$10,00, R$20,00, R$50,00, R$100,00 !')    
        valor_dep=int(input("Qual valor que gostaria de Sacar?\n")) 
        if valor_dep!=2 and valor_dep!=5 and valor_dep!=10 and valor_dep!=20 and valor_dep!=50 and valor_dep!=100:
            print ('Valor digitado invalido, somente números inteiros')
            op==2
        elif saldo <= 0:
            print ('Valor insuficiente para saldo, seu saldo é', saldo)
            op==2
        else:
            saldo=saldo-valor_dep
            print ('Seu saldo e:',saldo    )
    elif (op==3):
        print ('Seu saldo e:',saldo )
    elif (op==4):
        print ("\nPrograma Encerrado.\n\n") 
        quit()
    else:
        print ("Opção incorreta.")