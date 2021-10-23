
def check_difficulty(word):

    vowels = ('A', 'Ā', 'E', 'Ē', 'I', 'Ī', 'U', 'Ū', 'O')

    changed_word = word

    for index, burts in enumerate(changed_word):
        if burts in vowels:
            #replace all vowels with number 1
            changed_word = changed_word.replace(burts, str(1))
        else:
            #replace all consonants with number 2
            changed_word = changed_word.replace(burts, str(2))

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

    difficulty_score = repeated_letters('11') * 0.5 + repeated_letters('22')
    return difficulty_score
    #return difficulty_score
    #print(difficulty_score)

#print(check_difficulty(word))