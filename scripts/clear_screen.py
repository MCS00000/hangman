"""Šis modulis notīra ekrānu.

Modulis notīra līdz šim izvadīto tekstu no ekrāna.
Tas sastāv no vienas funkcijas: clear, ko eksportē uz moduļiem hangman un game2.
"""
import os

def clear():
    """Notīra ekrānu.

    Notīra līdz šim izvadīto tekstu no ekrāna neatkarīgi no lietotāja OS tipa.
    
    Args:
        Nav argumentu.
    Returns:
        Neko neatgriež.
    Raises:
        Nav izņēmuma paziņojumu.
    """
    os.system('cls' if os.name=='nt' else 'clear')