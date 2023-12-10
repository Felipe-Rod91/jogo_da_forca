import random

# Banco de palavras, palavra escolhida pela máquina e letras ditas pelo jogador
banco_de_palavras = ['python', 'javascript', 'computador', 'monitor', 'mouse', 'java', 'teclado']
palavra_certa = random.choice(banco_de_palavras)
letras_jogador = []
tentativas = 7

# Tentativa do jogador e a palavra escondida
for letra in palavra_certa:
    print('_', end=' ')
