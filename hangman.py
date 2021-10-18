from gameplay.game2 import Game
from random import shuffle
with open('data/words.txt', 'r', encoding = 'utf-8') as file:
    words = file.read()
words = words.split('\n')
shuffle(words)
while True:
    word = words.pop()
    game = Game(word)
    print('\n' + 'JAUNA SPĒLES PARTIJA' + '\n')
    game.play()


