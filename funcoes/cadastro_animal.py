import time, csv, os, sys

def mensagem_campo_vazio(nome_campo):
    """Mensagem de erro caso o campo setado esteja vazio"""
    os.system('cls')
    print('O campo {} não pode ficar vazio.'.format(nome_campo))
    time.sleep(3)



def cadastro_animal():

    lista_dados = []

    # PERGUNTA O BRINCO DO NOVO ANIMAL.
    while True:
        print('\n{}CADASTRAR NOVO ANIMAL{}\n'.format(25*'_', 25*'_'))                       
        brinco = input('Brinco: ').strip()

        # Valida se o campo brinco não é vazio.
        if brinco == '':
            mensagem_campo_vazio('nome')
        else:
            lista_dados.append(brinco)
            os.system('cls')
            break


    
    # PERGUNTA O PESO INICIAL DO NOVO ANIMAL
    while True:
        print('\n{}CADASTRAR NOVO ANIMAL{}\n'.format(25*'_', 25*'_'))
        peso_inicial = input('Peso inicial: ').strip()

        # Valida se o peso inicial não é vazio.
        if peso_inicial == '':
            mensagem_campo_vazio('Peso inicial')
            continue

        # Valida se o peso inicial possui mais que uma vírgula ou ponto.
        if peso_inicial.count(',') > 1 or peso_inicial.count('.') > 1:
            os.system('cls')
            print('Formato inválido para o campo Peso inicial, segue exemplo: 1.5')
            time.sleep(3)
            continue

        # Troca todos os pontos por vírgula
        if peso_inicial.count(".") == 1:
            peso_inicial = peso_inicial.replace('.', ',')

        # Valida se o peso inicial é númérico
        if (peso_inicial.replace(',', '').isnumeric() == False):      
            os.system('cls')
            print('O campo Peso inicial deve ser um valor numérico.')
            time.sleep(3)
            continue

        # Valida se o peso inicial tem mais que um ponto.
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


    # CONFIRMAÇÃO DOS DADOS
    while True:
        os.system('cls')
        print('\n{}CONFIRME OS DADOS ABAIXO{}\n'.format(15*'_', 15*'_'))
        print('Brinco{}{}\nPeso inicial{}{} Kg\n\n'.format((48-len(brinco))*'_', lista_dados[0], (39-len(str(peso_inicial)))*'_', lista_dados[1]))
        print(' 1 - Salvar   2 - Criar novo   3 - Voltar   4 - Sair\n')

        opcao = input(' Digite a opção desejada:').strip()

        # Valida se a opção não é vazia.
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

        # Se a opção for 1 o animal é salvo no arquivo csv.
        if int(opcao) == 1:
            # Abre o arquivo animais.csv que contem os animais cadastrados.
            with open('./data/animais.csv', 'a', newline='', encoding='utf-8') as file:
                w = csv.writer(file)
                w.writerow(lista_dados)
            os.system('cls')
            print('Animal cadastrado com sucesso!')
            time.sleep(2)
            break

        # Se a opção for 2 o menu é retornado para o início do cadastro.
        if int(opcao) == 2:
            os.system('cls')
            cadastro_animal()

        # Se a opção for 3 o programa volta ao menu anterior.
        if int(opcao) == 3:
            break

        # Se a opção for 4 o programa é encerrado.
        if int(opcao) == 4:
            os.system('cls')
            print('O programa será fechado, até mais :)')
            time.sleep(3)
            sys.exit()