"""Šis modulis atrod un izdrukā vārda skaidrojumu.

Modulis lietotāja ievadītam vārdam tiešsaistē atrod skaidrojumu tēzaurā un izdrukā to lietotājam.
Tas sastāv no vienas funkcijas: get_hint, ko eksportē uz moduli game2.
Modulis izmanto 3. puses pakotni BeautifulSoup un tā izpildei ir nepieciešams interneta pieslēgums.

    Tipisks pielietojuma piemērs:

    word_to_check = 'random_word'
    get_hint(word_to_check)
"""
import requests
from bs4 import BeautifulSoup

def get_hint(word):
    """Atrod un izdrukā ievadītā vārda skaidrojumu.

    Atrod ievadītā vārda skaidrojumu tēzaurā un izdrukā to lietotājam.
    Ja skaidrojumu neatrod, tad tiek izdrukāts attiecīgs paziņojums.
    
    Args:
        word: Vārds, kuram vēlas atrast skaidrojumu.
    Returns:
        Neko - rezultāts tiek izdrukāts ar print.
    Raises:
        Nav izņēmuma paziņojumu.
    """
    url = requests.get(f'https://tezaurs.lv/{word}')
    soup = BeautifulSoup(url.content, 'html.parser')
    hint = ''
    for glossary in soup.find_all('span', class_="dict_Gloss"):
        hint += f'- {glossary.text}\n'
    if hint == '':
        print('Vārda skaidrojums nav atrasts!')
    else:
        print(f'Vārda skaidrojums ir:\n{hint}')