"""Šis modulis aprēķina vārda grūtības pakāpi.

Modulis saņemtam vārdam aprēķina grūtības pakāpi, izmantojot vairākus 
parametriskus faktorus.
Tas sastāv no vienas funkcijas: check_difficulty, ko eksportē uz moduli
split_difficulty.
Modulis saņemto vārdu analizē uzreiz un atgriež rezultātu.

    Tipisks pielietojuma piemērs:

    word_to_check = 'random_word'
    check_difficulty(word_to_check)
"""


def check_difficulty(word):
    """Funkcija saskaita vārda grūtības līmeni.

    Vārda grūtības līmenis tiek saskaitīts izmantojot vairākus svērtus 
    kritērijus.
    Rezultātā katram vārdam tiek piešķirts skaitlis, kas raksturo to 
    grūtību un ļauj to ievietot kādā no vārdu uzglabāšanas failiem 
    atkarībā no tā grūtības pakāpes.

    Args:
        word: Vārds, kura grūtums tiek pārbaudīts
    Returns: 
        Vārda grūtības pakāpe
    Raises:
        Nav izņēmuma paziņojumu.
    """
    # Multiple factors must be checked.  Factor 1 evaluates repeated
    # vowels and repeated consonants.  Based on the number of
    # repeats, a factor score is calculated.

    vowels = ('A', 'Ā', 'E', 'Ē', 'I', 'Ī', 'U', 'Ū', 'O')

    changed_word = word

    for index, letter in enumerate(changed_word):
        if letter in vowels:
            # In order to analyze the word, all vowels must be
            # identifiable, so all are replaced with number 1.
            changed_word = changed_word.replace(letter, str(1))
        else:
            # Similarly all consonants must be replaced with number 2.
            changed_word = changed_word.replace(letter, str(2))

    def repeated_letters(letters):
        """Funkcija analizē vārdus izmantojot mainīgo,
        kas definē burtu.
        Funkcija parāda, cik reižu burts atkārtojas vārdā.
        """
        i = 0
        repeats = 0
        while i <= len(changed_word):
            index = changed_word.find(letters, i)
            if index != -1:
                repeats += 1
                i = index + 1
            else:
                i += 1
        return repeats

    # Score for factor 1 is calculated (consists of 2 components).
    repeated_vowels = repeated_letters('11') * 0.5
    repeated_consonants = repeated_letters('22')

    # Factor 2 evaluates word length. The longer the word, the
    # higher the score.  Factor 2 score is calculated directly.

    word_length = len(word) * 0.3

    # Factor 3 evaluates letter usage frequency within Latvian
    # language.  A fixed frequency table is being used.  The more
    # frequent the letter the higher the lower the score.

    frequency_table = {
        'A': 0.1178,
        'I': 0.0933,
        'S': 0.0806,
        'E': 0.0615,
        'T': 0.0604,
        'R': 0.0558,
        'U': 0.0516,
        'N': 0.043,
        'Ā': 0.0409,
        'K': 0.0392,
        'O': 0.0385,
        'M': 0.0354,
        'L': 0.0344,
        'D': 0.0303,
        'P': 0.0289,
        'V': 0.0284,
        'J': 0.0255,
        'Ī': 0.0192,
        'Z': 0.0182,
        'B': 0.0167,
        'G': 0.0167,
        'Ē': 0.0166,
        'C': 0.0119,
        'Š': 0.0095,
        'Ļ': 0.004,
        'Ū': 0.004,
        'Ņ': 0.0038,
        'F': 0.0033,
        'H': 0.0022,
        'Ž': 0.0021,
        'Ģ': 0.0016,
        'Ķ': 0.0014,
        'Č': 0.0008
    }

    # Only the unique letters must be taken into account.
    changed_word = set(word)
    letter_frequency = 0
    for index, letter in enumerate(changed_word):
        # The inverse value of frequency is needed, since the factor
        # has to be of higher value (= more difficult) when the letter
        # is less frequent.
        letter_frequency += 1 / frequency_table[letter]
    
    # The resulting frequency value must be normalized using
    # interpolation because the direct results are within a broad
    # range.  The values are reassigned in a range from 1 to 10.
    # Here the observed minimum and maximum values before
    # normalization are used (40 is the minimum and 1500 is the
    # maximum) for interpolation.
    letter_frequency_norm = 1 + (letter_frequency-40) * (10-1) / (1500-40)

    # The total difficulty score consists of each factor's score.
    difficulty_score = (repeated_vowels 
                        + repeated_consonants
                        + word_length
                        + letter_frequency_norm)
    return difficulty_score