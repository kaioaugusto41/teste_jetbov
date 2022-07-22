import time, csv, os, sys

def mensagem_campo_vazio(nome_campo):
    """Mensagem de erro caso o campo setado esteja vazio"""
    os.system('cls')
    print('O campo {} não pode ficar vazio.'.format(nome_campo))
    time.sleep(3)



def cadastro_animal():

    lista_dados = []

    # NOME DA ÁREA
    while True:
        print('\n{}CADASTRAR NOVO ANIMAL{}\n'.format(25*'_', 25*'_'))
        brinco = input('Brinco: ').strip()
        if brinco == '':
            mensagem_campo_vazio('nome')
        else:
            lista_dados.append(brinco)
            os.system('cls')
            break


    
    # PESO INICIAL
    while True:
        print('\n{}CADASTRAR NOVO ANIMAL{}\n'.format(25*'_', 25*'_'))
        peso_inicial = input('Peso inicial: ').strip()

        if peso_inicial == '':
            mensagem_campo_vazio('Peso inicial')
            continue

        if peso_inicial.count(',') > 1 or peso_inicial.count('.') > 1:
            os.system('cls')
            print('Formato inválido para o campo Peso inicial, segue exemplo: 1.5')
            time.sleep(3)
            continue

        if peso_inicial.count(".") == 1:
            peso_inicial = peso_inicial.replace('.', ',')

        if (peso_inicial.replace(',', '').isnumeric() == False):      
            os.system('cls')
            print('O campo Peso inicial deve ser um valor numérico.')
            time.sleep(3)
            continue

        if peso_inicial.replace(',', '.').count('.') > 1 or peso_inicial.replace('.', ',').count('.') > 1:
            if peso_inicial.count(',') > 1 or peso_inicial.count('.') > 1:
                os.system('cls')
                print('Formato inválido para o campo Peso inicial, segue exemplo: 1.5')
                time.sleep(3)
                continue
        else:
            if peso_inicial.count(',') == 1:
                peso_inicial = float(peso_inicial.replace(',', '.'))
                lista_dados.append(peso_inicial)
                os.system('cls')
                break
            else:
                peso_inicial = float(peso_inicial)
                lista_dados.append(peso_inicial)
                os.system('cls')
                break
    while True:
        os.system('cls')
        print('\n{}CONFIRME OS DADOS ABAIXO{}\n'.format(15*'_', 15*'_'))
        print('Brinco{}{}\nPeso inicial{}{} Kg\n\n'.format((48-len(brinco))*'_', lista_dados[0], (39-len(str(peso_inicial)))*'_', lista_dados[1]))
        print(' 1 - Salvar   2 - Criar novo   3 - Voltar   4 - Sair\n')

        opcao = input(' Digite a opção desejada:').strip()

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

        if int(opcao) == 1:
            with open('./data/animais.csv', 'a', newline='', encoding='utf-8') as file:
                w = csv.writer(file)
                w.writerow(lista_dados)
            os.system('cls')
            print('Animal cadastrado com sucesso!')
            time.sleep(5)
            break

        if int(opcao) == 2:
            os.system('cls')
            cadastro_animal()

        if int(opcao) == 3:
            break

        if int(opcao) == 4:
            os.system('cls')
            print('O programa será fechado, até mais :)')
            time.sleep(3)
            sys.exit()