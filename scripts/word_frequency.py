
import requests

from bs4 import BeautifulSoup
from nltk import word_tokenize

with open('../data/words.txt', 'r', encoding = 'utf-8') as file:
    words = file.read()
words = words.split('\n')
words.append('UN')
words.append('VAI')
words.append('IR')


wiki_text = ''
for i in range(3):
    url = requests.get('https://lv.wikipedia.org/wiki/Special:Random')
    soup = BeautifulSoup(url.content, 'html.parser')
    for paragraph in soup.find_all('p'):
        wiki_text += paragraph.text
    print(wiki_text)

wiki_words = [w.upper() for w in word_tokenize(wiki_text)
              if w.isalpha() and len(w) > 1]
for word in words:
    word_frequency = 0
    for wiki_word in wiki_words:
        if wiki_word == word:
            word_frequency += 1
    print(f'{word} frequency: {word_frequency}')