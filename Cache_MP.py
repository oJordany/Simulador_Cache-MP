import random
from time import sleep

print('='*60)
print('[ 1 ] PARA MÉTODO DE MAPEAMENTO DIRETO')
print('[ 2 ] PARA MÉTODO DE MAPEAMENTO ASSOCIATIVO')
R = int(input('Escolha uma opção: ')) #usuário escolhe um método de mapeamneto
print('='*60)

if R == 1:
    print('{:^60}'.format('MÉTODO DE MAPEAMENTO DIRETO'))
    print('{:^60}'.format('MEMÓRIA RAM: 32 bytes'))
    print('{:^60}'.format('BARRAMENTO DE ENDEREÇO: 5 bits'))
    cont = 0                         #Contador se inicia em 0
    res = 'C'                        #Resposta do usuário/processador recebe 'C'
    totbits = []                     #Cria-se uma lista vazia que vai receber o total de bits da MP
    MP = []                          #Cria-se uma lista vazia que corresponde a MP
    cache = [[[],[]], [[],[]], [[],[]], [[],[]]]    #Cria-se uma lista com 4 sublistas (linha) e dentro delas há 2 sublistas (bytes). Portanto as linhas têm largura de 2 bytes
    linhascache = [[['____']], [['____']], [['____']], [['____']]]   #linhascache corresponde à uma lista com a cópia dos 4 bits mais significativos do endereço em suas respectivas linhas
    MPblocos = []                    #MPblocos é uma lista que vai possuir a MP organizada em blocos(que são sublistas)

    # Gerador de dados aleatórios para colocar na MP
    for i in range(0,32):
        for c in range(0,8):
            totbits.append(random.randint(0, 1))
    #Nesse momento, a MP começa a receber o totbits organizada em forma de bytes(que são sublistas)
    for j in range(0, len(totbits), 8):
        MP.append(totbits[j:j + 8])
    #Nesse momento, MPblocos começa a receber as sublistas que correspondem aos blocos(de 2 bytes de largura) da MP
    for k in range(0,len(MP),2):
        MPblocos.append(MP[k:k + 2])
    for l in range(0,32):
        print(MP[l])

    #loop que reinicia sempre que o usuário/processador quiser fazer outra operação
    while res == 'C':
        print('{:^60}'.format('UC insere o sinal de leitura/escrita:'))
        print('[ 0 ] para escrita\n[ 1 ] para leitura')
        sinal = str(input(('escolha uma opção: ')))

        if sinal == '1':  #Se a opção 1 (leitura) for escolhida...
            cont += 1         #essse contador vai auxiliar para contar a quantidade de acessos do usuário/processador
            endereco = str(input('UCP insere o endereço desejado: '))   #usuário insere o endereço que deseja ler
            #aqui o endereço vai ser fatiado em seus respectivos campos (célula, linha, tag) e em uma parte para bloco
            celula = endereco[4:5]             #parte do endereço correspondente a célula
            linha = endereco[2:4]              #parte do endereço correspondente a linha
            tag = endereco[0:2]                #parte do endereço correspondnete a tag
            bloco = endereco[0:4]              #parte do endereço correspondente ao bloco
            #se for o primeiro acesso...
            if cont == 1:
                print('Ocorreu um miss\nAguarde, buscando informação na MP...')    #vai ocorrer um miss
                sleep(3)     #espera de 3 segundos
                cache[int(linha, 2)] = MPblocos[int(bloco, 2)]   #cache (na posição indicada pela linha) recebe MPblocos (na posição indicada pelo bloco)
                linhascache[int(linha, 2)][0] = [bloco] #linhascache (na posição indicada pela sublista 0 da sublista cuja posição é indicada pela linha) recebe uma lista contendo o valor do bloco
                print('BYTE : {}'.format(MP[int(endereco,2)])) #A informação(byte) desejado é buscada na MP diretamente através do endereço digitado
                print('CACHE:')        #Mostra a situação da cahe
                for l in range(0,4):
                    print(cache[l])
            #se não for o primeiro acesso...
            else:
                #se a tag digitada for igual a tag armazenada na sublista de posição 0 da sublista de posição indicada pelo valor da linha...
                if tag == linhascache[int(linha, 2)][0][0][0:2]:    #Basicamente, isso faz a função do comparador de tags
                    print('Ocorreu um hit!\nA informação já está na cache.')      #vai ocorrer um hit
                    print('BYTE: {}'.format(cache[int(linha,2)][int(celula, 2)])) #A informação(byte) é buscada na cache, na sublista cuja posição é indicada pela celula da sublista de posição indicada pela linha
                    linhascache[int(linha, 2)][0] = [bloco] #atualização da linhascache - linhascache (na posição indicada pela sublista 0 da sublista de posição indicada pela linha) recebe uma lista contendo o valor do bloco
                    print('CACHE:')    #Mostra a situação da cache
                    for l in range(0, 4):
                        print(cache[l])
                #se o comparador de tags não der igual...
                else: #o processo de busca de informação(byte) na MP é repetido, assim como acontece no primeiro acesso
                    print('Ocorreu um miss\nAguarde, buscando informação na MP...')
                    sleep(3)
                    cache[int(linha, 2)] = MPblocos[int(bloco, 2)]
                    linhascache[int(linha, 2)][0] = [bloco]
                    print('BYTE : {}'.format(MP[int(endereco, 2)]))
                    print('CACHE:')
                    for l in range(0, 4):
                        print(cache[l])

        elif sinal == '0':    #Se a opção 0 (escrita) for escolhida...
            cont += 1           #essse contador vai auxiliar para contar a quantidade de acessos do usuário/processador
            endereco = str(input('UCP insere o endereço desejado: '))  #endereço da escrita
            celula = endereco[4:5] #o endereço é fatiado no campo célula
            bloco = endereco[0:4]  #o endereço é fatiado no campo de bloco
            linha = endereco[2:4]  #o endereço é fatiado no campo linha
            infescrita = str(input('UCP insere a informação no BD (8 bits): '))  #informação(byte) que vai ser escrita
            infescritalista = [] #lista com a informação(byte) escrita
            #infescritalista recebe os valores de cada bit
            for c in range(0, 8):
                infescritalista.append(int(infescrita[c:c + 1]))
            if celula == '0':   #se a célula/byte endereçado for o 0...
                bytepermanente = []
                bytepermanente = MPblocos[int(bloco, 2)][1]   #byte que não vai mudar dentro do bloco
                cache[int(linha,2)][1] = bytepermanente
            if celula == '1':   #se a célula/byte endereçado for o 1...
                bytepermanente = []
                bytepermanente = MPblocos[int(bloco,2)][0]    #byte que não vai mudar dentro do bloco
                cache[int(linha,2)][0] = bytepermanente
            MP[int(endereco, 2)] = infescritalista   #MP é atualizada
            #MPblocos é atualizada
            MPblocos = []
            for k in range(0, len(MP), 2):
                MPblocos.append(MP[k:k + 2])
            cache[int(linha,2)][int(celula,2)] = infescritalista  #a célula da cache é atualizada na posição correta da célula pedida
            linhascache[int(linha, 2)][0] = [bloco]   #linhascache é atualizada
            print('CACHE: ')
            for l in range(0, 4):
                print(cache[l])   #Mostra a situação da cache
            print('MP:')
            for l in range(0, 32):
                print(MP[l])      #Mostra a situação da MP

        else:
            print('O sinal inserido não é válido\nTente novamente')
        # caso o usuário/processador queira realizar uma nova operação, ele dever apertar 'C', caso queira finalizar, ele deve apertar enter
        res = str(input('[C] para continuar ou [enter] para finalizar: ')).upper().strip()

elif R == 2:   #Caso o usuário tenha escolhido o método de mapeamento associativo
    print('{:^60}'.format('MÉTODO DE MAPEAMENTO ASSOCIATIVO'))
    print('{:^60}'.format('MEMÓRIA RAM: 32 bytes'))
    print('{:^60}'.format('BARRAMENTO DE ENDEREÇO: 5 bits'))
    cont = 0  # Contador se inicia em 0
    res = 'C'  # Resposta do usuário/processador recebe 'C'
    totbits = []  # Cria-se uma lista vazia que vai receber o total de bits da MP
    MP = []  # Cria-se uma lista vazia que corresponde a MP
    cache = [[[], []], [[], []], [[], []], [[],[]]]  # Cria-se uma lista com 4 sublistas (linha) e dentro delas há 2 sublistas (bytes). Portanto as linhas têm largura de 2 bytes
    blocoscache = [['____'], ['____'], ['____'], ['____']]  #blocoscache corresponde à uma lista com a cópia do endereço dos blocos(que são organizados em sublistas)
    MPblocos = []  # MPblocos é uma lista que vai possuir a MP organizada em blocos(que são sublistas)

    # Gerador de dados aleatórios para colocar na MP
    for i in range(0, 32):
        for c in range(0, 8):
            totbits.append(random.randint(0, 1))
    # Nesse momento, a MP começa a receber o totbits organizada em forma de bytes(que são sublistas)
    for j in range(0, len(totbits), 8):
        MP.append(totbits[j:j + 8])
    # Nesse momento, MPblocos começa a receber as sublistas que correspondem aos blocos(de 2 bytes de largura) da MP
    for k in range(0, len(MP), 2):
        MPblocos.append(MP[k:k + 2])
    for l in range(0,32):
        print(MP[l])

    # loop que reinicia sempre que o usuário/processador quiser fazer outra operação
    while res == 'C':
        print('{:^60}'.format('UC insere o sinal de leitura/escrita:'))
        print('[ 0 ] para escrita\n[ 1 ] para leitura')
        sinal = str(input(('UCP escolhe uma opção: ')))   #sinal de leitura ou escrita é inserido
        if sinal == '1':  #Se a opção 1 (leitura) for escolhida...
            cont += 1  #essse contador vai auxiliar para contar a quantidade de acessos do usuário/processador
            endereco = str(input('UCP insere o endereço desejado: '))  # usuário insere o endereço que deseja ler
            # aqui o endereço vai ser fatiado em seus respectivos campos (célula e bloco)
            celula = endereco[4:5]  # parte do endereço correspondente a célula
            bloco = endereco[0:4]  # parte do endereço correspondente ao bloco
            # se for o primeiro acesso...
            if cont == 1:
                print('Ocorreu um miss\nAguarde, buscando informação na MP...')  # vai ocorrer um miss
                sleep(3)  # espera de 3 segundos
                p_aleatoria = random.randint(0, 3)
                cache[p_aleatoria] = MPblocos[int(bloco,2)]  # cache (em uma posição aleatória que vai de 0 a 3) recebe MPblocos (na posição indicada pelo bloco)
                blocoscache[(p_aleatoria)] = [bloco]  # blocoscache (na mesma posição aleatória indicada na cache) recebe uma lista contendo o valor do bloco
                print('BYTE : {}'.format(MP[int(endereco,2)]))  # A informação(byte) desejada é buscada na MP diretamente através do endereço digitado
                print('CACHE:')      #Mostra a situação da cache
                for l in range(0,4):
                    print(cache[l])
            # se não for o primeiro acesso...
            else:
                #cria-se um indicador da sublista que a cache deve buscar
                if bloco == blocoscache[0][0]:
                    indicador = 0        #indicador da sublista que a cache deve buscar recebe 0
                if bloco == blocoscache[1][0]:
                    indicador = 1        #indicador da sublista que a cache deve buscar recebe 1
                if bloco == blocoscache[2][0]:
                    indicador = 2        #indicador da sublista que a cache deve buscar recebe 2
                if bloco == blocoscache[3][0]:
                    indicador = 3        #indicador da sublista que a cache deve buscar recebe 3

                # se o bloco digitado for igual a pelo menos um bloco armazenado em blocoscache...
                if bloco == blocoscache[0][0] or bloco == blocoscache[1][0] or bloco == blocoscache[2][0] or bloco == blocoscache[3][0] :  # Basicamente, isso faz a função do comparador de blocos
                    print('Ocorreu um hit!\nA informação já está na cache.')  # vai ocorrer um hit
                    print('BYTE: {}'.format(cache[indicador][int(celula,2)]))  # A informação(byte) é buscada na cache, na sublista indicada pela posição gerada pela variável indicador e dentro dessa sublista é escolhido o byte correspondente a variável celula
                    print('CACHE:')    #mostra a situação da cache
                    for l in range(0, 4):
                        print(cache[l])
                # se o comparador de tags não der igual...
                else:  # o processo de busca de informação(byte) na MP é repetido, assim como no primeiro acesso
                    print('Ocorreu um miss\nAguarde, buscando informação na MP...')
                    sleep(3)
                    p_aleatoria = random.randint(0, 3)
                    cache[p_aleatoria] = MPblocos[int(bloco,2)]
                    blocoscache[p_aleatoria] = [bloco]
                    print('BYTE : {}'.format(MP[int(endereco,2)]))
                    print('CACHE:')    #Mostra a situação da cache
                    for l in range(0, 4):
                        print(cache[l])
                    print('MP:')       #Mostra a situação da MP
                    for l in range(0, 32):
                        print(MP[l])

        elif sinal == '0':    #Se a opção 0 (escrita) for escolhida...
            cont += 1         #essse contador vai auxiliar para contar a quantidade de acessos do usuário/processador
            endereco = str(input('UCP insere o endereço desejado: '))   #endereço da escrita
            bloco = endereco[0:4]      #o endereço é fatiado no campo de bloco
            celula = endereco[4:5]     #o endereço é fatiado no campo célula
            infescrita = str(input('UCP insere a informação no BD: '))    #informação(byte) que vai ser escrita
            infescritalista = []    #lista com a informação(byte) escrito
            #infescritalista recebe os valores de cada bit
            for c in range(0,8):
                infescritalista.append(int(infescrita[c:c+1]))
            if celula == '0':   #se a célula/byte endereçado for o 0...
                bytepermanente
                bytepermanente = MPblocos[int(bloco, 2)][1]   #byte que não vai mudar dentro do bloco
                p_aleatoria = random.randint(0, 3)  # gerador de uma posição aleatória
                cache[p_aleatoria][1] = bytepermanente
            if celula == '1':   #se a célula/byte endereçado for o 1...
                bytepermanente
                bytepermanente = MPblocos[int(bloco,2)][0]    #byte que não vai mudar dentro do bloco
                p_aleatoria = random.randint(0, 3)  # gerador de uma posição aleatória
                cache[p_aleatoria][0] = bytepermanente
            MP[int(endereco, 2)] = infescritalista      #MP é atualizada
            MPblocos = []                               #MPblocos é atualizada
            for k in range(0, len(MP), 2):
                MPblocos.append(MP[k:k + 2])
            cache[p_aleatoria][int(celula,2)] = infescritalista  #cache é atualizada com a informação(que foi escrita) na mesma posição aleatória, na célula desejada
            blocoscache[p_aleatoria] = [bloco]            #blocoscache é atualizado com o endereço do bloco que foi escrito (na mesma linha aleatória em que a informação foi escrita na cache)
            print('CACHE: ')        #Mostra a situação da cache
            for l in range(0, 4):
                print(cache[l])
            print('MP: ')           #Mostra a situação da MP
            for l in range(0, 32):
                print(MP[l])
        else:
            print('O sinal inserido não é válido\nTente novamente')
        # caso o usuário/processador queira realizar uma nova operação, ele dever apertar 'C', caso queira finalizar, ele deve apertar enter
        res = str(input('[C] para continuar ou [enter] para finalizar: ')).upper().strip()
else:
    print('Erro! Essa opção não é válida\nFinalizando programa...')
