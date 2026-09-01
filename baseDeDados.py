with open('data/wordle.txt', 'r') as arquivo:
    conteudo_wordle = arquivo.read()

with open('data/termo.txt', 'r') as arquivo:
    conteudo_termo = arquivo.read()

palavras_wordle = conteudo_wordle.lower()
lista_wordle = palavras_wordle.split('\n')
lista_wordle = list(dict.fromkeys(lista_wordle))

palavras_termo = conteudo_termo.lower()
lista_termo = palavras_termo.split('\n')
lista_termo = list(dict.fromkeys(lista_termo))

# print(f'len w: {len(lista_wordle)}')
# print(f'len t: {len(lista_termo)}')





# with open('data/br-sem-acentos.txt', 'r') as arquivo:
#     conteudo = arquivo.read()

# palavras = conteudo.lower()
# palavras = palavras.split('\n')
# palavras = [palavra for palavra in palavras if len(palavra) == 5]
# # print(palavras[:100])
# # with open('data/termo.txt', 'w', encoding='utf-8') as arquivo:
# #     arquivo.write('\n'.join(palavras) + '\n')
