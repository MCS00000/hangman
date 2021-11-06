import requests
from bs4 import BeautifulSoup

def get_hint(word):
    url = requests.get(f'https://tezaurs.lv/{word}')
    soup = BeautifulSoup(url.content, 'html.parser')
    hint = ''
    for glossary in soup.find_all('span', class_="dict_Gloss"):
        hint += f'- {glossary.text}\n'
    if hint == '':
        print('Vārda skaidrojums nav atrasts!')
    else:
        print(f'Vārda skaidrojums ir:\n{hint}')