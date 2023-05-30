def game():
    import random
    wrong = 0
    correct = 0
    while wrong != 3:
        a = random.randint(0,100)
        b = random.randint(0,100)
        print(f'{a}+{b}=', end='')
        c = input()
        if a+b == int(c):
            print('Правильно!')
            correct += 1
        else:
            print('Ответ неверный')
            wrong += 1
    print('Игра окончена. Правильных ответов: ', correct)
game()
