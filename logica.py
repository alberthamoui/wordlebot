# No momento, caso a pessoa coloque espaco como um simbolo que nao eh "_", o codigo assume que esta errado, mas eh pra aceitar todos os simbulos que nao sao letras/numeros.
# Tambem, caso a pessoa colocou os verdes corretamente mas errou o amarelo, o codigo faz com que a pessoa reescreva os verdes, mas nao eh necessario.


def obter_entradas():
    """Solicita as entradas do usuário para letras verdes, amarelas e pretas."""
    
    while True:
        try:
            verdes = input("Digite as letras verdes (use '_' para espaços vazios, exemplo: 'a____'): ")
            if len(verdes) != 5 or not all(c.isalpha() or c == '_' for c in verdes):
                raise ValueError("As letras verdes devem ter exatamente 5 caracteres e conter apenas letras ou '_'.")
            
            amarelas = input("Digite as letras amarelas (use '_' para espaços vazios, exemplo: '__r__'): ")
            if len(amarelas) != 5 or not all(c.isalpha() or c == '_' for c in amarelas):
                raise ValueError("As letras amarelas devem ter exatamente 5 caracteres e conter apenas letras ou '_'.")
            
            pretas = input("Digite as letras pretas (todas juntas, exemplo: 'out'): ")
            if not all(c.isalpha() for c in pretas):
                raise ValueError("As letras pretas devem conter apenas letras.")

            # Se todas as entradas são válidas, saia do loop
            break

        except ValueError as e:
            print(e)
            print("Por favor, tente novamente.")

    # Transformar as strings em listas compatíveis
    v = [letra if letra.isalpha() else "" for letra in verdes]
    a = [letra if letra.isalpha() else "" for letra in amarelas]

    return v, a, pretas

def obter_entradas_terminal():
    """Entradas do terminal: verdes numa linha so e amarelas casa por casa."""

    while True:
        verdes = input("Letras verdes: ").strip().lower()
        # Aceita qualquer simbolo que nao seja letra/numero como espaco vazio.
        if len(verdes) == 5 and all(c.isalpha() or not c.isalnum() for c in verdes):
            break
        print("As letras verdes devem ter 5 caracteres, exemplo: 'cr_a_'.")

    v = [c if c.isalpha() else "" for c in verdes]

    a = []
    for casa in range(1, 6):
        while True:
            amarelas = input("Letras Amarelas " + str(casa) + " casa: ").strip().lower()
            if all(c.isalpha() for c in amarelas):
                break
            print("As letras amarelas devem conter apenas letras, exemplo: 'afr'.")
        a.append(amarelas)

    while True:
        pretas = input("Letras Pretas: ").strip().lower()
        if all(c.isalpha() for c in pretas):
            break
        print("As letras pretas devem conter apenas letras, exemplo: 'yhvz'.")

    return v, a, pretas

def obter_entrada_rodada():
    """Le as dicas de UMA tentativa. Tudo eh opcional: Enter deixa em branco."""

    while True:
        verdes = input("Letras verdes (Enter = nenhuma, exemplo: 'cr_a_'): ").strip().lower()
        if verdes == "":
            verdes = "_____"
        if len(verdes) == 5 and all(c.isalpha() or not c.isalnum() for c in verdes):
            break
        print("As letras verdes devem ter 5 caracteres, exemplo: 'cr_a_'.")

    v = [c if c.isalpha() else "" for c in verdes]

    a = []
    for casa in range(1, 6):
        while True:
            amarelas = input("Letras amarelas da " + str(casa) + "a casa (Enter = nenhuma): ").strip().lower()
            if all(c.isalpha() for c in amarelas):
                break
            print("As letras amarelas devem conter apenas letras, exemplo: 'afr'.")
        a.append(amarelas)

    while True:
        pretas = input("Letras pretas (Enter = nenhuma): ").strip().lower()
        if all(c.isalpha() for c in pretas):
            break
        print("As letras pretas devem conter apenas letras, exemplo: 'yhvz'.")

    return v, a, pretas


def mescla_dicas(v, a, pretas, novo_v, novo_a, novas_pretas):
    """Junta as dicas ja conhecidas com as da tentativa mais recente."""

    v = [novo_v[i] or v[i] for i in range(5)]

    # Cada casa guarda as letras que existem na palavra mas nao ficam ali.
    a = ["".join(dict.fromkeys(a[i] + novo_a[i])) for i in range(5)]

    pretas = "".join(dict.fromkeys(pretas + novas_pretas))

    # Uma letra confirmada como verde/amarela nunca pode contar como preta.
    conhecidas = set("".join(v) + "".join(a))
    pretas = "".join(letra for letra in pretas if letra not in conhecidas)

    return v, a, pretas


def processa_palavras(lista, v, a, pretas):
    """Processa a lista de palavras e retorna palavras possiveis com base nas letras pretas, verdes e amarelas."""
    possiveis = []
    texto_possiveis = ""

    vSoma = sum(len(letra) for letra in v)  # Contagem de letras verdes
    aSoma = sum(len(letra) for letra in a)  # Contagem de letras amarelas

    # Converte listas para estruturas mais rápidas
    pretas_set = set(pretas)
    verdes_posicoes = [(i, v[i]) for i in range(5) if v[i]]
    amarelas_posicoes = [(i, a[i]) for i in range(5) if a[i]]

    for palavra in lista:
        palavra = palavra.lower()
        if len(palavra) != 5:
            continue

        posicoes = [palavra[i] for i in range(5)]

        # Verifica letras pretas (usando conjunto para eficiência)
        if pretas_set & set(palavra):
            continue

        # Verifica letras verdes
        if not all(posicoes[i] == letra for i, letra in verdes_posicoes):
            continue

        # Verifica letras amarelas
        if not all(
            any(letra in palavra and posicoes[i] != letra for letra in letras_amarelas)
            for i, letras_amarelas in amarelas_posicoes
        ):
            continue

        possiveis.append(palavra)
        texto_possiveis += palavra

    return possiveis, texto_possiveis

def analisa_frequencia_letras(texto_possiveis):
    """Analisa a frequencia de cada letra nas palavras possiveis."""
    frequencia = {}
    for letra in texto_possiveis:
        frequencia[letra] = frequencia.get(letra, 0) + 1

    return sorted(frequencia.items(), key=lambda x: x[1], reverse=True)

def classifica_palavras_por_letras(possiveis, mLetras):
    """Classifica palavras possiveis com base na quantidade de letras em mLetras."""
    classificacao = {2: [], 3: [], 4: [], 5: [], "top": []}

    for palavra in possiveis:
        count = sum(1 for letra in mLetras if letra in palavra)
        if count >= 2:
            classificacao[min(count, 5)].append(palavra)
            if count > 5:
                classificacao["top"].append(palavra)

    return classificacao


if __name__ == "__main__":
    from baseDeDados import lista_wordle, lista_termo

    lista = None
    while lista == None:
        tipo = input("Wordle (w) / Termo (t): ")
        if tipo == 'w' or tipo == 'W':
            lista = lista_wordle
        elif tipo == 't' or tipo == 'T':
            lista = lista_termo
        else:
            print("USE UMA DAS QUE PASSEI!")

    # Solicitar entradas do usuário
    v, a, pretas = obter_entradas()

    # Processar palavras
    possiveis, texto_possiveis = processa_palavras(lista, v, a, pretas)

    # Analisar frequência de letras
    frequencia_letras = analisa_frequencia_letras(texto_possiveis)
    mLetras = [letra for letra, _ in frequencia_letras[:5]]

    # Classificar palavras
    classificacao = classifica_palavras_por_letras(possiveis, mLetras)

    # Exibir resultados
    print("Palavras possíveis:", possiveis)
    print("Classificação por letras:", classificacao)

