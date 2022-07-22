import csv
import os
import sys
from time import time

def consulta_areas():

    print('{}Nome{}Quantidade máx. de animais{}GMD\n{}'.format(7*' ', 12*' ', 12*' ', 71*'_'))
    with open('./data/areas.csv', newline='', encoding='utf-8') as file:
        linhas = csv.reader(file)
        for linha in linhas:
            print('{}{}{}{}{}{}'.format((12-len(linha[0]))*' ', linha[0], (24-len(str(linha[1])))*' ', linha[1], (28-len(str(linha[2])))*' ', linha[2]))
    print(71*'_')
    while True:
        print('\n')
        print('1 - Voltar    2 - Sair\n\n')
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
        if int(opcao) < 1 or int(opcao) > 2:
            os.system('cls')
            print('A opção deve ser entre 1 e {}'.format(str(2)))
            time.sleep(2)
            continue


        opcao = int(opcao)

        # Cadastro de áreas.
        if opcao == 1:
            os.system('cls')
            break

        # Cadastro de animais
        if opcao == 2:
            os.system('cls')
            print('O programa será fechado, até mais :)')
            time.sleep(3)
            sys.exit()


