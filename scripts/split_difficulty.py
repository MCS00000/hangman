"""No moduļa difficulty importē funkciju check_difficulty, kas sadala failos minamos vārdus pēc norādītās grūtības pakāpes.
Ir definētas trīs grūtības pakāpes - easy_words, medium_words, hard_words.
Vārdi tiek ielasīti no words.txt un izmantojot split metodi sadalīti sarakstos.
Izmantojot pop metodi vārdi tiek iedalīti atbilstošā sarakstā izmantojot mainīgo difficulty_score.
"""
from difficulty import check_difficulty

easy_words = []
medium_words = []
hard_words = []

with open('../data/words.txt', 'r', encoding = 'utf-8') as file:
    words = file.read()
words = words.split('\n')

while len(words) != 0:
    word = words.pop()
    difficulty_score = check_difficulty(word)
    if difficulty_score <=6:
        #easy
        easy_words.append(word)
    elif difficulty_score <=8:
        #med
        medium_words.append(word)
    else:
        #hard
        hard_words.append(word)

#papildina txt failus
with open('../data/easy_words.txt', 'w', encoding = 'utf-8') as file:
    file.write('\n'.join(easy_words))
with open('../data/medium_words.txt', 'w', encoding = 'utf-8') as file:
    file.write('\n'.join(medium_words))
with open('../data/hard_words.txt', 'w', encoding = 'utf-8') as file:
    file.write('\n'.join(hard_words))