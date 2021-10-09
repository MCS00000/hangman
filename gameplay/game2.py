class Game:
    def __init__(self, vards):
        self.minamais_vards = vards.upper()
        self.progress = list(len(self.minamais_vards) * '-')
        self.dzivibas = 6
        self.uzminets = False
        self.minetie_burti = []
        self.minetie_vardi= []


    def play(self):

        ievade = ''

        self.minetie_burti.append(' ')

        while self.dzivibas > 0 and self.uzminets == False:
            burts_atrasts = False
            burts_minets = False
            vards_minets = False
            ievade = input('Ievadi minamo burtu vai vārdu: ').upper()
            if len(ievade) == 0:
                print('Nekas netika ievadīts, mēģini vēlreiz!')
                continue
            elif len(ievade) == 1: #ir ievadīts 1 simbols
                if ievade.isalpha(): #ir ievadīts burts (pēc satura)
                    for x in self.minetie_burti:
                        if ievade == x:
                            burts_minets = True
                            break
                    if burts_minets:
                        print('Burts ir jau minēts, mēģini vēlreiz!')
                    else:
                        for index, y in enumerate(self.minamais_vards):
                            if ievade == y:
                                burts_atrasts = True
                                self.progress[index] = ievade
                        if burts_atrasts:
                            print('Burts ir šajā vārdā: ' + str(self.progress))
                        else:
                            self.dzivibas -= 1
                            print('Šī burta vārdā nav! Atlikušas ' + str(self.dzivibas) + ' dzīvības')
                        self.minetie_burti.append(ievade)
                else:
                    print('Nav ievadīts burts!')
            else: #ir ievadīti vairāki simboli

                if len(self.minamais_vards) == len(ievade) and ievade.isalpha():
                    for z in self.minetie_vardi:
                        if ievade == z:
                            vards_minets = True
                            break
                    if vards_minets:
                        print('Vārds ir jau minēts, mēģini vēlreiz!')
                    else:
                        if ievade == self.minamais_vards:
                            self.uzminets = True
                            print('Vārds atminēts!')
                        else:
                            self.dzivibas -= 1
                            print('Šis nav pareizais vārds! Atlikušas ' + str(self.dzivibas) + ' dzīvības')  
                        self.minetie_vardi.append(ievade)
                else:
                    print('Vārds ievadīts nepareizi!')
            if self.dzivibas == 0:
                print('Spēle zaudēta!')
                break    
            print('Minētie vārdi: ' + str(self.minetie_vardi))
            print('Minētie burti: ' + str(self.minetie_burti))
            if self.progress == list(self.minamais_vards):
                self.uzminets = True
                print('Vārds atminēts!')
                break
            else:
                pass