country = {'Россия': 'Москва', 'Казахстан':'Астана', 'Индия':'Нью Дели', 'Тайланд':'Бангкок'}
list_country = list(country.keys())
list_country.sort()
for i in list_country:
    print(i, ':', country[i])
print(country)
print(country['Казахстан'])
