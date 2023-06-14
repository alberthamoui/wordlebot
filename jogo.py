# JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR

amostra = 10 # Quantidade maxima de palavras visiveis

v0 = ''
v1 = ''
v2 = ''
v3 = ''
v4 = ''
# v0 = ''
# v1 = ''
# v2 = ''
# v3 = ''
# v4 = ''



pretas = ''
# pretas = ''

a0 = ''
a1 = ''
a2 = ''
a3 = ''
a4 = ''
# a0 = ''
# a1 = ''
# a2 = ''
# a3 = ''
# a4 = ''

mostrarVA = False
presentes = ''

# JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR


# PONTUACAO:

pontuacao = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0
    }


# 1 RODADA ->

# 2 RODADAS -> 

# 3 RODADAS -> 

# 4 RODADAS -> 

# 5 RODADAS -> 

# 6 RODADAS -> 


























from baseDeDados import lista
# BASE NESSESSARIA
possiveis = []
v = [v0,v1,v2,v3,v4]
vSoma = (len(v0)+len(v1)+len(v2)+len(v3)+len(v4))
a = [a0,a1,a2,a3,a4]
aSoma = (len(a0)+len(a1)+len(a2)+len(a3)+len(a4))

# EXTRAS
texto_possiveis = '' # palavras possiveis
dados_teste = {} # qnt de cada letra
mLetras = []
m2 = [] # letras que repetem 2x 
m3 = [] # letras que repetem 3x
m4 = [] # letras que repetem 4x
m5 = [] # letras que repetem 5x
mtop = []
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []



# CODIGO
if len(pretas) == 0 and aSoma == 0: # se nao tem letras pretas ou amarelas
        for palavra in lista: # roda todas as palavras
            palavra = palavra.lower()
            primeira = palavra[0]
            segunda = palavra[1]
            terceira = palavra[2]
            quarta = palavra[3]
            quinta = palavra[4]
            posicoes = [primeira, segunda, terceira, quarta, quinta]
    # ==================== SÓ VERDES ====================
            contagemVerde = vSoma    # valor fixo // qnt de letras verdes
            cv = 0    # contagem no codigo 
            for i in range(len(v)): # roda letras verdes
                if len(v[i])!=0:
                    if v[i] == posicoes[i]: # compara letra da palavra com letra verde
                        cv += 1
            if cv == contagemVerde: # se as letras verdes estao na mesma posicao na palavra 
                possiveis.append(palavra) # adiciona em lista de possiveis
else: # se tem letras pretas ou amarelas
    for palavra in lista: # roda todas as palavras
        black = False # essa parte fixa variaveis como false para condicional futura
        green = False # essa parte fixa variaveis como false para condicional futura
        yellow = False # essa parte fixa variaveis como false para condicional futura
        # count = 0
        palavra = palavra.lower()
        primeira = palavra[0]
        segunda = palavra[1]
        terceira = palavra[2]
        quarta = palavra[3]
        quinta = palavra[4]
        posicao = [primeira, segunda, terceira, quarta, quinta]

    # ==================== PRETAS ====================
        if len(pretas) > 0: # só roda se tem letra preta
            cp = 0
            for letra in pretas:
                if letra not in palavra:
                    cp += 1 # se nao tem NENHUMA letra preta na palavra soma na contagem
            if cp == len(pretas):
                black = True # se a contagem bate com a qnt de letra preta, passou no teste black
        else:
            black = True # se nao tem letra preta, passou no teste black

    # ==================== VERDES ====================
        if vSoma > 0 and black: # aqui ve a variavel black, pq se nao passa la, nao tem pq rodar essa parte
            contagemVerde = vSoma    # soma fixa
            cv = 0    # soma no codigo 
            for i in range(len(v)):
                if len(v[i])!=0:
                    if v[i] == posicao[i]: # compara letra da palavra com letra verde
                        cv += 1 # se as letras verdes estao na mesma posicao na palavra 
            if cv == contagemVerde:
                green = True # se a contagem bate, passou no teste green
        else:
            if vSoma == 0:
                green = True # se nao tem letra verde, passou no teste green
    
# ==================== AMARELAS ====================
        if aSoma > 0 and black and green: # ve a variavel black e green pelo mesmo motivo anterior
            contagemAmarela = aSoma # soma fixa
            ca = 0 # soma no codigo
            for i in range(len(a)):
                if len(a[i]) > 0:
                    for letra in a[i]:
                        if letra in palavra and posicao[i]!= letra: # se tem a letra amarela na palavra, mas nao na mesma posicao
                            ca += 1
            if ca == contagemAmarela:
                yellow = True # se a contagem bate, passou no teste yellow
        else:
            if aSoma == 0:
                yellow = True # se nao tem letra amarela, passou no teste yellow

# ==================== CONFIRMACAO ====================
        if black and green and yellow: # se passou em todos os teste, adiciona a palavra na lista de possiveis
            possiveis.append(palavra)
            texto_possiveis += str(palavra)


# ==================== EXTRAS ====================
final = {}
for letra in texto_possiveis:
    if letra not in final:
        final[letra] = 1
    else:
        final[letra] += 1
# print(final)
sort_final = sorted(final.items(), key=lambda x: x[1], reverse=True)
for i in sort_final:
	dados_teste[i[0]] = i[1]
chaves = list(dados_teste.keys())

if len(chaves) >= 5: #+ vSoma:
    for i in range(5):# + vSoma):
        mLetras.append(chaves[i])


for palavra in possiveis:
    count = 0
    for letra in mLetras:
        if letra in palavra:
            count += 1
    if count == 2:
        m2.append(palavra)
    if count == 3:
        m3.append(palavra)
    if count == 4:
        m4.append(palavra)
    if count == 5:
        m5.append(palavra)
    if count > 5:
        mtop.append(palavra)

# PROBLEMA LETRAS IGUAIS
if len(presentes) > 0:

    for palavra in lista:
        # palavra = palavra.lower()
        contagem = 0
        for letra in presentes:
            contagem += palavra.count(letra)
        if contagem == 1:
            p1.append(palavra)
        elif contagem == 2:
            p2.append(palavra)
        elif contagem == 3:
            p2.append(palavra)
        elif contagem == 4:
            p2.append(palavra)
        elif contagem == 5: 
            p5.append(palavra)



# ==================== PRINT ====================

if len(possiveis) == 0:
    print('\n\n\n\n\n')

    print('ALGO ESTA ERRADO, NAO TEM NENHUMA PALAVRA POSSIVEL')
else:
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('\nPOSSIVEIS',possiveis[0: amostra], '\n\n')
    print('EXISTEM {} PALAVRAS POSSIVEIS\n\n'.format(len(possiveis)))
    print('LETRAS: ',mLetras)
    if len(mtop) == 0:    
        if len(m5) == 0:
            if len(m4) == 0:
                if len(m3) == 0:
                    if len(m2) == 0:
                        print('NADA ESPECIAL')
                    else:
                        print('DUAS LETRAS: ', m2)
                else:
                    print('TRES LETRAS: ', m3)
            else:
                print('QUATRO LETRAS: ', m4)
        else:
            print('CINCO LETRAS', m5)
    else:
        print('FORA DO NORMAL', mtop)
    print('\n')
    if len(presentes) > 0:
        if len(p5) == 0:
            if len(p4) == 0:
                if len(p3) == 0:
                    if len(p2) == 0:
                        print('NAO EXISTE')
                    else:
                        print('DUAS LETRAS: ', p2[0])
                else:
                    print('TRES LETRAS: ', p3[0])
            else:
                print('QUATRO LETRAS: ', p4[0])
        else:
            print('CINCO LETRAS: ', p5[0])