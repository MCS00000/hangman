""" 
No Game2 moduļa tiek importēti galvenie spēles noteikumi un atribūti 
caur klasi Game. 
Izmantojot standarta bibliotēkas 'random' moduļa funkciju 'shuffle', 
sajaucam datu struktūru.
Funkcija countdown, no moduļa timer ir taimeris.
"""
import requests
from random import shuffle

from scripts.clear_screen import clear
from scripts.timer import countdown
from gameplay.game2 import Game

clear()
print('\nSveiciens karātavās!')

while True:
    # There are 2 word sources available for the player to choose from.
    source = input('\nIzvēlies spēles vārdu avotu (1 - lokālā latviešu vārdu '
                   'datubāze / 2 - nejauši izvēlēts angļu vārds no API): ')
    if source == '1':   
        while True:
            difficulty = input('\nIeraksti spēles grūtības pakāpi (viegli / '
            'vidēji / grūti): ').upper()
            if difficulty == 'VIEGLI':
                try:
                    with open('data/easy_words.txt', 'r', encoding = 'utf-8')\
                     as file:
                        words = file.read()
                except FileNotFoundError:
                    print('\nKļūda! Nav atrasts fails "easy_words.txt"! '
                    'Programma beidzas.')
                    raise SystemExit
                break
            elif difficulty == 'VIDĒJI':
                try:
                    with open('data/medium_words.txt', 'r', encoding = 'utf-8\
                    ') as file:
                        words = file.read()
                except FileNotFoundError:
                    print('\nKļūda! Nav atrasts fails "medium_words.txt"! '
                    'Programma beidzas.')
                    raise SystemExit
                break
            elif difficulty == 'GRŪTI':
                try:
                    with open('data/hard_words.txt', 'r', encoding = 'utf-8')\
                 as file:
                        words = file.read()
                except FileNotFoundError:
                    print('\nKļūda! Nav atrasts fails "hard_words.txt"! '
                    'Programma beidzas.')
                    raise SystemExit
                break
            else:
                print('Grūtības pakāpe tika nepareizi ievadīta, mēģini '
                'vēlreiz!')
                continue
        if not words:
            raise Exception('Kļūda! Ielasītais fails ir tukšs! Programma '
            'beidzas.')
        # Contents have to be split because the database file contains
        # each word in a separate line.
        words = words.split('\n')
        shuffle(words)
        break
    elif source == '2':
        break
    else:
        print('Vārdu avots tika nepareizi ievadīts, mēģini vēlreiz!')
        continue

clear()  # Each round must begin with a clean screen.

while True:
    if source == '1':
        try:
            word = words.pop()
        except IndexError:
            print('\nVārdu vairāk nav! Spēle beidzas!')
            break
        print('\nJauna spēles partija ar latviešu vārdu ar grūtības '
        f'pakāpi: {difficulty}!\n')
    elif source == '2':
        response = requests.get('https://random-word-api.herokuapp.com/word?'
        'number=1&swear=0')
        word = response.json()[0]
        print('\nJauna spēles partija ar nejauši izvēlētu angļu vārdu.\n')
    game = Game(word, source)
    game.play()
    # A 5 second pause is added between each round.
    t = 5
    countdown(int(t))


