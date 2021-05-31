ad = { 'Swaroop' : 'swaroop@swaropch.com',
       'larry' : 'larry@wall.org',
       'Matsumoto' : 'matz@ruby.org',
       'Spammer' :'spammer@hotmail.com'
       }

print("Адрес Swaroop'a:", ad['Swaroop'])


del ad['Spammer']

print('\nВ адресной книге {0} контакта\n'.format(len(ad)))

for name, addres in ad.items():
    print('Контакт {0} с адресом {1}'.format(name, addres))

ad['Guido'] = 'guido@python.org'

if 'Guido' in ad:
    print("\n Адрес Guido:", ad ['Guido'])