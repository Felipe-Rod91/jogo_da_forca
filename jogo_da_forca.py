import random

# Banco de palavras, palavra aleatória escolhida pelo computador e lista de letras ditas pelo jogador
banco_de_palavras = ['python', 'javascript', 'computador', 'monitor', 'mouse', 'java', 'teclado', 'windows', 'linux',
                     'macbook', 'apple', 'microsoft', 'rede', 'suporte', 'ligar', 'desligar', 'pasta', 'painel',
                     'erro', 'bug', 'qualidade']
palavra_certa = random.choice(banco_de_palavras)
palavra_certa = palavra_certa.upper()
letras_jogadas = []
tentativas = 7
venceu = False

# Palavra escondida com as letras que já foram acertadas
while True:
    for letra in palavra_certa:
        if letra in letras_jogadas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

    # Letras que o usuário tenta acertar
    while True:
        letra_escolhida = str(input('Digite uma letra: ').upper())
        if letra_escolhida in letras_jogadas:
            print('Esta letra já foi jogada. Tente outra.')
        else:
            letras_jogadas.append(letra_escolhida)
            if letra_escolhida not in palavra_certa:
                tentativas -= 1
                if tentativas > 0:
                    print(f'ERROU! Você tem mais {tentativas} tentativas.')
            venceu = True
            for letra in palavra_certa:
                if letra not in letras_jogadas:
                    venceu = False
        break

    # Final com mensagens se o jogador ganhou ou perdeu
    if tentativas == 0:
        print(f'Que pena, você perdeu! A palavra era {palavra_certa}.')
        break
    if venceu:
        print(f'Parabéns, você ganhou! A palavra certa era {palavra_certa}.')
        break

