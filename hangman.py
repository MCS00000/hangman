from gameplay.game2 import Game
from scripts.difficulty import check_difficulty
from random import shuffle
with open('data/words.txt', 'r', encoding = 'utf-8') as file:
    words = file.read()
words = words.split('\n')
shuffle(words)
while True:
    word = words.pop()
    #word = input('Vārds: ')
    #check difficulty of word
    difficulty_score = check_difficulty(word)
    print(f'Vārda grūtības indekss: {difficulty_score}')
    #print result
    game = Game(word)
    print('\n' + 'JAUNA SPĒLES PARTIJA' + '\n')
    game.play()


