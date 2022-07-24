
from funcoes.cadastro_animal import cadastro_animal
from funcoes.cadastro_area import cadastro_area
import os, time, sys
from funcoes.consulta_animais import consulta_animais
from funcoes.consulta_areas import consulta_areas

def menu_consultas():

    while True:
        os.system('cls')
        print('\n{}Digite uma das opções abaixo:{}\n'.format(20*'_', 20*'_'))
        print('{}1 - Consultar áreas    2 - Consultar animais   3 - Voltar    4 - Sair{}\n\n'.format(2*'', 2*''))
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
            consulta_areas()

        # Cadastro de animais
        if opcao == 2:
            os.system('cls')
            consulta_animais()

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