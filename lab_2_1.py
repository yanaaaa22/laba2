def stop():
    words = ""
    k = 0
    while k == 0:
        word = input("Введите слово: ")
        if word == 'stop':
            k = 1
            words += word + " "
    print(words)
stop()

