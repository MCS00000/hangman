from gameplay.game2 import Game
from scripts.difficulty import check_difficulty
from random import shuffle
from scripts.timer import countdown

print('\nSveiciens karātavās!')

while True:
    difficulty = input('\nIeraksti spēles grūtības pakāpi (viegli / vidēji / grūti): ').upper()
    if difficulty == 'VIEGLI':
        with open('data/easy_words.txt', 'r', encoding = 'utf-8') as file:
            words = file.read()
    elif difficulty == 'VIDĒJI':
        with open('data/medium_words.txt', 'r', encoding = 'utf-8') as file:
            words = file.read()
    elif difficulty == 'GRŪTI':
        with open('data/hard_words.txt', 'r', encoding = 'utf-8') as file:
            words = file.read()
    else:
        print('Grūtības pakāpe tika nepareizi ievadīta, mēģini vēlreiz!')
        continue
    print(f'\nJAUNA SPĒLES PARTIJA - būs {difficulty}!\n')
    words = words.split('\n')
    shuffle(words)
    word = words.pop()
    #check difficulty of word
    #difficulty_score = check_difficulty(word)
    #print result
    #print(f'Vārda grūtības indekss: {difficulty_score}')
    game = Game(word)
    game.play()
    t = 5
    countdown(int(t))


