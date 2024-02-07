import random

# Game setup and data base
data_base = ['python', 'javascript', 'computer', 'monitor', 'mouse', 'java', 'keyboard', 'windows', 'linux',
            'macbook', 'apple', 'microsoft', 'netword', 'support', 'file', 'error', 'bug']
hidden_word = random.choice(data_base).upper()
letters = []
chances = 7
win = False

# Hidden word
while True:
    for l in hidden_word:
        if l in letters:
            print(l, end=' ')
        else:
            print('_', end=' ')
    print()

    # Guessing system
    while True:
        letter = str(input('Type any letter: ').upper())
        if letter in letters:
            print('You already tried this letter. Try another one.')
        else:
            letters.append(letter)
            if letter not in hidden_word:
                chances -= 1
                if chances > 0:
                    print(f'WRONG! You got {chances} more chances.')
            win = True
            for l in hidden_word:
                if l not in letters:
                    win = False
        break

    # Win or lose messages
    if chances == 0:
        print(f'SORRY, YOU LOST! THE HIDDEN WORD WAS "{hidden_word}".')
        break
    if win:
        print(f'CONGRATULATIONS! THE HIDDEN WORD WAS "{hidden_word}".')
        break
