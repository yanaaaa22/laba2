game = {'авеинорст': 1, 'дклмпу': 2, 'бгёья': 3, 'йы': 4, 'жзхцч': 5, 'шею' : 8, 'фщъ' : 10}

def play(x):
    for key in game:
        if x in key:
            return game.get(key)

print(sum(map(play, input())))
