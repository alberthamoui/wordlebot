import pandas as pd

with open('wordle.txt', 'r') as arquivo:
    conteudo = arquivo.read()

palavras = conteudo.lower()
palavras = palavras.split('\n')
# print(palavras)

lista_wordle = []
for palavra in palavras:
    if palavra not in lista_wordle:
        lista_wordle.append(palavra)

df = pd.read_csv("palavras_termo.csv")

if "palavras" in df.columns:
	lista_termo = [p.lower() for p in df["palavras"].tolist()]
elif "Palavras" in df.columns:
	lista_termo = [p.lower() for p in df["Palavras"].tolist()]
else:
	lista_termo = [p.lower() for p in df.iloc[:, 0].tolist()]

# print(f'len w: {len(lista_wordle)}' )
# print(f'len t: {len(lista_termo)}' )