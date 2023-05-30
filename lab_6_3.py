ivanov = {'English', 'Russian'}
ivanov1 = list(ivanov)
petrov = {'Russian', 'German'}
petrov1 = list(petrov)
rusakov = {'Russian', 'Chinese', 'Japanese'}
rusakov1 = list(rusakov)
filatova = {'Russian', 'Chinese', 'Korean'}
filatova1 = list(filatova)
languages = ivanov | petrov | rusakov | filatova
languages1 = list(languages)
languages1.sort()
print(languages1)
a = 'Chinese'
if a in ivanov1:
    print('ivanov')

if a in petrov1:
    print('petrov')

if a in rusakov1:
    print('rusakov')

if a in filatova1:
    print('filatova')
