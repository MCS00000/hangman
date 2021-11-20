"""Funkcija, kas atskaita laiku starp spēles raundiem.

Izmantojot importēto moduli time tiek izveidota funkcija, kas tiek eksportēta uz hangman.py.
Šī funkcija darbojas kā taimeris, kurš ik pēc sekundes, nodzēšot iepriekšējo vērtību un tādējādi
nemainot rindiņas, izvada atlikušo laiku. Tiek veikta 5 sekunžu atskaita, kuru laikā citas darbības nav redzamas.
"""

import time


def countdown(t):
    """Atskaita 5 sekundes starp spēles raundiem

    Args:
        t: Laiks sekundēs
    Returns:
        Atlikušās sekundes līdz nākošajam raundam.
    Raises:
        Nav nepieciešama lietotāja ievade, tādēļ bez kļūdām
    """
    while t > -1:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('Nākamā partija sāksies pēc: ' + timer, end ="\r")
        time.sleep(1)
        t -= 1
