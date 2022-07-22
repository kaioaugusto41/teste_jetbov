

import os, time, csv


def areas_cadastradas():
    with open('./data/areas.csv', newline='', encoding='utf-8') as file:
        linhas = csv.reader(file)
        areas = []
        for linha in linhas:
            areas.append(linha)
    return len(areas)

def animais_cadastrados():
    with open('./data/animais.csv', newline='', encoding='utf-8') as file:
        linhas = csv.reader(file)
        animais = []
        for linha in linhas:
            animais.append(linha)
    return len(animais)



def simulacao():
    os.system('cls')
    # print('\n{}SIMULAÇÃO DE ROTAÇÃO{}\n'.format(25*'_', 26*'_'))
    # qtd_areas = input('Digite a quantidade de áreas envolvidas: ')
    # # Valida se o valor não é vazio.
    # if qtd_areas == '':
    #     os.system('cls')
    #     print('O campo de quantidade de áreas não pode ser vazio.')
    #     time.sleep(2)
    #     simulacao()
    
    # # Valida se o valor é numérico.
    # if not qtd_areas.isnumeric():
    #     os.system('cls')
    #     print('O campo de quantidade de áreas deve ser um número.')
    #     time.sleep(2)
    #     simulacao()
    
    # if int(qtd_areas) == 0:
    #     os.system('cls')
    #     print('O campo de quantidade de áreas não pode ser zero.')
    #     time.sleep(2)
    #     simulacao()
    
    # if int(qtd_areas) > areas_cadastradas():
    #     os.system('cls')
    #     print('Você não possui {} áreas cadastradas, mas sim {}.'.format(qtd_areas, areas_cadastradas()))
    #     time.sleep(2)
    #     simulacao()


    # else:
    areas_simulacao = []
    while True:
        os.system('cls')
        print('\n{}SIMULAÇÃO DE ROTAÇÃO{}\n'.format(25*'_', 26*'_'))
        print('{}Nome{}Quantidade máx. de animais{}GMD\n{}'.format(11*' ', 12*' ', 12*' ', 71*'_'))
        with open('./data/areas.csv', newline='', encoding='utf-8') as file:
            linhas = csv.reader(file)
            cont = 1
            for linha in linhas:
                print(cont, '- {}{}{}{}{}{}'.format((12-len(linha[0]))*' ', linha[0], (24-len(str(linha[1])))*' ', linha[1], (28-len(str(linha[2])))*' ', linha[2]))
                cont+=1
        print('\n\n')
        area_envolvida = input('Digite os números correspondentes às areas que deseja incluir na simulação\nseparados por vírgulas e sem espaços na ordem da movimentação.\nExemplo(1,5,4): ').strip().replace('.%$#@*&_-', '')

        if area_envolvida == '':
            os.system('cls')
            print('O campo de áreas envolvidas não pode ser vazio.')
            time.sleep(2)
            continue

        area_envolvida = int(area_envolvida)
        if area_envolvida > areas_cadastradas():
            os.system('cls')
            print('Á area de número {} não existe na base de dados.'.format(area_envolvida))
            time.sleep(2)
            continue
                    
        areas_simulacao.append(area_envolvida)

        print('\n{}Digite uma das opções abaixo:{}\n'.format(20*'_', 20*'_'))
        print('{}1 - Continuar    2 - Parar   3 - Voltar    4 - Sair{}\n\n'.format(6*' ', 6*' '))
        

        ###
        while True:
            os.system('cls')
            print('\n{}SIMULAÇÃO DE ROTAÇÃO{}\n'.format(25*'_', 26*'_'))
            qtd_animais = input('Digite a quantidade de animais envolvidos: ').strip()
            # Valida se o valor não é vazio.
            if qtd_animais == '':
                os.system('cls')
                print('O campo de quantidade de animais não pode ser vazio.')
                time.sleep(2)
                continue

            # Valida se o valor é numérico.
            if not qtd_animais.isnumeric():
                os.system('cls')
                print('O campo de quantidade de animais deve ser um número.')
                time.sleep(2)
                continue
            
            if int(qtd_animais) == 0:
                os.system('cls')
                print('O campo de quantidade de animais não pode ser zero.')
                time.sleep(2)
                continue
            
            
            if int(qtd_animais) > animais_cadastrados():
                os.system('cls')
                print('Você não possui {} animais cadastrados, mas sim {}.'.format(qtd_animais, animais_cadastrados()))
                time.sleep(2)
                continue

            
            with open('./data/areas.csv', newline='', encoding='utf-8') as file:
                linhas = csv.reader(file)
                linhas_list = []
                for linha in linhas:
                    linhas_list.append(linha)
                status_1 = True
                for i in range(0, len(areas_envolvidas_list)):
                    if int(qtd_animais) > int(linhas_list[i][1]):
                        os.system('cls')
                        print('A área {} só permite {} animais.'.format(linhas_list[i][0], linhas_list[i][1]))
                        time.sleep(2)
                        status_1 = False
                if status_1 == False:
                    continue
            while True:
                os.system('cls')
                print('\n{}SIMULAÇÃO DE ROTAÇÃO{}\n'.format(25*'_', 26*'_'))
                print('{}Brinco{}Peso Inicial\n{}'.format(14*' ', 27*' ', 71*'_'))
                with open('./data/animais.csv', newline='', encoding='utf-8') as file:
                    linhas = csv.reader(file)
                    cont = 1
                    for linha in linhas:
                        print(cont, '- {}{}{}{}{}'.format(round((27-len(linha[0]))/2)*' ', linha[0], round((35-len(linha[0]))/2)*' ', round((35-len(linha[1]))/2)*' ', linha[1], round((35-len(linha[1]))/2)*' '))
                        cont+=1
                print('\n\n')
                animais_envolvidos = input('Digite os números correspondentes aos animais que deseja incluir na simulação\nseparados por vírgulas e sem espaços.\nExemplo(1,5,4): ').strip().replace('.%$#@*&_-', '')

                if animais_envolvidos == '':
                    os.system('cls')
                    print('O campo de animais envolvidos não pode ser vazio.')
                    time.sleep(2)
                    continue

                if len(animais_envolvidos) == 1:
                    if not animais_envolvidos.isnumeric():
                        os.system('cls')
                        print('O campo de animais envolvidos deve obter apenas números.')
                        time.sleep(2)
                        continue
                if len(animais_envolvidos) > 0:
                    if (animais_envolvidos.count(',')+1) != len(animais_envolvidos.replace(',', '')):
                        os.system('cls')
                        print('O campo de animais envolvidos obteve um formato inválido, segue exemplo: (1,5,4)')
                        time.sleep(2)
                        continue
                    else:
                        animais_envolvidos_list = animais_envolvidos.split(',')
                        status = True
                        for animal in animais_envolvidos_list:
                            if int(animal) > animais_cadastrados():
                                status = False
                    
                        if len(animais_envolvidos_list) < int(qtd_animais):
                            os.system('cls')
                            print('O número de animais selecionados é menor que o fornecido anteriormente.')
                            time.sleep(2)
                            continue

                        if len(animais_envolvidos_list) > int(qtd_animais):
                            os.system('cls')
                            print('O número de animais selecionados é maior que o fornecido anteriormente.')
                            time.sleep(2)
                            continue


                        if status == False:
                            os.system('cls')
                            print('O animal de número {} não existe na base de dados.'.format(animal))
                            time.sleep(2)
                            continue

                        os.system('cls')
                        print('\n{}RESULTADO DA SIMULAÇÃO{}\n'.format(24*'_', 25*'_'))
                        time.sleep(100)








