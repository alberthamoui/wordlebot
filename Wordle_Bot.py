# JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR

v = ["", "", "", "", ""]  # Letras verdes
a = ["", "", "", "", ""]  # Letras amarelas
pretas = ""  # Letras pretas
presentes = ""  # Letras presentes para problema de letras iguais

# JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR





# LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC 

from baseDeDados import lista
from logica import *

possiveis, texto_possiveis = processa_palavras(lista, v, a, pretas, presentes)
frequencia_letras = analisa_frequencia_letras(texto_possiveis)
mLetras = [letra for letra, _ in frequencia_letras[:5]]
classificacao = classifica_palavras_por_letras(possiveis, mLetras)

print("Palavras possiveis:", possiveis)
print("Classificacao por letras:", classificacao)

# LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC 