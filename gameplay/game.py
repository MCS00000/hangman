
minamais_vards = 'vanna'.upper()
progress = list(len(minamais_vards) * '-')
dzivibas = 6
uzminets = False
minetie_burti = []
minetie_vardi= []
ievade = ''

minetie_burti.append(' ')

while dzivibas > 0 and uzminets == False:
    burts_atrasts = False
    burts_minets = False
    vards_minets = False
    ievade = input('Ievadi minamo burtu vai vārdu: ').upper()
    if len(ievade) == 0:
        print('Nekas netika ievadīts, mēģini vēlreiz!')
        continue
    elif len(ievade) == 1: #ir ievadīts 1 simbols
        if ievade.isalpha(): #ir ievadīts burts (pēc satura)
            for x in minetie_burti:
                if ievade == x:
                    burts_minets = True
                    break
            if burts_minets:
                print('Burts ir jau minēts, mēģini vēlreiz!')
            else:
                for index, y in enumerate(minamais_vards):
                    if ievade == y:
                        burts_atrasts = True
                        progress[index] = ievade
                if burts_atrasts:
                    print('Burts ir šajā vārdā: ' + str(progress))
                else:
                    dzivibas -= 1
                    print('Šī burta vārdā nav! Atlikušas ' + str(dzivibas) + ' dzīvības')
                minetie_burti.append(ievade)
        else:
            print('Nav ievadīts burts!')
    else: #ir ievadīti vairāki simboli

        if len(minamais_vards) == len(ievade) and ievade.isalpha():
            for z in minetie_vardi:
                if ievade == z:
                    vards_minets = True
                    break
            if vards_minets:
                print('Vārds ir jau minēts, mēģini vēlreiz!')
            else:
                if ievade == minamais_vards:
                    uzminets = True
                    print('Vārds atminēts!')
                else:
                    dzivibas -= 1
                    print('Šis nav pareizais vārds! Atlikušas ' + str(dzivibas) + ' dzīvības')  
                minetie_vardi.append(ievade)
        else:
            print('Vārds ievadīts nepareizi!')
    if dzivibas == 0:
        print('Spēle zaudēta!')
        break    
    print('Minētie vārdi: ' + str(minetie_vardi))
    print('Minētie burti: ' + str(minetie_burti))
    if progress == list(minamais_vards):
        uzminets = True
        print('Vārds atminēts!')
        break
    else:
        pass
