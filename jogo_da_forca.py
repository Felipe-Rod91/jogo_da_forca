import random

# Banco de palavras, palavra escolhida pela máquina e letras ditas pelo jogador
banco_de_palavras = ['python', 'javascript', 'computador', 'monitor', 'mouse', 'java', 'teclado']
palavra_certa = random.choice(banco_de_palavras)
palavra_certa = palavra_certa.upper()
letras_jogadas = []
tentativas = 7
venceu = False

# Tentativa do jogador e a palavra escondida
while True:
    for letra in palavra_certa:
        if letra in letras_jogadas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()
    while True:
        letra_escolhida = str(input('Digite uma letra: ')).upper()
        if letra_escolhida in letras_jogadas:
            print('Esta letra já foi jogada.')
        else:
            letras_jogadas.append(letra_escolhida)
            break
