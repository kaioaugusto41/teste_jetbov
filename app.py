from time import time
from opcoes.cadastros import menu_cadastros
import os, sys, time
from opcoes.consultas import menu_consultas
from opcoes.simulacao import simulacao


while True:
    os.system('cls')
    print('\n{}Digite uma das opções abaixo:{}\n'.format(20*'_', 20*'_'))
    print('{}1 - Cadastros    2 - Consultas   3 - Simular    4 - Sair{}\n\n'.format(6*' ', 6*' '))
   
    opcao = input('Digite a opção desejada:').strip()

    # Valida se o valor não é vazio.
    if opcao == '':
        os.system('cls')
        print('O campo de opções não pode ser vazio.')
        time.sleep(2)
        continue

    # Valida se o valor é numérico.
    if not opcao.isnumeric():
        os.system('cls')
        print('A opção deve ser um número.')
        time.sleep(2)
        continue

    # Valida se o valor é entre 1 e 4.
    if int(opcao) < 1 or int(opcao) > 4:
        os.system('cls')
        print('A opção deve ser entre 1 e {}'.format(str(4)))
        time.sleep(2)
        continue

    # CASO PASSE NAS VALIDAÇÕES O VALOR SE TORNA INTEIRO
    opcao = int(opcao)

    # Se a opção for 1 o menu de cadastros é iniciado.
    if opcao == 1:
        os.system('cls')
        menu_cadastros()

    # Se a opção for 2 o menu de consultas é iniciado.
    if opcao == 2:
       os.system('cls')
       menu_consultas()

    # Se a opção for 3 a simulação de rotação é iniciada.
    if opcao == 3:
        os.system('cls')
        simulacao()

    # Se a opção for 4 o programa é encerrado.
    if opcao == 4:
        os.system('cls')
        print('O programa será fechado, até mais :)')
        time.sleep(3)
        sys.exit()
