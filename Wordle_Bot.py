# JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR

from baseDeDados import lista_wordle, lista_termo
from logica import *


def escolhe_lista():
    """Pergunta qual jogo e devolve a lista de palavras correspondente."""
    while True:
        tipo = input("Wordle (w) / Termo (t): ").strip().lower()
        if tipo == 'w':
            return lista_wordle
        if tipo == 't':
            return lista_termo
        print("USE UMA DAS QUE PASSEI!")


def mostra_dicas(v, a, pretas):
    """Mostra tudo que o bot ja sabe ate agora."""
    verdes = "".join(letra if letra else "_" for letra in v)
    amarelas = " ".join(
        str(casa + 1) + ":" + (a[casa] if a[casa] else "-") for casa in range(5)
    )
    print("Dicas acumuladas -> verdes: " + verdes)
    print("                    amarelas: " + amarelas)
    print("                    pretas: " + (pretas if pretas else "-"))


def mostra_resultado(lista, v, a, pretas):
    """Filtra a lista com as dicas acumuladas e imprime as sugestoes."""
    possiveis, texto_possiveis = processa_palavras(lista, v, a, pretas)

    if not possiveis:
        print("Nenhuma palavra bate com essas dicas. Confira o que foi digitado ou use 'r' para recomecar.")
        return

    frequencia_letras = analisa_frequencia_letras(texto_possiveis)
    mLetras = [letra for letra, _ in frequencia_letras[:5]]
    classificacao = classifica_palavras_por_letras(possiveis, mLetras)

    print("Palavras possiveis (" + str(len(possiveis)) + "):", possiveis)
    print("Classificacao por letras:", classificacao)


def joga(lista):
    """Loop principal: cada rodada recebe so as letras da tentativa mais recente."""

    v = ["", "", "", "", ""]  # Letras verdes
    a = ["", "", "", "", ""]  # Letras amarelas por casa
    pretas = ""               # Letras pretas

    rodada = 1
    while True:
        print("\n--- Tentativa " + str(rodada) + " ---")
        print("Digite so as letras da palavra mais recente; o resto o bot ja guardou.")

        novo_v, novo_a, novas_pretas = obter_entrada_rodada()
        v, a, pretas = mescla_dicas(v, a, pretas, novo_v, novo_a, novas_pretas)

        print()
        mostra_dicas(v, a, pretas)
        print()
        mostra_resultado(lista, v, a, pretas)

        while True:
            escolha = input("\nEnter = proxima tentativa | r = recomecar | q = sair: ").strip().lower()
            if escolha in ("", "r", "q"):
                break
            print("USE UMA DAS QUE PASSEI!")

        if escolha == "q":
            print("Ate a proxima!")
            return
        if escolha == "r":
            v = ["", "", "", "", ""]
            a = ["", "", "", "", ""]
            pretas = ""
            rodada = 1
            print("\nDicas apagadas, comecando de novo.")
            continue

        rodada += 1


if __name__ == "__main__":
    lista = escolhe_lista()
    try:
        joga(lista)
    except (EOFError, KeyboardInterrupt):
        print("\nAte a proxima!")

# JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR
