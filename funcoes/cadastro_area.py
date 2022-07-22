import time, csv, os, sys

def mensagem_campo_vazio(nome_campo):
    """Mensagem de erro caso o campo setado esteja vazio"""
    os.system('cls')
    print('O campo {} não pode ficar vazio.'.format(nome_campo))
    time.sleep(3)



def cadastro_area():

    lista_dados = []

    # NOME DA ÁREA
    while True:
        print('\n{}CADASTRAR NOVA ÁREA{}\n'.format(26*'_', 26*'_'))
        nome = input('Nome da nova área: ').strip()
        if nome == '':
            mensagem_campo_vazio('nome')
        if len(nome) > 12:
            os.system('cls')
            print('O campo nome não pode ter mais que 12 caracteres.')
            time.sleep(3)
            os.system('cls')
            continue

        else:
            lista_dados.append(nome)
            os.system('cls')
            break


    # QUANTIDADE MÁXIMA DE ANIMAIS
    while True:
        print('\n{}CADASTRAR NOVA ÁREA{}\n'.format(26*'_', 26*'_'))
        quantidade_animais = input('Quantidade máxima de animais: ').strip()
       
        if quantidade_animais == '':
            mensagem_campo_vazio('Quantidade máxima de animais')
        if not quantidade_animais.isnumeric():
            os.system('cls')
            print('O campo quantidade máxima de animais deve ser um valor numérico e inteiro.')
            time.sleep(3)
        else:
            lista_dados.append(quantidade_animais)
            os.system('cls')
            break

    
    # GMD (GANHO MÉDIO DIÁRIO)
    while True:
        print('\n{}CADASTRAR NOVA ÁREA{}\n'.format(26*'_', 26*'_'))
        gmd = input('GMD: ').strip()

        if gmd == '':
            mensagem_campo_vazio('GMD')
            continue

        if gmd.count(',') > 1 or gmd.count('.') > 1:
            os.system('cls')
            print('Formato inválido para o campo GMD, segue exemplo: 1.5')
            time.sleep(3)
            continue

        if gmd.count(".") == 1:
            gmd = gmd.replace('.', ',')

        if (gmd.replace(',', '').isnumeric() == False):      
            os.system('cls')
            print('O campo GMD deve ser um valor numérico.')
            time.sleep(3)
            continue

        if gmd.replace(',', '.').count('.') > 1 or gmd.replace('.', ',').count('.') > 1:
            if gmd.count(',') > 1 or gmd.count('.') > 1:
                os.system('cls')
                print('Formato inválido para o campo GMD, segue exemplo: 1.5')
                time.sleep(3)
                continue
        else:
            if gmd.count(',') == 1:
                gmd = float(gmd.replace(',', '.'))
                lista_dados.append(gmd)
                os.system('cls')
                break
            else:
                gmd = float(gmd)
                lista_dados.append(gmd)
                os.system('cls')
                break
    while True:
        print('\n{}CONFIRME OS DADOS ABAIXO{}\n'.format(15*'_', 15*'_'))
        print('Nome{}{}\nQuantidade de animais{}{}\nGMD{}{}\n\n'.format((50-len(nome))*'.', lista_dados[0], (33-len(quantidade_animais))*'.', lista_dados[1], (51-3)*'.', lista_dados[2]))
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
            with open('./data/areas.csv', 'a', newline='', encoding='utf-8') as file:
                w = csv.writer(file)
                w.writerow(lista_dados)
            os.system('cls')
            print('Área cadastrada com sucesso!')
            time.sleep(2)
            break

        if int(opcao) == 2:
            os.system('cls')
            cadastro_area()

        if int(opcao) == 3:
            break

        if int(opcao) == 4:
            os.system('cls')
            print('O programa será fechado, até mais :)')
            time.sleep(3)
            sys.exit()