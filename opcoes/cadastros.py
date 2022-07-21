
from funcoes.cadastro_area import cadastro_area
import os, time, sys

def menu_cadastros():
    while True:
        print('\n{}Digite uma das opções abaixo:{}\n'.format(20*'_', 20*'_'))
        print('{}1 - Cadastrar área    2 - Cadastrar animal   3 - Voltar    4 - Sair{}\n\n'.format(6*'', 5*''))
        print(len('CADASTRAR NOVA ÁREA'))
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


        opcao = int(opcao)

        # Cadastro de áreas.
        if opcao == 1:
            os.system('cls')
            cadastro_area()

        # Cadastro de animais
        if opcao == 2:
            pass

        # Voltar
        if opcao == 3:
            os.system('cls')
            return breakpoint
        
        # Sair
        if opcao == 4:
            os.system('cls')
            print('O programa será fechado, até mais :)')
            time.sleep(3)
            sys.exit()