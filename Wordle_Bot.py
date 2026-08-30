# JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR

v = ["", "", "", "", ""]  # Letras verdes
a = ["", "", "", "", ""]  # Letras amarelas
pretas = ""  # Letras pretas

# JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR JOGAR





# DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO

import os
import sys


def rodando_pelo_vscode():
    """True se o arquivo foi iniciado pelo botao de rodar do VSCode."""

    # 1) Marcador injetado por .vscode/settings.json (python.terminal.launchArgs)
    if "vscode_run" in sys._xoptions:
        return True

    # 2) Depurador do VSCode (F5)
    if "debugpy" in sys.modules or "pydevd" in sys.modules:
        return True

    # 3) Fallback: o botao passa o caminho absoluto do script com barras normais;
    #    no terminal quase sempre se digita um caminho relativo.
    script = sys.argv[0]
    dentro_do_vscode = os.environ.get("TERM_PROGRAM") == "vscode"
    return dentro_do_vscode and os.path.isabs(script) and "/" in script


no_vscode = rodando_pelo_vscode()

# DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO DETECCAO


# LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC 

from baseDeDados import lista
from logica import *

# Pelo botao do VSCode usa os valores fixos la de cima; pelo terminal, pergunta.
if not no_vscode:
    v, a, pretas = obter_entradas_terminal()

possiveis, texto_possiveis = processa_palavras(lista, v, a, pretas)
frequencia_letras = analisa_frequencia_letras(texto_possiveis)
mLetras = [letra for letra, _ in frequencia_letras[:5]]
classificacao = classifica_palavras_por_letras(possiveis, mLetras)

print("Palavras possiveis:", possiveis)
print("Classificacao por letras:", classificacao)

# LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC LOGIC 