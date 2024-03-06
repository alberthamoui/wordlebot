with open('palavras_wordle.txt', 'r') as arquivo:
    conteudo = arquivo.read()

palavras = conteudo.replace('"','')
palavras = palavras.lower()
palavras = palavras.split(',')

lista = []
for palavra in palavras:
    if palavra not in lista:
        lista.append(palavra)
# print(len(lista))