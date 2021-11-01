
def check_difficulty(word):

    #========================
    #Factor 1 - check repeated consonants/vowels
    #========================

    vowels = ('A', 'Ā', 'E', 'Ē', 'I', 'Ī', 'U', 'Ū', 'O')

    changed_word = word

    for index, letter in enumerate(changed_word):
        if letter in vowels:
            #replace all vowels with number 1
            changed_word = changed_word.replace(letter, str(1))
        else:
            #replace all consonants with number 2
            changed_word = changed_word.replace(letter, str(2))

    def repeated_letters(letters):
        i = 0
        repeats = 0
        while i <= len(changed_word):
            index = changed_word.find(letters, i)
            if not index == -1:
                repeats += 1
                i = index + 1
            else:
                i += 1
        return repeats

    repeated_vowels = repeated_letters('11') * 0.5
    repeated_consonants = repeated_letters('22')

    #========================
    #Factor 2 - check word length
    #========================

    word_length = len(word) * 0.3

    #========================
    #Factor 3 - check letter frequency
    #========================

    frequency_table = {
        'A' : 0.1178,
        'I' : 0.0933,
        'S' : 0.0806,
        'E' : 0.0615,
        'T' : 0.0604,
        'R' : 0.0558,
        'U' : 0.0516,
        'N' : 0.043,
        'Ā' : 0.0409,
        'K' : 0.0392,
        'O' : 0.0385,
        'M' : 0.0354,
        'L' : 0.0344,
        'D' : 0.0303,
        'P' : 0.0289,
        'V' : 0.0284,
        'J' : 0.0255,
        'Ī' : 0.0192,
        'Z' : 0.0182,
        'B' : 0.0167,
        'G' : 0.0167,
        'Ē' : 0.0166,
        'C' : 0.0119,
        'Š' : 0.0095,
        'Ļ' : 0.004,
        'Ū' : 0.004,
        'Ņ' : 0.0038,
        'F' : 0.0033,
        'H' : 0.0022,
        'Ž' : 0.0021,
        'Ģ' : 0.0016,
        'Ķ' : 0.0014,
        'Č' : 0.0008
    }

    changed_word = set(word) #change to unique letters
    letter_frequency = 0
    for index, letter in enumerate(changed_word):
        letter_frequency += 1 / frequency_table[letter]
    
    #normalize the frequency using interpolation to assign values from 1 to 10
    letter_frequency = 1 + (letter_frequency - 40) * (10 - 1) / (1500 - 40) # 40 ir novērotā MIN vērtība, 1500 ir novērotā MAX vērtība
    #print(word + f': {letter_frequency}')

    #========================
    #Factor 4 - check word frequency
    #========================

    #import wikipedia
    #wikipedia.set_lang('lv')
    #wikipedia_text = wikipedia.page('America').content.split(' ')
    #the_word = 'Amerika'
    #word_frequency = 0
    #for any_word in wikipedia_text:
    #    if any_word == the_word:
    #        word_frequency += 1
    #print(f'Word {the_word} frequency: {word_frequency}')

    #import requests
    #import re
    #from bs4 import BeautifulSoup

    #urls = ['https://lv.wikipedia.org/wiki/Special:Random']
    #the_word = 'and'
    #for url in urls:
    #    print(url)
    #    r = requests.get(url, allow_redirects=False)
    #    soup = BeautifulSoup(r.text, 'html.parser')
    #    word_frequency = soup.find_all(text = re.compile(the_word))
    #    print(len(word_frequency))

    #calculate the total difficulty score
    difficulty_score = repeated_vowels + repeated_consonants + word_length + letter_frequency
    return difficulty_score