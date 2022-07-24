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

        # Valida se o campo nome é vazio.
        if nome == '':
            mensagem_campo_vazio('nome')
        
        # Valida se o campo não é maior que 12 caracteres.
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
       
       # Valida se o campo quantidade de animais não é vazio.
        if quantidade_animais == '':
            mensagem_campo_vazio('Quantidade máxima de animais')

        # Vaida se o campo quantidade de animais não é vazio.
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

        # Valida se o campo GMD nao é vazio.
        if gmd == '':
            mensagem_campo_vazio('GMD')
            continue

        # Valida se o campo GMD tem mais que um ponto ou vírgula.
        if gmd.count(',') > 1 or gmd.count('.') > 1:
            os.system('cls')
            print('Formato inválido para o campo GMD, segue exemplo: 1.5')
            time.sleep(3)
            continue

        # Se o campo GMD tiver apenas um ponto...
        if gmd.count(".") == 1:
            # O ponto é transformado em vírgula.
            gmd = gmd.replace('.', ',')

        # Valida se o campo GMD é numérico.
        if (gmd.replace(',', '').isnumeric() == False):      
            os.system('cls')
            print('O campo GMD deve ser um valor numérico.')
            time.sleep(3)
            continue

        # Valida se o campo GMD tem apenas um ponto ou vírgula.
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

        # Se a opção for 1 a área é cadastrada no arquivo areas.csv
        if int(opcao) == 1:
            with open('./data/areas.csv', 'a', newline='', encoding='utf-8') as file:
                w = csv.writer(file)
                w.writerow(lista_dados)
            os.system('cls')
            print('Área cadastrada com sucesso!')
            time.sleep(2)
            break
        
        # Se a opção for 2 o cadastro é reiniciado.
        if int(opcao) == 2:
            os.system('cls')
            cadastro_area()

        # Se a opção for 3 o programa volta ao menu anterior.
        if int(opcao) == 3:
            break

        # Se a opção for 4 o programa é encerrado.
        if int(opcao) == 4:
            os.system('cls')
            print('O programa será fechado, até mais :)')
            time.sleep(3)
            sys.exit()