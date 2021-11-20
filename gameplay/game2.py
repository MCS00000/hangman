"""Klases Game definīcija un spēles skelets.

Klase Game tiek importēta iekš moduļa hangman. Tiek noteikti galvenie atribūti un spēles noteikumi,
kas uz tiem ir balstīti. Tiek importēts get_hint kā papildu funkcija spēlē.
"""

from scripts.word_hint import get_hint
from scripts.clear_screen import clear

class Game:
    """Klase Game satur spēles objektu kopumu.

    Attributes:
        minamais_vards: Jebkurš vārds ņemts no dotās datu bāzes, kas tiek iekļauts spēles funkcijās.
        progress: Tajā norādīts minamā vārda atminētais un neatminētais apjoms burtu un simbolu izteiksmē.
        dzivibas: Spēlētāja dzīvību skaits, kas sākas ar 6 un tiek samazināts par 1 par katru nepareizo minējumu kā arī izmantojot help.
        uzminets: Boolean vērtība, kura nav patiesa līdz brīdim, kad vārds tiek atminēts
        minetie_burti: Saraksts ar spēles partijā minētajiem burtiem
        minetie_vardi: Saraksts ar spēles partijā minētajiem vārdiem
    """
    def __init__(self, vards, valoda):
        self.minamais_vards = vards.upper()
        self.progress = list(len(self.minamais_vards) * '-')
        self.dzivibas = 6
        self.uzminets = False
        self.minetie_burti = []
        self.minetie_vardi= []
        self.valoda = valoda

    def play(self):
        """Palaiž spēles ciklus, kas pieņem lietotāja ievadi.
        
        Tiek palaists cikls, kas turpina atkārtoties, kamēr spēlētājam ir dzīvības vai vārds netiek atminēts.
        Katrā ciklā spēlētājs veic minamā burta vai vārda ievadi, kura tiek pārbaudīta un saglabāta vēsturē.
        Veicot veiksmīgu minējumu, tiek atainots progress. Veicot neveiksmīgu minējumu, tiek atņemta dzīvība.
        Ciklam beidzoties, tiek izvadīts vai nu uzvaras vai zaudēšanas paziņojums.
        
        Args:
            Nav argumentu
        Returns:
            Neko - rezultāts tiek izdrukāts ar print.
        Raises:
            Nav izņēmuma paziņojumu.   
        """

        print('Minamais vārds ir ' + ''.join(self.progress) + f' un tā garums ir {len(self.minamais_vards)} burti. Tev ir {self.dzivibas} dzīvības. Lai veicas!')

        while self.dzivibas > 0 and self.uzminets == False:
            print('\nTavs progress: ' + ''.join(self.progress))
            print('Atlikušās dzīvības: ' + "\u2665 " * self.dzivibas)
            print('Minētie vārdi: ' + ', '.join(self.minetie_vardi))           
            print('Minētie burti: ' + ', '.join(self.minetie_burti) + '\n')
            print('Papildus komandas:')
            print('    HELP! - ja vēlies maksas padomu')
            print('    STOP! - ja vēlies pamest spēli pavisam\n')
            burts_atrasts = False
            ievade = input('Ievadi minamo burtu vai vārdu (vai papildus komandu): ').upper()
            clear()
            if len(ievade) == 0:
                print('Nekas netika ievadīts, mēģini vēlreiz!')
                continue
            elif len(ievade) == 1: #ir ievadīts 1 simbols
                if ievade.isalpha(): #ir ievadīts burts (pēc satura)
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
                            self.dzivibas -= 1
                            print(f'Šī burta vārdā nav - zaudēta dzīvība!')
                        self.minetie_burti.append(ievade)
                else:
                    print('Nav ievadīts burts!')
            else: #ir ievadīti vairāki simboli
                if ievade == 'HELP!':
                    self.dzivibas -= 1
                    print('Iztērēta dzīvība par padomu!')
                    get_hint(self.minamais_vards.lower(), self.valoda)
                elif ievade == 'STOP!':
                    print('Spēle pārtraukta!')
                    raise SystemExit
                elif len(self.minamais_vards) == len(ievade) and ievade.isalpha():
                    if ievade in self.minetie_vardi:
                        print('Vārds ir jau minēts, mēģini vēlreiz!')
                    else:
                        if ievade == self.minamais_vards:
                            self.uzminets = True
                            print('Vārds atminēts!')
                            import rickroll
                        else:
                            self.dzivibas -= 1
                            print(f'Šis nav pareizais vārds - zaudēta dzīvība!') 
                        self.minetie_vardi.append(ievade)
                else:
                    print('Vārds ievadīts nepareizi!')
            if self.dzivibas == 0:
                print(f'Spēle zaudēta! Pareizais vārds bija {self.minamais_vards}!')
                break    
            if self.progress == list(self.minamais_vards):
                self.uzminets = True
                print('Vārds atminēts!')
                import rickroll
                break