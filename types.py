capital = {
    'city': 'Москва',
    'temperature': 20
}
print(capital['city'])
capital['temperature'] = capital['temperature'] - 5
print(capital)
capital.get('country', 'Russia')
print(capital.get('country', 'Russia'))
capital['date'] = '27.05.2019'
print(capital)
