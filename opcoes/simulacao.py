import os, time, csv
import sys


# Função que retorna a quantidade de áreas cadastradas.
def areas_cadastradas():
    with open('./data/areas.csv', newline='', encoding='utf-8') as file:
        linhas = csv.reader(file)
        areas = []
        for linha in linhas:
            areas.append(linha)
    return len(areas)

# Função que retorna a quantidade de animais cadastrados.
def animais_cadastrados():
    with open('./data/animais.csv', newline='', encoding='utf-8') as file:
        linhas = csv.reader(file)
        animais = []
        for linha in linhas:
            animais.append(linha)
    return len(animais)


# Simulação
def simulacao():
    os.system('cls')

    # else:
    areas_simulacao = []
    animais_simulacao = []
    dias_simulacao = []
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
        area_envolvida = input('Digite o número da área que deseja incluir os animais.\nExemplo(3): ').strip().replace('.%$#@*&_-', '')

        if area_envolvida == '':
            os.system('cls')
            print('O campo de áreas envolvidas não pode ser vazio.')
            time.sleep(2)
            continue

        if not area_envolvida.isnumeric():
            os.system('cls')
            print('O campo de área envolvida deve obter apenas números.')
            time.sleep(2)
            continue

        area_envolvida = int(area_envolvida)
        if area_envolvida > areas_cadastradas():
            os.system('cls')
            print('Á area de número {} não existe na base de dados.'.format(area_envolvida))
            time.sleep(2)
            continue
    
                    
        areas_simulacao.append(area_envolvida)

        volta = False
        # COMEÇO ANIMAIS
        if len(animais_simulacao) == 0:
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
                
                    if status == False:
                        os.system('cls')
                        print('O animal de número {} não existe na base de dados.'.format(animal))
                        time.sleep(2)
                        continue

                    with open('./data/areas.csv', newline='', encoding='utf-8') as file:
                        linhas = csv.reader(file)
                        cont = 0
                        status = True
                        for linha in linhas:
                            cont+=1
                            if cont == int(area_envolvida):
                                if len(animais_envolvidos_list) > int(linha[1]):
                                    status = False
                                    nome_area = linha[0]
                                    quantidade_max = linha[1]
                                    break
                        if status == False:
                            os.system('cls')
                            print('A área {} só permite o máximo de {} animais.'.format(nome_area, quantidade_max))
                            time.sleep(2)
                            continue
                
        animais_simulacao.append(animais_envolvidos_list)
        while True:

            if volta == True:
                break

            os.system('cls')
            while True:
                os.system('cls')
                print('\n{}SIMULAÇÃO DE ROTAÇÃO{}\n'.format(25*'_', 26*'_'))
                dias = input('Digite a quantidade de dias em que os animais ficarão na área: ')

                if dias == '':
                    os.system('cls')
                    print('O campo de dias não pode ser vazio.')
                    time.sleep(2)
                    continue

                if not dias.isnumeric():
                    os.system('cls')
                    print('O campo de dias deve obter apenas números.')
                    time.sleep(2)
                    continue

                dias_simulacao.append(dias)
                break

            while True:
                os.system('cls')
                print('\n{}Digite uma das opções abaixo:{}\n'.format(20*'_', 20*'_'))
                print('{}1 - Continuar movimentando    2 - Ver resultado   3- Sair{}\n\n'.format(1*' ', 6*' '))
            
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
                if int(opcao) < 1 or int(opcao) > 3:
                    os.system('cls')
                    print('A opção deve ser entre 1 e {}'.format(str(3)))
                    time.sleep(2)
                    continue
                

                if int(opcao) == 1:
                    os.system('cls')
                    volta = True
                    break
                if int(opcao) == 2:
                    os.system('cls')
                    print('\n{}RESULTADO DA SIMULAÇÃO{}\n'.format(25*'_', 26*'_'))
                    areas = []
                    animais = []
                    animais_old = []
                    with open('./data/areas.csv', newline='', encoding='utf-8') as file:
                        linhas_areas = csv.reader(file)
                        for area in linhas_areas:
                            areas.append(area)
                    with open('./data/animais.csv', newline='', encoding='utf-8') as file:
                        linhas_animais = csv.reader(file)     
                        for animal in linhas_animais:
                            animais.append(animal)
                    with open('./data/animais.csv', newline='', encoding='utf-8') as file:
                        linhas_animais = csv.reader(file)     
                        for animal in linhas_animais:
                            animais_old.append(animal)

                    listas_simulacao = zip(areas_simulacao, animais_simulacao, dias_simulacao)
                    cont = 0
                    peso_inicio = []
                    for area, animal, dias in listas_simulacao:
                        cont+=1
                        brincos_str = ''
                        brincos_str_fim = ''
                        peso_inicial = 0
                        peso_final = 0
                        if cont == 1:
                            for i in animal:
                                peso_inicio.append(animais[int(i)-1][1])
                        for i in animal:
                            brincos_str = brincos_str+' {}({} Kg) '.format(animais[int(i)-1][0], animais_old[int(i)-1][1])
                            peso_inicial = peso_inicial+float(animais_old[int(i)-1][1])
                            porcentagem = ((float(animais[int(i)-1][1])+(int(dias_simulacao[cont-1])*float(areas[int(area)-1][2]))-float(animais_old[int(i)-1][1]))/float(animais_old[int(i)-1][1]))*100
                            brincos_str_fim = brincos_str_fim+' {}({} Kg)+{:.2f}% '.format(animais[int(i)-1][0], (float(animais[int(i)-1][1])+(int(dias_simulacao[cont-1])*float(areas[int(area)-1][2]))), porcentagem)
                            peso_final = peso_final+(float(animais[int(i)-1][1])+(int(dias_simulacao[cont-1])*float(areas[int(area)-1][2])))
                            animais[int(i)-1][1]=(float(animais[int(i)-1][1])+(int(dias_simulacao[cont-1])*float(areas[int(area)-1][2])))
                        print('{}° movimentação: {}'.format(cont, areas[int(area)-1][0]))
                        print('Duração: {} dias'.format(dias_simulacao[cont-1]))
                        print('Ganho total: {} Kg'.format((float(dias_simulacao[cont-1])*float(areas[int(area)-1][2]))*len(animais_envolvidos_list)))
                        print(73*'_')
                    print('Resultado: \n')
                    print("Início: {} ".format(brincos_str))
                    print("Peso inicial total: {} Kg \n".format(peso_inicial))
                    print("Fim   : {}".format(brincos_str_fim))
                    print("Peso final total  : {} Kg".format(peso_final))
                    print('Ganho total: {:.2f} Kg (+{:.2f}%) \n'.format(peso_final-peso_inicial, ((peso_final-peso_inicial)/peso_inicial)*100))
                    print('1 - Voltar    2 - Sair {}\n\n'.format(6*' '))
   
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

                    # CASO PASSE NAS VALIDAÇÕES O VALOR SE TORNA INTEIRO
                    opcao = int(opcao)

                    if opcao == 1:
                        os.system('cls')
                        breakpoint

                    if opcao == 2:
                        os.system('cls')
                        print('O programa será fechado, até mais :)')
                        time.sleep(3)
                        sys.exit()

                if int(opcao) == 3:
                    os.system('cls')
                    print('O programa será fechado, até mais :)')
                    time.sleep(2)
                    sys.exit()

                    






