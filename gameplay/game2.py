"""Klases Game definīcija un spēles skelets.

Klase Game tiek importēta iekš moduļa hangman. Tiek noteikti galvenie 
atribūti un spēles noteikumi,kas uz tiem ir balstīti. Tiek importēts 
get_hint kā papildu funkcija spēlē.
"""

from scripts.clear_screen import clear

from scripts.word_hint import get_hint


class Game:

    
    """Klase Game satur spēles objektu kopumu.

    Attributes:
        minamais_vards: Jebkurš vārds ņemts no dotās datu bāzes, kas 
        tiek iekļauts spēles funkcijās.
        progress: Tajā norādīts minamā vārda atminētais un neatminētais 
        apjoms burtu un simbolu izteiksmē.
        dzivibas: Spēlētāja dzīvību skaits, kas sākas ar 6 un tiek 
        samazināts par 1 par katru nepareizo minējumu kā arī 
        izmantojot help.
        uzminets: Boolean vērtība, kura nav patiesa līdz brīdim, kad 
        vārds tiek atminēts
        minetie_burti: Saraksts ar spēles partijā minētajiem burtiem
        minetie_vardi: Saraksts ar spēles partijā minētajiem vārdiem
    """
    
    def __init__(self, vards, valoda):
        self.minamais_vards = vards.upper()
        self.progress = list(len(self.minamais_vards) * '-')
        self.dzivibas = 6
        self.uzminets = False
        self.minetie_burti = []
        self.minetie_vardi = []
        self.valoda = valoda

    def play(self):
        
        """Palaiž spēles ciklus, kas pieņem lietotāja ievadi.
        
        Tiek palaists cikls, kas turpina atkārtoties, kamēr spēlētājam 
        ir dzīvības vai vārds netiek atminēts.
        Katrā ciklā spēlētājs veic minamā burta vai vārda ievadi, kura 
        tiek pārbaudīta un saglabāta vēsturē.
        Veicot veiksmīgu minējumu, tiek atainots progress. Veicot 
        neveiksmīgu minējumu, tiek atņemta dzīvība.
        Ciklam beidzoties, tiek izvadīts vai nu uzvaras vai zaudēšanas 
        paziņojums.
        
        Args:
            Nav argumentu
        Returns:
            Neko - rezultāts tiek izdrukāts ar print.
        Raises:
            Nav izņēmuma paziņojumu.   
        """

        print('Minamais vārds ir ' + ''.join(self.progress) + ' un tā garums'
              f' ir {len(self.minamais_vards)} burti. Tev ir {self.dzivibas}'
              ' dzīvības. Lai veicas!')

        while self.dzivibas > 0 and self.uzminets == False:
            # At the beginning of each guess the player's overall
            # progress has to be displayed at the top of the screen.
            print('\nTavs progress: ' + ''.join(self.progress))
            print('Atlikušās dzīvības: ' + "\u2665 " * self.dzivibas)
            print('Minētie vārdi: ' + ', '.join(self.minetie_vardi))           
            print('Minētie burti: ' + ', '.join(self.minetie_burti) + '\n')
            print('Papildus komandas:')
            print('    HELP! - ja vēlies maksas padomu')
            print('    STOP! - ja vēlies pamest spēli pavisam\n')
            burts_atrasts = False
            ievade = input('Ievadi minamo burtu vai vārdu'
                           ' (vai papildus komandu): ').upper()
            clear()
            # Empty input is not valid.
            if len(ievade) == 0:
                print('Nekas netika ievadīts, mēģini vēlreiz!')
                continue
            # A valid input is a single letter or a word.  Input with
            # 1 letter will always represent a guessed letter and
            # must be evaluated separately.
            elif len(ievade) == 1:
                if ievade.isalpha():
                    if ievade in self.minetie_burti:
                        print('Burts ir jau minēts, mēģini vēlreiz!')
                    else:
                        for index, burts in enumerate(self.minamais_vards):
                            if ievade == burts:
                                burts_atrasts = True
                                self.progress[index] = ievade
                        if burts_atrasts:
                            print('Burts ir šajā vārdā!')
                        else:
                            # The player is being punished for an
                            # incorrect letter guess.
                            self.dzivibas -= 1
                            print(f'Šī burta vārdā nav - zaudēta dzīvība!')
                        self.minetie_burti.append(ievade)
                else:
                    print('Nav ievadīts burts!')
            # Input with a word can represent either a specific
            # predefined command or a guessed word.
            else:
                # This section handles predefined commands.
                if ievade == 'HELP!':
                    # The player is being punished for using help.
                    self.dzivibas -= 1
                    print('Iztērēta dzīvība par padomu!')
                    get_hint(self.minamais_vards.lower(), self.valoda)
                elif ievade == 'STOP!':
                    print('Spēle pārtraukta!')
                    raise SystemExit
                # This section handles guessed words.
                elif (len(self.minamais_vards) == len(ievade) and
                      ievade.isalpha()):
                    if ievade in self.minetie_vardi:
                        print('Vārds ir jau minēts, mēģini vēlreiz!')
                    else:
                        if ievade == self.minamais_vards:
                            self.uzminets = True
                            print('Vārds atminēts!')
                            # The player is being rickrolled when the
                            # word has been guessed.  Import command
                            # must remain here since the expected
                            # actions are performed at the time of
                            # import. 
                            import rickroll
                        else:
                            # The player is being punished for an
                            # incorrect word guess.
                            self.dzivibas -= 1
                            print('Šis nav pareizais vārds'
                                  ' - zaudēta dzīvība!') 
                        self.minetie_vardi.append(ievade)
                else:
                    print('Vārds ievadīts nepareizi!')
            if self.dzivibas == 0:
                print('Spēle zaudēta! Pareizais vārds bija'
                      f' {self.minamais_vards}!')
                break    
            if self.progress == list(self.minamais_vards):
                self.uzminets = True
                print('Vārds atminēts!')
                # The player is being also rickrolled when all the
                # letters in the word have been guessed.  Import
                # command also must remain here for the code to work.
                import rickroll
                break