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

def get_hint(word, language):
    """Atrod un izdrukā ievadītā vārda skaidrojumu.

    Atrod ievadītā vārda skaidrojumu tēzaurā un izdrukā to lietotājam.
    Skaidrojums tiek meklēts 2 dažādos tēzauros atkarībā no vārda valodas.
    Ja skaidrojumu neatrod, tad tiek izdrukāts attiecīgs paziņojums.
    
    Args:
        word: Vārds, kuram vēlas atrast skaidrojumu.
        language: Skaidrojamā vārda valoda.
    Returns:
        Neko - rezultāts tiek izdrukāts ar print.
    Raises:
        KeyError - lai apstrādātu angļu valodas tēzaura API atgriezto tukšo ierakstu.
    """
    hint = ''
    if language == '1':
        url = requests.get(f'https://tezaurs.lv/{word}')
        soup = BeautifulSoup(url.content, 'html.parser')
        for glossary in soup.find_all('span', class_="dict_Gloss"):
            hint += f'- {glossary.text}\n'
    else:
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        returned_list = response.json()
        try:
            returned_dict = returned_list[0]
            meanings_list = returned_dict['meanings']
            hint = ''
            for i in range(len(meanings_list)):
                meanings_dict = meanings_list[i]
                definitions_list = meanings_dict['definitions']
                definitions_dict = definitions_list[0]
                definition = definitions_dict['definition']
                hint += f'- {definition}\n'
        except KeyError:
            hint = ''
    if hint == '':
        print('Vārda skaidrojums nav atrasts!')
    else:
        print(f'Vārda skaidrojums ir:\n{hint}')