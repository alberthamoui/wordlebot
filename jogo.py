from arrumando_banco_dados import lista
# alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
possiveis = []
texto_possiveis = ''
print('\n \n \n ')






for palavra in lista:
    palavra = palavra.lower()
    primeira = palavra[0]
    segunda = palavra[1]
    terceira = palavra[2]
    quarta = palavra[3]
    quinta = palavra[4]

    condicoes = [
    
    # primeira == '',     
    # segunda == '', 
    # terceira == '', 
    # quarta == '',
    # quinta == '',
    ]

    nsprimeira = ''
    nssegunda = ''
    nsterceira = ''
    nsquarta = ''
    nsquinta = ''

    presentes = ''
    negadas = ''














# CODIGO
    contagemcondicao = 0
    for condicao in condicoes:
        if condicao == True:
            contagemcondicao += 1 
    if contagemcondicao == len(condicoes):
        
        contagemnegada = 0
        for negada in negadas:
            if negada not in palavra:
                contagemnegada +=1 
        if contagemnegada == len(negadas):
            
            # PRIMEIRA
            cnprimeira = 0
            for nprimeira in nsprimeira:
                if nprimeira != palavra[0]:
                    cnprimeira +=1 
            if cnprimeira == len(nsprimeira):
                
                # SEGUNDA
                cnsegunda = 0
                for nsegunda in nssegunda:
                    if nsegunda != palavra[1]:
                        cnsegunda +=1 
                if cnsegunda == len(nssegunda):
                    
                    # TERCEIRA
                    cnterceira = 0
                    for nterceira in nsterceira:
                        if nterceira != palavra[2]:
                            cnterceira +=1 
                    if cnterceira == len(nsterceira):

                        # QUARTA
                        cnquarta = 0
                        for nquarta in nsquarta:
                            if nquarta != palavra[3]:
                                cnquarta +=1 
                        if cnquarta == len(nsquarta):

                            # QUINTA
                            cnquinta = 0
                            for nquinta in nsquinta:
                                if nquinta != palavra[4]:
                                    cnquinta +=1 
                            if cnquinta == len(nsquinta):

                                # PRESENTES
                                contagempresente = 0
                                if len(presentes) > 0:
                                    for presente in presentes:
                                        if presente in palavra:
                                            contagempresente += 1
                                    if contagempresente == len(presentes):
                                        possiveis.append(palavra)
                                        texto_possiveis += str(palavra)
                                else:
                                    possiveis.append(palavra)
                                    texto_possiveis += str(palavra)


print('PALAVRAS POSSIVEIS', possiveis)
print('QUANTIDADE DE POSSIBILIDADES', len(possiveis))
# print('PALAVRAS POSSIVEIS (TEXTO)', texto_possiveis)
final = {}
for letra in texto_possiveis:
    if letra not in final:
        final[letra] = 1
    else:
        final[letra] += 1
print(final)


sort_final = sorted(final.items(), key=lambda x: x[1], reverse=True)

for i in sort_final:
	print(i[0], i[1])