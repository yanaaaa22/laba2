
def rare():
    word = input("Введите слово: ")
    if 'Ф' in word or 'ф' in word:
        print('Ого! Это редкое слово!')
    else:
        print('Эх, это не очень редкое слово...')
rare()

