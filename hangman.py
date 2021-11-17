""" 
No Game2 moduļa tiek importēti galvenie spēles noteikumi un atribūti caur klasi Game. 
Izmantojot standarta bibliotēkas 'random' moduļa funkciju 'shuffle', sajaucam datu struktūru.
Funkcija countdown, no moduļa timer ir taimeris.
"""

from gameplay.game2 import Game
from random import shuffle
from scripts.timer import countdown

print('\nSveiciens karātavās!')

while True:
    difficulty = input('\nIeraksti spēles grūtības pakāpi (viegli / vidēji / grūti): ').upper()
    if difficulty == 'VIEGLI':
        try:
            with open('data/easy_words.txt', 'r', encoding = 'utf-8') as file:
                words = file.read()
        except FileNotFoundError:
            print('\nKļūda! Nav atrasts fails "easy_words.txt"! Programma beidzas.')
            raise SystemExit
        break
    elif difficulty == 'VIDĒJI':
        try:
            with open('data/medium_words.txt', 'r', encoding = 'utf-8') as file:
                words = file.read()
        except FileNotFoundError:
            print('\nKļūda! Nav atrasts fails "medium_words.txt"! Programma beidzas.')
            raise SystemExit
        break
    elif difficulty == 'GRŪTI':
        try:
            with open('data/hard_words.txt', 'r', encoding = 'utf-8') as file:
                words = file.read()
        except FileNotFoundError:
            print('\nKļūda! Nav atrasts fails "hard_words.txt"! Programma beidzas.')
            raise SystemExit
        break
    else:
        print('Grūtības pakāpe tika nepareizi ievadīta, mēģini vēlreiz!')
        continue

if not len(words):
    raise Exception('Kļūda! Ielasītais fails ir tukšs! Programma beidzas.')

words = words.split('\n')
shuffle(words)

while True:
    try:
        word = words.pop()
    except IndexError:
        print('Vārdu vairāk nav! Spēle beidzas!')
        break
    print(f'\nJauna spēles partija ar grūtības pakāpi: {difficulty}!\n')
    game = Game(word)
    game.play()
    t = 5
    countdown(int(t))


